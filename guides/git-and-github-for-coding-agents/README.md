# Git and GitHub for Coding-Agent Users

Git gives a project a reviewable memory: it records what changed, why it changed, and what happened before and after. For coding-agent work, that history is more than backup. It lets you inspect an agent’s changes, preserve useful progress, hand work to another person or agent, and recover without guessing.

You do **not** need to master every Git command. You need a reliable working loop: inspect the repository, make one coherent change, review it, validate it, record it with a useful commit, and publish it only when appropriate.

> **Core habit:** make frequent, atomic commits. Each commit should be a small, reviewable statement about one completed change and why it exists.

This guide focuses on Git, usually hosted on GitHub. Git is the version-control system that works on your computer; GitHub is one service that hosts Git repositories and adds collaboration and review tools.

## Contents

1. [The basic mental model](#the-basic-mental-model)
2. [Inspect before an agent changes anything](#inspect-before-an-agent-changes-anything)
3. [Atomic commits are durable agent memory](#atomic-commits-are-durable-agent-memory)
4. [Stage deliberately and review the exact commit](#stage-deliberately-and-review-the-exact-commit)
5. [Use branches as focused workspaces](#use-branches-as-focused-workspaces)
6. [GitHub, remotes, pushing, and pull requests](#github-remotes-pushing-and-pull-requests)
7. [Recover safely and recognize dangerous commands](#recover-safely-and-recognize-dangerous-commands)
8. [Keep secrets and generated clutter out of history](#keep-secrets-and-generated-clutter-out-of-history)
9. [Direct an agent through Git work](#direct-an-agent-through-git-work)
10. [A compact working checklist](#a-compact-working-checklist)

## The basic mental model

A **repository** is a project directory whose file history Git tracks. A **commit** is a named, permanent record of a deliberate set of changes. Commits connect to prior commits, creating history. A **branch** is a named line of that history, normally used to keep one piece of work separate from another.

The main pieces are:

```text
working files → staging area → local commit history → remote repository
                  git add       git commit          git push
```

| Term | Plain-language meaning |
| --- | --- |
| working tree | The files currently on your computer, including edits not yet committed. |
| staging area | The exact file changes selected for the next commit. |
| commit | A local, named snapshot of staged changes plus its place in history. |
| branch | A movable name for a line of work, such as `main` or `guides/git-basics`. |
| remote | A named external copy of a repository, commonly `origin`. |
| GitHub | A hosting and collaboration service for Git repositories. |
| pull request (PR) | A reviewable proposal to merge one branch into another on GitHub. |

A commit is local. A **push** sends commits to a remote such as GitHub. That distinction matters: committing records a local decision; pushing publishes it to collaborators and services that can access the remote.

## Inspect before an agent changes anything

Before an agent edits a repository, establish its current state:

```bash
git status
git branch --show-current
git log --oneline --decorate -10
git remote -v
```

These commands answer four important questions:

- Is there already uncommitted work?
- Which branch are we on?
- What happened recently?
- Is a remote configured, and where could work be pushed?

If `git status` reports existing changes, stop and inspect them before the agent touches related files:

```bash
git diff
git diff --cached
```

| Command | Question it answers |
| --- | --- |
| `git status` | What changed, what is staged, and what branch is active? |
| `git diff` | What file content is changed but not staged? |
| `git diff --cached` | What exact content would the next commit contain? |
| `git log --oneline --decorate -10` | What are the recent commits and branch pointers? |
| `git show <commit>` | What did a particular commit change? |

### Preserve work you did not start

An agent should not quietly absorb, overwrite, stage, or commit existing user changes. Those changes may be unfinished work, local configuration, another person’s work, or a deliberate experiment.

A safe instruction is:

> Inspect the repository state without modifying it. Identify the current branch, pre-existing changes, recent commits, and remotes. Keep unrelated existing changes untouched.

If the task requires working alongside existing changes, decide explicitly which files belong to the new work and which do not.

## Atomic commits are durable agent memory

An **atomic commit** is one coherent, reviewable change. It does not have to contain only one file or be artificially tiny. A guide plus its index entry is one coherent change. A report generator plus its tests and documentation may be one coherent change.

What makes a commit atomic is that a reviewer can answer, “What changed, why, and how was it checked?” without disentangling unrelated work.

### Why frequent atomic commits help

For an agent, a useful commit history acts as durable context after working memory, chat sessions, or personnel change. It enables:

- review of a small, understandable diff;
- recovery by reverting one decision rather than a week of mixed edits;
- identifying when a behavior or regression was introduced;
- resuming work with less dependence on an old conversation;
- selective transfer of a focused change to another branch; and
- clearer handoff to a human collaborator or another agent.

A large uncommitted change set is hard to inspect and easy to accidentally overwrite. Frequent commits turn completed, validated steps into a stable trail.

### Good commit messages

Use a concise imperative summary: describe what the commit does, not what you happened to type.

Good examples:

```text
Add Linux command line guide for agents
Document atomic commit workflow
Validate duplicate survey IDs before reporting
Ignore local environment files
Clarify approval boundary for external API calls
```

Weak examples:

```text
updates
fix stuff
WIP
changes from agent
final final version
```

If the reason is not evident from the summary and diff, add a short body explaining the decision, relevant constraint, or validation. For example:

```text
Use staged report generation for large document sets

Start with a sampled extraction pass so review effort and error rates are
visible before the full collection is processed.
```

### What should not be one commit

Avoid combining unrelated changes simply because they are ready at the same time:

```text
Update project
- add a new guide
- format unrelated source files
- upgrade dependencies
- add an experimental script
- change deployment configuration
```

Separate them into coherent commits such as:

```text
Add Git guide outline
Add atomic-commit examples to Git guide
Ignore local environment files
```

Atomic does **not** mean committing knowingly broken work just to create a checkpoint. Prefer a commit that leaves the project in a reasonable, validated state. If a temporary checkpoint is unavoidable, label its limitation clearly and do not publish or merge it as if it were ready.

## Stage deliberately and review the exact commit

The staging area lets you choose exactly what the next commit contains. `git add` does not upload or commit anything; it only selects changes for the next local commit.

Prefer explicit paths:

```bash
git add guides/git-and-github-for-coding-agents/README.md
git add guides/README.md
git diff --cached
git commit -m "Add Git and GitHub guide for agents"
```

This sequence is safer than staging every changed file by habit. `git add .` may be appropriate when you have deliberately inspected all changes, but it is not a good beginner default.

### A reliable commit loop

1. Make one coherent change.
2. Run the relevant check, test, or build.
3. Review unstaged content with `git diff`.
4. Stage only intended files or directories with `git add path`.
5. Review the proposed commit with `git diff --cached`.
6. Confirm it contains no secrets, generated clutter, or unrelated edits.
7. Commit with a clear message.
8. Inspect `git status` again.

If you staged a file by mistake, remove it from the staging area without discarding the file edit:

```bash
git restore --staged path/to/file
```

Then review and stage the right paths. This is one reason the staging area is useful: it separates “what I changed while working” from “what belongs in this particular historical record.”

## Use branches as focused workspaces

A branch is a separate line of work. Use one when a change is substantial, uncertain, experimental, needs review, or should not appear on `main` until it is ready.

Clear branch names describe purpose:

```text
guides/git-for-agents
fix/report-validation
experiment/document-extraction
```

Basic commands:

```bash
git switch -c guides/git-for-agents
git branch --show-current
git switch main
```

A focused branch helps keep reviews and reversions understandable. Avoid using a single long-lived “everything” branch for unrelated work.

### Protect the shared baseline

In many projects, `main` is the shared or release-ready baseline. A safe default is:

- create a branch for a feature, experiment, or material change;
- make atomic commits on that branch;
- review the diff against `main`;
- open a pull request when the work should be reviewed or merged; and
- push directly to `main` only when explicitly authorized by the project workflow.

An agent should not create, switch, merge, delete, or rewrite branches merely as a routine implementation detail. Those actions change the project’s collaboration structure and should be visible to the user.

## GitHub, remotes, pushing, and pull requests

Git works locally. GitHub stores a remote copy and provides collaboration features such as pull requests, issues, review comments, branch protections, and automation.

Inspect remotes with:

```bash
git remote -v
```

A common remote is named `origin`. Before pushing, confirm both the branch and the destination:

```bash
git branch --show-current
git remote -v
git status
```

Push a new branch with an upstream relationship:

```bash
git push -u origin guides/git-for-agents
```

The `-u` records the default remote branch for later pushes and pulls. A push publishes the commits to people and systems able to access that remote, so it is an external effect.

### Pull cautiously in collaborative repositories

When others may have updated the remote, inspect before integrating their work. A beginner-friendly command is:

```bash
git pull --ff-only
```

It updates your branch only when Git can move it forward without creating an implicit merge commit. If histories have diverged, it stops and gives you a chance to inspect the situation rather than inventing a merge strategy.

### Pull requests are review artifacts

A PR proposes bringing one branch into another, often into `main`. A useful PR has:

- a focused title describing the outcome;
- a concise explanation of what changed and why;
- validation performed and important limitations;
- a reviewable, focused diff; and
- no accidental secrets, generated output, or unrelated cleanup.

Creating a PR, merging it, or pushing commits are publishing actions. Require explicit approval unless the user has already delegated that publication step as part of the task.

## Recover safely and recognize dangerous commands

Git provides recovery tools, but some commands discard work or rewrite shared history. Start by inspecting, not by “fixing” blindly:

```bash
git status
git diff
git diff --cached
git log --oneline --decorate -10
```

### Commands that need a pause

| Command or action | Why to pause |
| --- | --- |
| `git restore file` | Can discard uncommitted edits in that file. |
| `git reset` | Its mode determines whether it unstages, moves history, or discards work. |
| `git reset --hard` | Discards local changes and moves the current branch; high risk. |
| `git clean -f` | Deletes untracked files; `-d` can include directories. |
| `git push --force` | Rewrites remote history and can hide collaborators’ work. |
| `git branch -D` | Deletes a branch even when its commits are not merged. |
| `git commit --amend` | Replaces a commit; can complicate shared history after push. |
| rebase, merge, or branch deletion | Changes history or collaboration structure and may need conflict resolution. |

Before any destructive or history-changing action, ask for explicit approval and state: the target, what might be lost or rewritten, whether work is already published, and the least destructive alternative.

### Prefer reversible recovery for published work

If a commit has already been shared, `git revert` is often safer than erasing it from history:

```bash
git revert <commit>
```

It creates a new commit that reverses the earlier change. That leaves a visible audit trail and avoids rewriting a shared branch. It still changes project behavior, so inspect the target and resulting diff before committing or pushing.

## Keep secrets and generated clutter out of history

A Git repository is easy to copy, search, mirror, and retain. Treat commits as durable and potentially visible. Do not commit API keys, passwords, private keys, tokens, `.env` files with real values, internal exports, personal data, or machine-specific credentials.

Use `.gitignore` to prevent newly untracked local files from being accidentally staged:

```gitignore
.env
.env.*
!.env.example
```

Commit a harmless `.env.example` that documents variable names and placeholders, not real values. Before every commit, inspect the staged content:

```bash
git diff --cached
git status
```

`.gitignore` is preventive, not retroactive. If a secret was already committed or pushed, removing the file in a later commit does not remove it from history or copies of the repository. Revoke or rotate the secret promptly, then follow the project’s incident process before considering history cleanup.

Generated outputs also deserve care. Commit them only when the project intentionally tracks generated artifacts. Otherwise, keep build directories, caches, local logs, editor state, and temporary exports out of commits so they do not obscure meaningful changes.

For fuller guidance on local `.env` files, separate agent accounts, and secret boundaries, see [The Linux Command Line for Coding-Agent Users](../linux-command-line-for-coding-agents/#secrets-env-files-and-external-access).

## Direct an agent through Git work

Tell the agent what Git boundaries apply. A capable instruction leaves routine commands to the agent while making project decisions and publication limits clear.

### Useful prompts

**Inspect safely**

> Inspect the repository without modifying it. Show the current branch, uncommitted changes, recent commits, configured remotes, and any project instructions that affect Git work.

**Implement one focused change**

> Implement this as a focused change. Preserve unrelated existing changes. Run the relevant checks and show the diff before staging anything.

**Plan atomic commits**

> Propose an atomic commit plan. Group only related files together, give each group a concise commit message, and identify the validation that should precede each commit.

**Review before committing**

> Stage only these files. Show `git diff --cached`, summarize the change, and wait for approval before committing.

**Work on a branch without publishing**

> Create a focused feature branch and make validated atomic commits. Do not push, open a pull request, merge, or modify `main` without my approval.

**Undo published behavior carefully**

> We need to undo this published behavior. Inspect the relevant commits and explain the safest reversible option before changing history or files.

### Recommended agent defaults

Unless the user directs otherwise, an agent should:

- inspect `git status` and existing changes before editing;
- leave unrelated user changes untouched;
- use explicit staged paths and review `git diff --cached`;
- make coherent, validated commits with clear messages when asked to commit;
- stop before pushing, opening/merging a PR, changing shared branches, or using destructive Git commands; and
- report the branch, commit IDs, validation results, and remaining uncommitted work.

Git is most useful when it records real decisions, not when it becomes ceremony. A small one-off change may not need a new branch or an immediate commit. A multi-step agent task, recurring workflow, or consequential change usually benefits from an understandable history.

## A compact working checklist

### Before agent work

- [ ] I know the current branch, remote, and `git status`.
- [ ] I have identified pre-existing changes and decided how they will be preserved.
- [ ] I know whether this work belongs on a focused branch.
- [ ] I know the project’s rules for commits, branches, reviews, and generated files.

### Before each commit

- [ ] The staged files represent one coherent purpose.
- [ ] I inspected `git diff --cached`, not only the working-tree diff.
- [ ] Relevant checks passed, and their limitations are understood.
- [ ] No secrets, local `.env` files, generated clutter, or unrelated edits are staged.
- [ ] The message clearly says what changed; a body explains important reasons or constraints.

### Before publishing

- [ ] The branch and remote destination are correct.
- [ ] Pushing, PR creation, or merging is explicitly approved.
- [ ] The diff is focused and reviewable.
- [ ] No destructive history rewrite or force push is needed; if one is proposed, its risk and alternatives were reviewed.

Frequent atomic commits let a project—and the agents working in it—remember what happened without relying on an old chat session. Inspect first, commit coherent validated steps, and treat publication and history rewriting as decisions rather than routine shell commands.
