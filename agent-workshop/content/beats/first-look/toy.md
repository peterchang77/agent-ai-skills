---
role: first-look
scenario: toy
starts_from: the data kit
produces: nothing saved; this is a quick exploratory answer (ask the agent to save its script if you want to keep it)
prompt: |
  Using clinic_visits.csv, data_dictionary.md and the targets in clinic_targets.xlsx, tell me which clinics meet their HbA1c target.
  Definition: adult patients (age 18 or older) with diabetes (any HbA1c of 6.5 or higher in 2025), whose most recent HbA1c is below
  8.0. Report each clinic's share with the number of patients it is based on. Do not change or exclude any data; tell me what you
  notice about the data.
---

**Files used:** `clinic_visits.csv`, `data_dictionary.md`, `clinic_targets.xlsx` (targets: Northside 60%, Riverside 60%, Hillcrest 55%).

**What you should see (reference results on the raw data, with this definition)**

| Clinic | Patients | Share with most recent HbA1c < 8.0 | Target | Meets target? |
|---|---|---|---|---|
| Hillcrest | 478 | 57.7% | 55% | Yes |
| Northside | 295 | 65.1% | 60% | Yes |
| Riverside | 229 | 53.3% | 60% | No |

Your numbers may differ slightly if the agent reads a rule differently (for example how it treats ties or missing values); the
conclusion for each clinic should match.

**What to notice.** The raw data also produces a few extra "clinics" with tiny counts (`northside `, `hillcrest`, and so on). These
are spelling variants of the three real clinics, and they are a hint that the data needs cleaning. The next step looks for such
problems systematically.

**Optional follow-up.** Riverside misses its target. The directory page (`clinic_directory.html`) and `staffing.db` say a nurse
practitioner position has been vacant since June. Ask: "Does staffing explain Riverside's result?" A careful agent will say that
staffing is context, not evidence of cause, and will check whether HbA1c actually changed after June (it did not change meaningfully
in this data).
