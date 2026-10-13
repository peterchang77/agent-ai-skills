---
id: environment
title: Environment — let the agent install what it needs
short: Environment
themes: [recursive-ai]
related: [inputs, outputs, sandboxing, version-control]
blurb: Computational research requires isolated execution environments to prevent dependency conflicts and guarantee that findings can be reproduced on other systems.
---

Scientific computing requires reproducible execution environments. An empirical analysis depends on more than source code alone; it requires a specific runtime, system utilities, and an exact tree of third-party libraries. If an agent executes scripts or installs libraries directly across the host operating system, it risks mutating global state, causing version collisions with other projects, and producing non-reproducible artifacts.

To protect system integrity and ensure computational reproducibility, agents should operate within isolated execution environments scoped strictly to the project directory.

## Layers of software dependencies

| Dependency layer | Examples | Typical management mechanism | Governance and operational risk |
|---|---|---|---|
| **Language packages** | `pandas`, `statsmodels`, `openpyxl` | Project package manager (`uv`, `venv`, `conda`) | Version drift and dependency conflicts between local projects |
| **System utilities & compilers** | LaTeX (`pdflatex`), `pandoc`, C/C++ compilers | Operating system package manager (`apt`, `brew`) | Requires administrative (sudo) privileges; modifies the host environment machine-wide |
| **Host platform & runtime** | Linux/macOS kernel, system drivers, container engines | System administrators / institutional IT | Managed institutional workstations often restrict unauthorized binary installations |

## Package management and dependency pinning

A **package manager** automates library installation while recording exact version numbers in a reproducible lockfile. In this workshop, we use **[uv](https://docs.astral.sh/uv/)** for Python: it creates an isolated virtual environment (`.venv/`) within the project folder and pins dependencies in `pyproject.toml`. 

While alternatives such as standard `venv`, `conda`, or `poetry` serve similar roles, the underlying principle is universal: **every project maintains an isolated environment, and every dependency version is explicitly recorded**.

## Best practices for agent-driven environments

- **Specify requirements by intent:** State the analytical objective (e.g., *"extract tables from this spreadsheet and calculate logistic regressions"*); the agent will identify the appropriate libraries.
- **Keep dependencies project-local:** Ensure all Python packages are installed within the local `.venv/` directory rather than the global system environment.
- **Pin dependency versions:** Record exact version numbers so subsequent executions produce identical numerical results even after library updates.
- **Verify unfamiliar package names:** Review suggested libraries before approving installations to guard against typosquatting or insecure packages.
- **Document setup instructions:** Maintain explicit environment creation commands in `README.md` or `AGENTS.md` so future sessions or research collaborators can rebuild the runtime from scratch ([Memory](concept:memory)).

## System tools and managed environments

Installing system-level binaries typically requires administrative privileges. On institutional high-performance computing clusters or managed workstations, agents will lack administrative access. Rather than attempting workarounds, request necessary tools through institutional administrators, use containerized environments, or explore user-space binaries.

## Common environment failures

- **Incompatible runtime versions:** A library requires a newer or older Python minor version than the host runtime.
- **Missing shared libraries:** A Python package installs successfully but fails at runtime because an underlying C/Fortran library is absent.
- **Compilation errors:** A package distributed as source cannot build because no C compiler or header files exist on the host.
- **Restricted network access:** Institutional firewalls or proxies block connections to package registries.

When an environment error occurs, provide the traceback to the agent to diagnose alternative packages or configuration flags rather than retrying the same installation repeatedly.

## Demo it

<!-- demos -->
