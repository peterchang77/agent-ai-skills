---
id: context-and-compaction
title: Manage context and compaction
estimated_minutes: 15
prerequisites:
  - reusable-skills
objectives:
  - explain why long conversations need durable state
  - create a compaction-ready handoff
checkpoint: artifact
required_artifacts:
  - handoff.md
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: concise
  goal-first: full
---

# Manage Context and Compaction

## In brief

An agent's **context** is the information it can currently use: recent messages, files it has read, tool results, instructions, and summaries. Its context window is finite. Large pasted documents, lengthy tool output, and long conversations consume it.

**Compaction** summarizes older conversation material so the agent can continue with recent work. It is useful but lossy: omitted detail may no longer be immediately available. The safest response is to preserve important facts in files before they are needed again.

> Conversation is working memory. Files are institutional memory.

## When to prepare a handoff

Do it at a phase boundary, after large outputs, before switching tasks, when a session becomes long, or before intentional compaction. In Pi, `/compact` starts manual compaction; automatic compaction may also run near the context limit. Other harnesses use different commands.

## Try it

Create `.tutorial/handoff.md` from the template. Fill in:

- objective and selected route;
- completed work and evidence;
- active file paths and artifacts;
- rules and approval boundaries;
- unresolved questions;
- exact next smallest action.

## Inspect

Imagine a different agent opens the handoff with no chat history. Can it safely resume without guessing what matters? If not, add the missing path, decision, or check result.

## Reflect

What information from your normal work is currently trapped in chat, email, or someone’s memory rather than a durable, searchable place?

## Record

Link the handoff in `progress.md`. Update it before intentional compaction or ending an unfinished session.

## Checkpoint

Explain why compaction alone is not a substitute for project notes, `AGENTS.md`, or a progress record.
