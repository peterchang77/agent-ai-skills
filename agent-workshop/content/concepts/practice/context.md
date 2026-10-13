---
id: context
title: Context — the agent's working memory
short: Context
themes: [context-discipline]
related: [memory, costs, scoping-work, inputs]
blurb: Context represents the model's active working memory. Because every turn re-transmits the complete conversation, long sessions increase latency, cost, and attention drift.
---

In language model architectures, **context** encompasses everything visible to the model on a given turn: system prompts, standing instructions such as `AGENTS.md`, user directives, previous agent replies, files loaded into memory, and the stdout/stderr of executed commands. Context serves as the agent's active working memory, but it is strictly finite, incurs computational and financial costs, and dissolves when the session terminates.

![Context accumulating over time. Turn 1 holds the base context: system rules, project memory such as AGENTS.md, and your goal. By turn 2 the agent has added tool calls and file contents. By turn N the full history, including terminal output, error logs, past iterations and revised scripts, approaches the token limit.](image:agent-context-accumulation)

## The mechanics of stateless inference

Because foundation models are mathematically stateless, they retain no internal memory between requests. To maintain continuity throughout an interactive session, the agent harness re-transmits the **complete conversation history**—alongside your newest directive—with every single turn.

This architectural requirement produces three direct consequences:
- **Escalating cost:** Token consumption compounds over time. Turn 20 processes all tokens generated across turns 1 through 19 plus its own output ([Costs](concept:costs)).
- **Increased latency:** Time-to-first-token increases as the model processes longer input sequences.
- **Attention degradation (Context pollution):** As the context window fills with verbose terminal logs, repetitive debugging attempts, and large text dumps, the model's attention mechanism becomes diluted. Early instructions and subtle constraints are more likely to be overlooked or deprioritized.

## Understanding token budgets

Language models process text as **tokens**—discrete sub-word character fragments. In English text, 1,000 tokens corresponds roughly to 750 words (about two pages of double-spaced prose). Context limits, computational throughput, and API pricing are measured in tokens.

## Realistic context limits in research workflows

While modern foundation models advertise context windows exceeding one million tokens, effective operational performance typically degrades well before reaching hardware limits. 

For precise analytical and coding tasks, maintain sessions **below 200,000 to 300,000 tokens**. Operating within this range preserves reasoning fidelity, reduces latency, and keeps token costs manageable. Compact or reset sessions earlier when executing sensitive statistical modeling or manuscript editing.

## Recognizing context saturation

- **Instruction regression:** The agent begins violating constraints established early in the session (e.g., modifying raw files it was told to leave untouched).
- **Repetitive questioning:** The agent asks questions or requests file paths that were already clarified earlier in the session.
- **Hallucinated drift:** The agent repeats previously failed approaches or drifts from the primary research hypothesis.

## Context management strategies

- **Dedicate one session per objective:** Scope each conversation to a single well-defined research milestone, starting a fresh session for the next task.
- **Execute manual compaction at natural milestones:** Rather than waiting for automatic compaction to truncate context unpredictably, request a structured summary at key breakpoints. Direct the agent to synthesize agreed decisions, completed scripts, and remaining questions into a Markdown file, then start a fresh session referencing that file.
- **Sample data schemas instead of printing raw tables:** Instruct the agent to inspect the schema (`df.info()`) and head/tail records with code, keeping raw multi-megabyte datasets out of the prompt ([Inputs](concept:inputs)).
- **Externalize key findings to disk:** Save intermediate artifacts, exclusion counts, and statistical estimates to local files ([Memory](concept:memory)).
- **Use fresh sessions for peer review:** When verifying code, launch a clean session with an empty context window so the reviewing agent evaluates the script independently without inheriting prior session momentum ([Verification](concept:verification)).
- **Monitor active token usage:** Keep an eye on the session's token consumption displayed by your harness to spot unexpected spikes.

## Demo it

<!-- demos -->
