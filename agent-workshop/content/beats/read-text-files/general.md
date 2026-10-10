---
role: read-text-files
title: Read and summarize text files
kind: full
summary: The agent opens local text files itself. You name the files and the task; you do not paste anything.
time: 5 min
teaches: [inputs, verification]
needs: [orient-in-folder]
---

Plain text is the easiest thing for an agent to work with. After this step you will know how to point an agent at local text
files, and how to confirm it really read them.

**Before you start:** a project folder with text-based files in it ([Setup](setup:)).

## Background

Text, Markdown, CSV, JSON, LaTeX, and HTML files are all just text, so the agent can open them directly with no extra
software ([Inputs](concept:inputs)). Pointing at a file is better than pasting its contents: nothing is retyped, nothing
loses its columns, and the file stays the single source of truth.

## General approach

Name the files and the task, and ask the agent to show where each claim came from.

```text
Read <file1> and <file2>. Summarize <what you want>. For each point, say which file it came from.
```

Asking for sources turns "it read something" into something you can check ([Verification](concept:verification)). If the
files contain sensitive data, check first that your model endpoint is approved for it ([Privacy](concept:privacy)).

<!-- example -->

## What to check

- The agent opened each named file (look for the read or command in the transcript).
- Each point in the summary traces to a specific file.
- Nothing in the summary is missing from the files, and nothing important in the files is missing from the summary.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| Vague summary | The task was vague | Say what the summary is for and in what shape |
| Claims not in the files | It filled gaps from general knowledge | Ask it to quote the supporting line, and drop unsupported points |
