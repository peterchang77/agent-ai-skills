# Agent context: 02 — Cohort curation with real chronology

## Assignment

Create an auditable cohort builder that reads the prepared metadata and writes a serial-imaging manifest with one same-patient prior/current transition per row. Inspect the actual metadata/schema first and explain how temporal order can be demonstrated before you implement pairing.

## Scientific background

The workshop predicts report-derived temporal change from a patient’s prior and current frontal chest radiograph. A previous sandbox cohort made a serious mistake: it treated `patient_report_date_order` adjacency as chronology. On a parseable subset that field had near-zero relation to actual dates and about 48% of nominal pairs were inverted. A working pipeline can therefore still encode an invalid study question.

The repaired approach parsed exam dates from report headers, documented date source, retained only demonstrable `prior_date < current_date` pairs, and typically used consecutive single-study days. For the workshop, use the prepared data and choose a small feasible cohort; temporal validity and patient-disjoint partitions matter more than sample size.

## Available resources

- Input should be the bounded metadata resource produced or identified in exercise 01, plus any instructor-provided prepared fields/files.
- Actual field names and report formats must be inspected rather than assumed.
- Use a fixed/recorded random seed for deterministic assignments.
- Keep created manifests, audits, and derived data in ignored `data/` or `outputs/` paths.

## Required outcome

Write a manifest containing equivalent fields to:

```text
transition_id, patient_id, partition,
prior_study_id, current_study_id,
prior_date, current_date, prior_date_source, current_date_source,
prior_image_path_or_id, current_image_path_or_id,
prior_impression, current_impression, gap_days
```

Retain only same-patient transitions with nonblank impressions and documented strict `prior_date < current_date`. State and implement a deterministic frontal-image selection rule if needed. Assign each patient to exactly one frozen partition: `development`, `validation`, or `test_locked`.

Produce an audit of source rows, date parsing, excluded rows by reason, retained transitions, gap distribution, unique patients, partition counts, and date-source counts. Include executable checks that no retained pair is inverted and no patient appears in multiple partitions. Preserve exclusion reasons; do not invent/impute dates.

## Boundaries

Do not use report row order as a date substitute, silently retain ambiguous same-day/multi-study orderings, use test outcomes to construct the cohort, or claim clinical validity. If the source data cannot establish chronology, explain the limitation and stop rather than emitting a plausible-looking invalid manifest.

## Definition of a credible result

A reviewer can inspect the manifest/audit, reproduce the same partitions from the seed, verify all `gap_days > 0`, deliberately test an inverted row, and trace why any excluded row was excluded.
