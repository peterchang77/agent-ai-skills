---
role: saturday-hours
scenario: toy
starts_from: the `cleaned` checkpoint
produces: nothing required; ask for `out/saturday.md` to keep the result
prompt: |
  Using data/clean/visits_clean.csv, compare the share of visits that are urgent before and after 2025-03-08 at Northside. Then do the same
  for the other two clinics combined. Report the counts, the change at each, and the difference between the changes with a 95% confidence
  interval. Also check whether the months before the change look similar across sites, and state your assumptions.
---

**Files used:** `data/clean/visits_clean.csv`, `clinic_directory.html` (confirms Saturday hours began 2025-03-08).

**Reference results**

| Group | Period | Urgent share | Visits |
|---|---|---|---|
| Northside | before 2025-03-08 | 28.0% | 382 |
| Northside | after | 14.1% | 1,850 |
| Other clinics | before | 24.8% | 990 |
| Other clinics | after | 20.5% | 4,228 |

The difference in differences is about −9.6 percentage points (95% CI about −15 to −4).

**What this shows.** Looking only at Northside, urgent visits fell by about 14 points. The other clinics also fell by about 4 points over the same
period (partly seasonal: urgent visits are more common in winter months, and the "before" period is mostly winter). The comparison-adjusted
estimate is therefore smaller than the naive one. That gap is the reason for the comparison group.

**Caution about the baseline.** The "before" period is only about ten weeks, mostly winter. A good report mentions it.
