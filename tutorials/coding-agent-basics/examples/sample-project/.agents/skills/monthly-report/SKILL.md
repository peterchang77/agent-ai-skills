---
name: monthly-report
description: Prepare a draft, validated monthly report from approved CSV exports. Use when asked to inspect monthly exports, calculate approved metrics, create a draft report, or report data-quality exceptions.
---

# Monthly Report

## Scope

Work only with approved sources. Do not edit raw inputs, publish a report, or resolve ambiguous records without approval.

## Workflow

1. Read `references/metric-definitions.md` and the project reporting rules.
2. Inspect expected inputs and report missing files.
3. Write all generated work to the project's output directory.
4. Record input counts, transformations, exceptions, and assumptions.
5. Run the project validation check when available.
6. Summarize outputs, evidence, and review items.

## Approval boundaries

Ask before changing a metric definition, excluding a record, correcting source data, or distributing a result.

## Expected outputs

- a draft report;
- a metrics or quality summary;
- a validation note naming sources, checks, exceptions, and assumptions.

## Validation

Confirm source inputs remain unchanged. Compare counts and flag missing, duplicate, or invalid records according to the referenced definitions.
