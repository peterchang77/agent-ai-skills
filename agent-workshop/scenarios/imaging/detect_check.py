# /// script
# requires-python = ">=3.10"
# dependencies = ["pydicom==2.4.4", "pylibjpeg==2.0.1", "pylibjpeg-libjpeg==2.3.0", "numpy", "scikit-learn"]
# ///
"""Developer check: do simple, vision-free detectors recover the planted problems?  uv run detect_check.py"""
import hashlib, json, re, warnings
from collections import defaultdict
from pathlib import Path
import numpy as np, pydicom
from sklearn.metrics import roc_auc_score
warnings.filterwarnings("ignore")
HERE = Path(__file__).parent
T = json.load(open(HERE / "truth/truth.json"))
planted = {k: set(v.get("files", [])) for k, v in T["planted"].items()}
flags = defaultdict(set); feats = {}
sop = defaultdict(list); pix = defaultdict(list); pid = defaultdict(list)
for p in sorted((HERE / "kit/images").glob("*.dcm")):
    n = p.name
    try:
        ds = pydicom.dcmread(p); a = ds.pixel_array
    except Exception as ex:
        flags["corrupt_truncated"].add(n); continue
    sop[ds.SOPInstanceUID].append(n); pix[hashlib.md5(a.tobytes()).hexdigest()].append(n)
    norm = re.sub(r"^SITE1-", "", str(ds.PatientID).strip()).lower(); pid[norm].append(n)
    if str(ds.PatientID) != str(ds.PatientID).strip() or str(ds.PatientID) != str(ds.PatientID).lower() or str(ds.PatientID).startswith("SITE1-"): flags["patient_id_variants"].add(n)
    if str(ds.PatientSex) not in ("M", "F"): flags["sex_variants"].add(n)
    age = str(ds.get("PatientAge", ""))
    m = re.fullmatch(r"(\d+)Y?", age)
    if not m or int(m.group(1)) > 120 or re.fullmatch(r"\d{3}Y", age): flags["age_problems"].add(n)
    if not str(ds.get("ViewPosition", "")): flags["view_position_blank"].add(n)
    if "PixelSpacing" not in ds: flags["pixel_spacing_missing"].add(n)
    if str(ds.get("PatientBirthDate", "")) or "OtherPatientIDs" in ds: flags["phi_in_header"].add(n)
    if ds.Modality != "CR": flags["modality_dx"].add(n)
    if ds.PhotometricInterpretation == "MONOCHROME1": flags["inverted_tagged_mono1"].add(n)
    if a.shape != (1024, 1024): flags["low_resolution_512"].add(n)
    x = a.astype(float)
    if ds.PhotometricInterpretation == "MONOCHROME1": x = 255 - x          # honor the tag
    # corner/outer-strip polarity: air outside the body should be dark
    h, w = x.shape; r = lambda a0, a1, b0, b1: x[int(a0*h):int(a1*h), int(b0*w):int(b1*w)].mean()
    strip = r(.29,.68,.46,.54) - (r(.29,.68,.2,.41) + r(.29,.68,.59,.8)) / 2   # mediastinum minus lungs
    feats[n] = dict(strip=strip, same_rows=(np.abs(np.diff(x, axis=0)).max(axis=1) < 1).mean(), mean=x.mean(), levels=len(np.unique(a)),
                    tl0=(a[:125, :420] == 0).mean(), tl255=(a[:125, :420] == 255).mean(), mono1=ds.PhotometricInterpretation == "MONOCHROME1")
    feats[n]["lr"] = x[int(.6*h):int(.93*h), int(.15*w):int(.47*w)].mean() - x[int(.6*h):int(.93*h), int(.53*w):int(.85*w)].mean()
chest = {n: f for n, f in feats.items() if f["levels"] > 60 and f["same_rows"] <= 0.9 and f["tl0"] < 0.6}
for n, f in feats.items():
    if f["levels"] <= 60 or f["same_rows"] > 0.9: flags["non_chest_image"].add(n)
    if f["tl0"] > 0.6 and f["tl255"] > 0.01: flags["burned_in_phi"].add(n)
for g in sop.values():
    if len(g) > 1: flags["exact_duplicate"] |= set(g[1:])
# pixel-hash duplicates with different UIDs
for g in pix.values():
    if len(g) > 1: flags["_pixhash_dups"] |= set(g)
for g in pid.values():
    if len(g) > 1: flags["_multi_image_patients"] |= set(g)
# inversion: pick threshold via strip brightness on non-text chest images
names = list(chest)
truth_inv = [int(n in planted["inverted_tag_wrong"]) for n in names]
auc_inv = roc_auc_score(truth_inv, [-chest[n]["strip"] for n in names])
auc_flip = roc_auc_score([int(n in planted["flipped_left_right"]) for n in names], [chest[n]["lr"] for n in names])
print(f"inversion (tag honored) strip-brightness AUC = {auc_inv:.3f}; flip L-R heuristic AUC = {auc_flip:.3f}")
s_in = sorted(chest[n]["strip"] for n in names if n in planted["inverted_tag_wrong"]); s_ok = sorted(chest[n]["strip"] for n in names if n not in planted["inverted_tag_wrong"])
print("mediastinum-minus-lung: inverted-wrong-tag", [round(v) for v in s_in], "| normal min/1%/median", round(s_ok[0]), round(np.percentile(s_ok,1)), round(np.median(s_ok)))
for n in names:
    if chest[n]["strip"] < -25: flags["inverted_tag_wrong"].add(n)
print(f"{'problem':28} planted found TP FP FN")
for k in planted:
    if k.startswith(("label", "scores")): continue
    f, p = flags.get(k, set()), planted[k]
    print(f"{k:28} {len(p):5} {len(f):5} {len(f & p):3} {len(f - p):3} {len(p - f):3}")
d = flags["_pixhash_dups"]; print("pixel-hash dup groups (exact + same_pixels_new_ids):", len(d), "planted:", len(planted["exact_duplicate"]) * 2 + len(planted["same_pixels_new_ids"]) * 2)
m = flags["_multi_image_patients"]; print("files sharing a normalized PatientID:", len(m), "(follow-ups: 40 expected + id-variant matches)")
