# Bootstrap templates

These are deliberately minimal starting points, not a mandatory generated tree. Substitute names and select **verified exact compatible versions** for the supported Python/runtime; the version markers below are placeholders.

## `pyproject.toml`

```toml
[build-system]
requires = ["hatchling==<verified-version>"]
build-backend = "hatchling.build"

[project]
name = "<distribution-name>"
version = "0.1.0"
description = "<one-line scientific or operational purpose>"
readme = "README.md"
requires-python = ">=<minimum-python>,<<next-unsupported-major>"
dependencies = []

[project.optional-dependencies]
# Add narrowly scoped extras only when an operation needs them.
# viz = ["matplotlib==<verified-version>"]
# ml = ["<backend>==<verified-version>"]

[project.scripts]
<command-name> = "<package_name>.cli:main"

[tool.hatch.build.targets.wheel]
packages = ["src/<package_name>"]

[dependency-groups]
dev = [
  "pytest==<verified-version>",
  "ruff==<verified-version>",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-ra"
markers = [
  "integration: requires an external integration or approved fixture",
  "requires_data: requires externally provisioned data",
  "requires_checkpoint: requires an externally provisioned checkpoint",
]

[tool.ruff]
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "I", "UP"]
```

For a declared framework runtime, add its verified compatible distribution under `dependencies` and a documented UV source only when the workspace path/source is intentionally supported. Do not add it to a generic scaffold preemptively.

## `src/<package_name>/__init__.py`

```python
"""<Package purpose>."""

__all__: list[str] = []
```

## `src/<package_name>/pipeline.py`

```python
from collections.abc import Sequence


def transform(values: Sequence[float]) -> list[float]:
    """Validate and transform one small, deterministic input sequence."""
    if not values:
        raise ValueError("values must not be empty")
    if any(not isinstance(value, (int, float)) for value in values):
        raise TypeError("values must contain only numbers")
    return [float(value) for value in values]
```

Replace this placeholder at once with the first domain-specific vertical slice. Keep file I/O, environment lookup, GPU initialization, and side effects outside pure core functions.

## `src/<package_name>/cli.py`

```python
from __future__ import annotations

import argparse
from pathlib import Path

from <package_name>.pipeline import transform


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="<Command purpose>")
    parser.add_argument("--values", type=float, nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow replacing an existing output file.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.output.exists() and not args.overwrite:
        raise FileExistsError(f"Refusing to overwrite {args.output}; pass --overwrite to replace it")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(map(str, transform(args.values))) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

A real CLI should identify input/config/model versions in its output metadata where applicable, validate paths before computation, and distinguish user input errors from runtime failures.

## `tests/test_pipeline.py`

```python
import pytest

from <package_name>.pipeline import transform


def test_transform_preserves_numeric_values() -> None:
    assert transform([1, 2.5]) == [1.0, 2.5]


@pytest.mark.parametrize("values", [[], ["not-a-number"]])
def test_transform_rejects_invalid_input(values: list[object]) -> None:
    with pytest.raises((TypeError, ValueError)):
        transform(values)  # type: ignore[arg-type]
```

## `.gitignore`

```gitignore
# Python/tooling
__pycache__/
*.py[cod]
.pytest_cache/
.ruff_cache/
.mypy_cache/
.venv/
dist/
build/
*.egg-info/

# Environment and secrets
.env
.env.*
!.env.example
*.pem
*.key

# Project runtime state: customize to the documented artifact root
artifacts/
outputs/
work/
cache/
logs/

# Externally provisioned/private assets: customize and document access
raw_data/
data/raw/
checkpoints/
models/
```

Do not blindly ignore `data/` if the project tracks small safe schemas, catalogs, or fixtures there. Prefer a documented split such as `data/fixtures/` (tracked, small, synthetic/public) and `data/raw/` (ignored, external).

## `README.md` outline

```md
# <Project name>

## Purpose
<Scientific/operational question and explicit non-goals.>

## Architecture
See [docs/architecture.md](docs/architecture.md) for the flat/versioned decision,
contracts, and framework role.

## Install
```bash
uv sync --all-groups
```

## Quick check
```bash
uv run pytest
uv run ruff check .
uv build
uv run <command-name> --help
```

## Data and models
<What is external/restricted, how authorized users obtain it, expected layout, and what is never committed.>

## Basic operation
<One fixture-backed command or library example, including input/output behavior.>

## Reproducibility and provenance
<Configuration precedence, model/dataset/evaluation identifiers, seed/determinism caveats, and artifact policy.>
```

## `docs/data-access.md` outline

```md
# Data and model access

## Ownership and authorization
- Owner/contact:
- Access requirements:
- License/IRB/security constraints:

## Inputs
- Dataset release/manifest:
- Expected schema, IDs, units, and validation:
- Authorized acquisition procedure:
- Local root configuration (do not commit local paths):

## Models/checkpoints
- Source, license, checksum, and selection policy:
- Compatible package/framework/runtime:

## Generated artifacts
- Output roots and overwrite/resume rules:
- What may be deleted/regenerated:
- What must be preserved as provenance:
```

## Named config/evaluation example

Only add this once it describes a real contract:

```text
configs/
  tasks/<task-name>.yml
  models/<model-name>.yml             # when model selection exists
eval/
  <evaluation-name>/
    README.md                          # question, cohort, endpoints, policy
    config.yml                         # inputs/model/metrics/output namespace
```

Use `datasets/dNN.yml` only for durable immutable data-release contracts, and `vNN/` only for independently reproducible model contracts. The shared architecture reference defines these terms.
