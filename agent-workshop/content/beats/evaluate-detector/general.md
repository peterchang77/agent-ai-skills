---
role: evaluate-detector
title: Evaluate an AI tool, with intervals
kind: full
summary: Measure how well a model separates positive from negative cases, compare models on the same patients, check subgroups, and report every estimate with its uncertainty.
time: 12 min
teaches: [verification, scoping-work]
needs: [build-cohort]
provides: [analyze-pilot]
---

A single number such as "AUC 0.78" is easy to produce and easy to over-read. In this exercise you direct the agent to report each estimate with an interval, to compare models fairly, and to treat subgroup differences with the caution a small sample requires.

**Before you start:** A cohort file with one row per patient, the reference label, and the model scores ([Build a cohort](beat:build-cohort)).

## Background

A model that outputs a score is judged on how well the scores **rank** positive cases above negative ones. The standard summary is the **AUC** (area under the ROC curve): 0.5 is chance, 1.0 is perfect. To turn a score into a yes/no decision you need a **threshold**, which trades **sensitivity** (positives caught) against **specificity** (negatives correctly left alone).

Three habits make an evaluation trustworthy ([Verification](concept:verification)):

- **Uncertainty.** With a small sample, every estimate has a wide margin of error. Resample whole patients (a *bootstrap*) to get a 95% interval.
- **Fair comparison.** When two models are scored on the same patients, compare them with a *paired* difference, not by eyeballing two separate intervals.
- **Pre-specified choices.** If you pick a threshold by looking at the same data you then report on, the result is optimistic. Fix the threshold (and the questions you will ask) beforehand. Subgroup comparisons that were not planned are *exploratory*, and several of them together will throw up an apparent difference by chance ([Scoping work](concept:scoping-work)).

## General methodology

Ask for the three analyses in turn, with the protocol's rules stated, and require counts and intervals everywhere:

```text
Using <cohort file> and <protocol>: (1) report the AUC of <primary model> with a 95% patient-level bootstrap interval; (2) compare it with each other model using a paired
bootstrap of the AUC difference on the same patients; (3) for <primary model>, compare <subgroups> by the difference in AUC with its interval and a permutation p-value.
Report the number of patients and positives behind every estimate. Write the script to <scripts/evaluate.py> and the results to <out/evaluation.md>.
Say which findings are exploratory, and what the sample cannot show.
```

Then ask for sensitivity and specificity at the thresholds the protocol fixed in advance.

<!-- example -->

## Verification criteria

- **Every estimate has an interval and its counts** (patients and positives).
- **Paired comparisons.** Models are compared on the same patients with a difference and its interval.
- **Resampling unit is the patient**, not the image.
- **No threshold tuning on the reported data**, unless clearly labelled as optimistic.
- **Honest limits.** The write-up says which findings are exploratory, and does not call a small difference "significant" or "equal" without support.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| A subgroup "difference" is announced from point estimates alone | Overlapping intervals were not considered | Ask: *"What is the difference between the groups, and its 95% interval?"* |
| "No significant difference" is read as "equivalent" | A small sample cannot show equivalence either | Ask what difference the sample could have detected |
| The best threshold is chosen and reported on the same data | Tuning and testing used the same patients | Ask for the pre-specified threshold, or label the result optimistic |
| Several comparisons, one headline | Multiple looks at the data | Count the comparisons made, and say so |
