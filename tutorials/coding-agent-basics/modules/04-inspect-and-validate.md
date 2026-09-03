---
id: inspect-and-validate
title: Act 3 — Investigate without changing sources
estimated_minutes: 15
prerequisites:
  - bounded-requests
mission_act: investigate-safely
objectives:
  - direct a source-preserving investigation
  - inspect validation evidence rather than a plausible explanation
checkpoint: artifact
required_artifacts:
  - validation-note.md
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: concise
  goal-first: full
---

# Act 3 — Investigate Without Changing Sources

## Situation

The job ticket is ready. Now the agent may inspect the CSV and create a draft quality report, but it must not decide which unusual records to remove or correct.

## Your move

Use `request.md` to direct the agent to inspect `data/raw/survey_results.csv`, create a draft report under `output/`, and write `validation-note.md`. Explicitly require it to report source count, duplicate IDs, missing scores, non-numeric scores, and any assumption it could not safely make.

## Agent mode

The agent inspects and writes only derived artifacts. It should preserve every raw record, cite paths, and flag uncertainty. If it proposes a cleaning rule, it must ask for approval before applying it.

## Inspect

Open the draft report and validation note. Compare the listed counts and exceptions to the raw CSV or run the sample skill’s `scripts/check_survey.py`. Confirm that `data/raw/` was not used as an output location.

## Unlock

Validation is not “the agent said it worked.” It is evidence appropriate to the work: paths, counts, exceptions, comparison, a reproducible check, and a record of what was not decided. For data, a useful default is:

```text
preserve source → create derived output → compare → flag exceptions → record evidence
```

## Checkpoint

Act 3 is unlocked when the report and validation note make both the findings and the remaining review work visible.
