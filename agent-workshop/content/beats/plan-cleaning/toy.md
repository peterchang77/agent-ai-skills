---
role: plan-cleaning
scenario: toy
starts_from: the data kit (and, optionally, the profile from the previous step)
produces: "`notes/cleaning-decisions.md` with your decisions"
prompt: |
  Do not change any files. Using the data problems you found in clinic_visits.csv, propose a cleaning plan. For each problem give the
  options, the consequences of each, and your recommendation. Group the mechanical fixes together, and ask me about any judgement call
  rather than deciding it yourself. When we agree, write the final decisions to notes/cleaning-decisions.md.
---

**Files used:** `clinic_visits.csv`, `data_dictionary.md`.

**Mechanical fixes (approve together).** Normalise clinic names; convert the six `MM/DD/YYYY` dates to ISO form; remove the 15 exact
duplicate rows; set the four systolic BP values of 0 to missing.

**Judgement calls (the agent should ask you).**

| Problem | Options | Why it is your decision |
|---|---|---|
| HbA1c values of 20 or more (10 rows) | Convert from mmol/mol to % using the standard formula; set to missing; exclude the rows | Converting assumes they are mmol/mol. That is likely, but it is an assumption about how the data was recorded. Setting to missing is safer, at the cost of 10 values. |
| Age 212 (1 row) | Treat as a typo for the patient's real age (their other visits give one consistent age, 70); set to missing; exclude the row | Repairing assumes the other visits are right. Whether you accept that depends on how much you trust the extract. |
| Two different visits sharing one `visit_id` (2 rows) | Keep both and flag; drop one; assign new IDs | Dropping loses a real visit; keeping may break a join on `visit_id`. |
| Patients under 18 (8 patients) | Keep in the cleaned data and exclude later at the analysis step; drop now | The pilot only covers adults, but other questions may not. Excluding later keeps your options open. |

**The point of this step.** There is no single correct choice for the age of 212 or the unit problem; the reference solution
converts the units, repairs the age from other visits, keeps both rows with a shared ID (flagged), and keeps minors until the cohort step.
You can choose differently, as long as you decide deliberately and write it down. If you set the values to missing instead, results change
very slightly, not materially; the lesson is that the decision is recorded, not that it matches ours.

The reference decisions are in `scenarios/toy/checkpoints/cleaned/notes/cleaning-decisions.md`.
