---
name: data-science-refactor
description: Refactor research or data-science code into a reproducible, testable Python project using uv, a src layout, declarative configuration, and standalone operational scripts. Use for archival research code, model inference/training pipelines, data preprocessing, experiment evaluation, or reproducibility audits.
---

# Data-Science Refactor

Use this skill to turn exploratory, archived, notebook-like, or ad hoc data-science code into a maintainable project without changing its scientific contract accidentally. Prefer a small importable Python package, explicit configuration, and thin standalone scripts for operational commands.

## Non-negotiable rules

- Start by auditing the repository, source artifacts, data/model inventory, package metadata, and existing tests before editing. Identify the actual source of truth when duplicates exist.
- Treat supplied archival code, datasets, expected outputs, checkpoints, papers, and raw inference outputs as immutable provenance unless the user explicitly asks otherwise. Do not reformat, move, regenerate, or overwrite them.
- Preserve behavior before improving structure. Write down historical input transforms, model topology, output shapes/order, split definitions, thresholding, score orientation, label semantics, seed values, and statistical procedures before replacing code.
- Before creating, flattening, or archiving versioned trees, classify apparent dataset releases, model versions, tasks, evaluations, runs, and archive-only material. Record a flat-versus-`vNN/` decision and the active source of truth; do not infer a model version merely from a directory or label. Read [`references/architecture.md`](references/architecture.md) when layout, versioning, archival, or framework integration is in scope.
- Never commit protected data, DICOMs, private datasets, model checkpoints, generated feature arrays, output predictions, credentials, caches, or build artifacts. Track documentation and checksums/instructions for externally provisioned artifacts instead.
- Use `uv`, `pyproject.toml`, a `src/` layout, Ruff, Pytest, pinned compatible dependencies, and `uv.lock`. Keep the supported Python range explicit.
- Do not add dependencies or make network requests without a clear need. Pin new dependencies exactly and explain any material risk.
- Make scripts thin: parse arguments, resolve paths/configuration, call importable package functions, persist outputs, and return useful exit codes. Keep scientific/business logic in `src/<package>/`.
- After edits, run the narrowest meaningful tests first, then format/lint, relevant integration tests, and build/package checks. Fix failures before reporting completion.
- For a legacy framework-managed project, inventory its distribution/version, configuration seeds, manifests, extension points, generated trees, materialized experiments, and stage commands before editing. Preserve the distinction between authored declarative inputs and generated caches/state.
- When maintained code imports a framework at runtime, declare it as a formal runtime dependency and resolve any local checkout through a documented UV source. Do not rely on an undeclared editable installation or hard-code a developer home directory in portable project configuration.
- Before moving a legacy project to a newer framework runtime, record the legacy and target distributions/versions, Python versions, and import paths. Treat an observed API, serialization, coordinate, path, or generated-driver difference as a compatibility gap to reproduce, document, and report—not silently normalize away.

## Recommended layout

Use this baseline unless the project has a justified compatibility constraint:

```text
project/
├── pyproject.toml
├── uv.lock
├── README.md
├── .gitignore
├── src/
│   └── <package>/
│       ├── __init__.py
│       ├── config.py
│       ├── data/
│       ├── features/
│       ├── models/
│       ├── training/
│       ├── evaluation/
│       └── cli.py                 # optional shared parser/entrypoints
├── scripts/
│   ├── check_environment.py
│   ├── preprocess_<dataset>.py
│   ├── create_labels.py
│   ├── create_splits.py
│   ├── train.py
│   ├── validate.py
│   ├── extract_features.py
│   ├── evaluate.py
│   └── run_golden_tests.py
├── configs/
│   ├── training/
│   ├── data/
│   └── evaluation/
├── tests/
│   ├── unit/
│   └── integration/
├── docs/
│   ├── provenance.md
│   └── data-access.md
└── artifacts/
    └── README.md                  # tracked; actual external artifacts ignored
```

Choose a namespace compatible with historical callers where that compatibility matters. Do not create a package merely to wrap a single command; do separate reusable logic from scripts once the pipeline has multiple stages or tests. For flat versus versioned layouts, dataset-release catalogs, evaluation organization, archival, and framework integration, read [`references/architecture.md`](references/architecture.md).

## Framework-aware architecture

Use this path when a repository has a substantial framework-owned configuration, generated state, or command lifecycle.

1. **Choose the framework role first.** Classify it as **incidental**, **legacy structured**, or **primary orchestration**. The migration/layout policy differs materially; read [`references/architecture.md`](references/architecture.md) §2 before moving files.
2. **Preserve the framework contract.** Audit configuration seeds, manifests, supported placeholders or path mechanisms, generated trees, materialized experiments, and stage commands. Do not hard-code machine paths or edit generated state by hand.
3. **Keep the boundaries clean.** Put reusable project logic and supported extensions in `src/<package>/`. Do not copy framework-owned data management, preprocessing, training, inference, generated-driver, or standard evaluation behavior without documenting a framework gap. Treat generated drivers/state and materialized experiments as generated/provenance material until proven otherwise.
4. **Keep authored evaluation distinct.** Use `eval/` for scientific evaluation definitions; retain framework-owned execution stages under their documented names. Do not add competing namespaces or rename framework stages merely for consistency.
5. **Establish migration evidence.** Compare legacy and target framework/Python runtimes and exercise representative configuration, serialization, generated-driver, and extension operations. Keep a compatibility-gap ledger; imports alone do not prove compatibility.

Do not invent `vNN/` merely for appearance: a single stable project may correctly keep one root configuration. In a framework-managed project, retain documented stage names and version roots; in a legacy project, preserve the historical contract before modernization.

## Workflow

1. **Inventory and contract.** Map files, dependencies, historical entry points, data flow, saved artifacts, and tests. Read the paper/protocol and evaluation code if present. Record the exact scientific contract in `docs/provenance.md` or an issue-level plan: preprocessing, labels, splits, architecture/checkpoint loading, metrics, CIs, and deviations from legacy code.
2. **Make the architecture decision.** Identify the active implementation using provenance, imports, documented commands, and recent authored-source activity—not output mtimes. Classify dataset releases, model versions, tasks, evaluations, runs, and archive-only trees; choose flat or `vNN/`; and identify the framework role when relevant. Record the decision before moving files. Read [`references/architecture.md`](references/architecture.md).
3. **Classify material.** Separate immutable provenance from maintained source and from external runtime artifacts. Add `.gitignore` rules before generating output. Document artifact path, expected size/hash, acquisition/access restrictions, and environment-variable/CLI override precedence.
4. **Establish package tooling.** Create or normalize `pyproject.toml`; pin Python and dependency versions compatible with historical model artifacts. Use dependency groups/extras for optional training, visualization, or environment-specific integrations rather than compromising a small inference environment. Run `uv lock` and use `uv run` consistently.
5. **Extract pure functions.** Move preprocessing, labels, alignment, split generation, feature extraction, model loading, thresholds, and metrics to typed, importable modules. Validate shapes, dtypes, IDs, order, paths, and configuration at boundaries; use immutable dataclasses for configuration where practical.
6. **Add standalone scripts.** Provide one script for each real operational command. All scripts must support `--help`, accept explicit input/output/config paths, avoid hard-coded machine paths, create outputs deliberately, report written artifacts, and delegate to package functions. Use environment variables only as documented optional defaults/overrides.
7. **Reproduce before extending.** Add golden or regression tests against immutable, legally usable fixtures. Compare identifiers before arrays; normalize at the documented boundary; test end-to-end paths such as raw input → preprocessing → model/features → persisted output when fixtures and checkpoints are authorized.
8. **Validate statistics correctly.** Match the publication/protocol exactly: validation-only model selection/orientation/thresholds, required label grouping, correct unit of bootstrap resampling, paired versus independent comparisons, seed, percentile convention, and rounding. Treat old path-specific score flips and hard-coded special cases as provenance to explain, not rules to perpetuate.
9. **Finish cleanly.** Run relevant tests, Ruff format/check, type/build checks where configured, package wheel/sdist build, and operational smoke tests. Verify Git status and ignored artifacts. Summarize what was changed, commands/results, any unrun checks, external prerequisites, and scientific caveats.

For a framework migration, prefer a small authorized **read-only real-data smoke** over an elaborate synthetic framework fixture. Select one to three representative records; read source artifacts only; direct every result to a fresh `TemporaryDirectory`/`mktemp` location; assert IDs, shapes, finiteness, and output schema; then verify source timestamps or hashes where appropriate and audit Git-ignore boundaries. Synthetic inputs remain appropriate for pure project logic, but integration fixtures must include valid framework metadata or they can misrepresent target behavior.

Exercise each declared optional extra through its actual project operation, including transitive reader/engine dependencies such as `openpyxl`, DICOM, image, or database drivers. Add every needed runtime dependency to the relevant extra, lock it, and rerun that operation.

## `uv` conventions

```bash
# Resolve and use the locked environment.
uv lock
uv sync --all-groups
uv run pytest
uv run ruff format --check .
uv run ruff check .
uv build

# Run a standalone operational command.
uv run python scripts/preprocess_dataset.py --input <path> --output <path>
```

- Put runtime dependencies in `[project.dependencies]`; use dependency groups or optional extras for test, lint, training, or local-only tools.
- Pin versions that affect serialized model/checkpoint compatibility, especially Python, TensorFlow/Keras/PyTorch, NumPy, and image/DICOM tooling.
- Keep local filesystem dependencies optional and marker-gated when they require a different Python/runtime stack.
- Prefer `uv run --python <supported-version>` for compatibility-sensitive checks when multiple interpreters are installed.

### Framework dependency convention

For a maintained project whose installed package or user-facing commands import a framework, place it in `[project.dependencies]`. Map a local checkout with UV only when that workspace relationship is an intentionally supported workflow:

```toml
[project]
requires-python = ">=<minimum-supported-version>"
dependencies = ["<framework-distribution>==<verified-compatible-version>"]

[tool.uv.sources]
<framework-distribution> = { path = "../<framework-checkout>", editable = true }

[dependency-groups]
dev = ["pytest==<compatible-version>", "ruff==<compatible-version>"]
```

Otherwise document an installable source. Put the framework only in a dependency group when it is truly development-only. Prefer `[dependency-groups]` over new uses of legacy `[tool.uv].dev-dependencies`; commit the resulting `uv.lock` and verify it against the supported framework version.

## Validation standard

Minimum completion gate after a refactor:

```bash
uv run ruff format --check .
uv run ruff check .
uv run pytest
uv build
```

Also run, when applicable:

- targeted unit tests for the changed behavior before the full suite;
- integration/golden tests that use authorized fixtures and externally provisioned checkpoints;
- CLI `--help` plus a small real or fixture-backed smoke command;
- environment compatibility checks and checkpoint load/output-shape checks;
- raw-data preprocessing equivalence (bitwise when the historical pipeline requires it);
- a Git-ignore audit proving data/models/results/caches are not staged;
- for framework projects: package/framework imports, relevant framework and project CLI help, configuration validation, and a small representative preparation or prediction path before any bulk regeneration;
- framework-boundary regressions for custom extensions, manifests/configuration resolution, IDs, shape/channel order, generated-driver resolution, and legacy-versus-refactored outputs compared by stable identifier;
- a legacy-to-target framework compatibility check that records the two runtime versions/import paths and tests representative serialization/load, coordinate conversion when applicable, configuration behavior, and used generated-driver APIs;
- a read-only real-data smoke, when authorized, using one to three representative records and a fresh temporary output directory; assert output IDs/schema/shapes/finiteness and prove source/provenance artifacts were not written;
- each optional dependency extra through a real corresponding operation, including required file-format engines; and
- an explicit compatibility-gap ledger. Report any difference from the legacy runtime—whether fixed, intentionally accepted, or unresolved—with a minimal repro and its scientific/operational impact.

Use `[tool.pytest.ini_options]` markers such as `integration`, `requires_checkpoint`, or `requires_data`, and skip with a clear reason when assets are unavailable. Do not make a passing unit suite appear to prove an unavailable full-data pipeline.

## Research-result audits

For an audit of reported results, use saved model outputs and labels whenever possible rather than retraining. Locate manuscript tables, original statistic scripts, split artifacts, probabilities/logits, report CSVs, and model-selection inputs. Independently recompute point estimates and confidence intervals; compare unrounded values to the manuscript’s stated precision. Explicitly report which values are independently reproducible, which derive only from archival reports, and whether historical scripts contain accidental implementation quirks.

Read [the detailed checklist](references/checklist.md) for implementation and review specifics.
