---
role: build-cohort
title: Build a study cohort with a flow table
kind: full
summary: Turn written inclusion rules into a cohort file, with a flow table showing how many people remain after each step.
time: 8 min
teaches: [verification, tools, inputs]
needs: [clean-data]
---

A research question needs a precisely defined group of people. After this step you will be able to turn written eligibility rules
into a cohort file, with a flow table that shows how many people remain after each rule, which is the standard way to document a
cohort.

**Before you start:** cleaned data and a written definition of the cohort ([Setup](setup:restore-a-starting-point)).

## Background

A **cohort definition** has parts that must each be stated exactly:

- **Population:** who is eligible (for example, adults at one site).
- **Index event:** the moment that starts follow-up for each person (for example, the first qualifying visit in a period).
- **Exposure:** what you compare (for example, received an intervention or not).
- **Outcome and window:** what you measure and when (for example, a repeat test within a time window after the index event).

Vague definitions are the largest source of silent error. If the definition lives in a document (a protocol, a memo), have the agent read the
document and **quote the exact rules** back to you before writing any code ([Inputs](concept:inputs)).

A **flow table** (cohort diagram) lists the number of people at each step. If the numbers fail to add up, something was dropped silently
([Verification](concept:verification)).

## General approach

```text
Read <protocol file>. Quote the exact eligibility rules, the index event, the exposure, and the outcome window. Then write a script
<scripts/build_cohort.py> that applies them to <clean data> and writes <out/cohort.csv> (one row per person) and <out/cohort_flow.md>
(people remaining after each step). Mark a person as exposed only if <the exposure condition>; everyone else in the cohort is unexposed,
so that nobody is left blank or dropped from the comparison. Tell me every place where you had to interpret the protocol.
```

The last sentence matters: it surfaces the assumptions.

<!-- example -->

## What to check

- The quoted rules match the protocol word for word.
- One row per person in the cohort file.
- Each flow step is no larger than the one before it, and the final count equals the cohort file's row count.
- Assumptions were listed, and you agree with them.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| More than one row per person | The index event was not restricted to the first qualifying visit | Group by person and keep the first |
| The comparison group is far smaller than expected | People with no record of the exposure were left blank instead of counted as unexposed | State the comparison group in the prompt: everyone in the cohort who is not exposed |
| Counts differ from a colleague's | A different interpretation of a window boundary | Compare the definitions, and note which edge cases decide it |
