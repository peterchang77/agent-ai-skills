# Bounded Request: Inspect Fictional Survey Data

## Goal

Inspect the fictional survey export and create a data-quality report.

## Inputs

`examples/sample-project/data/raw/survey_results.csv`

## Desired output

Create `output/data_quality_report.md` under the sample project.

## Rules and constraints

- Do not modify the source CSV.
- Preserve every source row in any derived output.
- Flag duplicate IDs, missing scores, and non-numeric scores; do not delete or replace records.
- Use the definitions in `examples/sample-project/notes/`.

## What to verify

Report input row count, duplicate IDs, missing scores, non-numeric scores, and confirmation that the source was not changed.

## What requires approval

Ask before excluding, correcting, or interpreting any record.
