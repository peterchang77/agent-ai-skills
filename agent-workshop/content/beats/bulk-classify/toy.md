---
role: bulk-classify
scenario: toy
starts_from: the committed project with `.env` set up
produces: "`scripts/classify_notes.py`, `out/note_labels.csv`"
prompt: |
  Write scripts/classify_notes.py that reads visit_notes.csv and, for each note, asks the model for exactly one label from [medication_refill, new_symptom,
  chronic_followup, preventive, administrative], returned as JSON. Save results incrementally to out/note_labels.csv so it can resume, with retries and a short
  delay. Add --limit and --dry-run (print the first prompt and an estimated cost; call nothing). Record the model name and prompt in the output. Then run the
  dry run and --limit 5, and show me both.
---

**Files used:** `visit_notes.csv` (200 short synthetic notes), `visit_notes_labeled_sample.csv` (correct labels for the first 30).

**Steps.** Dry run, then `--limit 5`, check the five by eye, estimate the total from the first batch, set a spending cap, then run all 200. Compare to the 30 labelled notes:

```text
Compare out/note_labels.csv with visit_notes_labeled_sample.csv for the 30 labelled notes. Report accuracy, and list the notes it got wrong.
```

**What you should see.** A table of predicted vs. correct labels for the 30 notes and a list of mismatches. Expect high accuracy, since these synthetic notes are
formulaic: a simple keyword rule gets about 97% on them. A real set of clinical notes would be harder, so treat the exercise as a test of the *workflow* (dry run, cap,
resume, accuracy check), not as evidence of how well a model classifies real notes.

**Cached result.** If you cannot use an API, the labelled sample is enough to practise the comparison step with any set of labels.
