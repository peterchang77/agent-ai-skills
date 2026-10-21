# /// script
# requires-python = ">=3.10"
# dependencies = ["torch", "torchxrayvision==1.4.0", "pydicom==2.4.4", "pylibjpeg==2.0.1", "pylibjpeg-libjpeg==2.3.0", "numpy", "scikit-image", "scikit-learn"]
# ///
"""Score the 250 pristine siim_small images with pretrained CPU models (one-off; output is committed).

    uv run score_images.py

Writes assets/pristine_scores.csv: one row per image (key = path inside siim_small) with one score column per model. The workshop
kit ships these precomputed scores so participants do not need torch. The same recipe is the optional "run a real model on CPU" step
(about 20 seconds per model for 250 images).

Models: torchxrayvision DenseNet121, output "Pneumothorax", at 224 x 224:
  all   trained on several public datasets combined (PRIMARY model in the workshop)
  chex  trained on CheXpert only
  nih   trained on NIH ChestX-ray14 only
  pc    trained on PadChest only
POSSIBLE OVERLAP: siim_small is believed to be drawn from NIH ChestX-ray14, which is part of the training data of "all" and "nih".
Treat their numbers as optimistic. The workshop is a toy demonstration, not a validation.
"""
import csv
import json
import math
import sys
from pathlib import Path

import numpy as np
import pydicom
import skimage.transform
import torch
import torchxrayvision as xrv

sys.path.insert(0, str(Path(__file__).parent))
from siim_data import fetch_siim_small  # noqa: E402

HERE = Path(__file__).parent
root = fetch_siim_small()
files = sorted(root.glob("**/*.dcm"))
MODELS = ["all", "chex", "nih", "pc"]
models = {w: xrv.models.DenseNet(weights=f"densenet121-res224-{w}").eval() for w in MODELS}
# By default the library rescales outputs so that each model's published operating point maps to 0.5, which compresses the scores
# into a narrow band, and with it disabled the model returns raw logits. We apply the sigmoid ourselves to get plain probabilities,
# and record the published operating points separately.
op = {w: float(m.op_threshs[m.pathologies.index("Pneumothorax")]) for w, m in models.items()}
for m in models.values(): m.op_threshs = None
json.dump(op, open(HERE / "assets" / "operating_points.json", "w"), indent=1)
rows = []
for f in files:
    a = pydicom.dcmread(f).pixel_array.astype(np.float32)
    img = skimage.transform.resize(xrv.datasets.normalize(a, 255), (224, 224), anti_aliasing=True)[None]
    scores = []
    for w, m in models.items():
        with torch.no_grad():
            logit = float(m(torch.from_numpy(img[None]).float())[0][m.pathologies.index("Pneumothorax")])
            scores.append(round(1 / (1 + math.exp(-logit)), 6))
    rows.append([str(f.relative_to(root)), "Pneumothorax" if "/Pneumothorax/" in str(f) else "No Pneumothorax", *scores])
with open(HERE / "assets" / "pristine_scores.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["source_path", "true_label", *[f"score_{m}" for m in MODELS]]); w.writerows(rows)
print(len(rows), "scored")
