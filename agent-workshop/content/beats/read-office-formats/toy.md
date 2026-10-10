---
role: read-office-formats
scenario: toy
starts_from: the data kit
produces: a `text/` folder with plain-text versions of the three files
prompt: |
  Read clinic_targets.xlsx, pilot_protocol.docx, and patient_newsletter.pdf. For each, tell me which tool you used and what was
  hard to extract. Then list each clinic's HbA1c target, the pilot's eligibility rules and outcome definition, and anything in the
  newsletter about Saturday hours. Finally, save plain-text versions of all three in a folder called text/ and tell me what changed
  in each conversion.
---

**Files used:** `clinic_targets.xlsx`, `pilot_protocol.docx`, `patient_newsletter.pdf`.

**What you should see**

| File | Expected |
|---|---|
| `clinic_targets.xlsx` | Two sheets, `Targets` and `Staffing (planned)`. The real header is on row 3, under a merged title row. Targets are fractions formatted as percent: Northside 0.60, Riverside 0.60, Hillcrest 0.55, for "most recent HbA1c < 8.0% (share of adult patients with diabetes)". |
| `pilot_protocol.docx` | Eligibility: adults (18 or older) at Hillcrest; index visit is the first visit from 2025-04-01 to 2025-08-31 with HbA1c of 7.0% or higher. Procedure: a nurse call within 10 days; record the date and whether the patient was reached (Y/N). Outcome: any HbA1c from 14 to 120 days after the index visit. A one-row table (Hillcrest, 2025-04-01, R. Alvarez, RN). |
| `patient_newsletter.pdf` | Three plain lines, including that Saturday hours are available at Northside and the Hillcrest follow-up call program. Extraction is clean because the PDF has a real text layer. |

The `text/` folder is what later work should read from. The protocol's definitions (index visit, outcome window) are exactly what the
pilot analysis needs, so they are worth saving as text.
