---
id: harnesses
title: Harnesses and models
themes: [recursive-ai]
related: [agent-vs-chat, costs, sandboxing, privacy]
blurb: An agent system separates the inference engine (the model), the orchestration software (the harness), and the execution target (the environment). Understanding this separation clarifies system capabilities and boundaries.
---

## The three architectural tiers

Coding agent architectures separate reasoning, orchestration, and execution into three distinct layers:

![The three layers of a coding agent system. The model, a cloud language model, receives context and returns tool calls. The harness assembles context, drives the loop and dispatches tools. The environment, your local filesystem and shell, runs the commands and returns output and errors.](image:three-layers-model-harness-interface)

| Architectural layer | Role and responsibility | Researcher choice |
|---|---|---|
| **Foundation model** | The underlying language model that processes context and generates structured tool calls. Because the model is stateless, it only perceives what is passed in the context window. | Provider, architecture tier, and context window size |
| **Agent harness** | The client application that manages session state, assembles system prompts, invokes tools, prompts for human permissions, and handles error recovery. | Choice of client CLI, IDE extension, or autonomous runtime |
| **Execution environment** | The computing infrastructure where shell commands execute and files reside. | Local workstation, isolated container, or remote compute cluster ([Environment](concept:environment)) |

The foundation model evaluates context and proposes actions; the harness enforces boundaries and dispatches commands; and the host environment runs code and returns console output. Harnesses also provide different **user interfaces**, including command-line interfaces (CLIs), code editor extensions, and standalone desktop applications.

Distinguishing between these layers prevents common misconceptions. The exact same foundation model can behave very differently across two different harnesses due to variations in system prompting, tool definitions, and context compaction strategies. Similarly, most harnesses allow switching between multiple model backends.

## Current landscape

| Ecosystem | Command-line (CLI/TUI) | Editor / IDE integration | Background / Autonomous |
|---|---|---|---|
| **Anthropic** | Claude Code | Claude Code in VS Code / JetBrains | Scheduled tasks, background agents |
| **OpenAI** | Codex CLI | Codex editor integrations | Background batch workers |
| **Google** | Gemini CLI, Antigravity CLI | Antigravity IDE | Autonomous background tasks |
| **AWS** | Kiro CLI | Kiro IDE | Cloud-backed agent tasks |
| **Open Source / Neutral** | pi, Aider | Extension ecosystems | Continuous background assistants |

System names and interfaces evolve rapidly. Rather than focusing on ephemeral product branding, focus on the structural patterns and underlying configurations.

## The spectrum of human supervision

![The continuum of control in AI harnesses, in four stages. In isolated chat there is no harness and you copy, run and verify everything. An inline copilot assists as you type in an editor. An interactive agent proposes actions and you grant permissions. An autonomous agent loops end to end in the background and you review the result.](image:continuum-of-agent-control)

Different research tasks call for different levels of autonomy and supervision:

- **Isolated chat:** No harness integration. You copy code out manually, execute it in a separate terminal, and verify all output.
- **Inline copilot:** Suggests code completions directly inside your editor as you write, keeping control localized to each line.
- **Interactive agent:** Proposes concrete shell commands, file modifications, or script executions, pausing for your explicit confirmation before executing. This interactive model is the central focus of this workshop: it offers transparency, prompt approval checkpoints, and file-based steering.
- **Autonomous agent:** Executes multi-step pipelines independently in the background, presenting artifacts upon completion. This approach saves time on repetitive tasks, but requires strict [sandboxing](concept:sandboxing) and [steering constraints](concept:steering) since you review work after execution.

## Selecting a harness and model

- Begin with a command-line harness connected to a foundation model you can access through existing institutional agreements or API keys.
- Confirm institutional data privacy approvals **before** analyzing sensitive or proprietary datasets ([Privacy and data handling](concept:privacy)).
- Store project conventions and procedures in **plain-text files** (`AGENTS.md`, modular skills, and documentation). Plain files are portable across harnesses, preventing vendor lock-in ([Memory](concept:memory)).

## Subscription vs. API access

Most agent harnesses support flat-rate monthly subscriptions or pay-per-token API endpoints. For a comparison of cost predictability, rate limits, and model access tiers, see [Costs](concept:costs).

## Cloud vs. local model deployment

While cloud-hosted models currently offer the highest reasoning and coding capabilities, foundation models can also run locally on dedicated GPU hardware. Local deployment provides total data residency and offline execution, making it an important option when institutional policies strictly prohibit transmitting data to external cloud services ([Privacy and data handling](concept:privacy)).

## Getting started

Installing an agent harness typically involves running a single package command or binary installer provided by the vendor. Step-by-step setup instructions are available on the [setup page](setup:).
