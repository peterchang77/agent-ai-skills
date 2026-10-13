---
id: version-control
title: Version control
themes: [recursive-ai]
related: [memory, secrets, privacy, verification]
blurb: Version control provides an immutable audit trail and safety net, allowing researchers to inspect every line changed by an agent and roll back errors instantly.
---

In computational research, **version control** provides an immutable record of how code, documentation, and analytical pipelines evolve over time. When collaborating with an agent that can modify multiple files in seconds, version control serves as both your safety net and your scientific audit trail.

## Git and collaborative repositories

- **Git:** The local distributed version control engine that tracks file changes, manages branching, and creates immutable commit histories on your computer.
- **GitHub / GitLab:** Remote repository hosting platforms that facilitate collaborative code review, issue tracking, and cloud backups.

## Core concepts

| Concept | Technical role in research workflows |
|---|---|
| **Repository** | A project directory tracked by Git, containing the complete history of all tracked files. |
| **Commit** | A permanent, cryptographic snapshot of staged project files, accompanied by a descriptive message. |
| **Diff** | The exact line-by-line insertions, deletions, and modifications between two commits or working states. |
| **Branch** | An isolated, parallel lineage of development that allows testing experimental scripts without affecting the main pipeline. |
| **Push / Pull** | Synchronizing local commits with a remote repository to back up work or collaborate with colleagues. |

## The supervisory collaboration loop

1. **Establish a clean baseline:** Ensure all existing work is committed before launching an agent task.
2. **Delegate the task:** Allow the agent to write scripts, modify functions, or generate tables.
3. **Inspect the unified diff:** Review `git diff` carefully to inspect the exact lines of code altered by the agent.
4. **Accept or reset:** Commit verified modifications with an informative commit message, or use `git restore` to discard flawed attempts instantly.

Adopt a pattern of small, modular commits: capturing one logical analytical change per commit makes peer review straightforward and allows precise rollbacks if an error is discovered later.

## Security and data governance guardrails

- **Require human approval for staging and pushing:** Treat committing and pushing to remote servers as operations with external side effects ([Steering](concept:steering)). An agent should draft commit messages, but researchers should review staged files before finalizing.
- **Enforce `.gitignore` exclusions:** Never commit [secrets](concept:secrets) (such as `.env` files), raw empirical datasets, large binary archives, or Python virtual environments (`.venv/`).
- **Protect against public repository leaks:** Pushing sensitive clinical records or proprietary intellectual property to a public GitHub repository represents a severe data incident that rewriting local history cannot easily undo ([Privacy and data handling](concept:privacy)).
- **Track project memory assets:** Maintain standing instructions (`AGENTS.md`), custom skills, and analysis scripts under version control so the evolution of project prompts is audited alongside the code ([Memory](concept:memory)).

For detailed CLI command references and disaster recovery workflows, consult the [Git and GitHub for coding agents](guide:git-and-github-for-coding-agents) guide.

## Demo it

<!-- demos -->
