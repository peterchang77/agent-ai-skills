# Bounded Request: Fictional Monthly Survey Report

## Goal

Create a draft data-quality summary for the fictional monthly survey export.

## Inputs

`data/raw/survey_results.csv`

## Desired output

Create a draft summary in `output/data_quality_report.md`. Do not publish or send it.

## Rules and constraints

- Do not modify `data/raw/survey_results.csv`.
- Preserve every source record in any derived output.
- Use `notes/metric-definitions.md` and `notes/reporting-rules.md`.
- Flag duplicate IDs, missing scores, and non-numeric scores. Do not correct, exclude, or interpret them.

## What to verify

Report the source row count, duplicate IDs, missing scores, non-numeric scores, and source-preservation check.

## What requires approval

Ask before changing metric definitions, correcting source data, excluding a record, or distributing a report.
