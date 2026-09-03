---
name: data-science-project-bootstrap
description: Create a new, reproducible data-science repository from scratch using uv, a src layout, explicit scientific contracts, and an intentionally chosen flat or versioned architecture. Use for new research, ML, data-processing, or evaluation projects.
---

# Data-Science Project Bootstrap

Use this skill when creating a new repository, not when rehabilitating an existing one. Build the smallest maintainable project that makes its scientific, data, model, and evaluation contracts explicit. Do not manufacture version trees, datasets, framework state, or operational stages before the project has a real need for them.

This skill shares its architecture taxonomy, flat-versus-versioned decision procedure, evaluation policy, and framework-integration guidance with `{skills/data-science-refactor/references/architecture.md}`. Read that reference before deciding the layout. Do not copy or fork that policy into project documentation.

## Required design record

Before generating files, write a concise architecture record in the issue, design note, or `docs/architecture.md`. It must state:

- the scientific question, intended users, supported operations, and explicit non-goals;
- initial data source(s), access restrictions, identifiers, schemas, label/target semantics, split policy, and provenance owner;
- expected inputs, transformations, model/pipeline behavior, outputs, units, coordinate conventions, and deterministic/seed policy;
- whether the repository is **flat** or uses `vNN/`, with the reason and classifications of any datasets, tasks, evaluations, and runs;
- whether an optional framework is absent, incidental, a legacy operational contract, or the primary orchestration layer; and
- which paths are maintained source versus externally provisioned data, runtime state, checkpoints, predictions, reports, and caches.

Use a flat layout by default. Create `vNN/` only for a durable, independently reproducible training-and-inference contract; never for a seed, fold, checkpoint, sweep point, report, ordinary cohort stratum, or experiment run. Use `eval/<name>/` for authored scientific evaluations; do not introduce a competing top-level namespace without a defined purpose.

A minimal `docs/architecture.md` can be:

```md
# Architecture decision

## Scope
- Question:
- Initial supported operation:
- Non-goals:

## Contracts
- Inputs and access:
- Transform/model contract:
- Outputs and provenance:
- Determinism and hardware:

## Classification and layout
- Dataset releases, model versions, tasks, evaluations, and runs:
- Flat or versioned, with rationale:
- Package/config/evaluation namespaces:
- Archive policy:

## Framework decision
- Framework mode:
- Maintained source versus generated state:

## Safety and validation
- Protected paths:
- Synthetic or authorized fixture:
- Required checks:
```

## Non-negotiable rules

- Keep scientific logic importable in `src/<package>/`; keep CLIs and scripts thin.
- Use `uv`, `pyproject.toml`, a `src` layout, `uv.lock`, Ruff, Pytest, exact compatible dependency pins, and explicit supported Python versions. Do not add speculative dependencies.
- Start with small synthetic or public fixtures. Never put private data, DICOMs, credentials, model weights, raw inputs, large generated arrays, predictions, or caches in Git.
- Document how protected assets are obtained, validated, and located. Track manifests, schemas, checksums, and metadata—not asset copies—when appropriate.
- Establish data/model/evaluation contracts and tests before implementing sophisticated algorithms or bulk operations. Every public CLI should have `--help`, validated paths, predictable output behavior, and useful exit codes.
- Make configuration declarative and layered: safe package defaults, version/task/evaluation configuration when justified, then explicit CLI/environment overrides. Do not silently depend on developer-local paths.
- Separate production/inference behavior from evaluation policy. An evaluation may select cohorts, endpoints, metrics, report rules, or figures, but must reference the tested model/pipeline instead of recreating it.
- Treat every generated output as replaceable runtime state unless it is deliberately promoted to immutable scientific provenance. Define output locations and overwrite/resume rules before the first real run.
- Do not make network requests, provision cloud resources, install system packages, access restricted data, or launch expensive training/inference without the user’s explicit authorization.
- Validate the scaffold immediately: package import, unit tests, lint, build, CLI help, configuration/schema checks, and—only when authorized—a small read-only fixture or real-data smoke into a fresh output directory.

## Construction workflow

1. **Elicit or record the contract.** Resolve unknowns that affect architecture: data and access, target semantics, inputs/outputs, model family, initial operation(s), framework role, evaluation needs, expected scale, and deployment/reproducibility constraints. Clearly label assumptions rather than inventing science.
2. **Choose architecture before scaffolding.** Apply the shared taxonomy. Record flat versus `vNN/`, package name, config namespaces, artifact roots, evaluation names, and any framework role.
3. **Create a minimal installable skeleton.** Add package metadata, `src/<package>/`, tests, documentation, Git ignore rules, one thin CLI, a configuration example/schema appropriate to the project, and CI only when it can run without restricted assets. Use the layouts in [templates](references/templates.md) as a starting point, not a mandatory directory checklist.
4. **Implement one vertical slice.** It should load a tiny fixture or declared input, run a pure transformation/pipeline, validate the result, and write an explicitly named output. Add focused tests for the contract and negative/error paths.
5. **Add optional concerns deliberately.** Add tasks, `dNN` catalogs, `vNN/`, framework integrations, remote storage, GPU execution, notebooks, workflow orchestration, or dashboards only when their operational contract is defined and tested.
6. **Document operation and provenance.** Describe installation, commands, data acquisition/access, configuration precedence, artifact handling, reproducibility limits, and the current architecture decision. Maintain an architecture decision log when significant contracts change.
7. **Validate and report.** Run the relevant validation checks below. Report the chosen architecture, generated files, validation evidence, unimplemented assumptions, and operations intentionally deferred.

## Vertical-slice checklist

Implement the smallest end-to-end behavior that proves the chosen contract:

1. obtain a tiny synthetic, public, or explicitly authorized fixture;
2. validate schema, IDs, shapes, and units before transformation;
3. run one deterministic pure function or pipeline stage;
4. validate output schema, value range, and units, associated with input IDs;
5. write only to an explicit destination without accidental overwrite; and
6. test a happy path, validation failure, and output/provenance behavior.

Do not launch training, download data, or generate large outputs merely to prove the scaffold. Label synthetic fixtures as non-scientific.

## Optional framework integrations

Do not shape a new project around an available framework unless it is an explicit operational requirement. First choose one mode:

- **Absent or incidental:** build a normal package and isolate any optional integration in an adapter.
- **Primary orchestration:** preserve the framework’s supported stage semantics; keep its configuration seeds and generated state separate from maintained source; use supported extension points rather than developer-local paths.
- **Compatibility with an existing contract:** this is a refactor/migration concern; use `data-science-refactor` and its compatibility procedure rather than starting over.

When a framework is a runtime dependency, pin its compatible distribution in `pyproject.toml`, document its source, keep state changes behind supported APIs, and test its minimal integration path. Do not add the dependency or generate its stage directories preemptively. Read the shared architecture reference before scaffolding framework-owned paths.

## Validation and handoff

After scaffolding and each meaningful increment, run the relevant subset:

```bash
uv run pytest
uv run ruff check .
uv build
uv run python -c "import <package_name>"
uv run <command> --help             # if a CLI was added
```

Also validate configuration parsing/schema, run the vertical-slice fixture, confirm a fresh clone/install can perform the documented basic operation, and audit that protected paths are ignored and unstaged. Run framework, GPU, real-data, remote-storage, or model-checkpoint smoke tests only when explicitly authorized. Record unavailable checks and their reason; do not imply that unit tests prove an unavailable integration.

At handoff, report the architecture decision; generated and deliberately deferred files; direct and optional dependencies with purpose; data/checkpoint/artifact boundaries and acquisition instructions; the proved vertical slice and its limitations; exact validation commands and outcomes; and assumptions or scientific/operational decisions that still need an owner.

## Completion criteria

A usable initial repository has a documented architecture decision; an installable locked package; a tested vertical slice; explicit protected-data/artifact policy; a usable CLI or library entry point; and passing targeted tests, lint, build, import, and help checks. It does **not** need real data, trained weights, every planned model, or empty future-oriented directory trees.
