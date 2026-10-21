---
role: bulk-classify
scenario: imaging
starts_from: the committed project with `.env` set up
produces: "`scripts/classify_reports.py`, `out/report_labels.csv`"
prompt: |
  Write scripts/classify_reports.py that reads radiology_reports.csv and, for each report, asks the model whether the report says a pneumothorax is present now, using exactly one label from [present, absent, uncertain], returned as JSON. A
  pneumothorax that has resolved is absent, and a report that says it cannot be excluded or is equivocal is uncertain. Save results incrementally to out/report_labels.csv so it can resume, with retries and a short delay. Add --limit and --dry-run (print the first prompt and
  an estimated cost; call nothing). Record the model name and prompt in the output. Then run the dry run and --limit 5, and show me both.
---

**Files used:** `radiology_reports.csv` (200 short synthetic reports), `radiology_reports_labeled_sample.csv` (correct categories for the first 30).

**Steps.** Dry run, then `--limit 5`, check the five by eye, estimate the total from the first batch, set a spending cap, then run all 200. Compare to the 30 labelled reports:

```text
Compare out/report_labels.csv with radiology_reports_labeled_sample.csv for the 30 labelled reports. Report accuracy, show the table of predicted vs. correct categories, and list the reports it got wrong.
```

**What you should see.** A table of predicted vs. correct categories for the 30 reports and a list of mismatches. Expect high accuracy, since these synthetic reports are formulaic; a real set of reports would be harder (negation, hedged wording, comparison with older studies).
The difficult cases to look at first are the **resolved** pneumothoraces ("previously seen... has resolved", which are *absent*) and the hedged ones ("difficult to exclude", "may represent a skin fold", which are *uncertain*). In the full set of 200, 114 are absent, 48 present and 38 uncertain.

**Not a link to the images.** The reports were written from templates and do not describe the specific images they are attached to, so do not use them to check a model's score on that image. Treat the exercise as a test of the *workflow* (dry run, cap, resume, accuracy check), not as evidence of how well a
model reads real reports.

**Cached result.** If you cannot use an API, the labelled sample is enough to practise the comparison step with any set of labels.
