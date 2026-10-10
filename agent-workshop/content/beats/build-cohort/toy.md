---
role: build-cohort
scenario: toy
starts_from: the `cleaned` checkpoint
produces: "`scripts/build_cohort.py`, `out/cohort.csv`, `out/cohort_flow.md`"
prompt: |
  Read pilot_protocol.docx (or text/pilot_protocol.md if you converted it earlier). Quote the exact eligibility rules, index visit,
  exposure and outcome window. Then write scripts/build_cohort.py that applies them to data/clean/visits_clean.csv and pilot_calls.csv
  and writes out/cohort.csv (one row per patient, with columns for age, sex, index HbA1c, whether the patient was reached by a call, and
  whether HbA1c was rechecked) and out/cohort_flow.md (patients remaining after each step). Tell me every place you had to interpret
  the protocol. Report the count with each step.
---

**Files used:** `pilot_protocol.docx`, `data/clean/visits_clean.csv`, `pilot_calls.csv`.

**Rules to be quoted from the protocol.** Adults (18 or older) at Hillcrest. Index visit: the first visit from 2025-04-01 to 2025-08-31 with
a measured HbA1c of 7.0% or higher. Exposure: reached by a pilot call (`reached` = `Y`). Outcome: any measured HbA1c from 14 to 120 days after
the index visit.

**Reference flow table**

| Step | Patients |
|---|---|
| Hillcrest patients with any HbA1c | 820 |
| Adults (age >= 18) | 819 |
| Index visit: first HbA1c >= 7.0% from 2025-04-01 to 2025-08-31 | 251 |

**Reference cohort.** 251 patients; 92 reached by a call; 92 rechecked.

**Interpretation points to look for.** "Reached" means `reached = Y`, not merely a call attempt: 11 further calls were not completed, and
those patients belong in the comparison group. Window boundaries (14 and 120 days) are inclusive. A patient with no measured HbA1c
cannot have an index visit. If the agent counts attempted calls as exposed, the exposed group will be 103, not 92, which is a good example
of why the definition has to be checked.

A reference version is in `scenarios/toy/checkpoints/cohort/out/`.
