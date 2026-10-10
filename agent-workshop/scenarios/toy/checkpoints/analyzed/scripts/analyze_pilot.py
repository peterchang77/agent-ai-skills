# /// script
# requires-python = ">=3.10"
# dependencies = ["pandas==2.2.3", "statsmodels==0.14.5", "numpy==2.1.3"]
# ///
"""Reference analysis (answer key; not part of kit/).

    uv run analyze_pilot.py CLEAN_VISITS.csv PILOT_CALLS.csv OUT_DIR

Cohort: adult Hillcrest patients whose first HbA1c >= 7.0% fell in 2025-04-01..08-31 (index visit).
Exposure: reached by a pilot call (reached == Y).  Outcome: any HbA1c 14-120 days after index.
Writes cohort.csv, cohort_flow.md and pilot_results.md; prints the flow and the crude / adjusted odds ratios.
"""
import sys
from pathlib import Path
import numpy as np, pandas as pd, statsmodels.formula.api as smf

visits, calls_p, out = sys.argv[1], sys.argv[2], Path(sys.argv[3]); out.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(visits, parse_dates=["visit_date"]); calls = pd.read_csv(calls_p)
h = df[(df.clinic == "Hillcrest") & df.hba1c.notna()]
flow = [("Hillcrest patients with any HbA1c", h.patient_id.nunique())]
a = h[h.age >= 18]; flow.append(("Adults (age >= 18)", a.patient_id.nunique()))
idx = a[(a.hba1c >= 7.0) & a.visit_date.between("2025-04-01", "2025-08-31")]
idx = idx.sort_values("visit_date").groupby("patient_id").head(1).set_index("patient_id")
flow.append(("Index visit: first HbA1c >= 7.0% from 2025-04-01 to 2025-08-31", len(idx)))
allv = df[df.hba1c.notna()].merge(idx[["visit_date"]].rename(columns={"visit_date": "idx"}), left_on="patient_id", right_index=True)
d = (allv.visit_date - allv.idx).dt.days
idx["recheck"] = idx.index.isin(set(allv[(d >= 14) & (d <= 120)].patient_id)).astype(int)
idx["called"] = idx.index.isin(calls[calls.reached == "Y"].patient_id).astype(int)
idx["age_c"] = idx["age"] - 60
idx.reset_index()[["patient_id", "age", "sex", "hba1c", "called", "recheck"]].to_csv(out / "cohort.csv", index=False)
crude = smf.logit("recheck ~ called", idx).fit(disp=0)
adj = smf.logit("recheck ~ called + age_c + C(sex) + hba1c", idx).fit(disp=0)
def orci(m):
    lo, hi = np.exp(m.conf_int().loc["called"]); return f"{np.exp(m.params['called']):.2f} (95% CI {lo:.2f}-{hi:.2f})"
rate = idx.groupby("called").recheck.agg(["sum", "size"])
flow_md = ["# Cohort flow", "", "| Step | Patients |", "|---|---|"] + [f"| {a_} | {b_} |" for a_, b_ in flow]
(out / "cohort_flow.md").write_text("\n".join(flow_md) + "\n")
lines = ["# Pilot results (synthetic data)", "", "See cohort_flow.md for how the cohort was built.",
         "", f"Analysis cohort: {len(idx)} patients; reached by call: {int(idx.called.sum())}; rechecked: {int(idx.recheck.sum())}.", "",
          "| Group | n | Rechecked | Rate |", "|---|---|---|---|"]
for k, lab in [(0, "Not reached"), (1, "Reached")]:
    lines.append(f"| {lab} | {rate.loc[k,'size']} | {rate.loc[k,'sum']} | {rate.loc[k,'sum']/rate.loc[k,'size']:.0%} |")
lines += ["", f"Crude odds ratio: {orci(crude)}", f"Adjusted odds ratio (age, sex, index HbA1c): {orci(adj)}", "",
          "Planted truth: log OR 0.55 (OR 1.73), confounded by age."]
(out / "pilot_results.md").write_text("\n".join(lines) + "\n"); print("\n".join(lines))
