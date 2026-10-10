---
role: first-look
title: A first answer from raw data
kind: full
summary: Get a quick answer from the raw data, with the definition and the denominator stated. It will look plausible, which is exactly why you should not trust it yet.
time: 6 min
teaches: [verification, inputs, scoping-work]
needs: [read-text-files]
---

An agent can answer a data question in minutes. This step shows how to ask for a first answer in a way that you can check, and sets
up the next steps, where cleaning the data changes the answer.

**Before you start:** a data file, a data dictionary, and (if the question has a target or benchmark) the file that holds it
([Setup](setup:)).

## Background

A first pass on raw data is useful for orientation, but it is **exploration, not a result**. Raw data usually has problems
that quietly change the numbers. A good first answer therefore states its definitions and shows how many rows each number rests on,
so you can see what to question ([Verification](concept:verification)).

## General approach

Put the definition in the prompt, so the agent does not invent one, and ask for denominators.

```text
Using <data file> and <data dictionary>, answer: <question>. Use this definition: <definition>. Report every number with the
number of rows (or people) it is based on. Do not change or exclude any data; just tell me what you notice.
```

"Do not change the data" keeps the first pass honest: you see what the raw data says, and you decide the cleaning later
([Scoping work](concept:scoping-work)).

<!-- example -->

## What to check

- The definition you gave was used (not a different one).
- Every number has its denominator.
- The agent mentioned anything odd it noticed, without silently fixing it.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| Answer uses a different definition | The definition was missing or ambiguous | Restate it exactly; ask which definition it used |
| No denominators | They were not requested | Ask: "How many rows is each number based on?" |
| Quietly dropped rows | Default behaviour of the code | Ask what was excluded, and why |
