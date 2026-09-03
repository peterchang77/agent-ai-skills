---
id: inspect-and-validate
title: Inspect and validate agent work
estimated_minutes: 15
prerequisites:
  - bounded-requests
objectives:
  - distinguish a plausible answer from evidence
  - perform a source-preserving validation check
checkpoint: artifact
required_artifacts:
  - validation-note.md
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: concise
  goal-first: full
---

# Inspect and Validate Agent Work

## In brief

An agent's explanation can sound credible even when its work is incomplete or wrong. Validation means checking the result against evidence appropriate to the task.

A useful default is:

```text
preserve source → create derived output → compare → check exceptions → record evidence
```

## Predict

A report says a CSV was cleaned successfully. What evidence would make you trust that source records were not silently lost?

Possible evidence includes separate paths, row counts before and after, duplicate or exclusion reports, and a readable record of applied rules.

## Try it

Use the sample project. Ask an agent to inspect `data/raw/survey_results.csv` and create a proposed—not destructive—data-quality report in `output/`. Give it the request from the prior module.

Do not ask it to edit the source. If it proposes a cleaning rule that needs judgment, require it to flag the case rather than decide silently.

## Inspect

Create `validation-note.md` with:

- source path and confirmation it remains unchanged;
- output paths;
- input and output row counts, if an output was created;
- checks performed;
- exceptions or assumptions needing review.

For documents, validation might be a side-by-side comparison. For data, it may include counts, schemas, ranges, IDs, or a sample review. For a script, it may include tests and a small known input.

## Reflect

Why is “the agent said it worked” not enough evidence for a decision that affects other people?

## Record

Link your validation note from `progress.md`.

## Checkpoint

You can state what was checked, what was not checked, and who must review any remaining ambiguity.
