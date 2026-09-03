# Validation Note

## Source and output paths

- Source: `data/raw/survey_results.csv`
- Output: `output/data_quality_report.md`

## Source preservation

- The report was created separately under `output/`; no step writes to `data/raw/`.
- A human should confirm source file status or checksum before using this pattern with a real export.

## Checks performed

- Counted CSV data rows.
- Counted repeated `respondent_id` values.
- Identified blank score fields.
- Identified non-empty scores that are not numeric.

## Counts and exceptions

- Input rows: 6
- Output rows: not applicable; this example produces a report, not a derived data table.
- Duplicate or invalid records: `R-002` is duplicated; one score is missing (`R-003`); `R-005` has non-numeric score `not-recorded`.

## Assumptions and human review needed

- No duplicate was removed and no score was corrected.
- A report owner must decide how to interpret the duplicate and invalid values before publication.
