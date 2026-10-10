---
id: environment
title: Environment — let the agent install what it needs
short: Environment
themes: [recursive-ai]
related: [inputs, outputs, sandboxing, version-control]
blurb: Give each project its own environment and let the agent install dependencies there, so your machine stays clean and the setup is reproducible.
---

Real tasks need software: a library to read spreadsheets, a LaTeX compiler, a PDF text extractor. An agent can usually
install what it needs. Your job is to make sure it does so **inside the project**, in a way that is recorded.

## Three layers of "what is installed"

| Layer | Examples | Managed with | Risk if mishandled |
|---|---|---|---|
| Python packages | `pandas`, `openpyxl`, `statsmodels` | a package manager (below) | Version conflicts between projects |
| System tools | LaTeX (`pdflatex`), `pandoc`, `pdftotext` | the operating system's package manager | Needs admin rights; affects the whole machine |
| The machine itself | OS, drivers, other users' software | you / your IT group | Shared or managed machines may forbid changes |

## What is a package manager?

A **package manager** downloads libraries and records which versions a project uses. This material uses
**[uv](https://docs.astral.sh/uv/)** for Python: it creates an isolated environment per project and writes the
dependencies to a file, so the project can be rebuilt later. Common alternatives are `pip` with `venv`, `conda`,
and `poetry`. Any of them works; the point is *one isolated environment per project, with the dependencies recorded*.

## Good habits

- **Say what you need, not how to install it.** "Read this spreadsheet" is enough; the agent picks the library.
- **Keep installs project-local.** Python packages go in the project environment, not into your system Python.
- **Pin versions** for anything you will rerun, so results do not change when a library updates.
- **Check unfamiliar package names** before approving. Look-alike (typosquatted) packages exist.
- **Record the setup** in the project `README.md` or `AGENTS.md` so the next session knows how to run things ([Memory](concept:memory)).

## System tools and managed machines

Installing system software usually needs administrator rights. On a managed or shared machine the agent may be unable
to install, and you should not work around that. Ask your IT group, use a container, or choose a user-space install.

## Common failures

- The wrong Python version for a package.
- A missing system library behind a Python package.
- A package that has to be compiled and no compiler is present.
- No network access to download anything.

When one occurs, paste the error to the agent and ask for options; do not retry the same command repeatedly.

## Demo it

<!-- demos -->
