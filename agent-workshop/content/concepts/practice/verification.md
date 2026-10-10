---
id: verification
title: Verification — check the evidence
short: Verification
themes: [recursive-ai]
related: [steering, outputs, version-control, scoping-work]
blurb: The agent can be confidently wrong. Ask for evidence, run cheap checks, and use a fresh second agent to look for errors.
---

You stay responsible for the result. A useful question is **"what could be wrong here?"** There are three layers:

1. The code did what you **asked**.
2. The code is **correct**.
3. You asked the **right question**.

Most advice covers the first two; the third is yours.

## Common agent failures

- Silently dropping, changing, or "fixing" data.
- Answering from a filename or a partial read instead of the whole file.
- Inventing a citation, a column, or a function.
- Saying a test passed that it never ran.
- Stopping at something that merely looks finished.

## Ask for evidence, not reassurance

"Are you sure?" gets "yes". These get something checkable:

```text
Show the command you ran and the row count behind every number.
List everything you excluded or changed, and why.
```

## A cheap checking ritual

- **Denominators:** every number comes with the count it is based on.
- **Exclusions:** what was dropped, and was it you who decided that?
- **A spot check:** compute two or three values a second way, by hand or with different code.
- **Rerun the script** and confirm the same output.
- **Invariants:** counts that must add up (rows in = rows out + rows removed).

## Reading code you did not write

You do not need to write code to review it. In a data script, look at: what is read, **what is filtered out**, how
missing values are handled, how tables are **joined**, and what is written. Ask the agent to explain any line you cannot follow.

## A second agent as reviewer

Start a fresh session and ask it to **find errors**, not to confirm: "Review this analysis for mistakes. List every assumption." A clean context avoids the first session's momentum. It is not independent proof; the same model can share blind spots.

## Match the effort to the stakes

A throwaway exploration needs a glance. A result going into a paper, a clinical decision, or a leadership report deserves the full ritual, a reviewer, and a record of what was checked.

## Demo it

<!-- demos -->
