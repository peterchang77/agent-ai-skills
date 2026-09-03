---
id: review-revise-reuse
title: Module 5 — Review evidence, steer revision, and retain only useful reuse
estimated_minutes: 18
prerequisites:
  - scope-and-friction
learning_loop: execute-review-reuse
objectives:
  - inspect output and evidence rather than trusting a plausible result
  - give a targeted revision based on audience or interpretation
  - decide whether any repeatable asset is justified
checkpoint: completion
---

# Module 5 — Review Evidence, Steer Revision, and Retain Only Useful Reuse

## Situation

The agent has a chosen route and an approved plan. It can now create the draft report using the project’s instructions, appropriate tools, and source-preserving boundary. The first deliverable is a draft to inspect—not a reason to stop thinking.

## Your move

Approve execution, then review the result and give one meaningful revision. For example:

> Create the approved draft and show the checks you ran. Then make the main report suitable for a manager: keep the findings, use a concise Markdown summary, and put assumptions and exception details in an appendix. Explain what changed and rerun relevant checks.

If this work may recur, also ask: “What is the smallest thing worth keeping so next month is easier and still trustworthy?”

## Agent mode

The agent creates derived artifacts only; it preserves `data/raw/`, uses existing project notes and the checker where appropriate, and reports the exact output paths and evidence. It distinguishes a structural or data-quality check from semantic correctness, publication approval, or a decision about ambiguous records.

For a recurring workflow, it recommends the smallest durable asset that fits the need:

| If the recurring need is | Consider keeping |
|---|---|
| a deterministic calculation or check | a script and its validation command |
| a report with a stable shape | a Markdown template |
| persistent project rules | a concise `AGENTS.md` or project instruction file |
| a recognizable multi-step workflow | a focused skill with references and tools |
| a long-running or transferred task | a concise handoff file |

It does not create every kind of artifact by default. A one-off task may need none.

## Inspect

Review four things:

1. **Fit:** does the result serve its intended audience and decision?
2. **Evidence:** what paths, counts, tool output, checks, or comparisons support it?
3. **Limits:** what does that evidence not prove, and what requires human judgment?
4. **Repeatability:** could the useful part be rerun without reconstructing a long chat?

## Unlock

Brute-force prompting often works briefly but can accumulate result, knowledge, reproducibility, technical, operational, or trust debt. Your durable role is to steer: notice friction, ask for a better route, inspect evidence, correct the meaningful part, and preserve only what future work will actually use.

## Checkpoint

The course is complete when the learner has directed one capable request, reviewed a plan and meaningful choice, assessed a larger-scope alternative, inspected evidence, and steered a revision. Any durable artifact is optional and justified by recurrence or handoff needs.