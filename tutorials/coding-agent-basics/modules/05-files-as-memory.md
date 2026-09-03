---
id: files-as-memory
title: Act 4 — Establish durable operating rules
estimated_minutes: 18
prerequisites:
  - inspect-and-validate
mission_act: establish-rules
objectives:
  - direct the creation of concise project operating instructions
  - place knowledge, rules, and repeatable procedures in appropriate files
checkpoint: artifact
required_artifacts:
  - AGENTS.md
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: concise
  goal-first: full
---

# Act 4 — Establish Durable Operating Rules

## Situation

The investigation uncovered report rules, exceptions, and a source-protection boundary. Leaving these only in the chat makes the next run inconsistent. The mission needs durable project memory.

## Your move

Tell the agent to inspect the existing `notes/` files and create or revise `AGENTS.md`. Direct it to include only the project purpose, protected source path, output path, rule to flag ambiguity, and required completion checks. Tell it to keep detailed metric definitions and decisions in `notes/`.

## Agent mode

The agent creates a concise operating file and reports its path. It should link or point to deeper knowledge rather than copying a long manual into always-loaded instructions.

## Inspect

Open `AGENTS.md`. Test it as a new operator: can you tell what must not change, where outputs go, and what evidence is required before the agent calls the task complete? Then confirm the definition of a metric and reason for a rule remain in the relevant note instead.

## Unlock

Use ordinary Markdown for knowledge people need to read and revise: definitions, policies, exceptions, and decisions. Use **`AGENTS.md`** for short, always-relevant project operating rules.

| Need | Best home |
|---|---|
| Meaning of a metric | `notes/metric-definitions.md` |
| Why a rule changed | `notes/decisions.md` |
| Never edit raw exports | `AGENTS.md` |
| Repeating procedure | a skill |

Many harnesses support `AGENTS.md`; Pi loads matching files at startup. Discovery differs elsewhere, so check the harness before relying on automatic loading.

## Checkpoint

Act 4 is unlocked when a new agent can operate safely from `AGENTS.md` and locate deeper context in notes.
