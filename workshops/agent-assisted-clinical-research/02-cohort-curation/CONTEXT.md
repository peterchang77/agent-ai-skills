# Context: longitudinal cohort

The task predicts report-derived change from a prior/current frontal chest-radiograph pair. A row must represent a same-patient transition with a temporally valid prior study and current study.

The sandbox’s first cohort was invalid because `patient_report_date_order` did not encode chronology. On a parseable subset, it correlated near zero with dates, about 48% of nominal prior/current pairs were inverted, and report comparison language usually referred to another study. The repaired cohort parsed report-header dates, retained only `prior_date < current_date`, and linked consecutive single-study days. Date recovery from a report comparison section may be useful, but must be recorded distinctly from header parsing.

For this workshop, construct a smaller cohort appropriate to the prepared data and runtime. The exact number is not important. Valid temporal roles and patient-disjoint splits are.

A defensible output uses dates rather than report ordering; retains a `date_source` / exclusion reason; includes prior/current report text paths or IDs and image paths or IDs; and saves a seed, filtering rules, and split assignments.

Do not use report text to choose model partitions. Do not silently fabricate or impute a date when parsing fails.
