# The Linux Command Line for Coding-Agent Users

A coding agent often works through a command line: it inspects files, runs checks, edits code, and reports the resulting paths and output. You do **not** need to become a shell expert to work effectively with one. You do need enough command-line literacy to understand where the agent is working, what a command will touch, what authority it has, and what evidence to review.

This guide uses Bash-like examples because Bash is common on Linux. The core ideas—commands, arguments, paths, permissions, pipes, redirection, and exit status—also apply to shells such as `sh`, `zsh`, and fish. Where shell syntax differs, prefer the documentation for the shell you are actually using.

> **Default safety baseline:** use a separate unprivileged account for agent work; activate only intended project directories through a narrow shared group or ACL; keep secrets outside agent-readable project folders; inspect before modifying; and require explicit approval for destructive, external, costly, or sensitive actions.

## Contents

1. [What the shell is](#what-the-shell-is)
2. [The few commands worth recognizing](#the-few-commands-worth-recognizing)
3. [Read a command before approving it](#read-a-command-before-approving-it)
4. [Paths, directories, and quoting](#paths-directories-and-quoting)
5. [Pipes, redirection, wildcards, and status](#pipes-redirection-wildcards-and-status)
6. [Permissions, owners, groups, and directory access](#permissions-owners-groups-and-directory-access)
7. [A safer separate-agent-account workflow](#a-safer-separate-agent-account-workflow)
8. [Secrets, `.env` files, and external access](#secrets-env-files-and-external-access)
9. [Working with an agent in a project](#working-with-an-agent-in-a-project)
10. [Recognize trouble and recover](#recognize-trouble-and-recover)
11. [A compact daily checklist](#a-compact-daily-checklist)

## What the shell is

A **shell** is a program that reads a command and starts other programs. Bash is a common Linux shell. A command such as:

```bash
rg --files guides
```

asks the `rg` program to list files under `guides`. The shell interprets the command syntax, passes arguments to the program, shows its output, and reports whether it succeeded.

A coding agent uses the same environment. It is not inherently safer because it is an agent: a command can read, modify, delete, install, upload, or send whatever the account running it is allowed to reach. The useful question is not “does the agent understand Linux?” but:

> What will this command do, which paths or services will it touch, and is this account authorized to do that?

### Shell versus terminal

A **terminal** is the window or application where you interact with a shell. The **shell** is the command interpreter running inside it. You may see a prompt such as:

```text
agent@workstation:~/projects/example$
```

It normally tells you the current account (`agent`) and current directory (`~/projects/example`). Do not rely on the prompt alone—use `pwd` when the directory matters.

## The few commands worth recognizing

You do not need to memorize a command catalog. These commands cover much of what an agent does while inspecting and validating a project.

| Goal | Common command | What to notice |
| --- | --- | --- |
| Show current directory | `pwd` | Many relative paths depend on this location. |
| List files | `ls`, `ls -la` | `-a` includes hidden files; `-l` shows owner, group, and permissions. |
| Change directory | `cd path` | `cd ..` moves up one directory; `cd ~` goes to the current user's home. |
| Read text safely | `less file`, `head file`, `tail file` | Use `less` for large files; it does not modify them. |
| Search text | `rg "term" path`, `grep -R "term" path` | Search existing material before duplicating it. |
| List/find files | `rg --files path`, `find path -type f` | Inventory a project before editing it. |
| Create a directory | `mkdir directory` | `mkdir -p a/b` also creates missing parents. |
| Copy or rename | `cp source target`, `mv old new` | Targets matter; a wrong target can overwrite or relocate work. |
| Remove | `rm file`, `rmdir directory` | Usually no normal trash or undo—treat as high risk. |
| Inspect project changes | `git status`, `git diff` | Review these after an agent changes a version-controlled project. |

A coding agent should normally begin with low-risk inspection commands such as `pwd`, `ls`, `rg --files`, `git status`, and `git diff`. Ask it to state what it found before it modifies files.

## Read a command before approving it

A simple command often has this shape:

```text
program  options  arguments-or-targets
```

For example:

```bash
rg --files guides
```

- `rg` is the program.
- `--files` changes the program's behavior.
- `guides` is the target directory.

Before approving a command, ask three questions:

1. **What program will run?** Is it an inspection tool, an editor, an installer, a network client, or a deletion command?
2. **What will it touch?** Look for paths, wildcards, environment variables, URLs, package names, and destination files.
3. **What kind of effect does it have?** Does it only read, or can it create, modify, delete, send, install, spend, or use credentials?

### A practical risk ladder

| Level | Typical examples | Normal handling |
| --- | --- | --- |
| Inspect | `pwd`, `ls`, `rg`, `git status`, `git diff` | Usually safe to run in the intended project. |
| Local change | `mkdir`, code formatter, test that writes output, `cp`, `mv` | Confirm current directory, targets, and expected output. |
| High impact | `rm`, recursive permissions, package installation, database migration | Require explicit approval and a clear target/rollback plan. |
| External or sensitive | `curl`, deploy/publish/send commands, cloud tooling, credential use | Require explicit approval; verify destination, cost, and data boundary. |

Do not approve a command solely because it is compact or because an agent suggests it. A short command can affect many files; a long command can be harmless. Inspect its targets and authority.

## Paths, directories, and quoting

A **path** names a file or directory. Paths are either absolute or relative:

```text
/home/agent/projects/report/data/input.csv    # absolute: starts at /
data/input.csv                                # relative: starts at the current directory
```

Useful path markers:

| Marker | Meaning |
| --- | --- |
| `.` | current directory |
| `..` | parent directory |
| `~` | current user's home directory |
| `/` | filesystem root, or a path separator |
| `.name` | a hidden file or directory, such as `.gitignore` |

This makes the current directory important. Before a modifying command, a safe habit is:

```bash
pwd
ls -la
```

Then ask the agent to report the exact output path it created or changed.

### Quote filenames and literal values

Spaces and special characters can cause the shell to split or reinterpret text. Quote paths and values unless you specifically intend shell expansion:

```bash
less "monthly report.md"
cp "source data.csv" "output/clean data.csv"
```

Double quotes are a practical default for ordinary paths. Single quotes are more literal in Bash-like shells, but behave differently around variable expansion. The important beginner habit is simple: **do not leave a path with spaces unquoted.**

## Pipes, redirection, wildcards, and status

You will see these operators in agent commands and scripts. Learn to recognize their effects before using them in a command that changes anything.

### Pipes: `|`

A pipe sends the output of the command on the left to the command on the right:

```bash
rg "TODO" | head
```

This searches for `TODO` and shows only the first lines of matches. Pipes are often useful for inspection, but later commands in a pipeline can still modify files or send data elsewhere.

### Redirection: `>` and `>>`

Redirection writes command output into a file:

```bash
rg --files > file-list.txt
```

`>` creates or **replaces** the destination file. `>>` appends instead. Treat the destination as a modification target and verify it before running the command.

### Wildcards: `*`, `?`, and character patterns

A wildcard, often called a glob, can match many filenames:

```bash
ls *.csv
```

This does not refer to a literal file named `*.csv`; the shell expands it to matching files. That is convenient for inspection but risky for changing commands. For example, never casually approve a deletion command containing `*` without first seeing exactly what it matches.

### Success and failure: exit status

Programs normally return an **exit status** to the shell. By convention, `0` means success and a nonzero value means failure or an exceptional condition. Some search tools use a nonzero status to mean “no matches,” which is not necessarily a system error.

`&&` runs the next command only if the preceding command succeeds:

```bash
python3 -m pytest && git status
```

Output is evidence, but it is not proof by itself. A command can print something useful and still fail; a quiet command may succeed, fail, or find nothing. For important work, ask the agent to report the command, exit status, important output, and the limitation of that check.

## Permissions, owners, groups, and directory access

Linux normally associates each file and directory with an **owner** and a **group**. Permissions are evaluated for the owner, the associated group, and other users.

The main permission letters are:

| Permission | File meaning | Directory meaning |
| --- | --- | --- |
| `r` | read file contents | list names in the directory |
| `w` | change file contents | create, remove, or rename directory entries |
| `x` | run a program/script | enter or traverse the directory and access known entries |

Inspect them with:

```bash
ls -ld project-directory
ls -l project-directory
```

A line such as this:

```text
drwxrws--- alice agent-projects project-directory
```

shows a directory owned by `alice`, associated with `agent-projects`, and accessible to members of that group. The exact permission string is less important than understanding which account and group have access.

### Directories need traversal permission

A common surprise is that an agent can have permission on a project directory but still cannot reach it because a parent directory blocks traversal. The agent needs directory `x` permission on **each parent directory** in the path it must traverse.

Do not solve this by broadly making a personal home directory readable or writable. Prefer a dedicated shared project location such as `/srv/agent-projects`, or a narrow project directory whose parent path grants only necessary traversal.

## A safer separate-agent-account workflow

A separate local Unix account is a useful default for coding-agent work. It reduces accidental access to personal files, browser sessions, shell history, and credentials, and makes it clearer which projects have been deliberately activated for the agent.

It is an access boundary, not a complete sandbox. The account can still do anything its permissions, mounted filesystems, network access, installed tools, and credentials allow. Do not give it `sudo` access for ordinary work.

### Recommended default design

1. Create an unprivileged account for the agent, for example `agent`.
2. Create a narrowly scoped shared group, for example `agent-projects`.
3. Add your normal account and the agent account to that group.
4. Keep agent-ready projects in a dedicated location where the shared group can traverse the path.
5. Activate only a project that you intentionally want the agent to use by assigning the shared group and needed group permissions.
6. Switch to the agent with a login shell, then work only from that account for agent sessions.
7. Keep secrets, personal directories, cloud credentials, SSH keys, and unrelated projects outside the agent account's reachable paths.

Account and group creation are administrator actions and vary slightly by Linux distribution. Perform them once, carefully, as an administrator; do not let an ordinary coding agent create or reconfigure accounts, groups, or broad permissions without explicit review.

### Activate one project deliberately

The following is a conceptual example for a project whose current owner is authorized to change its group. Replace the names and paths with your own. Review the target path before using recursive commands:

```bash
# From your normal account, activate only this project.
chgrp -R agent-projects /srv/agent-projects/example-project
chmod -R g+rwX /srv/agent-projects/example-project

# Make future entries inherit the project group.
chmod g+s /srv/agent-projects/example-project
```

Important details:

- `chgrp` changes the associated group; it **does not by itself grant access**.
- `g+rwX` grants the group read/write access to ordinary files and read/write/traverse access to directories (and preserves executable access where appropriate). Recursive permission changes should be reviewed carefully, especially in projects containing executable files or unusual content.
- The set-group-ID bit on a directory (`g+s`) makes newly created entries inherit the directory's group on common Linux filesystems. This reduces collaboration friction.
- A `umask` or explicit permissions may still be needed for new files to remain group-writable. Verify with a small test file before trusting the arrangement.
- If one group is too broad, use a more specific group or filesystem ACLs rather than granting wide access.

Then begin the agent session using a login shell:

```bash
su - agent
cd /srv/agent-projects/example-project
```

The `-` matters: it starts a login shell with the agent account's normal environment rather than carrying more of the current account's environment forward. On systems configured for it, `sudo -iu agent` is an alternative for authorized administrators.

### Verify before running an agent

At the start of a session, inspect identity and access:

```bash
whoami
id
pwd
ls -ld .
git status
```

You should be able to answer: “Which account is this?”, “Which groups does it have?”, “Which project directory is active?”, and “Are there already changes in this project?”

When an agent creates a file, inspect its owner and group:

```bash
ls -l path/to/new-file
```

If group access is unexpectedly absent, stop and correct the project setup rather than making broad directories world-writable.

### What this protects—and what it does not

A separate agent account can reduce direct access to files you did not share. It does **not** automatically protect against:

- secrets copied into an activated project;
- unrestricted outbound network access;
- malicious or compromised dependencies;
- unsafe commands within an activated directory;
- cloud services reachable through accessible credentials;
- mount points, shared drives, sockets, or services the account can use; or
- privileged escalation if you grant `sudo` or equivalent authority.

For stronger isolation, consider a disposable VM or container, restricted network access, least-privilege service credentials, and separate secrets. Those are additional layers, not replacements for careful review.

## Secrets, `.env` files, and external access

Treat a secret as any value that grants access or reveals sensitive information: API keys, tokens, passwords, private keys, database URLs, cloud credentials, cookies, personally identifiable data, and internal endpoints.

### Default rules

1. **Never commit secrets.** A deleted commit is not a reliable way to remove a secret from history.
2. **Never paste real secrets into an agent chat, prompt, issue, log, or source file.** Assume a prompt may be retained by the service or visible in session records.
3. **Do not put secrets in a project an agent can read unless the task truly requires them.** Prefer a narrowly scoped, revocable credential only for the necessary service.
4. **Do not print secrets in terminal output.** Avoid commands such as `cat .env`; redact values when sharing diagnostics.
5. **Require explicit approval before an agent uses network credentials, calls paid APIs, deploys, publishes, sends mail, or accesses production systems.**
6. **Use test data and test credentials by default.** Keep production access separate and deliberately approved.

### `.env` files: useful, local, and easy to mishandle

A `.env` file commonly stores environment-variable assignments for local development:

```dotenv
REPORT_API_URL=https://api.example.test
REPORT_API_TOKEN=replace-with-local-secret
```

It is convenient because many tools can load it locally. It is not encryption, a vault, or access control. Anyone who can read the file can read its values.

A safe project pattern is:

```text
.env             # local machine only; ignored by Git; may contain a real local secret
.env.example     # committed; variable names and harmless placeholders only
.gitignore       # contains .env and other local secret filenames
```

Example `.env.example`:

```dotenv
REPORT_API_URL=https://api.example.test
REPORT_API_TOKEN=replace-with-your-local-token
```

Add local secret files to `.gitignore` **before** creating them:

```gitignore
.env
.env.*
!.env.example
```

The exception keeps the safe example visible while ignoring local variants. Adjust this pattern if the project intentionally commits another non-secret `.env.*` file.

Before committing, inspect:

```bash
git status
git diff --cached
```

These checks are essential but not sufficient: an ignored `.env` can still be read by an agent with access to the folder, copied into logs, or included in an upload. Keep it outside the active project when the agent does not need it.

### Prefer least-privilege credentials

When a task must use a secret, prefer a credential that is:

- scoped to one service and purpose;
- limited to the smallest necessary data and actions;
- short-lived or easily revocable;
- non-production when possible;
- subject to a spending limit or usage alert where the service supports it; and
- stored outside version control and outside broad shared directories.

Tell the agent the boundary, not the secret value. For example:

> Use the approved test credential already supplied through the environment. Do not print it, read `.env` into output, upload it, change its scope, or call any external service until I approve the exact action and destination.

If a secret is accidentally exposed, revoke or rotate it promptly. Do not rely only on deleting a file or message.

## Working with an agent in a project

A good coding-agent session normally follows this sequence:

1. **Confirm the active account and project.** Run `whoami`, `pwd`, and `git status`.
2. **Inspect before editing.** Ask the agent to identify project instructions, existing scripts, dependencies, tests, and output conventions.
3. **State the outcome and boundary.** Name the intended audience/result, approved inputs, protected files, and actions needing approval.
4. **Request a plan for meaningful work.** Include likely tools, outputs, validation, assumptions, and decisions requiring your input.
5. **Start small when uncertain.** Use a sample, dry run, or staged plan for large, costly, sensitive, or recurring work.
6. **Review evidence.** Inspect output paths, `git diff`, test/check results, counts, exceptions, and limitations.
7. **Make reuse a deliberate choice.** Keep a script, template, instruction file, or handoff only if it reduces future friction.

Useful prompts:

- “Inspect this project without modifying it. Tell me what instructions, existing tools, tests, and output locations apply.”
- “Before editing, show the files you expect to change and propose the smallest plan that validates the result.”
- “Run this only against the approved sample data. Report exact output paths, checks run, and anything needing human review.”
- “What command would verify this without changing files?”
- “Before using any network service or environment credential, explain the destination, data sent, cost implication, and safer local alternative.”

## Recognize trouble and recover

| Symptom | First things to check |
| --- | --- |
| `No such file or directory` | `pwd`, spelling, relative versus absolute path, and quoting for spaces |
| `Permission denied` | `whoami`, `id`, owner/group from `ls -l`, and traversal permission on parent directories |
| `command not found` | Whether the tool is installed and on `PATH`; do not install it automatically without review |
| Output appeared in the wrong place | Ask for `pwd`, exact output paths, and `git status` |
| A command appears stuck | Whether it awaits input, processes many files, accesses a network, or writes output elsewhere |
| Too many files changed | Stop; inspect `git status` and `git diff`; identify the target pattern before attempting recovery |
| A secret may have appeared | Stop sharing output, revoke/rotate the credential, inspect history/logs, and remove access as appropriate |
| Repeated retries fail | Pause and ask for assumptions, practical options, existing tools, a smaller test, and a staged route |

Avoid trying to fix uncertainty by repeatedly telling the agent to “try again.” A better recovery request is:

> Step back. Explain what assumptions are failing, what the practical approaches are, why the current route is difficult, and what you recommend instead. Do not make further changes until I choose.

## A compact daily checklist

Before a session:

- [ ] I am using the intended unprivileged account, not an administrator account.
- [ ] I know the current directory and it is the project I deliberately activated.
- [ ] The project contains no unnecessary secrets or personal data reachable by the agent.
- [ ] I have inspected existing project instructions and the initial `git status`.

Before a consequential command:

- [ ] I know whether it reads, writes, deletes, installs, sends, spends, or uses credentials.
- [ ] I know its target paths, wildcard behavior, and destination if it uses a network.
- [ ] I have approved the effect and have a backup, dry run, or rollback plan when appropriate.

After work:

- [ ] I inspected output paths, `git status`, and `git diff` where applicable.
- [ ] I reviewed checks, exceptions, assumptions, and what the checks do not prove.
- [ ] I retained only the script, template, instruction, or handoff that will genuinely help next time.
- [ ] I removed or rotated temporary credentials and deactivated access that is no longer needed.

The command line becomes much less intimidating when you treat it as an inspectable interface: identify the account, location, command, target, authority, and evidence. That is enough to use coding agents productively while keeping meaningful control over the work.
