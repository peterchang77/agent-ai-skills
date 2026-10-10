---
role: plan-cleaning
title: Plan the cleaning and make the judgement calls
kind: full
summary: Ask for a plan with options before any change is made. The agent proposes; you decide the choices that affect meaning.
time: 7 min
teaches: [scoping-work, steering]
needs: [profile-data]
---

Cleaning data involves decisions, and some of them are yours. After this step you will be able to use a planning step to get
options from the agent, decide the ones that matter, and record your decisions before any change is made.

**Before you start:** a data-quality profile of your data ([Profile the data](beat:profile-data)). If you do not have one, a short list of known problems is enough.

## Background

Cleaning rules fall into two groups:

- **Mechanical fixes** have one sensible answer (trim stray spaces, standardise date formats, remove exact duplicate rows). The agent can propose these and you can approve them as a group.
- **Judgement calls** change what the data means or whom it includes (what to do with an impossible value, how to treat a unit mismatch, whether to exclude a group). The agent should *offer options with consequences*, and **you** decide.

A **plan** step enforces this. Many harnesses have a *plan mode* that prevents any change until you approve ([Scoping work](concept:scoping-work), [Steering](concept:steering)).

## General approach

```text
Do not change any files. Propose a cleaning plan for <data file> based on the problems above. For each problem give the options,
the consequences of each, and your recommendation. Group the mechanical fixes together. Ask me about any judgement call
instead of deciding it yourself.
```

Answer the questions, then ask the agent to restate the final plan in a short list. Save that list as a file
(`notes/cleaning-decisions.md`) so it outlives the conversation ([Memory](concept:memory)).

<!-- example -->

## What to check

- The plan separates mechanical fixes from judgement calls.
- It asks you about judgement calls rather than assuming.
- You can state each decision in one line. If you cannot, the plan is too vague.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| It starts editing during the planning step | Not in plan mode, or not told to wait | Interrupt; restate "do not change any files" |
| It decides every case itself | The prompt did not ask for options | Ask it to list options and wait for your choice |
