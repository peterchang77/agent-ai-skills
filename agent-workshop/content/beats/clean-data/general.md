---
role: clean-data
title: Clean the data with a script, and show the flow
kind: full
summary: Apply the agreed decisions in a script that writes a new file and a flow table showing what changed, so the result is reproducible and checkable.
time: 7 min
teaches: [verification, tools, environment]
needs: [plan-cleaning]
---

After this step you will have a cleaned copy of your data, a script that produces it, and a table of how many rows each rule touched.
Together they make cleaning something you can rerun and check, rather than something that happened once in a conversation.

**Before you start:** your cleaning decisions, written down ([Plan the cleaning](beat:plan-cleaning)) or restored from a checkpoint ([Setup](setup:restore-a-starting-point)).

## Background

Cleaning should be:

- **Scripted**, not done by hand or by asking the agent to "fix it": a script can be rerun on next month's data and read by a reviewer.
- **Non-destructive**: the original file is never modified. The output is a new file in a separate folder.
- **Accounted for**: a **flow table** lists each rule and how many rows it affected, with starting and ending row counts. Counts that do not add up reveal silent errors ([Verification](concept:verification)).

The agent may need a data library (for example `pandas`); it installs one inside the project ([Environment](concept:environment)).

## General approach

```text
Implement the decisions in <decisions file> as a script <scripts/clean.py> that reads <raw file> and writes <clean file> without
modifying the original. Also write a flow table (<out/cleaning_flow.md>) showing the starting row count, the rows affected by each
rule, and the final row count. Run it and confirm the numbers add up.
```

The result is a tool you can reuse ([Tools](concept:tools)).

<!-- example -->

## What to check

- The original file is unchanged (compare its size or checksum before and after).
- The flow table's counts match the problem counts from profiling.
- Starting rows minus removed rows equals final rows.
- You can read the script and find each of your decisions in it.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| Counts do not add up | A rule changed rows silently, or rules overlap | Ask the agent to reconcile each step |
| The script overwrote the input | Output path equals input path | Restore the original; require a separate output folder |
