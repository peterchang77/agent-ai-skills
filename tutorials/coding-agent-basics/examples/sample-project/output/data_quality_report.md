# Data Quality Report — Draft

## Reporting period

Fictional January 2026 fixture.

## Inputs inspected

- `data/raw/survey_results.csv` (6 data rows)

## Summary

The fixture contains four unique complete-response IDs plus one incomplete response and one repeated ID. This draft does not calculate a final score because the data contains review-needed exceptions.

## Data-quality exceptions

- `R-002` appears twice.
- `R-003` has a missing score.
- `R-005` has non-numeric score `not-recorded`.

## Assumptions and review needed

No source values were changed, excluded, or interpreted. A report owner must decide how to handle each exception.

## Validation performed

Counts and exceptions match `validation-note.md` and can be reproduced with `.agents/skills/monthly-report/scripts/check_survey.py`.
