---
id: agent-vs-chat
title: Agent vs. chat
themes: [text-formats, recursive-ai]
related: [what-code-can-do, harnesses, verification]
blurb: A standard chat model answers from training memory. An agent interacts with a live computing environment to inspect files, execute code, and produce verifiable artifacts.
---

Most researchers first encounter artificial intelligence through conversational chat interfaces: you provide a prompt, and the model generates a response based on patterns learned during training. A coding agent connects that same underlying language model to an execution environment—such as a local terminal, filesystem, and external tools. This operational interface fundamentally transforms both what tasks you can delegate and how you must evaluate the results.

![Chat compared with an agent. A chat model works only with text you paste in. An agent runs code in a local terminal, reads and writes local files, and fetches data from APIs and the web, inside an autonomous loop of acting, observing and fixing.](image:agent-vs-chat)

## What does "agency" mean here?

In everyday conversation, "agency" often implies conscious intent, free will, or independent desire. In artificial intelligence, the term has a much more practical and concrete meaning rooted in **choice and navigation**:

> **A standard language model has only one path.** Given a prompt, token generation proceeds sequentially along a single forward track until it emits a stop token. The model cannot pause to consult an external resource, verify a claim against local reality, or alter its trajectory.
>
> **An agent has choices.** Equipped with a suite of tools, the model actively decides how to **navigate the external world**.

When an agent works toward a research objective, the path is not predetermined:
- **Choosing where to look:** When entering an unfamiliar project directory, the agent decides whether to inspect the directory tree, read a configuration file, or examine the top rows of a data table.
- **Choosing which tools to deploy:** Rather than guessing an answer from static training memory, the agent selects among available tools—dispatching a shell command, executing a Python test, querying an API, or searching documentation.
- **Navigating dynamically from feedback:** When a script encounters an unexpected error or a data parser hits an unmapped column, the agent inspects the console output, diagnoses the failure, and chooses an alternate path forward.

Tools serve as navigational instruments. Without tools, a language model is confined to a single speculative output stream. With tools, the model gains the agency to explore, probe, and manipulate its environment.

Crucially, this agency is **delegated and bounded**: the human researcher defines the objective, sets operating constraints, and decides how much supervisory control to retain.

## An intuitive analogy: the phone consultant vs. the bench colleague

To understand the difference in daily practice, consider two ways to collaborate on research:

- **Conversational chat is like a phone consultation:** Imagine calling an expert statistician while sitting in your laboratory. You describe a messy dataset verbally over the phone; they dictate a statistical script from memory. If their dictated code has a typo, or if your dataset contains an unexpected column format, neither of you knows until you hang up, copy the code into your editor, and run it yourself. If it crashes, you must call them back, paste the error message into the conversation, and start over. The interaction is closed-book, memory-based, and disconnected from your files.
- **A coding agent is like a colleague sitting at the terminal:** You seat the colleague in front of the workstation where your raw files live. You specify the objective: *"Check the distribution of baseline variables and calculate summary tables."* They don't merely dictate text; they open the data file, examine column headers, draft a Python script, execute it, encounter a formatting error, adjust the parsing logic, rerun the script, verify that the table rendered properly, and hand you the verified results alongside the complete terminal log.

## Architectural comparison

| Dimension | Conversational chat | Coding agent |
|---|---|---|
| **Information source** | Pre-training data plus text pasted into the prompt | Pre-training data plus local files, databases, APIs, and the web |
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

In practice, the boundary between chat and agents is a spectrum of **navigational freedom** (the tools, APIs, and file access granted to the model) and **delegated authority** (whether commands run automatically or require human approval). As autonomy increases, establishing clear [steering boundaries](concept:steering) and [environment sandboxing](concept:sandboxing) becomes essential.

## Next step: seeing environmental grounding in practice

To see tool-mediated navigation and environmental grounding in action, the first practical step is to launch your agent in a project directory and have it explore the workspace. In the next exercise, [Orient the agent in a folder](beat:orient-in-folder), you will witness how an agent actively navigates reality rather than guessing from training memory.

## Demo it

<!-- demos -->
