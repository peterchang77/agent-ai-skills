---
id: glossary
title: Glossary
blurb: Definitions of foundational terms and concepts used across the workshop.
---

| Term | Definition |
|---|---|
| **Agent** | An AI system pairing a foundation model with an operational harness, enabling it to inspect files, execute code, and interact with external environments. See [Agent vs. chat](concept:agent-vs-chat). |
| **Agent Harness** | The client application that manages session state, assembles system prompts, invokes tools, and prompts for human approvals. See [Harnesses and models](concept:harnesses). |
| **Foundation Model** | The underlying language model that processes input context and generates text or structured tool invocations. |
| **Context** | The complete sequence of text tokens available to the model on an active turn, including instructions, conversation history, and terminal output. See [Context](concept:context). |
| **Token** | A discrete sub-word character fragment; the base unit used to measure context window size, throughput, and compute pricing. |
| **Compaction** | Synthesizing a lengthy session history into a structured summary to free working context while preserving critical analytical state. |
| **Prompt** | The text instruction, query, or constraint provided to the agent by the user. |
| **AGENTS.md** | A standardized repository configuration file containing standing instructions and conventions loaded by the agent at session initialization. See [Memory](concept:memory). |
| **Skill** | A packaged operational runbook stored in a dedicated directory, loaded dynamically when a user prompt matches its role. |
| **Tool** | An executable program, library, or script that an agent can invoke to inspect state or perform deterministic computations. See [Tools](concept:tools). |
| **API** | Application Programming Interface: a structured network interface enabling software systems to exchange data. |
| **Environment** | The isolated software runtime, package libraries, and system utilities configured for a specific project. See [Environment](concept:environment). |
| **Package Manager** | A tool (such as `uv` or `conda`) that automates library installation and pins dependency versions in reproducible lockfiles. |
| **Sandbox** | An isolated execution boundary (e.g., container or virtual machine) restricting an agent's filesystem and network privileges. See [Sandboxing](concept:sandboxing). |
| **Prompt Injection** | An adversarial attack where untrusted text read by an agent contains instructions intended to hijack model behavior. |
| **Repository (Repo)** | A project directory tracked by Git, containing the complete history of all tracked files. See [Version control](concept:version-control). |
| **Commit / Diff** | An immutable cryptographic snapshot of staged project files / the exact line-by-line differences between revisions. |
| **Secret** | A sensitive authentication credential, such as an API key, database password, or private certificate. See [Secrets](concept:secrets). |
| **OCR** | Optical Character Recognition: converting raster images of text into machine-readable character strings. |
| **BibTeX** | A standardized text format used for storing bibliographic references and citations. |
| **EDA** | Exploratory Data Analysis: the empirical practice of profiling distributions, missing values, and anomalies before formal modeling. |
