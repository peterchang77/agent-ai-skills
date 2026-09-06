# Contract: serial cohort manifest

## Required row-level fields

Use equivalent names if the prepared dataset differs, but the output manifest must contain:

```text
transition_id, patient_id, partition,
prior_study_id, current_study_id,
prior_date, current_date, prior_date_source, current_date_source,
prior_image_path_or_id, current_image_path_or_id,
prior_impression, current_impression,
gap_days
```

## Inclusion rules

- Both studies belong to the same patient.
- Both impressions are nonblank after normalization.
- Each retained row satisfies a parsed/otherwise documented `prior_date < current_date`.
- A deterministic frontal image selection rule is documented if a study has multiple candidate images.
- A patient occurs in exactly one of `development`, `validation`, or `test_locked`.
- Split seed and proportions are recorded.

## Required audit outputs

Create an ignored audit JSON/CSV/Markdown artifact containing counts for source rows, date parsing, exclusions by reason, retained transitions, gap distribution, unique patients, and partitions. Include an assertion or failed-run condition for inverted retained pairs and patient leakage.

## Out of scope

Clinical adjudication, use of the locked test set for design choices, and silently fixing malformed dates. If date parsing cannot support the intended exercise, stop and report the limitation.
