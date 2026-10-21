# Reference evaluation (synthetic workshop kit; toy example for demonstration only)

Cohort: 203 adult patients (one index image each), 59 with pneumothorax. PA 120, AP 83.

## Q1. Overall discrimination (AUC, patient-level bootstrap, 4000 resamples)

| Model | AUC (95% CI) |
|---|---|
| all | 0.782 (0.715 to 0.843) |
| chex | 0.719 (0.642 to 0.793) |
| nih | 0.673 (0.592 to 0.748) |
| pc | 0.694 (0.614 to 0.769) |

## Q2. Is the primary model (`all`) better than the others? (paired bootstrap on the same patients)

| Comparison | AUC difference (95% CI) | p |
|---|---|---|
| all minus chex | 0.063 (-0.021 to 0.146) | 0.150 |
| all minus nih | 0.109 (0.037 to 0.180) | 0.004 |
| all minus pc | 0.088 (0.007 to 0.163) | 0.031 |

## Q3. Subgroups for `all` (difference in AUC, bootstrap CI; permutation p). Exploratory: three comparisons, none pre-registered.

| Comparison | n (positives) | AUC | Difference (95% CI) | permutation p |
|---|---|---|---|---|
| PA minus AP | 120 (40) vs 83 (19) | 0.85 vs 0.74 | 0.111 (-0.028 to 0.258) | 0.092 |
| male minus female | 97 (32) vs 101 (27) | 0.77 vs 0.77 | 0.000 (-0.134 to 0.132) | 0.998 |
| under 65 minus 65 or older | 162 (48) vs 41 (11) | 0.78 vs 0.79 | -0.015 (-0.161 to 0.154) | 0.858 |

## Q4. Operating point: each model's published threshold, fixed in advance

| Model | Threshold | Sensitivity (95% CI) | Specificity (95% CI) |
|---|---|---|---|
| all | 0.0098 | 0.915 (0.837 to 0.982) | 0.465 (0.381 to 0.548) |
| chex | 0.0531 | 0.475 (0.352 to 0.603) | 0.785 (0.714 to 0.851) |
| nih | 0.0057 | 0.881 (0.796 to 0.954) | 0.431 (0.350 to 0.513) |
| pc | 0.0013 | 0.864 (0.778 to 0.946) | 0.340 (0.264 to 0.416) |

Pilot bar (protocol): sensitivity >= 0.85 and specificity >= 0.80 at one threshold. Best specificity reachable at sensitivity >= 0.85 on these same data (optimistic: threshold chosen after the fact):

| Model | best specificity | 95% range with the threshold re-chosen in every resample |
|---|---|---|
| all | 0.65 | 0.46 to 0.73 |
| chex | 0.40 | 0.27 to 0.64 |
| nih | 0.44 | 0.19 to 0.58 |
| pc | 0.35 | 0.13 to 0.61 |
