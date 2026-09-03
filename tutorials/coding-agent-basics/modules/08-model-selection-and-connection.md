---
id: model-selection-and-connection
title: Act 6 — Choose the operating setup
estimated_minutes: 15
prerequisites:
  - context-and-compaction
mission_act: make-it-resumable
objectives:
  - direct a safe provider-connection plan
  - create a task-based model-selection decision
checkpoint: decision
required_artifacts:
  - model-selection.md
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: concise
  goal-first: full
---

# Act 6 — Choose the Operating Setup

## Situation

The mission needs an intentional operating setup. A fast model may be enough to inspect a well-defined CSV, while ambiguous interpretation needs more reasoning and review. Privacy, context capacity, cost, and tool reliability also matter.

## Your move

Tell the agent to create `model-selection.md` for this mission. Require it to document the task, consequence of error, input size, privacy requirements, speed/cost constraints, model qualities needed, validation plan, and a condition that would make you choose differently.

If you want to connect a real provider, stop after the plan and explicitly approve a provider-specific login or credential action. Do not place keys in the project.

## Agent mode

The agent drafts the decision from the mission constraints. It must not claim a subscription includes API access, reveal credentials, or connect an account without approval.

## Inspect

Check that the decision selects by observed needs rather than a brand name. It should distinguish a low-risk first-pass task from an ambiguous, high-impact decision and keep validation in both cases.

## Unlock

A **provider** gives authenticated access to a **model**; an agent uses that model with workspace tools. Connection usually means choosing an approved provider or local setup, authenticating through a supported secure mechanism, selecting a model, then running a harmless smoke test.

| Need | Prefer |
|---|---|
| Routine high-volume checks | Fast, cost-effective tool use plus strong checks. |
| Ambiguous planning or debugging | Stronger reasoning and reliable tool use. |
| Large documents or projects | Enough context capacity. |
| Sensitive/offline work | Approved private or local option, if capable enough. |

A more expensive model never removes the need for evidence and human review.

## Checkpoint

Act 6 is unlocked when `model-selection.md` ties the model choice to the mission’s risks, constraints, and validation plan.
