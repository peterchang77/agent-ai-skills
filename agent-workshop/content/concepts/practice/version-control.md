---
id: version-control
title: Version control
themes: [recursive-ai]
related: [memory, secrets, privacy, verification]
blurb: Git records every change so you can see what an agent did and undo it. It is the safety net that makes more autonomy tolerable.
---

**Version control** records the history of a project. With an agent making many edits, it becomes your undo button and your audit trail.

## Git and GitHub

- **Git** is the tool that records history on your computer.
- **GitHub** (and similar services) hosts a copy for sharing and backup.

## The vocabulary you need

| Term | Meaning |
|---|---|
| Repository | A project folder tracked by Git |
| Commit | A saved snapshot with a message |
| Diff | The exact lines that changed between two snapshots |
| Branch | A separate line of work |
| Push / pull | Send / receive commits to and from a hosted copy |

## The core loop with an agent

1. **Commit** a clean state.
2. Let the agent work.
3. **Review the diff.**
4. Commit what you accept, discard what you do not.

Prefer small, focused commits; one logical change each makes review and rollback easy. Let the agent draft the message and read it.

## Rules

- **Do not let the agent commit or push on its own** unless you have said so. Publishing is a side effect ([Steering](concept:steering)).
- **Never commit** [secrets](concept:secrets), large data files, or sensitive or patient data ([Privacy](concept:privacy)). Use a `.gitignore`.
- **A public repository is public.** Pushing sensitive data to one is a common mistake that is hard to undo.
- **Track your memory files** (`AGENTS.md`, skills, tools) so their history is reviewable ([Memory](concept:memory)).

For commands and recovery, see the [Git and GitHub for coding-agent users](guide:git-and-github-for-coding-agents) guide.

## Demo it

<!-- demos -->
