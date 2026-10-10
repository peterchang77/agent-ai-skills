# Cleaning decisions (analyst-approved)

Original files are never modified. Cleaned data goes in data/clean/, other outputs in out/.

1. Clinic names: strip whitespace and normalise case.
2. Dates: MM/DD/YYYY values are converted to ISO YYYY-MM-DD.
3. Exact duplicate rows: removed.
4. A visit_id shared by two different visits: both rows kept and flagged in `id_conflict`.
5. Systolic BP of 0: set to missing.
6. HbA1c values of 20 or more are in mmol/mol, not %: converted with NGSP = IFCC / 10.929 + 2.15.
7. Age above 120: repaired from the same patient's other visits (analyst's choice).
8. Patients under 18 are kept in the cleaned data and excluded at the cohort step.
