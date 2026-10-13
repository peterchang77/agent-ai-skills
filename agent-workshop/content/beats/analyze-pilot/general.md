---
role: analyze-pilot
title: Analyze an exposure and outcome, crude and adjusted
kind: full
summary: Conduct crude and multivariable adjusted statistical comparisons, evaluating how controlling for baseline confounders alters estimated effect sizes.
time: 8 min
teaches: [verification, scoping-work]
needs: [build-cohort]
---

In this exercise, you direct the agent to conduct a statistical analysis contrasting unadjusted (crude) comparisons against multivariable regression models adjusted for confounding covariates. Observing how point estimates shift after controlling for baseline imbalances provides a foundational lesson in empirical analysis.

**Before you start:** A cohort file containing one record per individual, an exposure indicator, an outcome endpoint, and candidate covariates ([Setup](setup:restore-a-starting-point)).

## Background

A **crude statistical comparison** evaluates raw differences in outcome rates between exposed and unexposed groups. In observational research, crude comparisons are frequently biased by **confounding**: baseline imbalances across characteristics that influence both exposure likelihood and outcome risk. For example, if older patients are more likely to receive clinical outreach and independently experience higher re-encounter rates, age confounds the observed association.

A **multivariable logistic regression** models the relationship between exposure and outcome while holding candidate covariates (such as age, sex, and baseline severity) constant, estimating an **adjusted odds ratio (aOR)**:

- $\text{OR} = 1.0$: Indicates no association.
- $\text{OR} > 1.0$: Indicates higher odds of the outcome among the exposed.
- $95\%\text{ Confidence Intervals}$: Quantify estimation uncertainty; intervals spanning 1.0 indicate associations consistent with chance variation.

In observational studies, estimated odds ratios reflect **statistical association rather than definitive causal effect**, and summary write-ups must adhere to cautious scientific phrasing.

Covariate selection represents a substantive methodological decision that must be determined *a priori* based on clinical reasoning rather than automated stepwise significance hunting.

## General methodology

Direct the agent to compute both unadjusted and multivariable adjusted estimates, mandating explicit sample accounting across both models:

```text
Using <cohort file>, analyze the association between <exposure> and <outcome>.
Report raw sample sizes, event counts, and incidence rates for both exposed and unexposed cohorts.
Calculate the unadjusted crude odds ratio, followed by an adjusted odds ratio from a multivariable logistic regression controlling for <covariates>, each with 95% confidence intervals.
Save the analysis script to <scripts/analyze.py> and formatted results to <out/results.md>.
Specify model formulas, regression diagnostics, and total sample counts utilized in each model (which should match <cohort size>).
Provide a concise narrative interpreting why the adjusted point estimate shifts relative to the crude estimate.
```

<!-- example -->

## Verification criteria

- **Sample size consistency:** Exposed and unexposed subgroup totals strictly sum to the total cohort sample size.
- **Crude estimate reconciliation:** The reported crude odds ratio matches a manual 2x2 contingency table cross-product calculation ($[A \times D] / [B \times C]$).
- **Model sample retention:** Both unadjusted and adjusted models reflect identical sample sizes, confirming no records were dropped due to missing covariate entries.
- **Cautious scientific interpretation:** Narrative summaries discuss observed statistical associations without making unverified causal claims.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Sample size drops in adjusted model | Missing values in covariate columns triggered automatic listwise deletion | Impute covariates or verify why records contain missing covariate fields |
| Highly divergent estimates between runs | Non-deterministic sampling or shifting input files | Fix input paths; standard logistic regression estimation is completely deterministic |
| Extreme odds ratios or vast confidence intervals | Quasi-complete separation: zero events within a specific covariate sub-stratum | Re-evaluate model parameterization, collapse sparse categorical bins, or report model instability |
