---
role: prepare-environment
title: Prepare your environment
kind: mini
summary: Direct the agent to audit local dependencies, initialize an isolated project virtual environment, and document lockfile-pinned setup procedures.
time: 5 min
teaches: [environment]
needs: [orient-in-folder]
---

Subsequent analytical stages require specialized computational tools: libraries to parse spreadsheets, modeling packages to compute statistics, and rendering engines to compile PDF reports. In this exercise, the agent audits available system tools, initializes an isolated project virtual environment, and records reproducible setup commands. Establishing this dependency boundary early prevents execution failures in later exercises.

**Before you start:** An active agent running inside your project directory ([Setup](setup:)).

## Background

To preserve computational reproducibility and prevent dependency conflicts across projects, language packages should reside in an isolated environment local to the project. We use `uv` to manage Python runtimes and package lockfiles within the `.venv/` directory.

System-level binaries, such as `pandoc` or LaTeX compilers (`pdflatex`), operate globally across the operating system and typically require administrative (sudo) privileges. Consequently, the agent must audit system dependencies transparently and request explicit human approval before proposing system-level installations ([Environment](concept:environment)).

## General methodology

Direct the agent through four sequential tasks: auditing existing tools, initializing a project-local environment with pinned dependencies, pausing for approval before any system-level installations, and documenting the environment rebuild commands in `README.md`.

```text
Check which of these tools are installed and report the version of each: <tools to audit>.
Then create a project-local virtual environment with <package manager> and install <required packages>, pinning the exact versions installed.
Keep all files within this project directory. If a system-level tool is missing, report the tool name and exact proposed installation command, and wait for my explicit approval.
Finally, add a "Setup" section to README.md documenting the exact shell commands needed to reproduce this environment from scratch.
```

If the package manager itself (`uv`) is absent from the host, the agent can recommend official installation steps. Inspect installer scripts carefully before approving execution.

<!-- example -->

## Verification criteria

- **Audited version numbers:** The agent reports genuine version numbers obtained from running version commands (e.g., `uv --version`), rather than placeholder values.
- **Project-scoped environment:** Language packages are installed inside the local `.venv/` directory and defined in `pyproject.toml`, leaving the global system Python environment untouched.
- **Administrative authorization:** The agent paused for explicit confirmation before attempting any command requiring administrative permissions.
- **Reproducible documentation:** The `README.md` file contains exact, runnable commands that allow a collaborator to reconstruct the computational environment.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| `"command not found: uv"` | The package manager is not installed on the system | Ask the agent for the official installation command, review the command, approve execution, and open a new terminal session if paths need refreshing |
| Permission denied on system utility | Installation requires administrative privileges | Request assistance from your system administrator, or omit optional steps requiring that specific binary |
| Package compilation fails | Host lacks required C compilers or header files | Provide the error traceback to the agent to identify pre-compiled binary wheels or alternative packages |
| Registry connection timeouts | Corporate firewall or proxy restricts package downloads | Configure package manager proxy settings or point to an approved institutional mirror |
