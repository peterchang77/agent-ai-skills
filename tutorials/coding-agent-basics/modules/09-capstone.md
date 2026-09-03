---
id: capstone
title: Act 7 — Review and hand off the trustworthy draft
estimated_minutes: 45
prerequisites:
  - model-selection-and-connection
mission_act: review-the-draft
objectives:
  - direct an end-to-end review of the reporting workflow
  - verify durable artifacts, validation evidence, and handoff readiness
checkpoint: capstone
required_artifacts:
  - request.md
  - AGENTS.md
  - validation-note.md
  - .agents/skills/monthly-report/SKILL.md
  - .tutorial/handoff.md
  - model-selection.md
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: full
  goal-first: full
---

# Act 7 — Review and Hand Off the Trustworthy Draft

## Situation

The mission has a draft report, instructions, a reusable procedure, validation evidence, and a handoff. The final obstacle is proving that these parts fit together without pretending that a structural check proves the report is correct.

## Your move

Tell the agent to review the mission artifacts and run the structural validator. Require it to report:

- which required files exist;
- which evidence confirms raw inputs stayed separate from outputs;
- exceptions still requiring human judgment; and
- what the validator cannot prove.

Use the sample project or a safe equivalent. Do not publish, send, or modify raw data.

## Agent mode

The agent runs the validator and reports its exact result. It must distinguish a passed structure check from semantic correctness, accurate calculations, approval to publish, or suitability for real data.

## Inspect

From `tutorials/coding-agent-basics/`, run or ask the agent to run:

```bash
python3 checks/validate_tutorial.py --project examples/sample-project
```

Then inspect `request.md`, `AGENTS.md`, `validation-note.md`, `.agents/skills/monthly-report/SKILL.md`, `.tutorial/handoff.md`, and `model-selection.md`. Confirm that they agree on protected sources, outputs, approval boundaries, and unresolved exceptions.

## Unlock

You have directed an agent through a complete, inspectable workflow:

```text
read-only survey → bounded request → protected investigation → validation
→ durable project rules → reusable skill → handoff and operating decision → review
```

Code made the repeatable inspection and checking possible. Your judgment set the objective, boundaries, interpretation, and approval point.

## Checkpoint

Act 7 is complete when the mission log links the required artifacts and the learner can identify one responsibility that remains human: interpreting ambiguity, approving changes, or deciding whether to distribute the report.
