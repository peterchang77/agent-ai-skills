---
role: review-with-second-agent
title: Review the analysis with a fresh second agent
kind: detour
summary: Open a new session and ask a second agent to find errors in the first one's work. It is cheap, independent of the first session's momentum, and often catches something.
time: 6 min
teaches: [verification, context, recursive-ai]
needs: [analyze-pilot]
---

After this step you will know how to use a second agent, with a clean context, as a reviewer of work done by a first, and what a review can and
cannot tell you.

**Before you start:** a finished piece of work saved in files: a script and a results file ([Setup](setup:restore-a-starting-point)).

## Background

The agent that did the work is poorly placed to check it: it has the whole conversation in context, including its own assumptions, and tends to
confirm them. A **new session** has none of that. It reads only the files, so it behaves like a colleague seeing the work for the first time
([Context](concept:context)).

Frame the review as **finding errors**, not confirming. A request such as "is this right?" invites agreement. Also be aware of the limit: the
same model can share the first session's blind spots, so a clean review lowers risk but does not prove correctness
([Verification](concept:verification)).

## General approach

Start a new session in the project and give it the files, not the history:

```text
You are reviewing someone else's analysis. Read <the protocol or definition>, <the script>, and <the results>. Find errors, questionable
assumptions, and anything in the write-up not supported by the results. Check the script against the definition line by line. Do not
change any files; list the issues in order of importance, each with the evidence.
```

Then decide which findings are real. A reviewer can be wrong too.

<!-- example -->

## What to check

- Each finding points to a specific line, number, or sentence.
- You have confirmed the important ones yourself before acting.
- The review did not modify any files.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| "Looks good" with no detail | The prompt asked for confirmation | Ask for a list of at least the assumptions and risks |
| Many trivial findings | No ranking requested | Ask for the top three that could change a conclusion |
| It rewrote the analysis | Not told to leave files alone | Restate "do not change any files" |
