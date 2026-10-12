# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml==6.0.2"]
# ///
"""Validate content and generate docs/ + mkdocs.yml.

Source of truth is content/:
  concepts/<group>/<id>.md          scenario-independent concept pages
  beats/<role>/general.md           the general (reusable) part of one demo step
  beats/<role>/<scenario>.md        the scenario-specific example for that step
  setup/primer.md, setup/<scenario>.md
  tracks/*.md                       the three tracks (track: concepts | demo | tutorial)

A beat page = general.md with `<!-- example -->` replaced by one tab per scenario, each holding a
labelled "Workshop example" admonition built from <role>/<scenario>.md.

Link syntax in content:  (concept:ID)  (beat:ROLE)  (setup:ANCHOR)  (guide:NAME)
Usage: uv run scripts/build.py
"""
import os, re, shutil, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
CONTENT, DOCS = ROOT / "content", ROOT / "docs"
REPO_URL = "https://github.com/peterchang77/agent-ai-skills/tree/main/guides/"
errors: list[str] = []


def load(p: Path):
    m = re.match(r"---\n(.*?)\n---\n(.*)", p.read_text(), re.S)
    if not m:
        errors.append(f"{p}: missing front matter")
        return {}, p.read_text()
    return yaml.safe_load(m[1]) or {}, m[2].strip()


concepts = {}   # id -> (fm, body)
for p in sorted((CONTENT / "concepts").rglob("*.md")):
    fm, body = load(p); fm["group"] = p.parent.name; concepts[fm.get("id")] = (fm, body)
beats = {}      # role -> (fm, body)
examples = {}   # (scenario, role) -> (fm, body)
for d in sorted((CONTENT / "beats").iterdir()):
    for p in sorted(d.glob("*.md")):
        fm, body = load(p)
        if p.name == "general.md": beats[fm.get("role")] = (fm, body)
        else: examples[(fm.get("scenario"), fm.get("role"))] = (fm, body)
tracks = {}
for p in sorted((CONTENT / "tracks").glob("*.md")):
    fm, body = load(p); tracks[fm.get("id")] = (fm, body)
primer = load(CONTENT / "setup" / "primer.md")
setup_scn = {}
for p in sorted((CONTENT / "setup").glob("*.md")):
    if p.name != "primer.md":
        fm, body = load(p); setup_scn[fm["scenario"]] = (fm, body)
scenarios = sorted(setup_scn, key=lambda s: (s != "toy", s))
label = lambda s: setup_scn[s][0].get("label", s)

# ---------------- derived + validation ----------------
for cid, (fm, _) in concepts.items():
    fm["beats"] = [r for r, (bfm, _) in beats.items() if cid in (bfm.get("teaches") or [])]
for cid, (fm, body) in concepts.items():
    for k in ("id", "title", "blurb"):
        if k not in fm: errors.append(f"concept {cid}: missing '{k}'")
    for rel in fm.get("related", []) or []:
        if rel not in concepts: errors.append(f"concept {cid}: unknown related '{rel}'")
for role, (fm, body) in beats.items():
    for k in ("title", "kind", "summary", "time", "teaches"):
        if k not in fm: errors.append(f"beat {role}: missing '{k}'")
    for n in fm.get("needs", []) or []:
        if n not in beats: errors.append(f"beat {role}: needs unknown beat '{n}'")
    for t in fm.get("teaches", []) or []:
        if t not in concepts: errors.append(f"beat {role}: teaches unknown concept '{t}'")
    if "<!-- example -->" not in body: errors.append(f"beat {role}: general.md lacks <!-- example --> marker")
    if not any((s, role) in examples for s in scenarios): errors.append(f"beat {role}: no scenario example")
for (sc, role), (fm, body) in examples.items():
    if role not in beats: errors.append(f"example {sc}/{role}: no general.md")
    if sc not in setup_scn: errors.append(f"example {sc}/{role}: unknown scenario")
    for k in ("starts_from", "produces", "prompt"):
        if k not in fm: errors.append(f"example {sc}/{role}: missing '{k}'")
anchors = set(re.findall(r"^#+\s+(.*)$", primer[1], re.M))
slug = lambda t: re.sub(r"[^\w\- ]", "", t.lower()).strip().replace(" ", "-")
anchor_ids = {slug(a) for a in anchors} | {slug(a) for _, (_, b) in setup_scn.items() for a in re.findall(r"^#+\s+(.*)$", b, re.M)}
all_bodies = [(f"concept {c}", b) for c, (_, b) in concepts.items()] + \
             [(f"beat {r}", b) for r, (_, b) in beats.items()] + \
             [(f"example {k}", b) for k, (_, b) in examples.items()]
for src, body in all_bodies:
    for kind, ident in re.findall(r"\]\((concept|beat|setup|guide):([\w#-]*)\)", body):
        if kind == "concept" and ident not in concepts: errors.append(f"{src}: broken link concept:{ident}")
        if kind == "beat" and ident not in beats: errors.append(f"{src}: broken link beat:{ident}")
        if kind == "setup" and ident and ident not in anchor_ids: errors.append(f"{src}: unknown setup anchor {ident}")
        if kind == "guide" and not (ROOT.parent / "guides" / ident).exists(): errors.append(f"{src}: unknown guide {ident}")

def steps_of(fm):
    if "sections" in fm: return [(sec["name"], sec["steps"]) for sec in fm["sections"]]
    return [(None, fm.get("steps", []))]
for tid, (fm, _) in tracks.items():
    if fm.get("track") not in ("concepts", "demo", "tutorial"): errors.append(f"track {tid}: bad 'track'")
    for _, steps in steps_of(fm):
        for s in steps:
            if "concept" in s and s["concept"] not in concepts: errors.append(f"track {tid}: unknown concept {s['concept']}")
            if "beat" in s and s["beat"] not in beats: errors.append(f"track {tid}: unknown beat {s['beat']}")
    if fm.get("track") in ("demo", "tutorial"):   # every beat's prerequisites must appear earlier in the demo track
        seen = []
        for _, steps in steps_of(fm):
            for s in steps:
                if "beat" in s:
                    for n in beats[s["beat"]][0].get("needs", []) or []:
                        if n not in seen: errors.append(f"track {tid}: {s['beat']} needs {n} earlier")
                    seen.append(s["beat"])
if errors:
    print("\n".join(errors)); sys.exit(1)
tr = [t for t in tracks.values() if t[0].get("track") == "concepts"]
covered = {s["concept"] for t in tr for _, st in steps_of(t[0]) for s in st if "concept" in s}
for c in concepts:
    if c not in covered: print(f"note: concept '{c}' is not in the concept track")
dtr = [t for t in tracks.values() if t[0].get("track") == "demo"]
dcov = {s["beat"] for t in dtr for _, st in steps_of(t[0]) for s in st if "beat" in s}
for b in beats:
    if b not in dcov: print(f"note: beat '{b}' is not in the demo track")

# ---------------- rendering helpers ----------------
concept_file = lambda c: Path("concepts") / f"{c}.md"
beat_file = lambda r: Path("demo") / f"{r}.md"
SETUP_FILE = Path("demo") / "setup.md"
rel = lambda frm, to: Path(os.path.relpath(to, frm.parent)).as_posix()

def resolve(text: str, here: Path) -> str:
    text = re.sub(r"\]\(concept:([\w-]+)\)", lambda m: f"]({rel(here, concept_file(m[1]))})", text)
    text = re.sub(r"\]\(beat:([\w-]+)\)", lambda m: f"]({rel(here, beat_file(m[1]))})", text)
    text = re.sub(r"\]\(setup:([\w-]*)\)", lambda m: f"]({rel(here, SETUP_FILE)}{'#' + m[1] if m[1] else ''})", text)
    return re.sub(r"\]\(guide:([\w-]+)\)", lambda m: f"]({REPO_URL}{m[1]}/)", text)

indent = lambda t, n=4: "\n".join(" " * n + l if l.strip() else "" for l in t.strip().splitlines())
tabs = lambda items: "\n\n".join(f'=== "{k}"\n\n{indent(v)}' for k, v in items.items())

def example_block(sc, role, here, full=True):
    fm, body = examples[(sc, role)]
    if not full:
        inner = f"```text\n{fm['prompt'].strip()}\n```"
    else:
        head = (f"**Start from:** {fm['starts_from']} ([how to restore]({rel(here, SETUP_FILE)}#restore-a-starting-point))  \n"
                f"**Produces:** {fm['produces']}\n\n")
        inner = head + "**Prompt**\n\n```text\n" + fm["prompt"].strip() + "\n```\n\n" + body
    return f'!!! example "Workshop example · {label(sc)}"\n\n{indent(inner)}'

short = lambda fm: fm.get("short") or fm["title"]

def render_concept(cid, here):
    fm, body = concepts[cid]
    # Concept pages stand alone; they link to the steps that apply the idea instead of embedding them.
    links = [f"- [{beats[r][0]['title']}]({rel(here, beat_file(r))}). {beats[r][0]['summary']}" for r in fm["beats"]]
    if links: body = body.replace("## Demo it", "## Try it").replace("<!-- demos -->", "\n".join(links))
    else: body = re.sub(r"\n*## Demo it\s*\n\s*<!-- demos -->\s*", "\n", body)
    out = [f"# {fm['title']}", "", f"*{fm['blurb']}*", "", resolve(body, here)]
    rel_links = [c for c in fm.get("related", []) or []]
    if rel_links:
        out += ["", "## Related", "", " · ".join(f"[{short(concepts[c][0])}]({rel(here, concept_file(c))})" for c in rel_links)]
    return "\n".join(out) + "\n"

def badge(cls, text=None):
    return f'<span class="wk-badge wk-{cls}">{text or KIND.get(cls, cls.title())}</span>'
KIND = {"full": "Full step", "mini": "Quick step", "detour": "Optional detour", "advanced": "Advanced"}
def render_beat(r, here):
    fm, body = beats[r]
    ex = {label(s): example_block(s, r, here) for s in scenarios if (s, r) in examples}
    meta = f'<p class="wk-meta">{badge(fm["kind"])} &nbsp;about {fm["time"]}</p>'
    page = body.replace("<!-- example -->", tabs(ex))
    out = [f"# {fm['title']}", "", meta, "", resolve(page, here), "", "## Concepts behind this", ""]
    for c in fm["teaches"]:
        cf = concepts[c][0]
        out.append(f"- **{short(cf)}.** {cf['blurb']} [Go deeper →]({rel(here, concept_file(c))})")
    if fm.get("needs"):
        out += ["", "**Builds on:** " + ", ".join(f"[{beats[n][0]['title']}]({rel(here, beat_file(n))})" for n in fm["needs"])]
    return "\n".join(out) + "\n"

def render_setup(here):
    fm, body = primer
    out = [f"# {fm['title']}", "", resolve(body, here), "", "## Your scenario's data", "",
           tabs({label(s): setup_scn[s][1] for s in scenarios})]
    return resolve("\n".join(out), here) + "\n"

def render_step(step, here):
    if "concept" in step: return render_concept(step["concept"], here)
    if "beat" in step: return render_beat(step["beat"], here)
    return render_setup(here)
def step_title(step):
    if "concept" in step: return short(concepts[step["concept"]][0])
    if "beat" in step: return beats[step["beat"]][0]["title"]
    return "Setup"
def write(path, text):
    (DOCS / path).parent.mkdir(parents=True, exist_ok=True); (DOCS / path).write_text(text)

# ---------------- generate ----------------
step_path = lambda s: concept_file(s["concept"]) if "concept" in s else SETUP_FILE if "setup" in s else beat_file(s["beat"])
step_type = lambda s: badge("concept", "Concept") if "concept" in s else badge("demo", "Demo") if "beat" in s else badge("setup", "Setup")
def step_desc(s):
    if "concept" in s: return concepts[s["concept"]][0]["blurb"]
    if "beat" in s: return beats[s["beat"]][0]["summary"]
    return "Restore the data kit and any starting point you need."
def beat_kind(s): return badge(beats[s["beat"]][0]["kind"]) if "beat" in s else badge("setup", "Setup")
def beat_time(s): return beats[s["beat"]][0]["time"] if "beat" in s else ""

def toc_tables(kind, toc, index):
    out = []
    for name, rows in toc:
        if name: out += [f"### {name}", ""]
        if kind == "concepts":
            out += ["| Concept | What it covers |", "|---|---|"]
            out += [f"| [{step_title(s)}]({rel(index, f)}) | {step_desc(s)} |" for _, s, f in rows]
        elif kind == "demo":
            out += ["| Step | Kind | Time | What you do |", "|---|---|---|---|"]
            out += [f"| [{step_title(s)}]({rel(index, f)}) | {beat_kind(s)} | {beat_time(s)} | {step_desc(s)} |" for _, s, f in rows]
        else:
            out += ["| Step | Type | What it covers |", "|---|---|---|"]
            out += [f"| [{step_title(s)}]({rel(index, f)}) | {step_type(s)} | {step_desc(s)} |" for n, s, f in rows]
        out.append("")
    return "\n".join(out)

if DOCS.exists(): shutil.rmtree(DOCS)
shutil.copytree(ROOT / "assets", DOCS, dirs_exist_ok=True)   # logo, css
nav = [{"Home": "index.md"}]
for tid, (fm, body) in tracks.items():
    kind = fm["track"]; index = Path(kind) / "index.md"
    sec_nav, toc, n = [], [], 0
    for name, steps in steps_of(fm):
        entries, rows = [], []
        for s in steps:
            n += 1
            f = Path("tutorial") / f"{s.get('concept') or s.get('beat') or 'setup'}.md" if kind == "tutorial" else step_path(s)
            if kind == "tutorial" and (DOCS / f).exists(): errors.append(f"tutorial: duplicate step {f.stem}")
            write(f, render_step(s, f))
            entries.append({step_title(s): f.as_posix()}); rows.append((n, s, f))
        sec_nav.append({name: entries} if name else entries); toc.append((name, rows))
    flat = [{"Overview": index.as_posix()}]
    for e in sec_nav: flat += e if isinstance(e, list) else [e]
    nav.append({fm["title"]: flat})
    page = body.replace("<!-- toc -->", toc_tables(kind, toc, index))
    write(index, f"# {fm['title']}\n\n" + resolve(page, index) + "\n")
if errors: print("\n".join(errors)); sys.exit(1)
write(Path("index.md"), resolve((CONTENT / "home.md").read_text().strip(), Path("index.md")) + "\n")
(ROOT / "mkdocs.yml").write_text((ROOT / "mkdocs.base.yml").read_text().rstrip() + "\n" + yaml.safe_dump({"nav": nav}, sort_keys=False, allow_unicode=True))
# --- downloadable kits for assets/install.sh: deterministic zip + per-file manifest + zip checksum ---
import hashlib, zipfile
def publish_zip(name, src):
    out = DOCS / "downloads"; out.mkdir(parents=True, exist_ok=True)
    files = sorted(f for f in src.rglob("*") if f.is_file())
    with zipfile.ZipFile(out / f"{name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            zi = zipfile.ZipInfo(f.relative_to(src).as_posix(), (2020, 1, 1, 0, 0, 0))
            zi.external_attr = 0o644 << 16; zi.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(zi, f.read_bytes())
    h = lambda b: hashlib.sha256(b).hexdigest()
    (out / f"{name}.manifest").write_text("".join(f"{h(f.read_bytes())}  {f.relative_to(src).as_posix()}\n" for f in files))
    (out / f"{name}.zip.sha256").write_text(h((out / f"{name}.zip").read_bytes()) + "\n")
publish_zip("toy-kit", ROOT / "scenarios/toy/kit")
publish_zip("toy-checkpoints", ROOT / "scenarios/toy/checkpoints")
print(f"ok: {len(concepts)} concepts, {len(beats)} beats, {len(examples)} examples, {len(tracks)} tracks -> docs/")
