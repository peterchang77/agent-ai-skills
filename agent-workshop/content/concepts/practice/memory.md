---
id: memory
title: Memory — durable knowledge lives in files
short: Memory
themes: [context-discipline, recursive-ai]
related: [context, tools, steering, version-control]
blurb: Agents forget everything between sessions. Anything worth keeping goes in a file the agent reads, and the most durable form is a tool.
---

Nothing carries over from one session to the next except **files**. So the workaround for forgetting is the same each time: write it down.

## Levels of durable knowledge

| Level | What it is | Loaded | Use for |
|---|---|---|---|
| `AGENTS.md` | A short instructions file in the project | Automatically, at the start of every session | Conventions, paths, "always/never" rules |
| Notes and `README.md` | Ordinary documents | When the agent is told to read them or goes looking | Background, decisions, how to rerun |
| Skills (`SKILL.md`) | A packaged procedure in its own folder | On demand, when the task matches | A repeatable task ("write the monthly report") |
| Tools | Reusable code (a script or command-line program) | When run | Anything that should happen the same way each time |

**Rule of thumb:** when you explain something twice, write it down; when you ask for the same task a third time, make it a skill or a tool.

The names can vary between harnesses (`AGENTS.md` is a widely used convention; some tools use their own filename), but plain files travel well between them.

## Built-in memory features

Some products add their own memory that persists across sessions. These differ by product and change often, so check
what yours stores, where, and how to see or delete it. Files you control are easier to review and share.

## What to record

- **Decisions** and why (cleaning rules, definitions, "we tried X and it failed because Y").
- **How to run things** and where the data lives.
- **Preferences and rules** the agent keeps getting wrong.

Do not record what the agent can re-derive from the code. Keep memory files **short and specific**: everything in them is loaded into [context](concept:context) every session, so a sprawling file wastes space and gets ignored.

## Use the agent to write the file

Ask the agent to draft `AGENTS.md` from what you just did, then review it and cut anything vague. Using the agent to improve its own instructions is a core habit.

## Tools are the strongest memory

A prose instruction depends on interpretation; a script does the same thing every time and can be tested. When a
procedure is stable, turn it into a tool and let the instructions simply say how to run it ([Tools](concept:tools)).

## Maintain it

Stale instructions are worse than none. Keep memory files in [version control](concept:version-control), review changes to them like code, and never store [secrets](concept:secrets) in them.

## Demo it

<!-- demos -->
