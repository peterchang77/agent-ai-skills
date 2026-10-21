# /// script
# requires-python = ">=3.10"
# dependencies = ["torch", "torchxrayvision==1.4.0", "pydicom==2.4.4", "pillow", "numpy", "scikit-image"]
# ///
"""Reference: run the pretrained models on the cleaned cohort images (CPU) and compare with the provided scores.

    uv run reference/run_model.py out/cohort.csv data/clean/images out/my_scores.csv [--models all,chex] [--limit 40]

Recipe (the same as the kit's precomputed scores): pixels -> torchxrayvision normalization (8-bit range) -> 224 x 224 -> DenseNet121 ->
logit for "Pneumothorax" -> sigmoid. The library's built-in rescaling around each model's operating point is switched off so the numbers
are plain probabilities (the published operating points are in data_dictionary.md).
Weights (about 30 MB per model) are downloaded the first time from the library's release page.
"""
import argparse, csv, math, sys
from pathlib import Path
import numpy as np, pydicom, skimage.transform, torch, torchxrayvision as xrv

ap = argparse.ArgumentParser(); ap.add_argument("cohort"); ap.add_argument("images"); ap.add_argument("out")
ap.add_argument("--models", default="all"); ap.add_argument("--limit", type=int, default=0)
a = ap.parse_args()
M = a.models.split(",")
rows = list(csv.DictReader(open(a.cohort)))
if a.limit: rows = rows[: a.limit]
models = {}
for m in M:
    net = xrv.models.DenseNet(weights=f"densenet121-res224-{m}").eval(); net.op_threshs = None; models[m] = net
res = []
for r in rows:
    px = pydicom.dcmread(Path(a.images) / r["image_file"]).pixel_array.astype(np.float32)
    x = skimage.transform.resize(xrv.datasets.normalize(px, 255), (224, 224), anti_aliasing=True)[None]
    out = dict(image_file=r["image_file"])
    for m, net in models.items():
        with torch.no_grad(): logit = float(net(torch.from_numpy(x[None]).float())[0][net.pathologies.index("Pneumothorax")])
        out[f"my_score_{m}"] = round(1 / (1 + math.exp(-logit)), 6); out[f"kit_score_{m}"] = float(r[f"score_{m}"])
    res.append(out)
with open(a.out, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(res[0])); w.writeheader(); w.writerows(res)
for m in M:
    mine = np.array([r[f"my_score_{m}"] for r in res]); kit = np.array([r[f"kit_score_{m}"] for r in res]); d = np.abs(mine - kit)
    print(f"{m}: {len(res)} images, correlation {np.corrcoef(mine, kit)[0, 1]:.4f}, median abs diff {np.median(d):.5f}, max abs diff {d.max():.5f}, "
          f"{int((d > 0.001).sum())} differ by more than 0.001")
