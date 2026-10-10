---
role: commit-work
title: Review and commit what the agent produced
kind: mini
summary: Look at exactly what changed, keep the data and secrets out, and save a snapshot you can return to.
time: 5 min
teaches: [version-control, secrets, privacy]
needs: [make-tool-and-skill]
---

After this step you will have your project in Git with a sensible `.gitignore`, you will have reviewed what the agent changed, and you will know which files
should never be committed.

**Before you start:** a project folder with work in it, and Git installed ([Setup](setup:)). For a fuller treatment see the
[Git and GitHub](guide:git-and-github-for-coding-agents) guide.

## Background

Version control records snapshots (commits) of your project. Reviewing the **diff** before each commit is the best check on what an agent did
([Version control](concept:version-control)). Decide what stays out of the repository: data that is sensitive or large, generated files, and anything secret
([Secrets](concept:secrets), [Privacy](concept:privacy)).

## General approach

```text
Initialise a git repository here if there is none. Create a .gitignore that excludes data files, outputs, secrets, and environment folders. Show me
git status and a summary of what would be committed. Do not commit yet.
```

Read the list. Then:

```text
Commit the scripts, notes, README.md, AGENTS.md and the skill with a clear message. Do not push.
```

Pushing to a hosted copy is a separate decision, and a public repository is public.

<!-- example -->

## What to check

- No data files, secrets, or generated outputs are in the commit list.
- The message describes what changed.
- Nothing was pushed without your say-so.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| Large or sensitive files appear in status | `.gitignore` incomplete | Add them and verify with `git status` |
| A secret was committed | It was not ignored | Treat as leaked: revoke and replace it ([Secrets](concept:secrets)) |
