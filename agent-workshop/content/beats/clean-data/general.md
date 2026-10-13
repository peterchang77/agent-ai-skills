---
role: clean-data
title: Clean the data with a script, and show the flow
kind: full
summary: Implement approved cleaning rules in a non-destructive script that produces cleaned datasets and a reconciled record-flow table.
time: 7 min
teaches: [verification, tools]
needs: [plan-cleaning]
---

In this exercise, you implement the agreed data cleaning protocol as a standalone, non-destructive script. Running this script generates the cleaned dataset alongside a formal record-flow table accounting for every altered or dropped row. This approach transforms cleaning from an ephemeral conversation into a deterministic, reproducible computational pipeline.

**Before you start:** A documented data cleaning protocol ([Plan the cleaning](beat:plan-cleaning)) or a restored project checkpoint ([Setup](setup:restore-a-starting-point)).

## Background

Rigorous data curation adheres to three foundational computational principles:

- **Programmatic implementation:** Cleaning logic is executed via an inspectable script (e.g., Python using `pandas` or `polars`) rather than manual spreadsheet edits, allowing identical transformations on future dataset releases.
- **Non-destructive workflows:** The raw input data remains strictly read-only and immutable. Cleaned outputs and intermediate tables are written to a separate directory (such as `data/clean/`).
- **Conservation of records (Flow accounting):** A **record-flow table** tracks total counts at each processing stage, showing the starting row count, records affected by each specific rule, and the final retained count. Reconciling counts proves that no records were silently lost or unintentionally duplicated ([Verification](concept:verification)).

## General methodology

Direct the agent to translate the agreed cleaning decisions into a standalone script, mandating an accompanying flow table to verify record counts:

```text
Implement the rules in <decisions file> as an executable script (<scripts/clean.py>) that reads <raw file> and writes <clean file> without modifying the original input.
Generate a record-flow table (<out/cleaning_flow.md>) documenting initial row counts, rows modified or excluded by each rule, and the final row count.
Run the script and verify that initial rows minus excluded rows strictly equals the final row count.
```

The resulting script functions as a permanent, reusable tool in your computational pipeline ([Tools](concept:tools)).

<!-- example -->

## Verification criteria

- **Raw data immutability:** The raw dataset file remains completely unaltered (verified by inspecting file checksums or timestamps before and after execution).
- **Exact flow reconciliation:** Initial row count minus all documented exclusions strictly equals the final cleaned row count in `out/cleaning_flow.md`.
- **Consistency with data profiling:** Row exclusion counts match the anomaly counts identified during initial profiling.
- **Auditable script logic:** Each transformation in `scripts/clean.py` maps cleanly to an approved rule in the cleaning protocol.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Flow table counts do not reconcile | Overlapping filtering rules or unhandled nulls silently dropped rows | Instruct the agent: *"Reconcile row counts step-by-step and report any overlapping exclusions"* |
| Script overwrote the raw input file | Output file path was set identical to the input path | Restore the raw file from backup or checkpoint; configure the script to write exclusively to an isolated `data/clean/` directory |
