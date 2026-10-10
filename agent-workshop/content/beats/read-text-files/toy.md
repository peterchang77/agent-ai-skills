---
role: read-text-files
scenario: toy
starts_from: the data kit
produces: nothing new; this step only reads
prompt: |
  Read clinic_notes.txt and data_dictionary.md. List the questions I am being asked to answer, and for each one, which columns
  or files I would need. Say which file each point came from.
---

**Files used:** `clinic_notes.txt` (an operations memo) and `data_dictionary.md`.

**What you should see.** Three questions:

1. Which clinics are meeting their HbA1c targets (targets are in `clinic_targets.xlsx`)?
2. Did the Hillcrest follow-up pilot increase HbA1c rechecks, with care about older patients getting more calls, plus a
   one-page abstract with references?
3. If time allows, did Northside's Saturday hours (from March 8) reduce urgent visits?

The columns needed are `clinic`, `hba1c`, `age`, `visit_date`, and `visit_type` from `clinic_visits.csv`, and `pilot_calls.csv`
for question 2. The memo also warns that the data came from three scheduling systems, which hints at inconsistencies to
look for later.
