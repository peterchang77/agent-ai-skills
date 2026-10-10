#!/usr/bin/env python3
"""Build checkpoints/ (restorable project states) by running the reference scripts.

    python3 reference/make_checkpoints.py      (needs uv)

Each checkpoint is a complete project folder a participant can copy and start from:
  kit/                  the data kit only (the starting state for early beats)
  checkpoints/cleaned/  kit + scripts/clean_visits.py + data/clean/visits_clean.csv + out/cleaning_flow.md
                        + notes/cleaning-decisions.md
  checkpoints/cohort/   cleaned + AGENTS.md + out/cohort.csv + out/cohort_flow.md
  checkpoints/analyzed/ cohort + scripts/analyze_pilot.py + out/pilot_results.md
  checkpoints/referenced/ analyzed + references.bib + refs/search-log.md
  checkpoints/reported/ referenced + out/abstract.tex + out/abstract.pdf (compiled with pdflatex + bibtex)
"""
import shutil, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent; TOY = HERE.parent; KIT = TOY / "kit"; CK = TOY / "checkpoints"
run = lambda *a: subprocess.run([str(x) for x in a], check=True, stdout=subprocess.DEVNULL)
shutil.rmtree(CK, ignore_errors=True)

DECISIONS = """# Cleaning decisions (analyst-approved)

Original files are never modified. Cleaned data goes in data/clean/, other outputs in out/.

1. Clinic names: strip whitespace and normalise case.
2. Dates: MM/DD/YYYY values are converted to ISO YYYY-MM-DD.
3. Exact duplicate rows: removed.
4. A visit_id shared by two different visits: both rows kept and flagged in `id_conflict`.
5. Systolic BP of 0: set to missing.
6. HbA1c values of 20 or more are in mmol/mol, not %: converted with NGSP = IFCC / 10.929 + 2.15.
7. Age above 120: repaired from the same patient's other visits (analyst's choice).
8. Patients under 18 are kept in the cleaned data and excluded at the cohort step.
"""
AGENTS = """# Project instructions

- Data: `clinic_visits.csv`, `pilot_calls.csv`; column meanings are in `data_dictionary.md`.
- Never modify original files. Cleaned data goes in `data/clean/`; all other outputs in `out/`.
- Apply the rules in `notes/cleaning-decisions.md` (run `scripts/clean_visits.py`); do not invent new cleaning rules without asking.
- Every number you report must include its row or patient count.
- HbA1c is in percent (NGSP). Targets: share of adult patients with diabetes whose most recent HbA1c is below 8.0%.
- List anything you excluded or changed, and why.
- Use `uv` for Python dependencies and record new ones in `README.md`.
- Never print, log, or commit credentials.
"""
c = CK / "cleaned"; shutil.copytree(KIT, c)
for d in ("data/clean", "out", "notes", "scripts"): (c / d).mkdir(parents=True)
shutil.copy(HERE / "clean_visits.py", c / "scripts")
run("uv", "run", HERE / "clean_visits.py", KIT / "clinic_visits.csv", c / "data/clean/visits_clean.csv", c / "out/cleaning_flow.md")
(c / "notes/cleaning-decisions.md").write_text(DECISIONS)

k = CK / "cohort"; shutil.copytree(c, k); (k / "AGENTS.md").write_text(AGENTS)
tmp = CK / "_tmp"; run("uv", "run", HERE / "analyze_pilot.py", c / "data/clean/visits_clean.csv", KIT / "pilot_calls.csv", tmp)
for f in ("cohort.csv", "cohort_flow.md"): shutil.copy(tmp / f, k / "out" / f)

a = CK / "analyzed"; shutil.copytree(k, a); shutil.copy(tmp / "pilot_results.md", a / "out"); shutil.copy(HERE / "analyze_pilot.py", a / "scripts")
shutil.rmtree(tmp)

r = CK / "referenced"; shutil.copytree(a, r); (r / "refs").mkdir()
shutil.copy(HERE / "references.bib", r); shutil.copy(HERE / "search-log.md", r / "refs")

t = CK / "reported"; shutil.copytree(r, t)
shutil.copy(HERE / "abstract_src" / "abstract.tex", t / "out"); shutil.copy(HERE / "references.bib", t / "out")
for cmd in (["pdflatex", "-interaction=nonstopmode", "abstract.tex"], ["bibtex", "abstract"],
            ["pdflatex", "-interaction=nonstopmode", "abstract.tex"], ["pdflatex", "-interaction=nonstopmode", "abstract.tex"]):
    subprocess.run(cmd, cwd=t / "out", check=True, stdout=subprocess.DEVNULL)
for f in t.joinpath("out").glob("abstract.*"):
    if f.suffix not in (".tex", ".pdf"): f.unlink()
(t / "out" / "references.bib").unlink()
print("checkpoints:", sorted(p.name for p in CK.iterdir()))
