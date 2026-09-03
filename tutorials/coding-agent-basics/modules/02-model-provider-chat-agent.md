---
id: model-provider-chat-agent
title: Model, provider, chat, and agent
estimated_minutes: 15
prerequisites:
  - what-is-a-coding-agent
objectives:
  - distinguish model, provider, interactive chat, and coding agent
  - identify which layer may be responsible for a simple failure
checkpoint: conceptual
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: concise
  goal-first: full
---

# Model, Provider, Chat, and Agent

## In brief

These terms name different parts of a system:

| Term | Plain meaning |
|---|---|
| **Model / LLM** | The language-and-reasoning engine. |
| **Provider** | The service that gives authenticated access to one or more models. |
| **Interactive chat** | A text-first conversation, often limited to information you paste or upload. |
| **Coding agent** | A model paired with tools and a workspace so it can inspect, act, and check. |

```text
You → coding agent → model ← provider
             ↓
      files, code, tools, services
```

A model can power both chat and an agent. The difference is not that one model “knows code”; it is whether the surrounding system can use tools and act in an environment.

## Predict

Match each problem to the most likely layer:

1. “My sign-in or API key is rejected.”
2. “The assistant cannot see my local files.”
3. “The assistant can read a file but makes weak reasoning mistakes.”

## Suggested answer

1. Provider or credentials. 2. Agent environment, permissions, or missing tool. 3. Model capability, prompt, or missing context. More than one layer can contribute.

## Try it

Describe your current setup in one sentence using all four terms. Example:

> I use a coding agent that accesses a model through a provider; it can inspect my local project files when I grant it access.

## Practical note

A chat subscription and API or agent access may be separate products. Provider availability, billing, privacy rules, and supported models vary. Keep credentials in the approved login or secret mechanism; never place them in project files or version control.

## Record

Add your one-sentence setup description and any access constraint to `progress.md`.

## Checkpoint

Explain why a capable model can still be unable to inspect a file on your computer.
