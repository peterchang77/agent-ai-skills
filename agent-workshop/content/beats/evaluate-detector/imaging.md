---
role: evaluate-detector
scenario: imaging
starts_from: the `cohort` checkpoint
produces: "`scripts/evaluate.py`, `out/evaluation.md`"
prompt:
  - label: Overall and model comparison
    text: |
      Using out/cohort.csv and eval_protocol.docx: (1) report the AUC of each of the four models with a 95% patient-level bootstrap interval (at least 2000 resamples); (2) compare score_all with each other model using a paired
      bootstrap of the AUC difference on the same patients, with the interval and a p-value. Report the number of patients and positives. Write the script to scripts/evaluate.py and the results to out/evaluation.md.
  - label: Subgroups
    text: |
      Add to the same script: for score_all, compare PA vs AP, male vs female, and under 65 vs 65 or older by the difference in AUC with a 95% bootstrap interval and a permutation p-value, with the number of patients and positives in each group.
      Say which of these findings are exploratory and what the sample cannot show.
  - label: Operating point and pilot bar
    text: |
      Add to the same script: for each model, sensitivity and specificity with 95% intervals at its published operating point from the protocol, fixed in advance. Say whether any model meets the pilot bar, and report separately,
      clearly labelled as optimistic, the best specificity reachable at sensitivity of at least 0.85 on these same data.
---

**Files used:** `out/cohort.csv` (203 patients, 59 with pneumothorax), `eval_protocol.docx`.

**Reference results**

| Model | AUC (95% CI) | `score_all` minus this model (95% CI) | p |
|---|---|---|---|
| `score_all` | 0.78 (0.72 to 0.84) | | |
| `score_chex` | 0.72 (0.64 to 0.79) | +0.06 (-0.02 to +0.15) | 0.15 |
| `score_nih` | 0.67 (0.59 to 0.75) | +0.11 (+0.04 to +0.18) | 0.004 |
| `score_pc` | 0.69 (0.61 to 0.77) | +0.09 (+0.01 to +0.16) | 0.03 |

| Subgroup (`score_all`) | Patients (positives) | AUC | Difference (95% CI) | p |
|---|---|---|---|---|
| PA vs AP | 120 (40) vs 83 (19) | 0.85 vs 0.74 | +0.11 (-0.03 to +0.26) | 0.09 |
| Male vs female | 97 (32) vs 101 (27) | 0.77 vs 0.77 | 0.00 (-0.13 to +0.13) | 1.0 |
| Under 65 vs 65 or older | 162 (48) vs 41 (11) | 0.78 vs 0.79 | -0.02 (-0.16 to +0.15) | 0.86 |

| Model | Threshold | Sensitivity (95% CI) | Specificity (95% CI) |
|---|---|---|---|
| `score_all` | 0.0098 | 0.92 (0.84 to 0.98) | 0.47 (0.38 to 0.55) |
| `score_chex` | 0.0531 | 0.48 (0.35 to 0.60) | 0.79 (0.71 to 0.85) |
| `score_nih` | 0.0057 | 0.88 (0.80 to 0.95) | 0.43 (0.35 to 0.51) |
| `score_pc` | 0.0013 | 0.86 (0.78 to 0.95) | 0.34 (0.26 to 0.42) |

**What this shows.**

- `score_all` has the highest AUC. It beats the NIH-only and PadChest-only models on the same patients; the difference from the CheXpert model is within chance. A good write-up compares models with the paired difference, not by looking at overlapping intervals.
- PA looks better than AP (0.85 vs 0.74), but the interval on the difference includes zero. With only 19 AP positives this is a lead to follow up, not a finding. The other two comparisons show nothing. A good write-up counts the three
  comparisons and labels them exploratory.
- No model meets the pilot bar (sensitivity at least 0.85 and specificity at least 0.80). `score_all`, `score_nih` and `score_pc` are sensitive but not specific at their own operating points; `score_chex` is the reverse. The scores are
  not comparable across models, so the same threshold means different things for each. The best specificity `score_all` reaches at sensitivity 0.85 is about 0.65 (range 0.46 to 0.73 with the threshold re-chosen in every resample), and that is
  optimistic, and still short.
- `score_all` and `score_nih` may have seen these images in training, so their numbers are likely high.

**Check the work.** The unadjusted AUC can be checked in any statistics tool from `out/cohort.csv`. Resampling should be by patient: the cohort has one row per patient, so rows and patients coincide, but ask the agent to confirm. Your numbers will
differ in the third decimal because the bootstrap is random; the conclusions should match.

The reference script and result are in `scenarios/imaging/checkpoints/evaluated/`.
