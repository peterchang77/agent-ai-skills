---
role: clean-data
scenario: toy
starts_from: the data kit plus `notes/cleaning-decisions.md` (restore the `cleaned` checkpoint and delete `scripts/`, `data/clean/` and `out/` if you want to rebuild from scratch)
produces: "`scripts/clean_visits.py`, `data/clean/visits_clean.csv`, `out/cleaning_flow.md`"
prompt: |
  Implement the decisions in notes/cleaning-decisions.md as scripts/clean_visits.py. It must read clinic_visits.csv, write
  data/clean/visits_clean.csv without modifying the original, and write out/cleaning_flow.md with the starting row count, the rows
  affected by each rule, and the final row count. Run it and confirm the numbers add up.
---

**Files used:** `clinic_visits.csv`, `notes/cleaning-decisions.md`.

**Reference flow table (with the reference decisions)**

| Step | Rows |
|---|---|
| Raw rows | 7465 |
| US-style dates converted | 6 |
| Exact duplicate rows removed | 15 |
| Rows sharing a visit_id (flagged, kept) | 2 |
| Systolic BP of 0 set to missing | 4 |
| HbA1c converted from mmol/mol to % | 10 |
| Impossible ages repaired from other visits | 1 |
| **Final rows** | **7450** |

Check: 7,465 − 15 duplicates = 7,450. The other rules change values, not row counts. If your decisions differ (for example you drop the
unit-mismatch rows), your final count and flow table will differ; the check is that your table matches **your** decisions.

The reference script is `scenarios/toy/checkpoints/cleaned/scripts/clean_visits.py`. Compare yours to it only after you have checked yours.
