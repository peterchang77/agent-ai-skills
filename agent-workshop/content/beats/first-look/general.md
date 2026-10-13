---
role: first-look
title: A first answer from raw data
kind: full
summary: Generate an initial exploratory estimate from uncleaned data, requiring explicit definitions and denominators to establish an uncleaned baseline.
time: 6 min
teaches: [verification, inputs, scoping-work]
needs: [read-text-files]
---

An agent can calculate preliminary metrics across a raw dataset in minutes. This exercise demonstrates how to request an initial exploratory estimate while enforcing strict verification standards: requiring explicit variable definitions, reporting exact denominators, and documenting baseline anomalies before cleaning begins.

**Before you start:** A raw dataset, an accompanying data dictionary, and any relevant performance target files ([Setup](setup:)).

## Background

Generating an initial estimate from uncleaned data provides useful orientation, but represents **exploratory profiling rather than definitive findings**. Uncurated observational datasets almost always contain latent anomalies—such as placeholder test entries, date format discrepancies, or unit mismatches—that silently distort calculations. 

A rigorous first pass must explicitly declare the analytical definitions used and report the active sample sizes (denominators) supporting each metric, establishing an empirical baseline against which subsequent cleaning impacts can be audited ([Verification](concept:verification)).

## General methodology

Include the exact operational definition within the prompt to prevent the agent from assuming informal definitions, and mandate explicit sample size reporting:

```text
Using <data file> and <data dictionary>, evaluate: <research question>.
Apply this operational definition: <definition>.
Report every calculated metric alongside the exact count of underlying rows or individuals (denominator).
Do not filter, clean, or modify any data points yet; report the raw numbers and note any data anomalies observed.
```

Explicitly instructing the agent not to filter data keeps the initial baseline honest: you observe what the uncurated records state, leaving data cleaning decisions for subsequent planned stages ([Scoping work](concept:scoping-work)).

<!-- example -->

## Verification criteria

- **Operational definition fidelity:** The agent adhered strictly to the provided definition rather than substituting a default metric.
- **Unambiguous denominators:** Every summary percentage or mean displays both the numerator and the active denominator.
- **Anomaly transparency:** The agent flags irregular records or impossible values observed during calculation without silently omitting them.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Calculation uses an unexpected definition | Operational definition was omitted or ambiguous | Restate the exact formula and prompt: *"Which mathematical definition was applied here?"* |
| Missing denominators | Prompt did not explicitly mandate sample counts | Instruct the agent: *"Report the exact row and patient counts supporting each metric"* |
| Silent record exclusions | Scripting library omitted nulls or outliers automatically | Direct the agent to report the total count of unmapped or dropped rows |
