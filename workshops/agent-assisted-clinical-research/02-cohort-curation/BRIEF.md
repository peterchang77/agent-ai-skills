# 02 — Cohort curation: make time real

## Learning goal

Ask an agent to construct a small, auditable serial-imaging cohort while testing—not assuming—the temporal meaning of source fields.

Read [`CONTEXT.md`](CONTEXT.md), [`CONTRACT.md`](CONTRACT.md), and [`ACCEPTANCE.md`](ACCEPTANCE.md). Write your own request, then ask the agent first to inspect the metadata schema and propose a date-validation approach.

## Deliverable

Create a cohort-builder that reads the prepared metadata and writes a manifest with one prior/current transition per row. It must construct patient-disjoint development, validation, and locked-test partitions and emit an audit summary.

## The deliberate trap

A prior Report2Delta cohort treated `patient_report_date_order` adjacency as chronology. It was not chronological: among parseable pairs, roughly 48% were inverted. A valid pipeline can therefore produce an invalid task. Do not use a named order/index field as a date substitute without direct evidence.

## Expected working pattern

Have the agent inspect date-bearing fields or report headers, explain unparseable/ambiguous cases, then build only pairs where chronology is demonstrable. Require it to preserve excluded-row reasons and to calculate an audit showing `prior_date < current_date` for every retained pair.

## Recovery

After your own attempt, compare your request with [`../reference-prompts/02-cohort-curation.md`](../reference-prompts/02-cohort-curation.md).
