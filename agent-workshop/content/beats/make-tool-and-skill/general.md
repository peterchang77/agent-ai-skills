---
role: make-tool-and-skill
title: Turn the analysis into a tool and a skill
kind: full
summary: When you will repeat a task, package it as a script with a help message, test it against a known answer, and write a short skill that says when and how to use it.
time: 10 min
teaches: [tools, memory, verification]
needs: [add-agents-md, analyze-pilot]
---

After this step you will have a tested command that reproduces an analysis on new data, and a short skill that tells a future session how to use it. That
is the most durable kind of memory: the next run costs a sentence, not a conversation.

**Before you start:** a working analysis script and its outputs ([Setup](setup:restore-a-starting-point)).

## Background

A prompt-driven analysis may come out slightly differently each time. A **tool** (a script with arguments and `--help`) does the same thing every time, runs
without the model, and can be tested ([Tools](concept:tools)). A **skill** is a short document in its own folder that tells the agent *when* to use the tool and
*how*, without you re-explaining ([Memory](concept:memory)).

A useful split:

| Piece | Holds |
|---|---|
| Tool (script) | The logic. Deterministic. Tested. |
| `README.md` | What it does, inputs, outputs, an example run |
| Skill (`SKILL.md`) | When to use it, the exact command, what to check afterwards |
| `AGENTS.md` | Project-wide rules that always apply |

## General approach

1. **Package.** 

```text
Combine the cleaning, cohort, and analysis steps into one command-line tool scripts/pilot_report.py with arguments for the input files and an output folder,
and a --help. It must not modify its inputs. Write a short README.md for it.
```

2. **Test.** Run it on the same data and compare the output with your saved results. Add a test that checks key numbers against the known answers
(`pytest` or a simple check script).

3. **Write the skill.**

```text
Create a skill in .agents/skills/pilot-report/SKILL.md (under 40 lines): when to use it, the exact command, the inputs it needs, and what to check
in the output. Do not repeat what the README already says; link to it.
```

4. **Prove it.** Start a new session, ask for the report on the data, and see whether the agent finds and uses the skill.

Where a skill lives, and how it is discovered, depends on your harness; check its documentation ([Harnesses](concept:harnesses)).

<!-- example -->

## What to check

- The tool reproduces your earlier numbers exactly.
- A test fails if a key number changes.
- The skill is short, specific, and points at the tool and README rather than copying them.
- The skill and tool contain no secrets.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| The new session does not use the skill | Wrong location or an unclear description | Check where your harness looks; sharpen the skill's description line |
| Tool output differs from before | Logic changed while combining steps | Compare step by step against the saved results |
