# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "scikit-learn"]
# ///
"""Reference dashboard.   uv run reference/make_dashboard.py COHORT_CSV OUT.html

One self-contained page (inline SVG, no network requests, no patient-level data): ROC curves for the four models, AUC with a patient-level bootstrap
interval, and sensitivity / specificity at each model's published operating point against the pilot bar. Aggregated numbers only.
"""
import csv, sys, html
import numpy as np
from sklearn.metrics import roc_auc_score, roc_curve

COHORT, OUT = sys.argv[1], sys.argv[2]
M = ["all", "chex", "nih", "pc"]; COL = {"all": "#0f766e", "chex": "#b45309", "nih": "#6d28d9", "pc": "#be123c"}
OP = {"all": 0.009812, "chex": 0.053129, "nih": 0.00573, "pc": 0.001263}   # published operating points (data dictionary)
rows = list(csv.DictReader(open(COHORT)))
y = np.array([r["label"] == "Pneumothorax" for r in rows], int); S = {m: np.array([float(r[f"score_{m}"]) for r in rows]) for m in M}
n, npos = len(y), int(y.sum()); rng = np.random.default_rng(2026)

def boot_ci(f, B=1000):
    v = []
    for _ in range(B):
        i = rng.integers(0, n, n)
        if y[i].min() == y[i].max(): continue
        v.append(f(i))
    return np.percentile(v, [2.5, 97.5])
def sens_spec(m, i=slice(None)):
    p = S[m][i] >= OP[m]; t = y[i] == 1
    return p[t].mean(), (~p[~t]).mean()

stats = {}
for m in M:
    a = roc_auc_score(y, S[m]); lo, hi = boot_ci(lambda i: roc_auc_score(y[i], S[m][i]))
    se, sp = sens_spec(m)
    ses = np.array([sens_spec(m, rng.integers(0, n, n)) for _ in range(1000)])
    stats[m] = dict(auc=a, lo=lo, hi=hi, se=se, sp=sp, se_ci=np.percentile(ses[:, 0], [2.5, 97.5]), sp_ci=np.percentile(ses[:, 1], [2.5, 97.5]))

W = H = 320; P = 40; X = lambda v: P + v * (W - 2 * P); Y = lambda v: H - P - v * (H - 2 * P)
roc = [f'<rect x="{P}" y="{P}" width="{W-2*P}" height="{H-2*P}" fill="none" stroke="#999"/>',
       f'<line x1="{X(0)}" y1="{Y(0)}" x2="{X(1)}" y2="{Y(1)}" stroke="#bbb" stroke-dasharray="4"/>']
for t in (0, .5, 1):
    roc += [f'<text x="{X(t)}" y="{H-P+16}" font-size="11" text-anchor="middle">{t:g}</text>', f'<text x="{P-8}" y="{Y(t)+4}" font-size="11" text-anchor="end">{t:g}</text>']
roc += [f'<text x="{W/2}" y="{H-6}" font-size="12" text-anchor="middle">1 − specificity (false-positive rate)</text>',
        f'<text transform="rotate(-90)" x="{-H/2}" y="12" font-size="12" text-anchor="middle">Sensitivity</text>']
for m in M:
    fpr, tpr, _ = roc_curve(y, S[m]); pts = " ".join(f"{X(a):.1f},{Y(b):.1f}" for a, b in zip(fpr, tpr))
    roc.append(f'<polyline points="{pts}" fill="none" stroke="{COL[m]}" stroke-width="2"/>')
    roc.append(f'<circle cx="{X(1-stats[m]["sp"]):.1f}" cy="{Y(stats[m]["se"]):.1f}" r="4.5" fill="{COL[m]}" stroke="#fff"/>')
# pilot bar: sensitivity >= 0.85 and specificity >= 0.80 -> top-left region fpr <= 0.20, tpr >= 0.85
roc.append(f'<rect x="{X(0)}" y="{Y(1)}" width="{X(0.2)-X(0)}" height="{Y(0.85)-Y(1)}" fill="#0f766e" fill-opacity="0.12" stroke="#0f766e" stroke-dasharray="3"/>')
roc.append(f'<text x="{X(0.22)}" y="{Y(0.93)}" font-size="11" fill="#0f766e">pilot bar</text>')
legend = "".join(f'<span class="k"><i style="background:{COL[m]}"></i>{m}</span>' for m in M)

fx = lambda v: f"{v:.2f}"
auc_rows = "".join(f'<tr><td><i class="dot" style="background:{COL[m]}"></i>{m}</td><td>{fx(s["auc"])}</td><td>{fx(s["lo"])} to {fx(s["hi"])}</td></tr>' for m, s in stats.items())
op_rows = "".join(
    f'<tr><td><i class="dot" style="background:{COL[m]}"></i>{m}</td><td>{OP[m]:.4f}</td><td>{fx(s["se"])} ({fx(s["se_ci"][0])} to {fx(s["se_ci"][1])})</td>'
    f'<td>{fx(s["sp"])} ({fx(s["sp_ci"][0])} to {fx(s["sp_ci"][1])})</td><td>{"yes" if s["se"] >= .85 and s["sp"] >= .80 else "no"}</td></tr>' for m, s in stats.items())
page = f"""<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pneumothorax detector evaluation (toy example)</title>
<style>body{{font:15px/1.5 system-ui,sans-serif;max-width:900px;margin:1.5rem auto;padding:0 1rem;color:#1a2a2a}}h1{{font-size:1.4rem}}h2{{font-size:1.1rem;margin-top:1.8rem}}
table{{border-collapse:collapse;width:100%}}td,th{{border-bottom:1px solid #d5e6e4;padding:.35rem .5rem;text-align:left}}.k{{margin-right:1rem}}.k i,.dot{{display:inline-block;width:.7rem;height:.7rem;border-radius:50%;margin-right:.35rem}}
.note{{background:#eef7f6;border-radius:8px;padding:.6rem .9rem}}svg text{{fill:currentColor}}</style>
<h1>Pneumothorax detector evaluation</h1>
<p class="note">Toy example with a small public image sample and planted data problems, for demonstration only. {n} adult patients, {npos} with pneumothorax. Aggregated results only.</p>
<h2>ROC curves</h2><svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="ROC curves for four models">{''.join(roc)}</svg>
<p>{legend}</p><p>Dots mark each model's published operating point. The shaded region is the pilot bar (sensitivity at least 0.85 and specificity at least 0.80).</p>
<h2>Discrimination (AUC, 95% patient-level bootstrap interval)</h2><table><tr><th>Model</th><th>AUC</th><th>95% interval</th></tr>{auc_rows}</table>
<h2>At each published operating point</h2><table><tr><th>Model</th><th>Threshold</th><th>Sensitivity (95% CI)</th><th>Specificity (95% CI)</th><th>Meets pilot bar</th></tr>{op_rows}</table>
</html>"""
open(OUT, "w").write(page)
print(f"wrote {OUT}")
