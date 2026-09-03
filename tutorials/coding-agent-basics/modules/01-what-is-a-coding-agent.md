---
id: what-is-a-coding-agent
title: Act 1 — Survey the workspace safely
estimated_minutes: 12
prerequisites:
  - mission-setup
mission_act: survey-safely
objectives:
  - direct a read-only workspace inspection
  - identify evidence and the limits of agent access
checkpoint: artifact
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: concise
  goal-first: full
---

# Act 1 — Survey the Workspace Safely

## Situation

Before reporting, you need to know what material exists. The first risk is accidental change: an agent that begins by “cleaning” a raw export can destroy the evidence needed to review its decisions.

## Your move

Direct the agent to survey the sample project. Your command must say:

- what it may inspect;
- that it must not change anything; and
- what evidence it should report.

For example, you might ask it to list the project files, identify the raw input and project instructions, and report the tool or command it used.

## Agent mode

After your instruction, the agent performs only the approved read-only inspection. It reports actual paths and the evidence it used; it does not invent file contents or create an output.

## Inspect

Check that the reported paths exist and that the source lives under `data/raw/`. Confirm no generated file appeared and no source changed. If the agent cannot inspect the project, treat that as an access limitation, not a reason to guess.

## Unlock

A coding agent is a model paired with an action loop, workspace, and tools. Its useful loop is:

```text
request → inspect → plan → act → check → report
```

The read-only tool result is evidence from the agent environment. A fluent answer without that evidence is not a completed inspection.

## Checkpoint

Act 1 is unlocked when you have directed a read-only survey and inspected its evidence.
