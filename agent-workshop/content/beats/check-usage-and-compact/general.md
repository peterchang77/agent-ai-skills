---
role: check-usage-and-compact
title: Check usage and compact the conversation
kind: mini
summary: Monitor cumulative token consumption, synthesize session decisions into a persistent summary file, and initialize a clean working context.
time: 5 min
teaches: [context, costs]
needs: [orient-in-folder]
---

In this exercise, you audit active token usage in your agent harness, synthesize key analytical decisions into a concise Markdown summary, and initialize a fresh working session without losing project state.

**Before you start:** An active agent session that has executed multiple turns across earlier exercises ([Setup](setup:)).

## Background

Because language model inference is stateless, each turn re-transmits the complete conversation transcript. Consequently, long-running sessions exhibit increased latency, higher token costs, and attention drift ([Context](concept:context), [Costs](concept:costs)). Most modern harnesses display active context usage and provide commands to compact or clear history.

Executing manual compaction at logical project milestones is far superior to automatic truncation: you select the precise transition point and decide which decisions to preserve.

## General methodology

1. **Audit token consumption:** Inspect your harness's token or context indicator to observe total tokens consumed and percentage of the sequence window occupied.
2. **Synthesize state to disk:** Instruct the agent to summarize project state into a persistent document:

```text
Summarize this session for a future fresh session:
- The core analytical objective.
- Specific data cleaning and modeling decisions made, along with justifications.
- Files generated and their analytical roles.
- Current project state and open research questions.
Save this summary as notes/session-summary.md (under 40 lines). Do not include credentials or unredacted confidential data.
```

3. **Initialize a fresh session:** Start a new agent session and direct it to read `notes/session-summary.md` to resume work with minimal context overhead.
4. **Audit the summary document:** Review `notes/session-summary.md` carefully: because new sessions inherit claims recorded here, correct any inaccurate statements before continuing ([Memory](concept:memory)).

<!-- example -->

## Verification criteria

- **Decision-centric summary:** The summary synthesizes methodological decisions and file roles rather than logging conversational dialogue.
- **Context reduction:** The new session initializes with substantially reduced token overhead while accurately identifying where prior work concluded.
- **Durable external state:** All critical conventions discussed in the earlier conversation now exist as persistent files on disk.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Summary is excessively verbose | Prompt lacked line constraints or section structure | Direct the agent to condense the document to under 40 lines across four explicit sections |
| Key methodological rule omitted | Decision was discussed conversationally but never committed to disk | Add the missing rule directly to `notes/session-summary.md` and append to `AGENTS.md` |
