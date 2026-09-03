---
id: model-provider-chat-agent
title: Act 1 — Identify the operating boundary
estimated_minutes: 15
prerequisites:
  - what-is-a-coding-agent
mission_act: survey-safely
objectives:
  - distinguish model, provider, interactive chat, and coding agent through operation
  - identify the likely layer behind a simple failure
checkpoint: operational-decision
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: concise
  goal-first: full
---

# Act 1 — Identify the Operating Boundary

## Situation

The report workflow needs a reasoning engine, access to it, and an environment that can inspect and check files. If one layer fails, the correct next action depends on which layer it is.

## Your move

Ask the agent to state its operating boundary for this mission. Tell it to separate:

- its access to the project files and tools;
- the model it is using, if that information is available; and
- provider, account, or credential limits it cannot verify.

Require it to label uncertainty instead of guessing.

## Agent mode

The agent reports only what it can inspect in its current environment. It should never reveal credentials or claim to know a provider or model that the harness does not expose.

## Inspect

Use the result to decide the next safe action:

- rejected sign-in or API key → provider or credentials;
- inability to see files → agent environment, permissions, or missing tool;
- weak analysis despite file access → model capability, prompt, or missing context.

## Unlock

A **model** is the language-and-reasoning engine. A **provider** supplies authenticated access to a model. **Interactive chat** is usually text-first. A **coding agent** combines a model with a workspace and tools so it can act and check.

```text
You → coding agent → model ← provider
             ↓
      files, code, tools, services
```

A strong model cannot inspect files that the agent environment cannot access. Keep credentials in approved secret or login mechanisms, never in project files.

## Checkpoint

Act 1 is complete when you can identify which layer to investigate if a reporting action cannot access files or authenticate.
