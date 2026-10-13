---
id: memory
title: Memory — durable knowledge lives in files
short: Memory
themes: [context-discipline, recursive-ai]
related: [context, tools, steering, version-control]
blurb: Language models do not retain memory across sessions. Preserving knowledge requires externalizing guidelines, documentation, and tools into persistent files.
---

Autoregressive foundation models maintain no persistent internal state across independent invocations. Once an interactive session ends, the active context window is discarded. Consequently, the only durable mechanism for preserving project knowledge between sessions is external storage: **persisting guidelines, decisions, and logic into local files**.

## The hierarchy of externalized project memory

| Memory layer | Artifact structure | Ingestion mechanism | Optimal research role |
|---|---|---|---|
| **Standing instructions** | `AGENTS.md` in the project root | Loaded into context automatically at session initialization | Global repository rules, directory paths, and mandatory coding standards |
| **Project documentation** | `README.md`, protocol notes | Read on demand when directed by the user or discovered via file search | Study background, data provenance, analytical rationale, rerun instructions |
| **Procedural skills** | `SKILL.md` in dedicated skill folders | Loaded dynamically when a user prompt matches skill criteria | Complex multi-step runbooks (e.g., *"compile monthly quality control report"*) |
| **Deterministic tools** | Parameterized scripts with CLI interfaces | Executed as standalone programs in the local shell | Core analytical algorithms, data transformations, and statistical pipelines |

**A guiding principle:** If you explain a methodological preference twice, document it in `AGENTS.md`; if you request the same multi-step procedure a third time, codify it as a reusable skill or executable tool.

While file naming conventions vary across agent harnesses (`AGENTS.md` is an emerging cross-vendor standard, though some tools use platform-specific files), storing conventions in plain Markdown ensures your instructions remain portable across platforms.

## Proprietary harness memory features

Certain commercial agent platforms offer built-in semantic memory systems that automatically index past user interactions. If you use these features, understand what data is retained, where it is stored, and how to audit or delete entries. For shared research environments, storing instructions in repository files provides greater transparency, auditability, and team collaboration.

## What to document in project memory

- **Methodological decisions:** Document variable definitions, outlier thresholds, and analytical justifications (e.g., *"Excluded site C due to telemetry clock drift"*).
- **Environment and execution commands:** Explicit instructions for activating virtual environments and running pipelines.
- **Negative constraints:** Explicit boundaries detailing actions the agent must avoid (e.g., *"Never edit raw CSV files directly"*).

Avoid recording trivial implementation details that an agent can easily derive by reading the code. Keep `AGENTS.md` **concise and focused**: because standing instructions consume context tokens on every single turn, bloated instruction files reduce available context and dilute the model's focus.

## Using the agent to draft its own documentation

An effective pattern is to prompt the agent to synthesize recent analytical decisions directly into `AGENTS.md` or a study log:

```text
Summarize the data cleaning rules and cohort exclusion criteria we just established.
Append them to AGENTS.md in a clean, concise bulleted format.
```

Review the draft carefully to trim redundant explanations and verify accuracy before committing the changes.

## Deterministic tools as the highest form of memory

Prose instructions require stochastic interpretation by the model on every run. In contrast, an executable script performs the exact same mathematical operations every time and can be validated with automated tests. Once an analytical procedure stabilizes, package the logic into a standalone tool and reference its command syntax in documentation ([Tools](concept:tools)).

## Maintenance and version control

Outdated instructions are worse than missing instructions: they cause agents to run obsolete scripts or reference missing directories. Keep memory files under [version control](concept:version-control), review instruction changes alongside code diffs, and ensure credentials never enter persistent documentation ([Secrets](concept:secrets)).

## Demo it

<!-- demos -->
