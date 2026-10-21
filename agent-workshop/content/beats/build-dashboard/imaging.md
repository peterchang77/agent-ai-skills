---
role: build-dashboard
scenario: imaging
starts_from: the `evaluated` checkpoint
produces: "`scripts/make_dashboard.py`, `out/dashboard.html`"
prompt: |
  Write scripts/make_dashboard.py that reads out/cohort.csv and writes out/dashboard.html: a single self-contained page (no external network requests) with (1) ROC curves for the four models with each model's published
  operating point marked and the pilot bar shown as a region, (2) a table of AUC with a 95% patient-level bootstrap interval, and (3) a table of sensitivity and specificity with intervals at each published operating point. Use aggregated
  numbers only: no patient IDs, file names or images. Label axes and units. Tell me what you chose and why.
---

**Files used:** `out/cohort.csv` (and the operating points in `data_dictionary.md`).

**What you should see.** A page with four ROC curves, the primary model (`all`) highest. Each model's published operating point is a dot, and none falls in the pilot-bar region (top left: sensitivity at least 0.85, specificity at least 0.80). An AUC table matches the evaluation:
0.78 (0.71 to 0.84), 0.72, 0.67, 0.69. A reference version is `scenarios/imaging/reference/make_dashboard.py` (its output is in the `reported` checkpoint).

**Things to try**

- `Mark the pilot bar clearly and say whether each model meets it.`
- `Add a note that this is a toy example with synthetic data problems.`
- `Add the cohort flow (258 to 203) as a small table.`

**Check.** Open `out/dashboard.html` in a browser, then search the file for `http` to confirm it makes no external requests. Search for a file name such as `img_` to confirm no patient-level information was embedded.
