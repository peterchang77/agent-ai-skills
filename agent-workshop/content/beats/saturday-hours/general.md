---
role: saturday-hours
title: Before-and-after comparison with a comparison group
kind: detour
summary: Execute a quasi-experimental difference-in-differences analysis comparing intervention and control sites to account for secular temporal trends.
time: 7 min
teaches: [verification, scoping-work]
needs: [clean-data]
---

In this optional exercise, you evaluate a policy intervention by contrasting a simple pre-post analysis against a quasi-experimental **difference-in-differences** design that incorporates unexposed control sites. This exercise demonstrates why unadjusted temporal comparisons are vulnerable to secular confounding.

**Before you start:** Cleaned data containing temporal dates, site identifiers, and an intervention introduced on a known date ([Setup](setup:restore-a-starting-point)).

## Background

When an outcome changes following a clinical or policy intervention, other background factors (such as seasonal illness waves, staffing turnover, or regional shifts) may have occurred simultaneously. A simple pre-post comparison at the intervention site cannot isolate the intervention effect from these concurrent trends.

Incorporating a **comparison group** of unaffected sites illustrates what would have happened in the absence of the intervention. A **difference-in-differences** estimator computes:

$$\Delta_{\text{DID}} = (\bar{Y}_{\text{Intervention, After}} - \bar{Y}_{\text{Intervention, Before}}) - (\bar{Y}_{\text{Control, After}} - \bar{Y}_{\text{Control, Before}})$$

This design relies on the **parallel trends assumption**: assuming that intervention and control sites would have experienced parallel trajectories had the policy not been introduced. Consequently, report findings as consistent with an intervention effect rather than definitive causal proof.

## General methodology

Direct the agent to compute the pre-post changes for both target and control sites alongside closed-form confidence intervals, requesting pre-intervention monthly trends to evaluate the parallel trends assumption:

```text
Using <clean data>, evaluate the proportion of visits classified as <outcome> before and after <intervention date> at <intervention site>.
Perform the identical calculation for the unexposed comparison sites combined.
Report cell counts, baseline and follow-up rates, the absolute change within each group, and the difference-in-differences point estimate with a 95% confidence interval.
Calculate standard errors using closed-form analytical formulas based on cell counts, avoiding computationally expensive bootstrap resampling.
Provide a table of monthly outcome proportions across each site during the pre-intervention period, and document key methodological assumptions.
```

Explicitly specifying closed-form analytical formulas ensures the script executes in seconds. If an analysis script runs unexpectedly long, interrupt execution to ensure the agent has not defaulted to computationally intensive resampling loops ([Steering](concept:steering)).

<!-- example -->

## Verification criteria

- **Explicit baseline and follow-up partitions:** Temporal intervals and comparison site definitions match the evaluation protocol exactly.
- **Complete contingency counts:** Raw numerator and denominator counts are displayed for all four cells of the difference-in-differences matrix.
- **Documented methodological assumptions:** The summary explicitly discusses the parallel trends assumption and potential unmeasured confounders.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Script execution stalls for minutes | The agent defaulted to computationally intensive bootstrap resampling or complex hierarchical modeling | Interrupt execution and mandate closed-form analytical standard errors |
| Seasonal patterns bias estimates | The pre and post observation periods span discordant seasons (e.g., comparing winter to summer) | Restrict comparisons to matched seasonal months, or incorporate explicit calendar month controls |
| Sparse pre-intervention baseline | Policy intervention was introduced near the beginning of data collection | Acknowledge that the brief baseline window widens estimation uncertainty |
