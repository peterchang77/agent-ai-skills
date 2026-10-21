# /// script
# requires-python = ">=3.10"
# dependencies = ["pydicom==2.4.4", "pylibjpeg==2.0.1", "pylibjpeg-libjpeg==2.3.0", "numpy"]
# ///
"""Reference cleaning script (the 'cleaned' checkpoint).

    uv run reference/clean_images.py KIT_DIR OUT_DIR [--review review.csv]

Never touches KIT_DIR. Writes OUT_DIR/images/*.dcm (cleaned copies), manifest.csv (one row per input file: kept / fixed / excluded
and why), labels_clean.csv, scores_clean.csv and cleaning_flow.md.

Rules (decided before any model score is read):
  exclude  unreadable, not a chest radiograph, matrix not 1024x1024, confirmed mirrored, duplicates with conflicting labels
  fix      MONOCHROME1 -> invert pixels, set MONOCHROME2;  confirmed inverted-with-wrong-tag -> invert pixels;
           burned-in text box -> blacked out;  header PHI cleared;  IDs, sex, age, view, modality normalized
  dedupe   identical pixels -> keep the first file
  leave    lossy JPEG, varying pixel spacing, AP/PA mix, 8-bit depth
review.csv (exported from the viewer) has columns file,decision,flags. A confirmed row whose flags contain 'inver' or 'flip' triggers that action.
"""
import argparse, csv, hashlib, math, re, warnings
from collections import defaultdict
from pathlib import Path
import numpy as np, pydicom
from pydicom.uid import ExplicitVRLittleEndian
warnings.filterwarnings("ignore")

ap = argparse.ArgumentParser(); ap.add_argument("kit"); ap.add_argument("out"); ap.add_argument("--review"); a = ap.parse_args()
KIT, OUT = Path(a.kit), Path(a.out); (OUT / "images").mkdir(parents=True, exist_ok=True)
review = {}
if a.review:
    for r in csv.DictReader(open(a.review)):
        if r["decision"] == "confirm": review[r["file"]] = "inverted" if "inver" in r["flags"] else "flipped" if "flip" in r["flags"] else ""
man = {}   # file -> dict(action, reasons)


def note(f, reason, action=None):
    m = man.setdefault(f, dict(action="kept", reasons=[]))
    m["reasons"].append(reason)
    if action == "exclude" or (action == "fix" and m["action"] != "exclude"): m["action"] = action


def set_pixels(ds, arr):
    ds.PixelData = np.clip(arr, 0, 255).astype(np.uint8).tobytes(); ds.Rows, ds.Columns = arr.shape
    ds.file_meta.TransferSyntaxUID = ExplicitVRLittleEndian; ds.is_little_endian, ds.is_implicit_VR = True, False


def norm_label(s):
    s = s.strip().lower()
    return "Pneumothorax" if s in ("pneumothorax", "ptx") else "No Pneumothorax" if s in ("no pneumothorax", "normal") else None


data, flow = {}, []
files = sorted((KIT / "images").glob("*.dcm"))
for p in files:
    n = p.name; man[n] = dict(action="kept", reasons=[])
    try: ds = pydicom.dcmread(p); arr = ds.pixel_array
    except Exception: note(n, "unreadable file", "exclude"); continue
    x = arr.astype(float)
    if len(np.unique(arr)) <= 60 or (np.abs(np.diff(x, axis=0)).max(axis=1) < 1).mean() > 0.9:
        note(n, "not a chest radiograph", "exclude"); continue
    if arr.shape != (1024, 1024): note(n, f"matrix {arr.shape}, protocol requires 1024x1024", "exclude"); continue
    if review.get(n) == "flipped": note(n, "mirrored left-right (confirmed on review); laterality unsafe", "exclude"); continue
    data[n] = (ds, arr)
flow += [("Files received", len(files)), ("Readable 1024x1024 chest radiographs, not mirrored", len(data))]

labels_raw = {r["image_file"]: r["label"] for r in csv.DictReader(open(KIT / "labels.csv"))}
groups = defaultdict(list)
for n in sorted(data): groups[hashlib.md5(data[n][1].tobytes()).hexdigest()].append(n)
for g in groups.values():
    if len(g) < 2: continue
    if len({norm_label(labels_raw.get(f, "")) for f in g}) > 1:
        for f in g: note(f, f"duplicate pixels with conflicting labels ({', '.join(g)})", "exclude"); data.pop(f)
    else:
        for f in g[1:]: note(f, f"duplicate of {g[0]}", "exclude"); data.pop(f)
flow.append(("After removing duplicates (pairs with conflicting labels removed entirely)", len(data)))

for n in sorted(data):
    ds, arr = data[n]; cur = arr
    if ds.PhotometricInterpretation == "MONOCHROME1":
        cur = 255 - arr.astype(int); ds.PhotometricInterpretation = "MONOCHROME2"; set_pixels(ds, cur)
        note(n, "MONOCHROME1: pixels inverted, tag set to MONOCHROME2", "fix")
    elif review.get(n) == "inverted":
        cur = 255 - arr.astype(int); set_pixels(ds, cur); note(n, "inverted but tagged MONOCHROME2 (confirmed on review): pixels inverted", "fix")
    tl = cur[:125, :420]
    if (tl == 0).mean() > 0.6 and (tl == 255).mean() > 0.01:       # burned-in text box: black rectangle with white characters
        ys, xs = np.where(cur[:200, :600] == 255); c = np.array(cur, copy=True); c[: ys.max() + 12, : xs.max() + 12] = 0
        set_pixels(ds, c); note(n, "burned-in text blacked out", "fix")
    if str(ds.get("PatientBirthDate", "")) or "OtherPatientIDs" in ds or "^" in str(ds.get("PatientName", "")):
        ds.PatientBirthDate = ""
        if "OtherPatientIDs" in ds: del ds["OtherPatientIDs"]
        note(n, "header PHI cleared (name, birth date, other IDs)", "fix")
    pid = re.sub(r"^site1-", "", str(ds.PatientID).strip().lower())
    if str(ds.PatientID) != pid: note(n, f"PatientID normalized from {str(ds.PatientID)!r}", "fix")
    ds.PatientID = ds.PatientName = pid
    sx = {"MALE": "M", "FEMALE": "F", "M": "M", "F": "F"}.get(str(ds.PatientSex).upper(), "")
    if str(ds.PatientSex) != sx: note(n, f"PatientSex {str(ds.PatientSex)!r} -> {sx!r}", "fix")
    ds.PatientSex = sx
    m = re.fullmatch(r"(\d+)Y?", str(ds.PatientAge)); age = int(m.group(1)) if m else None
    if age is not None and age > 120: note(n, f"PatientAge {str(ds.PatientAge)!r} implausible; blanked", "fix")
    ds.PatientAge = f"{age:03d}Y" if age is not None and age <= 120 else ""     # bare '62' -> '062Y' is a silent format change
    if not str(ds.get("ViewPosition", "")):
        ds.ViewPosition = "AP" if str(ds.SeriesDescription).endswith("AP") else "PA"; note(n, "ViewPosition filled from SeriesDescription", "fix")
    if ds.Modality != "CR": note(n, f"Modality {ds.Modality} -> CR", "fix"); ds.Modality = "CR"
    if "PixelSpacing" not in ds: note(n, "PixelSpacing missing (left missing)")
    ds.save_as(OUT / "images" / n, write_like_original=False)
kept = sorted(data)
flow.append(("Cleaned images written", len(kept)))

with open(OUT / "manifest.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["file", "action", "reasons"])
    for n in sorted(man): w.writerow([n, man[n]["action"], "; ".join(man[n]["reasons"])])
with open(OUT / "labels_clean.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["image_file", "label"])
    for n in kept:
        l = norm_label(labels_raw.get(n, ""))
        if l: w.writerow([n, l])
sc = {}                 # join case-insensitively; a row with any value outside [0,1] holds logits -> sigmoid
for r in csv.DictReader(open(KIT / "model_scores.csv")):
    vals = {k: (float(v) if v.strip() else None) for k, v in r.items() if k != "image_file"}
    if any(v is not None and not 0 <= v <= 1 for v in vals.values()):
        vals = {k: (1 / (1 + math.exp(-v)) if v is not None else None) for k, v in vals.items()}
    sc[r["image_file"].lower()] = vals
cols = ["score_all", "score_chex", "score_nih", "score_pc"]
with open(OUT / "scores_clean.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["image_file", *cols])
    for n in kept:
        v = sc.get(n.lower())
        if v and all(v[c] is not None for c in cols): w.writerow([n, *[round(v[c], 5) for c in cols]])
(OUT / "cleaning_flow.md").write_text("# Cleaning flow\n\n| Step | Images |\n|---|---|\n" + "\n".join(f"| {a} | {b} |" for a, b in flow) + "\n")
print((OUT / "cleaning_flow.md").read_text())
