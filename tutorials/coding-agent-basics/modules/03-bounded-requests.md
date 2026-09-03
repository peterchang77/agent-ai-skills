---
id: bounded-requests
title: Ask for bounded, checkable work
estimated_minutes: 15
prerequisites:
  - model-provider-chat-agent
objectives:
  - write a bounded task request
  - specify verification and approval boundaries
checkpoint: artifact
required_artifacts:
  - request.md
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: concise
  goal-first: full
---

# Ask for Bounded, Checkable Work

## In brief

A strong request gives an agent enough structure to act safely and show its work. You do not need to write code; you need to make the desired result and boundaries clear.

Use this pattern:

```text
Goal:
Inputs:
Desired output:
Rules and constraints:
What to verify:
What requires approval:
```

## Example

```text
Goal: Create a cleaned copy of the survey data and a data-quality summary.
Inputs: data/raw/survey_results.csv
Desired output: output/survey_results_clean.csv and output/data_quality_report.md
Rules: Never change the source. Preserve respondent IDs. Flag duplicates; do not delete them.
What to verify: Report input/output row counts, missing values by column, and duplicate IDs.
What requires approval: Ask before excluding rows or deciding that a value is invalid.
```

## Predict

Which missing field makes it hardest to know whether the agent succeeded: the goal, desired output, or what to verify? Why?

## Try it

Create `request.md` for a small task from your work or copy and adapt [`examples/request-examples/clean-csv-request.md`](../examples/request-examples/clean-csv-request.md). Keep it low risk and use samples or a copy.

## Inspect

Before giving the request to an agent, check that another person could answer all six headings without guessing. In particular, identify the source path, output path, non-negotiable rules, and approval boundary.

## Reflect

Vague request: “Clean up this spreadsheet.”

Bounded request: “Create a cleaned copy, preserve the source, flag ambiguous values, and report what changed.”

What ambiguity did the second version remove?

## Record

Save the final request path and one rule you consider non-negotiable in `progress.md`.

## Checkpoint

Your request is complete when it names a goal, inputs, outputs, constraints, a check, and an approval boundary.
