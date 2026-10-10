---
role: check-usage-and-compact
title: Check usage and compact the conversation
kind: mini
summary: See how large your conversation has become, summarise it into a file, and continue in a fresh session.
time: 5 min
teaches: [context, costs]
needs: [orient-in-folder]
---

After this step you will know how to see how much context a session is using, how to compact it deliberately, and how to carry the important parts into a new session.

**Before you start:** an agent session that has been running for a while, ideally after several of the earlier steps ([Setup](setup:)).

## Background

Every turn re-sends the whole conversation, so long sessions get slower, costlier, and less reliable ([Context](concept:context), [Costs](concept:costs)). Harnesses typically show
a context or token indicator and offer a command to compact or clear the conversation; the names differ, so check yours.

A manual compaction beats an automatic one because you choose the moment and decide what to keep.

## General approach

1. **Look.** Find your harness's usage display. Note the tokens used and the share of the window.
2. **Summarise to a file.**

```text
Summarise this session for a future session: what we were trying to do, the decisions made and why, the files created and what each is for, the current
state, and the open questions. Save it as notes/session-summary.md. Keep it under 40 lines. Do not include anything sensitive.
```

3. **Restart.** Start a new session and ask it to read `notes/session-summary.md` and continue. Or use your harness's compaction command and compare.
4. **Review the summary.** It is memory: anything wrong in it is inherited ([Memory](concept:memory)).

<!-- example -->

## What to check

- The summary captures decisions and file purposes, not a transcript.
- The new session starts with far less context, and can still answer "where did we leave off?".
- Anything important that was only in the conversation now exists in a file.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| Summary too long or generic | No length limit or structure | Ask for specific sections and a line limit |
| Key decision missing | It was never written down | Add it to the summary and to `AGENTS.md` if it is a rule |
