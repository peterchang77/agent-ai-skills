---
role: orient-in-folder
title: Orient the agent in a folder
kind: mini
summary: Ask a question about your files. A chat cannot answer it; an agent answers by looking.
time: 3 min
teaches: [agent-vs-chat, harnesses]
needs: []
---

An agent starts with no idea what is on your computer. Your first useful move in any project is to have it look. After this
step you will know how an agent discovers files, and you will have seen the practical difference between chat and an agent.

**Before you start:** an agent running inside a project folder that contains some files ([Setup](setup:)).

## Background

An agent works in the folder where you launched it. It looks around by running ordinary commands (list a directory, open
a file) and reading the output as text ([Agent vs. chat](concept:agent-vs-chat)). That is why it matters where you start it.

## General approach

Ask for an inventory, and ask which files it could not read as plain text. That second question tells you early which
files will need conversion ([Inputs](concept:inputs)).

```text
What files are in this folder? Describe each in one line, and tell me which ones you could not read as plain text.
```

For contrast, ask the same question in an ordinary chat window. It can only guess, because it cannot see your files.

<!-- example -->

## What to check

- The agent actually listed the folder (you can see the command), rather than guessing from the project name.
- It opened or inspected files before describing them.
- It flagged binary formats (spreadsheets, Word documents, PDFs, databases) as needing a reader.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| It describes files that do not exist | It answered from habit, not by looking | Ask: "Which command did you run to see this?" |
| It sees an empty or wrong folder | The agent was started somewhere else | Quit, `cd` to the right folder, and restart |
