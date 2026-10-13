---
id: harnesses
title: Harnesses and models
themes: [recursive-ai]
related: [agent-vs-chat, costs, sandboxing, privacy]
blurb: The model is the brain; the harness is the program that gives it files and tools; the environment is where its commands run. Keep the three separate in your head.
---

## Three layers

![The three layers of a coding agent system. The model, a cloud language model, receives context and returns tool calls. The harness assembles context, drives the loop and dispatches tools. The environment, your local filesystem and shell, runs the commands and returns output and errors.](image:three-layers-model-harness-interface)

| Layer | What it is | The choice you make |
|---|---|---|
| **Model** | The language model that reads and writes. It is stateless: it only sees what the harness sends | Which provider, which size and version |
| **Harness** | The program that assembles the context, runs the loop, sends tool calls to the environment, and asks for your approval | Which agent application |
| **Environment** | The computer where commands run and files live | Your own machine, a container, or a remote server ([Environment](concept:environment)) |

The model proposes actions, the harness carries them out in the environment, and the output returns to the model as text. You also choose an **interface** for the harness: a terminal, an editor, a desktop app, or an always-on service.

Most confusion comes from mixing these layers up. The same model behaves differently in different harnesses, and one harness can often run several models.

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

![The continuum of control in AI harnesses, in four stages. In isolated chat there is no harness and you copy, run and verify everything. An inline copilot assists as you type in an editor. An interactive agent proposes actions and you grant permissions. An autonomous agent loops end to end in the background and you review the result.](image:continuum-of-agent-control)

- **Isolated chat** has no harness. You copy code out, run it yourself, and check everything.
- **An inline copilot** suggests code in your editor while you direct each line.
- **An interactive agent** proposes actions and runs them once you grant permission. A terminal agent is the usual example, and it is the focus of this material: you see each command, approve steps, and customise behaviour with plain files.
- **An autonomous agent** loops from task to result, often in the background. It is powerful for routine work, but you review results after the fact, so it needs more careful [isolation](concept:sandboxing) and [steering](concept:steering).

Moving right means delegating more. Interface and control are related but separate: editors and desktop apps can host an interactive agent too, usually with a friendlier view and inline diffs.

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
