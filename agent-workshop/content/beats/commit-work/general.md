---
role: commit-work
title: Review and commit what the agent produced
kind: mini
summary: Audit repository state, configure .gitignore to exclude raw data and secrets, and record an immutable Git commit snapshot.
time: 5 min
teaches: [version-control, secrets, privacy]
needs: [make-tool-and-skill]
---

In this exercise, you initialize Git version control, configure `.gitignore` exclusions to safeguard raw datasets and credentials, review the exact code diff produced by the agent, and commit an immutable snapshot of your project.

**Before you start:** A project directory with analytical scripts and documentation, and Git installed on your system ([Setup](setup:)). For a comprehensive guide, see [Git and GitHub](guide:git-and-github-for-coding-agents).

## Background

Version control creates permanent cryptographic snapshots of your project. Reviewing the line-by-line **unified diff** before staging files is the most effective supervisory mechanism for auditing code authored by an agent ([Version control](concept:version-control)). 

Strictly exclude non-source files from version control: sensitive or high-volume datasets, intermediate binary build outputs, Python virtual environment trees (`.venv/`), and configuration files containing access credentials ([Secrets](concept:secrets), [Privacy and data handling](concept:privacy)).

## General methodology

Direct the agent to initialize the repository, configure exclusions, and display staged files without executing the commit autonomously:

```text
Initialize a Git repository here if none exists.
Create a .gitignore file explicitly excluding raw data directories, generated output files, .env credential files, and virtual environments (.venv/).
Display git status and a unified diff summarizing staged changes.
Do not commit yet.
```

Review the output carefully to verify that no excluded assets appear in the staging area. Then instruct the agent to commit the approved files:

```text
Commit scripts/, notes/, README.md, AGENTS.md, and custom skills with an informative commit message.
Do not execute git push.
```

Publishing commits to a remote hosting platform (such as GitHub) is an operation with external side effects that should always require explicit human authorization ([Steering](concept:steering)).

<!-- example -->

## Verification criteria

- **Clean staging area:** No raw datasets, private credentials, or large binary outputs appear in `git status`.
- **Informative commit message:** The commit message clearly characterizes the analytical additions and tools introduced.
- **Local confinement:** The repository was committed locally without pushing to remote servers.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Datasets or `.venv/` appear in `git status` | `.gitignore` pattern was missing or misconfigured | Add missing directory patterns to `.gitignore` and re-verify with `git status` |
| Credential committed to Git history | `.env` was staged prior to adding to `.gitignore` | Treat the token as compromised: revoke and rotate the secret immediately ([Secrets](concept:secrets)) |
