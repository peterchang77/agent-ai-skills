---
role: prepare-environment
title: Prepare your environment
kind: mini
summary: Have the agent check what is installed, set up a project environment, and record how to rebuild it, so later steps do not stall on missing tools.
time: 5 min
teaches: [environment]
needs: [orient-in-folder]
---

Later steps read spreadsheets, run statistics and build documents, and each needs software. You will have the agent check what your machine already has,
create a project environment for the Python packages, and write down how to rebuild it. Doing this once up front keeps the rest of the work moving.

**Before you start:** an agent running in your project folder ([Setup](setup:)).

## Background

Python packages belong in an environment that lives with the project, managed by a package manager such as `uv`, so they never touch your system Python.
System tools such as `pandoc` or LaTeX are different. They install machine-wide and often need administrator rights, so the agent should tell you what is
missing and ask before it installs anything ([Environment](concept:environment)).

## General approach

Ask for four things in order: a report of what is installed, a project environment with the packages you expect to need, a rule that system-level installs wait
for your approval, and a written record of the setup.

```text
Check which of these are installed and report the version of each: <the tools you expect to need>.
Then create a Python environment for this project with <package manager> and install <the packages you expect to need>, pinned to the versions you install.
Keep everything inside this folder. If a system-level tool is missing, tell me what it is and the exact command you would run, and wait for my approval.
Finally, add a "Setup" section to README.md with the commands to rebuild this environment from scratch.
```

If `uv` itself is missing, the agent can suggest how to install it. Read any installer command before you approve it.

<!-- example -->

## What to check

- The report lists real version numbers from commands it ran, not guesses.
- Packages went into a project environment (a `pyproject.toml` and a `.venv/` folder), not into your system Python.
- Anything that needed administrator rights was proposed to you, not run silently.
- `README.md` has commands you could paste into a fresh terminal to rebuild the environment.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| "command not found: uv" | The package manager is not installed | Ask the agent how to install it, read the command, then approve it. Open a new terminal afterwards |
| A permission error on a system tool | The install needs administrator rights | Ask your IT group, or skip the steps that need that tool |
| A package fails to build | The wrong Python version, or a missing compiler or library | Paste the error to the agent and ask for options before retrying |
| No network | A firewall or proxy blocks downloads | Use your institution's mirror or proxy settings |
