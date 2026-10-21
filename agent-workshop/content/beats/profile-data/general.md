---
role: profile-data
title: Profile the data and find problems
kind: full
summary: Generate a systematic data-quality audit documenting anomalies, null patterns, and unit mismatches without modifying source files.
time: 7 min
teaches: [verification, steering]
needs: [first-look]
---

Observational datasets invariably contain anomalies that can alter downstream statistical estimates. In this exercise, you direct the agent to execute a systematic data-quality audit, quantifying affected record counts and providing concrete examples while keeping raw files strictly untouched.

**Before you start:** The raw dataset and its accompanying data dictionary ([Setup](setup:)).

## Background

Data profiling characterizes dataset distributions and integrity issues without altering records: auditing column types, missingness structures, duplicate keys, physiologically implausible values, and unit discordance. 

Profiling is intentionally **decoupled from data cleaning**. Many apparent anomalies are not data errors; for instance, missing laboratory values often indicate that a test was clinically unnecessary rather than omitted by accident. Furthermore, determining how to address anomalies involves substantive research decisions that belong to the investigator, not the agent ([Steering](concept:steering)).

| Anomaly class | Illustrative manifestation | Methodological risk |
|---|---|---|
| **Entity duplicates** | Multiple rows sharing identical patient IDs and timestamps | Distorts variance estimates and inflates sample size |
| **Categorical discordance** | Inconsistent string casing (e.g., `Site A`, `site a `, `SITE A`) | Fractures categorical strata during regression modeling |
| **Implausible values** | Negative ages, blood pressure of 0, heart rate of 999 | Biases distribution means and regression coefficients |
| **Unit discordance** | Laboratory values recorded in both mg/dL and mmol/L | Introduces bimodal artifactual distributions |
| **Mixed date formats** | Interleaved `YYYY-MM-DD` and `MM/DD/YYYY` strings | Triggers parsing failures or incorrect temporal sorting |
| **Structured missingness** | Unpopulated fields across specific visit types | Violates Missing Completely at Random (MCAR) assumptions |
| **Content that contradicts its metadata** | A file whose header says one thing and whose contents show another (e.g. an image stored upside down or mirrored) | Silently corrupts any measurement taken from the content |

Not all data is a table. For files such as images, the same audit applies to two layers: the **metadata** (headers and tags, which code can check exhaustively) and the **content** itself (which code can check only partly, so a person may need to look). Say which layer each finding comes from.

## General methodology

Direct the agent to profile the dataset against the data dictionary, quantifying affected rows and isolating real errors from expected structural missingness:

```text
Profile <data file> using <data dictionary>.
Document every data-quality anomaly found, reporting the total count of affected rows and 2-3 illustrative row identifiers.
Distinguish definitive data corruption from expected structural nulls.
Do not modify or clean any records yet.
```

Follow up by evaluating potential remediation strategies: *"For each identified issue, summarize plausible remediation approaches and describe how each option could alter downstream analytical findings."* This analysis establishes the decision space for the subsequent planning stage.

<!-- example -->

## Verification criteria

- **Explicit row accounting:** Every reported anomaly includes an exact count of affected records and inspectable row identifiers.
- **Contextual null assessment:** Missing values are evaluated against data dictionary definitions rather than flagged generically as corruption.
- **Strictly read-only execution:** The raw dataset remains completely unmodified (verified via file checksums or modification timestamps).

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Agent modifies files during profiling | Prompt allowed ambiguous write permissions | Intervene immediately: *"Profile the data only; do not write or modify any files"* |
| Unit discrepancies overlooked | Script validated basic datatypes (float vs string) without evaluating numerical range plausibility | Instruct the agent to compare empirical minimum and maximum ranges against expected physiological boundaries in the data dictionary |
