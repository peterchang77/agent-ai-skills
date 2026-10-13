---
id: agent-vs-chat
title: Agent vs. chat
themes: [text-formats, recursive-ai]
related: [what-code-can-do, harnesses, verification]
blurb: A standard chat model answers from training memory. An agent interacts with a live computing environment to inspect files, execute code, and produce verifiable artifacts.
---

Most researchers first encounter artificial intelligence through conversational chat interfaces: you provide a prompt, and the model generates a response based on patterns learned during training. A coding agent connects that same underlying language model to an execution environment—such as a local terminal, filesystem, and external tools. This operational interface fundamentally transforms both what tasks you can delegate and how you must evaluate the results.

![Chat compared with an agent. A chat model works only with text you paste in. An agent runs code in a local terminal, reads and writes local files, and fetches data from APIs and the web, inside an autonomous loop of acting, observing and fixing.](image:agent-vs-chat)

## Architectural comparison

| Dimension | Conversational chat | Coding agent |
|---|---|---|
| **Information source** | Pre-training data and text pasted into the prompt | Pre-training data plus local files, databases, APIs, and the web |
| **System capability** | Pure text generation; user manually copies outputs | Reads and writes files, executes shell commands, and installs libraries |
| **Audit trail** | Unverifiable claims; requires manual calculation to check | Inspectable scripts, terminal execution logs, and output datasets |
| **Primary risk** | Confident hallucinations or plausible inaccuracies | Hallucinations combined with unintended filesystem or system state changes |
| **Best suited for** | Conceptual explanations, brainstorming, text editing | Multi-step empirical analyses, data pipelines, and reproducible modeling |

## How an agent interacts with a computer

An agent interacts with the operating system through text-based protocols. The model outputs structured tool calls or shell commands; an orchestrating program called the [harness](concept:harnesses) executes those instructions in the local environment and returns the console output back to the model as context. Through this single feedback mechanism, the agent can access virtually any tool or service available from the command line ([What code makes possible](concept:what-code-can-do)).

### The agentic execution loop

![The agent loop. Starting from your directive, the agent observes the environment and files, acts by writing and running code, and evaluates the output and errors. It repeats until the result is verified, then returns artifacts and a summary.](image:agent-loop)

Rather than generating an entire solution in a single pass, the agent operates in an iterative loop:

1. **Observe:** Inspect files, directory structures, or command outputs.
2. **Act:** Write code, run an analysis, or execute a terminal command.
3. **Evaluate:** Examine runtime stdout, stderr, and generated data files.
4. **Refine:** Diagnose errors or unexpected values and adjust the approach until the objective is met.

This iterative execution leads to two predictable operational dynamics:
- **Self-correction:** When a script encounters a syntax error or a missing column, the agent reads the traceback, updates the code, and re-executes it, delivering functioning programs rather than plausible pseudocode.
- **Context and cost accumulation:** Every iteration appends tool calls and console output to the session history ([Context](concept:context)), meaning complex debugging loops increase latency and token consumption ([Costs](concept:costs)).

## Choosing between chat and agents

- **Use conversational chat** for conceptual questions, literature brainstorming, or editing brief text excerpts. Chat requires minimal setup and introduces zero risk to local files.
- **Use a coding agent** when the workflow requires manipulating local datasets, executing multi-stage scripts, generating reproducible figures, or auditing data transformations across files.

## Foundational limits

A coding agent remains an autoregressive language model. It can misinterpret file schemas, introduce subtle statistical errors, or prematurely declare that a task is finished. The crucial difference is that an agent leaves a concrete computational audit trail—scripts, execution logs, and generated tables—enabling researchers to independently verify every step ([Verification](concept:verification)).

## The spectrum of agency

In practice, the boundary between chat and agents is a spectrum of **environmental access** (file access, shell execution, web retrieval) and **delegated authority** (whether commands run automatically or require human approval). As autonomy increases, establishing clear [steering boundaries](concept:steering) and [environment sandboxing](concept:sandboxing) becomes essential.

## Demo it

<!-- demos -->
