---
id: context-and-compaction
title: Act 6 — Make the mission resumable
estimated_minutes: 15
prerequisites:
  - reusable-skills
mission_act: make-it-resumable
objectives:
  - direct the creation of a compaction-ready handoff
  - preserve mission state outside the conversation
checkpoint: artifact
required_artifacts:
  - handoff.md
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: concise
  goal-first: full
---

# Act 6 — Make the Mission Resumable

## Situation

The reporting workflow now has several files, decisions, and checks. A long conversation can run out of working memory, and compaction can omit details. The mission must survive a new session or a new operator.

## Your move

Tell the agent to create `.tutorial/handoff.md` from the template. Require it to include the mission, current act, completed artifacts and evidence, active paths, source-protection rules, unresolved exceptions, and the exact next command.

## Agent mode

The agent writes the handoff from inspected project state. It must not fill gaps with invented history; it should mark missing evidence or decisions for review.

## Inspect

Imagine a different agent opens only the handoff. Check whether it can safely find the source, understand what is protected, see which quality exceptions remain, and take one next step without guessing. Add any missing path, rule, or result.

## Unlock

**Context** is the agent’s current working memory: messages, read files, tool results, instructions, and summaries. It is finite. **Compaction** summarizes older material to make room, but it can omit detail.

> Conversation is working memory. Files are institutional memory.

Prepare a handoff at phase boundaries, after large outputs, before changing tasks, or before intentional compaction. In Pi, `/compact` starts manual compaction; other harnesses differ.

## Checkpoint

Act 6 is unlocked when the handoff lets another session resume the mission without relying on the old conversation.
