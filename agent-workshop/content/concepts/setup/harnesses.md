---
id: harnesses
title: Harnesses and models
themes: [recursive-ai]
related: [agent-vs-chat, costs, sandboxing, privacy]
blurb: The model is the brain; the harness is the program that gives it files and tools; the interface is how you talk to it. Keep them separate in your head.
---

## Three layers

| Layer | What it is | Examples of the choice you make |
|---|---|---|
| **Model** | The language model that reads and writes | Which provider, which size/version |
| **Harness** | The program that connects the model to files, commands, and tools, and asks for your approval | Which agent application |
| **Interface** | How you interact with the harness | Terminal, editor/IDE, desktop app, or an always-on service |

Most confusion comes from mixing these up. The same model behaves differently in different harnesses, and one harness can often run several models.

## A grid of examples

| Provider | Terminal (CLI/TUI) | Editor / IDE / desktop | Long-running agent |
|---|---|---|---|
| Anthropic | Claude Code | Claude Code in an editor, desktop app | scheduled / background agents |
| OpenAI | Codex CLI | Codex in an editor or app | background tasks |
| Google | Gemini CLI, Antigravity CLI | Antigravity (IDE) | background tasks |
| AWS | Kiro CLI | Kiro IDE | background tasks |
| Provider-neutral | pi and other open-source agents | editor extensions | always-on assistants (e.g. OpenClaw, Hermes) |

This is the landscape as of October 2026. Products and names change quickly, so look up what is current.

## A continuum of control

```text
more interactive, customisable, controllable                     less
Terminal / TUI  ───────────▶  Editor / IDE / GUI  ───────────▶  Long-running agent
```

- **Terminal agents** give you the most visibility and control: you see each command, approve steps, and can customise with plain files. They are the focus of this material.
- **Editor and desktop apps** add a friendlier interface and inline diffs, with somewhat less transparency.
- **Long-running agents** work while you are away. They are powerful for routine tasks, but you review results after the fact, so they need more careful [isolation](concept:sandboxing) and [steering](concept:steering).

## How to choose

- Start with a terminal agent from a provider whose model you can already access (through a subscription, your institution, or an API key).
- Check what your institution approves **before** using real data ([Privacy](concept:privacy)).
- Prefer to keep your knowledge in **plain files** (`AGENTS.md`, skills, scripts, notes). Those travel between harnesses, so switching later is cheap ([Memory](concept:memory)).

## Subscription or API access

Many harnesses accept either a flat-rate subscription or pay-per-use API access. The trade-offs are covered in [Costs](concept:costs).

## Local models

A model can also run on your own computer. Local models keep data on the machine and can work offline, but they are currently less capable than the large hosted models and need capable hardware. They are worth considering when data cannot leave a machine ([Privacy](concept:privacy)).

## Getting set up

Installation is usually one command from the vendor's own instructions. The steps are on the [setup page](setup:).
