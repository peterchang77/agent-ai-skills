---
role: profile-data
title: Profile the data and find problems
kind: full
summary: Before analysing, have the agent list the problems in the data, with counts and examples, and change nothing.
time: 7 min
teaches: [verification, steering]
needs: [first-look]
---

Most data has problems, and most problems change the answer. After this step you will be able to ask an agent for a systematic
data-quality report, and you will know which problems to look for.

**Before you start:** the data file and its data dictionary ([Setup](setup:)).

## Background

Profiling means describing the data without altering it: columns and types, missing values, duplicates, impossible values,
inconsistent labels, and values in the wrong units. Profiling is **separate from cleaning** on purpose. Some "problems" are not errors
(a blank lab value usually just means the test was not done), and many cleaning choices are your decisions, not the agent's
([Steering](concept:steering)).

Common problems to look for:

| Kind | Example |
|---|---|
| Duplicates | Identical rows; the same ID on two different records |
| Inconsistent labels | `Northside`, `northside `, `NORTHSIDE` |
| Impossible values | Age 212; blood pressure 0 |
| Wrong units | A lab reported in a different unit from the rest of the column |
| Mixed formats | Dates as `2025-05-03` and `05/03/2025` in one column |
| Missing values | Blanks (check whether the blank is expected) |

## General approach

```text
Profile <data file> using <data dictionary>. List every data-quality problem you find, with the number of affected rows and a few
example row IDs. Separate real errors from things that are probably fine. Do not fix or change anything.
```

Then ask: "For each problem, what are the plausible ways to handle it, and which would change my results?" This produces the
options you will choose among in the next step.

<!-- example -->

## What to check

- Counts are given for every problem, with example rows you can look up yourself.
- Blank values are explained rather than called errors (when the dictionary says blank means "not measured").
- Nothing was modified.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| It "cleaned" while profiling | The prompt allowed changes | Restate: "Report only; do not change anything" |
| It misses unit problems | It checked types but not meaning | Ask it to compare each column's range against the dictionary |
