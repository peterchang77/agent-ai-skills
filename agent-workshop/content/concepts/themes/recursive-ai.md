---
id: recursive-ai
title: Theme — use AI recursively
short: Use AI recursively
blurb: "Apply the agent recursively to improve your collaboration workflows: drafting plans, refining instructions, reviewing code, and packaging tools."
related: [scoping-work, memory, verification, tools, steering]
---

A high-leverage pattern in computational research is **applying the agent to refine the collaborative workflow itself**:

| Recursive task | Research application | Reference module |
|---|---|---|
| **Pre-execution planning** | Formulate structured analytical proposals and identify open methodological questions | [Scoping work](concept:scoping-work) |
| **Instruction maintenance** | Synthesize agreed rules into `AGENTS.md` and prune redundant guidelines | [Memory](concept:memory), [Steering](concept:steering) |
| **Independent peer review** | Audit a prior session's analysis using a separate agent with a fresh context | [Verification](concept:verification) |
| **Tool codification** | Convert an interactive exploratory workflow into a parameterized script or custom skill | [Tools](concept:tools) |
| **Environment configuration** | Audit local dependencies and document environment setup in `pyproject.toml` | [Environment](concept:environment) |
| **Provenance tracking** | Draft informative Git commit messages and explain code diffs | [Version control](concept:version-control) |

Always audit generated artifacts critically. Recursive workflows amplify productivity only when the human researcher maintains methodological leadership.
