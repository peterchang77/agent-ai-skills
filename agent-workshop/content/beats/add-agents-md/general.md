---
role: add-agents-md
title: Make the agent remember with AGENTS.md
kind: full
summary: Persist critical project rules and analytical conventions in AGENTS.md, ensuring new sessions maintain project memory without redundant steering.
time: 8 min
teaches: [memory, context, steering]
needs: [clean-data]
---

Because language models maintain no persistent internal state across independent sessions, launching a new conversation typically requires re-explaining directory structures, cleaning conventions, and project constraints. In this exercise, you observe this loss of context firsthand and resolve it by establishing an `AGENTS.md` configuration file.

**Before you start:** A project directory where key analytical decisions have already been made ([Setup](setup:restore-a-starting-point)).

## Background

When an interactive session terminates, the active conversational context is discarded ([Context](concept:context)). The only way to preserve state across sessions is through persistent **files**. 

An **`AGENTS.md`** file located in the project root is automatically ingested by most modern agent harnesses at session initialization, providing a standardized, portable mechanism for project memory ([Memory](concept:memory)). 

Effective standing instructions must be concise and specific: documenting directory locations, active cleaning definitions, output paths, and strict negative constraints (such as never overwriting raw datasets). Because every line in `AGENTS.md` consumes context tokens on every turn, keep the file concise and focused.

## General methodology

1. **Observe context loss:** Launch a fresh agent session in the project directory and prompt it with a question that depends on prior decisions. Note how the agent either makes incorrect assumptions or asks for clarification on previously resolved conventions.
2. **Draft standing instructions:** Instruct the agent to synthesize the established project conventions into `AGENTS.md`:

```text
Create an AGENTS.md file in the project root (under 25 lines) documenting:
- Relative paths to raw data, cleaned datasets, and the data dictionary.
- Key data cleaning rules and cohort definitions established so far.
- Designated output directories for generated tables and figures.
- Explicit operational constraints (e.g., raw data is read-only; all numbers must report denominators).
Keep instructions concise and specific. Omit trivial details that can be derived directly from the code.
```

3. **Verify memory persistence:** Launch another new session and re-issue the initial query from step 1. The agent should now execute the task adhering to the documented conventions without asking redundant questions.
4. **Refine instructions recursively:** Direct the agent: *"Review AGENTS.md and remove any vague generalities or redundant rules."* Using the agent to audit its own instructions is a high-leverage maintenance practice ([Steering](concept:steering)).

<!-- example -->

## Verification criteria

- **Concise and specific:** The file remains under 25 lines and provides concrete rules rather than vague generalities.
- **Security compliance:** The file contains zero API keys, passwords, or confidential data ([Secrets](concept:secrets)).
- **Effective steering:** In a clean test session, the agent correctly cites and adheres to the rules defined in `AGENTS.md`.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Agent ignores instructions | File name or directory location does not match harness configuration conventions | Verify the expected instruction file convention for your specific agent harness |
| Bloated, generic instructions | Prompt failed to enforce brevity constraints | Edit the file to retain only high-impact rules that prevent genuine operational mistakes |
| Contradictory rules | Instructions reflect outdated draft decisions rather than finalized rules | Reconcile `AGENTS.md` directly against `notes/cleaning-decisions.md` |
