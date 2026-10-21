# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "scikit-learn"]
# ///
"""Reference evaluation (the 'evaluated' checkpoint).   uv run reference/evaluate.py COHORT_CSV OUT.md

Input: out/cohort.csv from build_cohort.py (adults, one index image per patient).
Every patient is a test patient (the models are pretrained); no train/test split is needed because no threshold is tuned on these data:
the threshold is each model's published operating point, fixed in advance (see the data dictionary).
"""
import csv, json, sys, warnings
from pathlib import Path
import numpy as np
from sklearn.metrics import roc_auc_score
warnings.filterwarnings("ignore")
COHORT, OUT = Path(sys.argv[1]), Path(sys.argv[2])
OP = {"all": 0.009812, "chex": 0.053129, "nih": 0.00573, "pc": 0.001263}   # published operating points; also listed in data_dictionary.md
M = ["all", "chex", "nih", "pc"]; B = 4000
rng = np.random.default_rng(2026)

rows = list(csv.DictReader(open(COHORT)))
idx = [dict(y=int(r["label"] == "Pneumothorax"), view=r["view"], sex=r["sex"], age=int(r["age"]), **{m: float(r[f"score_{m}"]) for m in M}) for r in rows]
N = len(idx); drops = {}
y = np.array([r["y"] for r in idx]); S = {m: np.array([r[m] for r in idx]) for m in M}
view = np.array([r["view"] for r in idx]); sex = np.array([r["sex"] for r in idx]); age = np.array([r["age"] for r in idx])
auc = lambda yy, ss: roc_auc_score(yy, ss)
ci = lambda v: np.percentile(v, [2.5, 97.5])
def boot(f):
    out = []
    for _ in range(B):
        i = rng.integers(0, N, N)
        if y[i].min() != y[i].max(): out.append(f(i))
    return np.array(out)
fmt = lambda d, lo, hi: f"{d:.3f} ({lo:.3f} to {hi:.3f})"
L = ["# Reference evaluation (synthetic workshop kit; toy example for demonstration only)\n"]
L.append(f"Cohort: {N} adult patients (one index image each), {int(y.sum())} with pneumothorax. "
         f"PA {int((view == 'PA').sum())}, AP {int((view == 'AP').sum())}.\n")
L.append("## Q1. Overall discrimination (AUC, patient-level bootstrap, 4000 resamples)\n\n| Model | AUC (95% CI) |\n|---|---|")
for m in M:
    v = boot(lambda i: auc(y[i], S[m][i])); L.append(f"| {m} | {fmt(auc(y, S[m]), *ci(v))} |")
L.append("\n## Q2. Is the primary model (`all`) better than the others? (paired bootstrap on the same patients)\n\n| Comparison | AUC difference (95% CI) | p |\n|---|---|---|")
for m in M[1:]:
    v = boot(lambda i: auc(y[i], S["all"][i]) - auc(y[i], S[m][i])); d = auc(y, S["all"]) - auc(y, S[m])
    L.append(f"| all minus {m} | {fmt(d, *ci(v))} | {2 * min((v <= 0).mean(), (v >= 0).mean()):.3f} |")
L.append("\n## Q3. Subgroups for `all` (difference in AUC, bootstrap CI; permutation p). Exploratory: three comparisons, none pre-registered.\n\n"
         "| Comparison | n (positives) | AUC | Difference (95% CI) | permutation p |\n|---|---|---|---|---|")
def sub(name, ga, gb, la, lb):
    ia, ib = np.where(ga)[0], np.where(gb)[0]
    f = lambda a_, b_: auc(y[a_], S["all"][a_]) - auc(y[b_], S["all"][b_])
    d = f(ia, ib); D = np.array([f(rng.choice(ia, len(ia)), rng.choice(ib, len(ib))) for _ in range(B)])
    pool = np.r_[ia, ib]; P = np.array([f((p := rng.permutation(pool))[:len(ia)], p[len(ia):]) for _ in range(B)])
    L.append(f"| {name} | {len(ia)} ({int(y[ia].sum())}) vs {len(ib)} ({int(y[ib].sum())}) | {auc(y[ia], S['all'][ia]):.2f} vs {auc(y[ib], S['all'][ib]):.2f} | "
             f"{fmt(d, *ci(D))} | {(np.abs(P) >= abs(d)).mean():.3f} |")
sub("PA minus AP", view == "PA", view == "AP", "PA", "AP")
known = np.isin(sex, ["M", "F"]); sub("male minus female", (sex == "M") & known, (sex == "F") & known, "M", "F")
sub("under 65 minus 65 or older", age < 65, age >= 65, "<65", ">=65")
L.append("\n## Q4. Operating point: each model's published threshold, fixed in advance\n\n| Model | Threshold | Sensitivity (95% CI) | Specificity (95% CI) |\n|---|---|---|---|")
for m in M:
    t = OP[m]; se = lambda i: (S[m][i][y[i] == 1] >= t).mean(); sp = lambda i: (S[m][i][y[i] == 0] < t).mean()
    a, b = ci(boot(se)), ci(boot(sp)); i0 = np.arange(N)
    L.append(f"| {m} | {t:.4f} | {fmt(se(i0), *a)} | {fmt(sp(i0), *b)} |")
L.append("\nPilot bar (protocol): sensitivity >= 0.85 and specificity >= 0.80 at one threshold. "
         "Best specificity reachable at sensitivity >= 0.85 on these same data (optimistic: threshold chosen after the fact):\n")
def best(ss, yy):
    ts = np.unique(ss); return max(((ss[yy == 0] < t).mean() for t in ts if (ss[yy == 1] >= t).mean() >= 0.85), default=0)
L.append("| Model | best specificity | 95% range with the threshold re-chosen in every resample |\n|---|---|---|")
for m in M:
    v = boot(lambda i: best(S[m][i], y[i])) if False else np.array([best(S[m][j], y[j]) for j in (rng.integers(0, N, N) for _ in range(1000)) if y[j].min() != y[j].max()])
    L.append(f"| {m} | {best(S[m], y):.2f} | {ci(v)[0]:.2f} to {ci(v)[1]:.2f} |")
OUT.write_text("\n".join(L) + "\n"); print(OUT.read_text())
