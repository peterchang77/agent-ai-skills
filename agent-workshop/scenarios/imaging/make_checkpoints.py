# /// script
# requires-python = ">=3.10"
# ///
"""Build the imaging checkpoints from the kit with the reference scripts (deterministic).   uv run make_checkpoints.py

Needs kit/ (run build_kit.py first). Writes checkpoints/{cleaned,cohort,evaluated,referenced,reported}/, each a full copy of the kit plus the work done so far,
so a participant can start any later step in an empty folder. Generated, large, and not meant for Git.
"""
import shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
KIT, REF, OUT = HERE / "kit", HERE / "reference", HERE / "checkpoints"
run = lambda *a: subprocess.run(["uv", "run", *map(str, a)], check=True, stdout=subprocess.DEVNULL)
if not (KIT / "images").exists(): sys.exit("kit/ missing: run build_kit.py first")
shutil.rmtree(OUT, ignore_errors=True)

DECISIONS = """# Cleaning decisions

Decided before any model score was read. Originals in `images/` are never modified; cleaned copies are written to `data/clean/`.

| Problem | Decision |
|---|---|
| Unreadable file; not a chest radiograph; matrix other than 1024 x 1024 | Exclude, log in the manifest |
| Mirrored left-right (found on visual review) | Exclude: laterality is safety-critical, so we do not "repair" it |
| Inverted, tagged MONOCHROME1 | Fix: invert pixels, set MONOCHROME2 |
| Inverted, tagged MONOCHROME2 (found on visual review, confirmed by a person) | Fix: invert pixels |
| Burned-in patient text in the pixels | Black out the text box |
| Patient name, birth date, other IDs in the header | Clear |
| Patient ID case, spacing or `SITE1-` prefix | Normalize to lower case, no prefix |
| Sex written MALE / FEMALE / lower case | Normalize to M / F; blank stays blank |
| Age implausible (212Y, 150Y) | Blank it; adults must have a recorded age, so these drop out at the cohort step |
| ViewPosition blank | Fill from SeriesDescription ("view: AP/PA") |
| Modality DX | Set to CR to match the rest of the set |
| PixelSpacing missing | Leave missing; not needed for this analysis |
| Identical pixels in two files | Keep the first |
| Identical pixels with conflicting labels | Exclude both; neither label can be trusted |
| Lossy JPEG, varying pixel spacing, AP/PA mix, 8-bit | Leave alone: not errors |
| Patients under 18 | Keep in the cleaned set; exclude at the cohort step |
| Logit scores mixed with probabilities | Rows with any value outside [0, 1] are logits: convert with the sigmoid |
| Scores with different letter case in the file name | Join case-insensitively |
"""
AGENTS = """# Project rules

- Never modify files in `images/` or the other original files. Write all outputs under `data/` and `out/`.
- Cleaning decisions are in `notes/cleaning-decisions.md`. Follow them; ask before deviating.
- Exclusion rules are decided before model scores are read. Never exclude an image because of what a model scored it.
- The unit of analysis is the patient. Use one index image (the earliest study) per patient.
- Report AUC and every other estimate with a 95% interval from a patient-level bootstrap, plus the number of patients and positives.
- Compare models on the same patients with paired differences, not by eye.
- Treat subgroup comparisons as exploratory; report the difference with its interval.
- Scripts are run with `uv run`. State what was changed and what could not be checked.
- This is a toy demonstration; results are not clinical evidence.
"""
def copy_kit(dst):
    shutil.copytree(KIT, dst)
def put(src, dst): Path(dst).parent.mkdir(parents=True, exist_ok=True); shutil.copy(src, dst)

# cleaned
c = OUT / "cleaned"; copy_kit(c)
run(REF / "clean_images.py", KIT, c / "data/clean", "--review", REF / "review.csv")
(c / "out").mkdir(); shutil.move(c / "data/clean/cleaning_flow.md", c / "out/cleaning_flow.md")
put(REF / "review.csv", c / "out/review.csv"); put(REF / "clean_images.py", c / "scripts/clean_images.py"); put(REF / "make_viewer.py", c / "scripts/make_viewer.py")
(c / "notes").mkdir(); (c / "notes/cleaning-decisions.md").write_text(DECISIONS)
# cohort
k = OUT / "cohort"; shutil.copytree(c, k)
run(REF / "build_cohort.py", c / "data/clean", k / "out")
put(REF / "build_cohort.py", k / "scripts/build_cohort.py"); (k / "AGENTS.md").write_text(AGENTS)
# evaluated
e = OUT / "evaluated"; shutil.copytree(k, e)
run(REF / "evaluate.py", k / "out/cohort.csv", e / "out/evaluation.md"); put(REF / "evaluate.py", e / "scripts/evaluate.py")
# referenced: evaluated + verified references (extras/ was produced with scripts/pubmed_refs.py)
r = OUT / "referenced"; shutil.copytree(e, r)
EX = HERE / "extras"
put(EX / "pubmed_refs.py", r / "scripts/pubmed_refs.py"); put(EX / "references.bib", r / "references.bib"); put(EX / "search-log.md", r / "refs/search-log.md")
with open(r / "AGENTS.md", "a") as f:
    f.write("- Citations come only from retrieved PubMed records. Each entry in `references.bib` must contain a PMID. Never write a citation from memory.\n")
# reported: referenced + dashboard + abstract (tex, and pdf if LaTeX is installed)
d = OUT / "reported"; shutil.copytree(r, d)
run(REF / "make_dashboard.py", e / "out/cohort.csv", d / "out/dashboard.html"); put(REF / "make_dashboard.py", d / "scripts/make_dashboard.py")
put(EX / "abstract.tex", d / "out/abstract.tex")
if shutil.which("pdflatex") and shutil.which("bibtex"):
    sh = lambda *a: subprocess.run(a, cwd=d / "out", check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.copy(d / "references.bib", d / "out/references.bib")
    for cmd in (["pdflatex", "-interaction=nonstopmode", "abstract.tex"], ["bibtex", "abstract"], ["pdflatex", "-interaction=nonstopmode", "abstract.tex"], ["pdflatex", "-interaction=nonstopmode", "abstract.tex"]):
        subprocess.run(cmd, cwd=d / "out", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for junk in ("abstract.aux", "abstract.log", "abstract.bbl", "abstract.blg", "references.bib"): (d / "out" / junk).unlink(missing_ok=True)
print("checkpoints:", sorted(p.name for p in OUT.iterdir()))
