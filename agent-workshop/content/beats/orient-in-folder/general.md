---
role: orient-in-folder
title: Orient the agent in a folder
kind: mini
summary: Direct the agent to audit local project files, establishing environmental grounding and identifying files requiring specialized parsers.
time: 3 min
teaches: [agent-vs-chat, harnesses]
needs: []
---

When launched, a coding agent possesses no implicit knowledge of local project contents. The essential first step in any research workflow is establishing environmental grounding: directing the agent to inspect the active directory, inventory available datasets, and characterize file formats. This exercise provides your first tactile experience of tool-mediated agency in action—watching the agent actively choose how to navigate your directory rather than being confined to a single guessing path from pre-trained memory.

**Before you start:** An active agent running inside your project directory ([Setup](setup:)).

## Background

An agent operates strictly within the working directory where its harness process was launched. It explores the workspace by executing standard operating system utilities (such as `ls` or directory walks) and reading the resulting stdout stream into working memory ([Agent vs. chat](concept:agent-vs-chat)). Ensuring the agent is initialized in the correct project root is critical for accurate file discovery.

This prompt serves as an immediate diagnostic test of the difference between chat and agents:

- Submitting *"What files are in this folder?"* to a standard chat window yields an apology or an invented guess, because a standalone model cannot touch your storage.
- Submitting the same prompt to an agent causes the harness to dispatch a shell command, read the console output, and report empirical reality.

## General methodology

Instruct the agent to provide a structured directory inventory and identify files that cannot be parsed as plain text. This diagnostic step immediately reveals which datasets or documentation will require specialized libraries or conversion pipelines ([Inputs](concept:inputs)).

```text
What files are in this folder? Describe each in one line, and identify which ones cannot be parsed as plain text.
```

<!-- example -->

## Verification criteria

- **Verified command execution:** Confirm that the agent ran an actual terminal command (e.g., `ls -la` or `find`) rather than inferring file contents from the project directory name.
- **Empirical file inspection:** Verify that the agent sampled file headers or metadata before generating descriptions.
- **Format discrimination:** Ensure the agent correctly flagged binary containers (such as `.xlsx`, `.docx`, or `.pdf`) as requiring dedicated readers.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Describes non-existent files | Hallucination due to lack of tool execution | Prompt: *"Which specific command did you execute to inspect this directory?"* |
| Reports an empty directory | Agent was launched from an incorrect parent or child directory | Terminate the session, change into the intended project directory (`cd ~/workshop-demo`), and relaunch |

## Next step: how code expands the agent's reach

Now that the agent can perceive your project directory, what can it actually do with these files? To understand how an agent manipulates data, generates figures, and compiles publications, the next concept explores how an agent uses code as a universal scientific instrument ([What code makes possible](concept:what-code-can-do)).
