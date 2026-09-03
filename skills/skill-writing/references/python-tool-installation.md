# Python tool installation

For a reusable Python command-line tool, prefer a portable UV tool installation from its canonical GitHub repository rather than copying the source checkout into the skill environment or manually creating a virtualenv:

```bash
uv tool install 'git+https://github.com/<owner>/<repository>@<tag-or-commit>'
command -v <command>
<command> --help
```

Pin a release tag or commit when reproducibility matters. Use `--force` only to replace an existing installation deliberately. Use `uvx --from 'git+https://github.com/<owner>/<repository>@<tag-or-commit>' <command> ...` for a one-off invocation that does not need to remain installed. If the executable is not on `PATH` after installation, run `uv tool update-shell` or report the environment issue instead of relying on a checkout-specific path.

This approach gives each installed tool an isolated environment and lets UV resolve its Python dependencies without requiring the agent to manage virtualenv activation. It does not provide operating-system dependencies, network access, credentials, or a compiler, and it does not replace a project environment when the task needs the repository's importable source, local editable changes, or several packages sharing one environment.

Document the required Python version, tool version, non-Python dependencies, and any authentication or network requirement in the skill. Verify the installed command before use and prefer a pinned, published Git ref over a floating branch.
