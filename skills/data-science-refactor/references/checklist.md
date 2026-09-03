# Data-science refactor checklist

Use this reference after loading `SKILL.md`. Adapt it to the project; do not create empty machinery solely to satisfy the layout.

## 1. Audit before mutation

- Identify the repository root and run a status check. Preserve unrelated user changes.
- Map top-level source, notebooks, scripts, archived trees, datasets, checkpoints, generated outputs, package metadata, CI, and tests. Use Git history for tracked authored source and filesystem timestamps only for untracked authored candidates; discount generated data, checkpoints, arrays, logs, images, caches, build products, and generated framework trees.
- Find duplicate archives and select the complete/canonical source based on contents, provenance documentation, imports/entry points, and artifacts—not directory names or timestamps alone.
- Classify every apparent dataset release, model version, task, evaluation, run, and archive-only tree. Select one active implementation, choose flat or `vNN/`, and record the decision before moving files; see [architecture.md](architecture.md).
- Inspect historical environment/version files, model serialization formats, and command invocations before selecting Python/framework versions.
- Make no outbound request that uploads project code, data, model weights, or credentials without explicit authorization.
- For a framework-managed project, first classify the framework role as incidental, legacy structured, or primary orchestration; preserve the appropriate contract rather than forcing every project into a framework-shaped tree. Read [architecture.md](architecture.md) §2.
- For a framework-managed project, inventory its distribution/version, configuration seed(s), manifests, extension points, installed package hooks, generated stage trees when present, materialized experiment/checkpoint directories, and actual stage commands. Read the applicable framework documentation before changing framework behavior.
- Record the legacy and target framework distributions/versions, Python versions, module import paths, and relevant local checkout commits before migrating. Build a compatibility ledger for configuration expansion, serialization/alignment/coordinates, generated drivers, and any project-used API; an observed difference is a gap to reproduce and report, not a behavior to silently smooth over.

Useful commands:

```bash
find . -maxdepth 3 -type f | sort
find . -name pyproject.toml -o -name requirements.txt -o -name environment.yml
uv run pytest --collect-only
uv run python scripts/check_environment.py  # once provided
```

## 2. Preserve the scientific contract

For each pipeline stage, record inputs, outputs, shape/dtype/range/order, IDs, and all transforms. Explicitly establish:

- image/domain preprocessing order (e.g., LUT, inversion, scaling, resize/interpolation, normalization);
- ID extraction and alignment rules—never assume `os.listdir()` order;
- label schema, aliasing, uncertain-label semantics, derived classes, and grouping reductions;
- split method, grouping/stratification, seed, saved split manifests, and no-leakage constraints;
- model architecture, custom layers/objects, selected layer, checkpoint type, and output dimension;
- train/validation/test separation and the source of every threshold or model-selection decision;
- metric averaging/micro-macro semantics, threshold convention, bootstrap sampling unit/count/seed, CI method, and score orientation; and
- publication rounding versus stored precision.

If a legacy script has a hard-coded path, threshold, row order, magic score inversion, or silent fallback, determine whether it represents an intentional scientific rule. Replace only with a general rule supported by the protocol; record the historical quirk in provenance notes.

## 3. Source and artifact hygiene

Track source/documentation; exclude runtime artifacts by default:

```gitignore
# Sensitive/external research artifacts
artifacts/*
!artifacts/README.md
*.h5
*.ckpt
*.pt
*.pth
*.dcm
*.dicom
*.npy
*.npz
outputs/
data/
.cache/
.pytest_cache/
.ruff_cache/
dist/
build/
*.egg-info/
```

Tailor patterns: do not blanket-ignore a small, authorized fixture that must be tracked for tests. Store checksum, byte size, required destination, override variables, intended framework/runtime, access constraints, and a human owner/contact in `artifacts/README.md`.

Artifact resolution should be deterministic, generally:

1. explicit CLI/function argument;
2. documented environment variable;
3. conventional project-relative provisioned path; and
4. clear `FileNotFoundError` that tells the user how to provision it.

Verify hash before declaring checkpoint-backed tests valid.

Framework-specific hygiene: classify configuration seed files and project-owned package code as authored material; classify generated stage directories, manifests, and materialized experiment outputs as caches, state, or historical provenance until proven otherwise. Ignore generated data, checkpoints, array outputs, and caches, but preserve enough configuration, hashes, and documentation to reproduce or inspect them. Do not manually edit generated state; preserve supported portable configuration patterns.

When dataset releases are meaningful, maintain a small authored `datasets/dNN.yml` catalog or equivalent provenance documentation. It may point to a framework configuration or workspace namespace, but must not duplicate the full operational configuration or replace framework runtime state. See [architecture.md](architecture.md) §3.

## 4. Package and API design

Use a `src/` layout. Favor narrow modules with explicit domain names:

```text
src/<package>/
  config.py              # typed immutable config + validation
  artifacts.py           # artifact discovery and verification
  data/
    preprocess.py
    labels.py
    alignment.py
    splits.py
  models/
    layers.py
    encoder.py
    classifiers.py
  features/extraction.py
  evaluation/
    groupings.py
    thresholds.py
    metrics.py
    bootstrap.py
```

Guidelines:

- No expensive I/O, model construction, GPU access, or mutable global state on import.
- Accept `Path`/array/dataframe inputs and return explicit results; write files at a separate wrapper boundary.
- Enforce array shape, data type, finite values, class dimensions, and ID coverage at interfaces.
- Use `numpy.random.default_rng(seed)` and accept/inherit seed explicitly.
- Put only reusable behavior in the package. Scripts remain discoverable operational entry points.
- Retain legacy import names only where downstream compatibility demands it; document the compatibility decision.
- For framework extension points, keep reusable project-owned logic, cohort selection, and evaluation functions under `src/<package>/`. Use documented configuration mechanisms to reference installed files. Do not copy framework functionality into the project without a documented framework gap.
- Keep `Path` objects within project code, but verify target framework load/save APIs at each boundary. If an API does not accept `os.PathLike`, convert only that call to `str(path)`, document the compatibility adaptation, and add a small serialization round-trip test.

## 5. Script interface pattern

Every executable script should have clear paths and a noninteractive interface:

```python
#!/usr/bin/env python3
"""Preprocess a dataset into deterministic encoder-ready arrays."""
from __future__ import annotations

import argparse
from pathlib import Path

from my_package.data.preprocess import preprocess_directory


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--config", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    count = preprocess_directory(args.input, args.output)
    print(f"Wrote {count} arrays to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

Avoid scripts that import from `archive/`, alter source fixtures, or silently read a machine-specific absolute path. Prefer separate scripts for preprocessing, label building, splits, training, feature extraction, evaluation, environment checks, and golden tests rather than one opaque all-in-one driver.

## 6. Configuration

Keep committed configuration declarative and separate from code:

```text
configs/
  data/<dataset>.yaml
  training/<model>.yaml
  evaluation/<protocol>.yaml
```

A good configuration records dataset paths symbolically, preprocessing assumptions, class ordering/groupings, split seed, architecture/checkpoint selection, optimizer/schedule, batch size, evaluation thresholds, bootstrap iterations/seed, and artifact outputs. Validate it in Python before executing work. Do not put credentials or local/private absolute paths in committed configuration.

For a primary framework, treat its documented configuration seed as source when it is regenerable. Version only scientifically distinct, independently reproducible model contracts; put shared code in the installable package and retain version-specific configuration or thin drivers in `vNN/`. Validate configuration generation before data processing or training, and never substitute developer-local absolute paths for portable framework settings. For incidental framework use, keep ordinary project configuration instead; for detailed layout policy, see [architecture.md](architecture.md) §§1–3.

Use `eval/`, not a competing top-level `studies/`, for authored scientific evaluation. Keep framework execution stages under their documented names; `eval/` defines cohort policy, exact model/experiment references, comparisons, and report logic without copying the model pipeline. Use `vNN/eval/<name>/` for a single-version evaluation and root `eval/<name>/` only for cross-version evaluations; see [architecture.md](architecture.md) §4.

## 7. Tests: layers of evidence

1. **Unit**: array normalization, grouping, label alignment, config errors, deterministic splits, thresholds, score orientation, statistics.
2. **Artifact/model**: custom-object checkpoint loading, expected model shape/dimension, selected layer, deterministic feature output.
3. **Integration**: raw sample → preprocessing → package API → saved artifact. Assert ID alignment and historical output equality/tolerance appropriate to the domain.
4. **CLI smoke**: `--help`, fixture-backed command, expected files/results.
5. **Result audit**: reconstruct reported paper/table metrics from saved raw outputs, including CIs and paired comparisons.

Test exact behavior only where it is scientifically/technically warranted. For a known historical image transform, a bitwise preprocessed-array regression is valuable. For floating-point inference, use defensible tolerances and compare values by ID. Never regenerate a golden reference as part of the test workflow.

For framework-bound behavior, also test: package/framework imports under `uv run`; project and relevant framework CLI help; config validation; a fixture-backed integration path; a minimal one- or two-record preparation or prediction path; and legacy-versus-refactored values keyed by stable IDs. Exercise generated drivers only through their supported generation path; test project extensions rather than editing generated code.

For authorized framework integration evidence, prefer one to three representative **real source records** read only, with every output directed to `TemporaryDirectory`/`mktemp`. Assert IDs, shapes, finite values, and output schema; record or compare source timestamps/hashes as appropriate; then audit that source data, derived state, and experiments remain ignored and unchanged. Avoid elaborate synthetic integration fixtures unless they include required framework metadata; otherwise they can make target behavior appear broken.

Exercise every optional extra through its real project operation. Include transitive reader/engine dependencies (for example `openpyxl` for committed Excel annotations) in that extra, run `uv lock`/`uv sync --extra <name>`, and repeat the operational smoke.

## 8. Final acceptance report

State concisely:

- selected active source of truth, framework mode when applicable, flat-versus-versioned decision, and classification of apparent releases/versions/tasks/evaluations/runs/archive trees;
- generated versus maintained file policy; data/config/experiment/prediction namespaces and collision prevention where applicable;
- archive decisions, including retained compatibility paths and why inactive trees were not promoted;
- artifact requirements, checksum verification, and how to provision assets;
- exact validation commands and outcomes;
- skipped/blocked integration tests and why;
- unsupported scope (e.g., full training not reproduced, protected data unavailable); and
- Git status/ignored-artifact outcome, without staging or committing unless asked.

## 9. Legacy framework modernization gate

Before declaring a legacy framework refactor complete, verify all of the following:

1. **Architecture and provenance:** one active implementation and the framework mode (if applicable) are identified; source config seed, generated cache/state, historical experiments, external assets, and archive-only trees are explicitly classified; generated material was neither silently adopted as source nor overwritten.
2. **Version/evaluation structure:** every apparent version/run is classified as dataset release, model version, task, evaluation, run, or archive. A root seed remains single-version when appropriate; `vNN/` is used only for independently reproducible scientific/model contracts, with shared code in `src/<package>/`. Authored scientific evaluations use `eval/`; framework-generated execution stages retain their roles and are not duplicated by a competing `studies/` tree.
3. **Formal UV packaging:** the project has `pyproject.toml`, `uv.lock`, a `src/` package, and Hatch-compatible build configuration. If installed code or user-facing commands import the framework, `[project.dependencies]` declares its resolved compatible version and `[tool.uv.sources]` documents an intentionally supported editable local checkout; a development-only framework dependency belongs in `[dependency-groups]` instead.
4. **Framework integration:** the project preserves supported configuration and state semantics, references project-owned extensions through documented mechanisms, and does not duplicate framework-owned data, preprocessing, training, inference, generated-driver, or evaluation behavior without justification.
5. **Migration compatibility and evidence:** the legacy and target framework/Python runtime versions and import paths are recorded; representative configuration, serialization/load, coordinate when applicable, and generated-driver paths have been checked; `uv lock`, `uv sync --all-groups`, package/framework import, focused tests, Ruff checks, `uv build`, config validation, CLI help, and a small authorized framework smoke path have been run or explicitly reported as blocked.
6. **Gap reporting:** every observed legacy-to-target difference has a minimal reproduction and is recorded as fixed, intentionally accepted, or unresolved, with scientific/operational impact. Do not infer compatibility from imports alone.
7. **Optional and real-data coverage:** each declared extra has been exercised through its actual operation; when authorized, a read-only one-to-three-record smoke writes only to a fresh temporary directory and proves source/provenance material was not changed.

Useful baseline:

```toml
[project]
requires-python = ">=<minimum-supported-version>"
dependencies = ["<framework-distribution>==<verified-compatible-version>"]

[tool.uv.sources]
<framework-distribution> = { path = "../<framework-checkout>", editable = true }

[dependency-groups]
dev = ["pytest==<compatible-version>", "ruff==<compatible-version>"]
```

Use a repository-relative path only for an intentionally supported workspace; otherwise provide a documented installable source. Keep all compatibility-sensitive versions and the lockfile synchronized with the actual framework checkout.
