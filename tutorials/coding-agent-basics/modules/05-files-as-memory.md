---
id: files-as-memory
title: Keep knowledge in files
estimated_minutes: 18
prerequisites:
  - inspect-and-validate
objectives:
  - distinguish ordinary Markdown notes from AGENTS.md
  - create concise project operating instructions
checkpoint: artifact
required_artifacts:
  - AGENTS.md
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: concise
  goal-first: full
---

# Keep Knowledge in Files

## In brief

A conversation is temporary working memory. Files are durable project memory. Store information where the next person—or the next agent session—can find and review it.

Start with ordinary Markdown for knowledge that people need to read and revise:

```text
notes/
├── data-dictionary.md
├── reporting-rules.md
└── decisions.md
```

Use Markdown for definitions, policies, exceptions, decision records, and requirements.

## `AGENTS.md` is different

`AGENTS.md` is a short project instruction file supported by many coding-agent harnesses. It tells an agent how to operate in this project: purpose, commands, protected paths, output locations, conventions, and completion checks.

In Pi, matching `AGENTS.md` files can load at startup from the user directory, parent directories, and current project. Other harnesses differ, so treat the filename as a useful convention and check your agent's documentation.

Keep it short. Do not put a large manual or all historical knowledge in it: always-loaded instructions consume working memory and can become stale.

## Compare

| Use | Best home |
|---|---|
| Meaning of a metric | `notes/metric-definitions.md` |
| Why a rule changed | `notes/decisions.md` |
| Never edit raw exports | `AGENTS.md` |
| How to run the report check | `AGENTS.md` or a linked script README |
| Exact steps for a recurring workflow | a skill |

## Try it

Read the sample project's [`AGENTS.md`](../examples/sample-project/AGENTS.md). Then create or adapt an `AGENTS.md` for a safe practice project. Include only:

```markdown
# Project Instructions

## Purpose

## Working rules
-

## Paths
- Sources:
- Outputs:

## Before finishing
-
```

## Inspect

Can a new agent answer these without guessing?

1. What should it avoid changing?
2. Where should it write outputs?
3. What check must it perform before saying work is done?

## Record

Link your `AGENTS.md` from `progress.md`. Put deeper domain knowledge in a separate note and link it rather than inflating the instruction file.

## Checkpoint

Explain why both a detailed Markdown note and a short `AGENTS.md` can be useful in the same project.
