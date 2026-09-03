---
id: model-selection-and-connection
title: Connect safely and choose a model
estimated_minutes: 15
prerequisites:
  - context-and-compaction
objectives:
  - describe a safe provider-connection sequence
  - choose a model based on task requirements
checkpoint: decision
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: concise
  goal-first: full
---

# Connect Safely and Choose a Model

## In brief

A provider gives authenticated access to a model. A coding agent uses that model within a workspace and tool environment. The exact login, API-key, local-model, subscription, privacy, and billing arrangements vary by provider and harness.

Use this safe sequence:

1. Choose an approved provider or local setup.
2. Authenticate through the agent's supported login or secure credential mechanism.
3. Select a model appropriate to the task.
4. Run a harmless smoke test: inspect sample files or write a temporary note.
5. Keep credentials out of repositories, screenshots, and ordinary Markdown files.

Do not connect a real account or transmit work data merely for this lesson. Follow your organization's security and data policies.

## Select by task, not brand

| Need | Prefer |
|---|---|
| Routine, high-volume work | Fast, cost-effective tool use with strong checks. |
| Ambiguous planning or debugging | Stronger reasoning and reliable tool use. |
| Large documents or projects | Enough context capacity for the materials. |
| Sensitive or offline work | An approved private or local option, if capable enough. |
| Important final output | A capable model plus independent validation and human review. |

Compare actual quality, tool reliability, latency, context capacity, privacy, and cost. A more expensive model does not remove the need to validate.

## Predict

You need to turn 500 similar files into a checked summary, then review a handful of ambiguous cases. Would one model setting be ideal for both phases? Why or why not?

## Try it

Write `model-selection.md` for one of your workflows. Include:

- task and consequences of error;
- input size and privacy needs;
- desired speed and cost constraints;
- model qualities needed;
- validation and human-review plan.

## Inspect

Confirm the decision does not rely only on a model name or marketing claim. It should name a test or observable criterion that would cause you to choose differently.

## Record

Link `model-selection.md` from `progress.md`.

## Checkpoint

Explain why a smaller model may be appropriate for a well-bounded task but not for an ambiguous, high-impact decision without stronger checks.
