---
id: bounded-requests
title: Act 2 — Define the reporting job
estimated_minutes: 15
prerequisites:
  - model-provider-chat-agent
mission_act: define-the-job
objectives:
  - direct an agent to create a bounded task request
  - set verification and approval boundaries
checkpoint: artifact
required_artifacts:
  - request.md
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: concise
  goal-first: full
---

# Act 2 — Define the Reporting Job

## Situation

“Clean this spreadsheet” leaves an agent to guess what clean means, where outputs belong, and when a person must decide. The mission needs a job ticket before the investigation begins.

## Your move

Tell the agent to draft `request.md` for this report. Include, in your own words:

```text
Goal:
Inputs:
Desired output:
Rules and constraints:
What to verify:
What requires approval:
```

For this mission, make the raw CSV read-only, put outputs under `output/`, and require ambiguous records to be flagged rather than resolved.

## Agent mode

The agent drafts the file and reports its path. It should ask you to fill any consequential gap rather than choosing a deletion, correction, or publication rule itself.

## Inspect

Read `request.md` as though another person will use it tomorrow. Verify it names a source path, a separate output path, a non-negotiable rule, a check, and an approval boundary. Revise the command if any of those are missing.

## Unlock

A bounded request is an operational contract, not a polished prompt. It turns a broad wish into inspectable work: desired output plus constraints, evidence, and a point where the agent must stop for human judgment.

## Checkpoint

Act 2 is unlocked when `request.md` lets another operator run the first report step without guessing.
