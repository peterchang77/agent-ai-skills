---
id: scope-and-friction
title: Module 4 — Recognize scale, friction, and a better route
estimated_minutes: 12
prerequisites:
  - options-and-tools
learning_loop: scope-before-work
objectives:
  - distinguish a bounded task from a batch workflow
  - identify resource drivers and pause signals
  - request a staged plan instead of brute-forcing a difficult path
checkpoint: scope-plan
---

# Module 4 — Recognize Scale, Friction, and a Better Route

## Situation

“Summarize this PDF” and “review 10,000 PDFs” are not the same task at different sizes. The first may be direct inspection. The second requires inventory, extraction, batching, failure handling, storage, sampling, resource limits, and validation. The same difference applies to one email versus an inbox, or one quick report versus a recurring reporting system.

A rough planning model is:

```text
effort ≈ number of items × work per item + coordination + output complexity + risk
```

## Your move

How would you ask the agent to assess a larger version of this work before it begins?

For example: “If this were 10,000 PDFs rather than one survey CSV, assess the scope before processing anything. Explain the likely tools, resource drivers, risks, staged approach, expected outputs, and decisions you need from me.”

## Agent mode

The agent does not fabricate precise time or cost estimates. It classifies the work relatively—small, moderate, or large—and identifies practical drivers such as file count and size, OCR, rate limits, context limits, available compute, storage, permissions, rendering, and review effort. It recommends a staged route such as:

```text
inventory → sample → choose extraction/classification method → batch process
→ record failures → validate/sample-check → summarize
```

It asks for approval before accessing sensitive sources, connecting accounts, incurring material cost, or processing an entire large collection.

## Inspect

Look for the difference between a direct task and a workflow. Would the proposed approach still work if one file fails, the format varies, the collection doubles, or the result needs auditability? Is the agent reusing established tools where they reduce friction?

## Unlock

Pause rather than repeatedly saying “try again” when you see a signal of accumulating debt:

- repeated fixes without convergence;
- an unclear assumption or result you cannot explain;
- rapidly growing scope, time, or cost;
- reinvention of an available tool or project convention;
- a workflow that will recur but has no repeatable path; or
- evidence too weak for the stakes.

Useful reset prompts include: “Step back: why is this difficult, what alternatives exist, and which do you recommend?” and “Inventory the work and propose a staged approach before continuing.”

## Checkpoint

Continue when the learner can identify whether a request is a direct task or a workflow and can ask for a scope assessment before large or uncertain work.