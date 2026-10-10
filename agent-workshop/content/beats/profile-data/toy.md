---
role: profile-data
scenario: toy
starts_from: the data kit
produces: a profile report (ask the agent to save it as `out/profile.md`)
prompt: |
  Profile clinic_visits.csv using data_dictionary.md. List every data-quality problem you find, with the number of affected rows and
  a few example visit_ids. Separate real errors from things that are probably fine. Do not fix or change anything. Save the report
  as out/profile.md.
---

**Files used:** `clinic_visits.csv`, `data_dictionary.md`.

**Reference results.** The raw file has 7,465 rows. The planted problems, with counts:

| Problem | Count | Notes |
|---|---|---|
| Clinic name variants | 45 rows | Six variants of the three clinic names (case and trailing spaces) |
| Dates in `MM/DD/YYYY` form | 6 rows | The rest are ISO `YYYY-MM-DD` |
| Systolic BP recorded as 0 | 4 rows | Impossible value |
| HbA1c of 20 or more | 10 rows | These look like mmol/mol, not the percent the dictionary specifies |
| Age of 212 | 1 row | Impossible; the same patient has other visits at one consistent age |
| Exact duplicate rows | 15 rows | |
| A `visit_id` shared by two different visits | 2 rows | Different dates and patients under one ID |
| Visits for patients under 18 | 25 rows (8 patients) | Not an error, but relevant to who is eligible later |

**Not errors:** about 4,100 blank HbA1c values and about 880 blank LDL values. The dictionary says blank means "not measured", and
HbA1c is measured only at some visits. A good report says so, rather than flagging them as defects.

If your agent finds a problem not on this list, check it: it may be real (the data is random, so oddities occur), or it may be a
misreading.
