# Data dictionary (synthetic)

## clinic_visits.csv: one row per visit, calendar year 2025

| Column | Meaning | Notes |
|---|---|---|
| visit_id | Visit identifier | `V` + 5 digits; should be unique |
| patient_id | De-identified patient | `P` + 4 digits |
| visit_date | Date of visit | ISO `YYYY-MM-DD` expected |
| clinic | Clinic site | Northside, Riverside, Hillcrest |
| age | Age in years at visit | |
| sex | `F` or `M` | |
| visit_type | routine, follow-up, urgent | |
| systolic_bp | Systolic blood pressure, mmHg | |
| hba1c | Glycated hemoglobin, **percent (NGSP)** | blank if not measured |
| ldl | LDL cholesterol, mg/dL | blank if not measured |
| bmi | Body mass index, kg/m^2 | |

A patient is treated as having diabetes if any HbA1c in 2025 is 6.5% or higher.

## pilot_calls.csv: one row per patient who was called by the Hillcrest pilot

| Column | Meaning |
|---|---|
| patient_id | Matches clinic_visits.csv |
| call_date | Date of the call attempt |
| reached | `Y` if the patient was reached and counseled; `N` if not reached |

## Other files

- `clinic_targets.xlsx`: 2025 targets and staffing (formatted for people, not machines).
- `pilot_protocol.docx`: pilot eligibility and outcome definitions.
- `patient_newsletter.pdf`: patient-facing newsletter.
- `clinic_directory.html`: clinic hours and program announcements.
- `staffing.db`: SQLite database with monthly staffing by clinic.
