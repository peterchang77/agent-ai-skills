---
role: orient-in-folder
title: Orient the agent in a folder
kind: mini
summary: Direct the agent to audit local project files, establishing environmental grounding and identifying files requiring specialized parsers.
time: 3 min
teaches: [agent-vs-chat, harnesses]
needs: []
---

When launched, a coding agent possesses no prior knowledge of local project contents. The essential first step in any research workflow is establishing environmental grounding: directing the agent to inspect the active directory, inventory available datasets, and characterize file types. This exercise demonstrates how an agent discovers local files through active tool execution rather than static memory.

**Before you start:** An active agent running inside your project directory ([Setup](setup:)).

## Background

An agent operates strictly within the working directory where its harness process was launched. It explores the workspace by executing standard operating system utilities (such as `ls` or directory walks) and reading the resulting stdout stream into working memory ([Agent vs. chat](concept:agent-vs-chat)). Ensuring the agent is initialized in the correct project root is critical for accurate file discovery.

## General methodology

Instruct the agent to provide a structured directory inventory and identify files that cannot be parsed as plain text. This diagnostic step immediately reveals which datasets or documentation will require specialized libraries or conversion pipelines ([Inputs](concept:inputs)).

```text
What files are in this folder? Describe each in one line, and identify which ones cannot be parsed as plain text.
```

By comparison, submitting this prompt to a conversational chat interface produces speculative guesses, as a pure chat model lacks an execution harness to inspect your local storage.

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
