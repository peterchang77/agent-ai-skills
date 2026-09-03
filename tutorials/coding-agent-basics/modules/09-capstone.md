---
id: capstone
title: Build a reliable reporting workflow
estimated_minutes: 45
prerequisites:
  - model-selection-and-connection
objectives:
  - apply the course concepts in one inspectable workflow
  - create durable instructions, a skill outline, validation evidence, and a handoff
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

# Capstone: Build a Reliable Reporting Workflow

## Scenario

A team receives monthly CSV exports and needs a draft summary. The source files must remain unchanged. Ambiguous records need human review before publication.

Use [`examples/sample-project/`](../examples/sample-project/) or a safe equivalent. Keep all generated work separate from `data/raw/`.

## Build

1. **Bound the task.** Create `request.md` for the report workflow.
2. **Set project rules.** Create or adapt `AGENTS.md` with purpose, protected sources, output paths, and completion checks.
3. **Preserve knowledge.** Put metric definitions and decisions in `notes/`.
4. **Package the repeatable part.** Create a focused `SKILL.md` under `.agents/skills/monthly-report/`.
5. **Validate.** Create `validation-note.md` that records input/output paths, checks, assumptions, and exceptions.
6. **Choose intentionally.** Create `model-selection.md` for this workflow.
7. **Prepare resumption.** Update `.tutorial/handoff.md` and `progress.md`.

You may ask an agent to propose or create these files, but inspect them. Do not publish, send a report, or modify raw inputs.

## Inspect

Run:

```bash
# Run from tutorials/coding-agent-basics/
python3 checks/validate_tutorial.py --project examples/sample-project
```

The script checks expected paths and required headings only. Review content yourself: structure is not correctness.

## Reflect

Which part of this workflow benefits most from code? Which part still needs a person’s judgment?

## Checkpoint

You have completed the course when your artifacts show the six required outcomes from [`SKILL.md`](../SKILL.md), you have run the structural check, and you can explain the evidence behind each claim.
