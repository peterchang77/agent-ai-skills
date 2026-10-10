---
role: analyze-pilot
scenario: toy
starts_from: the `cohort` checkpoint
produces: "`scripts/analyze_pilot.py`, `out/pilot_results.md`"
prompt: |
  Using out/cohort.csv, compare HbA1c recheck between patients reached by a call and patients not reached. Report counts and rates for
  each group, then the unadjusted odds ratio, then an odds ratio from a logistic regression adjusted for age, sex and index HbA1c, each
  with a 95% confidence interval. Write the script to scripts/analyze_pilot.py and the results to out/pilot_results.md. State the model, the
  number of patients in each model, and why the adjusted estimate differs from the crude one.
---

**Files used:** `out/cohort.csv` (251 patients).

**Reference results**

| Group | Patients | Rechecked | Rate |
|---|---|---|---|
| Not reached | 159 | 47 | 30% |
| Reached | 92 | 45 | 49% |

| Model | Odds ratio | 95% CI |
|---|---|---|
| Unadjusted | 2.28 | 1.34 to 3.88 |
| Adjusted for age, sex, index HbA1c | 1.80 | 1.03 to 3.15 |

**What this shows.** The unadjusted estimate is larger because older patients were more likely both to be called and to have a recheck. The
adjusted estimate is closer to the effect built into the synthetic data (an odds ratio of about 1.7), and its interval is wider and just
excludes 1. A good write-up says the adjusted estimate is the one to report, and notes that the interval is wide and the design is observational.

**Hand check.** The unadjusted odds ratio is (45/47) / (47/112) = 0.957 / 0.420 ≈ 2.28. If your agent's number does not match this, find out why before going on.

Your adjusted value may differ slightly if the agent codes sex or age differently; it should still be near 1.8 with an interval close to 1.0 to 3.2.
