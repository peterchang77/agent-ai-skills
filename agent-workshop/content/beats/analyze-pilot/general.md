---
role: analyze-pilot
title: Analyze an exposure and outcome, crude and adjusted
kind: full
summary: Compare an outcome between exposed and unexposed groups, then adjust for a confounder. The change from crude to adjusted is the lesson.
time: 8 min
teaches: [verification, scoping-work]
needs: [build-cohort]
---

After this step you will be able to ask an agent for a simple group comparison and a regression adjusted for confounders, and you will
know what to check before believing either.

**Before you start:** a cohort file with one row per person, an exposure, an outcome, and covariates ([Setup](setup:restore-a-starting-point)).

## Background

A **crude** comparison simply contrasts the outcome rate between groups. It can mislead when the groups differ in other ways that
also affect the outcome (**confounding**). For example, if older patients are both more likely to receive an intervention and more
likely to have the outcome, age inflates the crude difference. A **logistic regression** estimates an **odds ratio** for the exposure
while holding the other variables (age, sex, a baseline measurement) constant.

Reading an odds ratio: 1 means no association; above 1 means higher odds of the outcome among the exposed; the confidence interval shows
the uncertainty. An observational analysis shows **association**, not proof of cause, and the write-up should say so.

The choice of covariates is a modelling decision that belongs to you. Decide it **before** looking at results, and say why.

## General approach

```text
Using <cohort file>, compare <outcome> between <exposed> and <unexposed>. Report counts and rates for each group, then the unadjusted
odds ratio, then an odds ratio from a logistic regression adjusted for <covariates>, each with a 95% confidence interval. Write the script
to <scripts/analyze.py> and the results to <out/results.md>. State the model and any assumptions, and the number of people in each model.
```

Ask the agent to state, in words, why the adjusted estimate differs from the crude one.

<!-- example -->

## What to check

- Group sizes add up to the cohort.
- The crude odds ratio matches a hand calculation from the 2×2 counts.
- The same number of people is in both models.
- The write-up uses language of association, not causation.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| Different numbers each run | Randomness or a changing input | Fix the input file; the analysis itself here is deterministic |
| Perfect separation or huge confidence intervals | Too few events for the number of covariates | Use fewer covariates, or say the estimate is unstable |
