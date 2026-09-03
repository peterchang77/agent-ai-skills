---
id: what-is-a-coding-agent
title: What a coding agent is
estimated_minutes: 12
prerequisites:
  - welcome-and-pretest
objectives:
  - explain an agent's action loop
  - name the access and verification limits of an agent
checkpoint: conceptual
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: concise
  goal-first: full
---

# What a Coding Agent Is

## In brief

A coding agent is an AI assistant that can use a workspace and available tools to carry out bounded work. It can often read files, write code, run commands, create outputs, and inspect what happened.

A useful mental model is:

```text
request → inspect → plan → act → check → report
```

The agent may repeat parts of this loop. Code is the intermediary that makes many tasks expressible and repeatable: transform a spreadsheet, compare documents, query a database, create a report, or check a folder.

## Predict

An assistant gives a convincing description of a CSV but cannot name files in your project folder. What is likely missing: reasoning ability, file access, or a provider account?

## Try it

In a sample workspace, ask:

> List the files you can inspect. Do not change anything. State which tool or command you used and what it found.

## Inspect

Check three things:

1. The response names real files, not generic examples.
2. It identifies evidence, such as a tool result or command output.
3. No file was changed.

## Limits that matter

An agent cannot bypass permissions, obtain data it cannot access, or make an uncertain result true by saying it confidently. Tools and services may have limits, costs, policies, and side effects. Ask for approval before deletion, publication, external communication, purchases, or changes to important sources.

## Reflect and record

Name one task from your work that would benefit from the loop above. Record the task and its most important approval boundary in `progress.md`.

## Checkpoint

Explain the difference between “an agent answered a question” and “an agent completed an inspectable task.”
