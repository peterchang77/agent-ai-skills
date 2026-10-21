# /// script
# requires-python = ">=3.10"
# dependencies = ["pydicom==2.4.4", "pillow==10.4.0", "numpy"]
# ///
"""Reference cohort builder (the 'cohort' checkpoint).   uv run reference/build_cohort.py CLEAN_DIR OUT_DIR

Applies eval_protocol.docx to the cleaned data: adults (age recorded, >= 18) with a reference label and all four scores,
one index image per patient (the earliest study). Writes OUT_DIR/cohort.csv and OUT_DIR/cohort_flow.md.
"""
import csv, sys, warnings
from pathlib import Path
import pydicom
warnings.filterwarnings("ignore")
CLEAN, OUT = Path(sys.argv[1]), Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
lab = {r["image_file"]: r["label"] for r in csv.DictReader(open(CLEAN / "labels_clean.csv"))}
sc = {r["image_file"]: r for r in csv.DictReader(open(CLEAN / "scores_clean.csv"))}
cols = ["score_all", "score_chex", "score_nih", "score_pc"]
files = sorted(p.name for p in (CLEAN / "images").glob("*.dcm"))
flow = [("Cleaned images", len(files))]
step1 = [n for n in files if n in lab and n in sc]; flow.append(("With a reference label and all four scores", len(step1)))
rows = []
for n in step1:
    ds = pydicom.dcmread(CLEAN / "images" / n, stop_before_pixels=True)
    rows.append(dict(image_file=n, patient_id=str(ds.PatientID), study_date=str(ds.StudyDate), label=lab[n], view=str(ds.ViewPosition),
                     sex=str(ds.PatientSex), age=int(str(ds.PatientAge)[:-1]) if str(ds.PatientAge) else None, **{c: sc[n][c] for c in cols}))
step2 = [r for r in rows if r["age"] is not None]; flow.append(("Age recorded and plausible", len(step2)))
step3 = [r for r in step2 if r["age"] >= 18]; flow.append(("Adults (age >= 18)", len(step3)))
by = {}
for r in sorted(step3, key=lambda r: r["study_date"]): by.setdefault(r["patient_id"], r)
cohort = list(by.values()); flow.append(("One index image per patient (earliest study)", len(cohort)))
with open(OUT / "cohort.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(cohort[0])); w.writeheader(); w.writerows(cohort)
pos = sum(r["label"] == "Pneumothorax" for r in cohort)
(OUT / "cohort_flow.md").write_text("# Cohort flow\n\n| Step | Images / patients |\n|---|---|\n" + "\n".join(f"| {a} | {b} |" for a, b in flow)
    + f"\n\nFinal cohort: {len(cohort)} patients, {pos} with pneumothorax. PA {sum(r['view']=='PA' for r in cohort)}, AP {sum(r['view']=='AP' for r in cohort)}.\n")
print((OUT / "cohort_flow.md").read_text())
