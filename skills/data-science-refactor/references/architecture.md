# Project architecture, versioning, and framework migration guide

Read this reference when deciding whether to create, preserve, flatten, or archive a project layout; when a repository uses an orchestration framework; or when several historical implementations compete to be the active source of truth. Do not create empty directories merely to conform to a diagram.

## 1. Make the decision before moving files

Classify every apparent version, model, experiment, cohort, and analysis as exactly one of these:

| Kind | Meaning | Typical location |
| --- | --- | --- |
| Dataset release (`dNN`) | Immutable input-cohort, annotation, schema, or split contract | `datasets/dNN.yml`, or documented in `docs/provenance.md` |
| Model version (`vNN`) | Durable, independently reproducible training and inference contract | `vNN/` |
| Task | Different target under a shared data/training/evaluation system | `configs/tasks/` or a task config namespace |
| Evaluation | A scientific question, cohort definition, comparison, or report policy | `eval/<name>/` or `vNN/eval/<name>/` |
| Experiment/run | Fold, seed, sweep point, checkpoint, job, or materialized execution | framework-managed experiment/artifact storage |
| Archive | Inactive historical source retained for evidence but not imported by active code | `archive/legacy/<name>/` |

A named item is a **model version** only when it changes a durable reproducibility contract, for example:

- source data schema, annotation policy, or an independently materialized training dataset;
- preprocessing, coordinate convention, normalization, label semantics/order, or split policy;
- input geometry, model input/output shape, architecture, or inference/postprocessing behavior; or
- a trained model that must be selected and rerun without reconstructing context from another tree.

Treat seed, fold, epoch, hyperparameters, sampling weights, checkpoint selection, report formatting, and ordinary cohort stratification as run/evaluation variation unless they change that contract. A data release and a model version are independent: one data release may support several versions; a model version may be evaluated on several releases or cohorts.

Default to a flat root and one configuration when all variation is experiment-level. Create `vNN/` only when the version boundary prevents configuration/state collisions and provides real independent reproducibility. Do not use `vNN/` just to make a project look organized.

Before mutation, record the decision in `README.md`, `docs/provenance.md`, or a migration plan:

```yaml
architecture_decision:
  active_implementation: <path>
  layout: flat | versioned
  framework_mode: absent | incidental | legacy-structured | primary-orchestration
  classifications:
    - name: d05
      kind: dataset-release
      rationale: ...
    - name: v05
      kind: model-version
      rationale: ...
    - name: timing-analysis
      kind: evaluation
      rationale: ...
  shared_code: src/<package>/
  archived_trees: [...]
  compatibility_requirements: [...]
```

## 2. Choose the correct framework role

A framework can have three distinct roles. Audit its version/source, configuration, manifests, extension points, generated trees, experiment directories, and current commands before choosing one.

### A. Incidental use

Use this when a framework is used for isolated operations—data loading, visualization, image operations, workflow utilities, or compute helpers—but it is not the project’s durable pipeline contract. Indicators include no authoritative configuration seed, no reproducible framework lifecycle, and no materialized framework state that downstream work requires.

Refactor to a normal project. Isolate retained framework calls in an adapter such as `src/<package>/integrations/<framework>.py`. Do not create framework-looking directories merely because old scripts imported it.

```text
project/
  pyproject.toml
  src/<package>/
  configs/
  datasets/                 # optional authored release catalog
  eval/                     # optional authored evaluations
  tests/
  docs/
  archive/legacy/
```

### B. Legacy structured framework project

Use this when the repository has a meaningful historical framework layout—often a root configuration seed and generated stage directories—but drivers and configuration were partly hand-written or predate the current automated workflow.

Preserve the historical operational contract first. Modernize around it: put maintained reusable logic in `src/<package>/`, keep compatibility shims only where historical callers need them, and document authored versus generated/provenance material. Do not move historical generated state or experiments merely to make the root resemble a new project.

A legacy project remains flat unless an actual new model-version boundary is introduced or reconstructed with adequate provenance.

```text
project/
  <framework-config>        # retained authored seed, if authoritative
  src/<package>/
  <stage>/                  # compatibility shims or historical generated boundary
  <runtime-state>/          # generated; normally ignored
  <experiments>/            # materialized historical experiments; normally ignored
  docs/provenance.md
  tests/
```

### C. Primary orchestration framework

Use this when framework configuration defines preparation, data/materialization, training, experiment creation, inference, or deployment; project-specific code is called through supported extension points; and the framework is the primary operational contract.

Keep the framework’s documented stage names and version roots. Put reusable, version-agnostic project code in `src/<package>/`; put the authoritative configuration seed at the framework-supported location; allow the framework to generate its operational directories. Do not copy framework-owned data management, preprocessing, training, inference, or reporting logic locally without a documented framework gap.

```text
project/
  pyproject.toml
  src/<package>/            # reusable project code and supported extensions
  datasets/                 # optional small authored release catalog
  v00/                      # only when the model contract warrants a version
    <framework-config>      # authoritative model-version contract
    README.md               # version provenance, if useful
    <generated-stage>/      # generated when the stage is used
    <runtime-state>/        # generated when the stage is used
    <experiments>/          # materialized experiments when the stage is used
    eval/                   # authored version-specific evaluation definitions
  eval/                     # optional authored cross-version evaluations
  tests/
  docs/
```

Do not manufacture absent stages. The `vNN/` root is warranted by the model contract; framework directories exist only when the relevant workflow is used.

## 3. Separate source/provenance from framework execution state

Framework operational directories are not replacements for a project’s source and provenance documentation:

| Concern | Authoritative location | Do not do |
| --- | --- | --- |
| Reusable project logic | `src/<package>/` | Copy it into generated drivers or every version subtree |
| Framework pipeline contract | documented config seed | Duplicate operational queries, hooks, or transforms in a second hand-maintained catalog |
| Dataset release identity | optional `datasets/dNN.yml` or provenance documentation | Treat generated manifests as the dataset catalog |
| Query/materialized state | framework workspace and external data root | Hand-edit generated state or relocate it casually |
| Scientific evaluation definition | `eval/<name>/` or `vNN/eval/<name>/` | Hide study policy in generated execution files |
| Runtime artifacts | ignored/external version- and experiment-scoped paths | Commit protected data, checkpoints, caches, or results by default |

An optional dataset-release record should be small and point to, rather than clone, the framework configuration:

```yaml
id: d05
status: active
source_roots: [/data/raw/project/...]
cohort_definition: docs/cohorts/d05.md
annotation_revision: ...
split_definition: ...
framework:
  distribution: <framework-distribution>
  config: v05/<framework-config>
  workspace_namespace: ...
used_by: [v05]
```

Use `docs/provenance.md` instead when there is only one data contract. Never put credentials, protected local paths, or a duplicate full operational configuration in the catalog.

## 4. Evaluation: one human-facing namespace

Use **`eval/`**, not an additional top-level `studies/`, for authored scientific evaluation. This avoids competing organization beside framework-owned execution stages.

- Framework execution stages retain their documented semantics and may be generated.
- `eval/` is the human-facing, authored **scientific question**: cohort inclusion, exact model/experiment references, score aggregation, subgroup definitions, comparisons, bootstrap/report policy, and conclusions.

Do not rename framework execution stages into `eval/`; they retain useful framework meaning. Do not put broad authored research logic directly in generated trees. A study can invoke framework operations, but has one authored home.

Use `src/<package>/evaluation/` for reusable domain-specific score, cohort, metric, comparison, and reporting functions. Use `vNN/eval/<name>/` for a study tied to exactly one model version. Use root `eval/<name>/` only when a study compares models/versions or otherwise belongs to no single version.

A study manifest should reference exact inputs instead of copying model pipeline details:

```yaml
id: external-validation-2026
model:
  version: v02
  experiment: <experiment-id>
  config: ../../v02/<experiment-config>
dataset:
  id: pilot-2026
  root: /data/raw/project_pilot
prediction:
  path_pattern: outputs/v02/{subject_id}/prediction.<format>
analysis:
  score_method: project-specific-score-v1
  subgroups: [site, age_band]
  report: report.py
```

For new external cohorts, prefer the framework’s supported inference path over a handwritten copy of preprocessing or postprocessing. Preserve a historical custom driver only when it is needed to reproduce a documented or published result, and label it as compatibility/provenance code.

## 5. Generated-file boundary

Read applicable framework documentation before changing framework-facing code. In a generated workflow, files produced by the framework are normally overwritten. Put custom logic in supported non-generated extension points, a version-specific thin driver when truly necessary, or preferably `src/<package>/` referenced through documented configuration mechanisms.

Preserve portable configuration and supported APIs. Do not substitute developer-local absolute paths into portable config, hand-edit generated state, or use a second handwritten implementation when the framework owns the contract. A materialized experiment configuration is evidence of the actual training contract; retain it as provenance.

## 6. Identify the active implementation and archive deliberately

Use recency as a navigation heuristic, not scientific proof:

1. inspect current user changes and branch intent first;
2. use recent Git commits touching source, configs, tests, docs, and package metadata;
3. use filesystem modification time only for untracked authored candidates;
4. confirm active paths through imports, entry points, documented commands, and artifact lineage; and
5. heavily discount generated data, checkpoints, arrays, logs, images, caches, build products, and generated framework trees.

Promote one coherent active implementation rather than treating every historical tree as co-equal. Preserve inactive authored code under `archive/legacy/<name>/` only after recording old path, commit or timestamp, purpose, commands/environment, linked data/model artifacts, and why it is no longer active. Never archive or move external/generated provenance without explicit authorization.

## 7. Safe migration sequence

1. **Freeze and inventory.** Capture status, HEAD, active entry points, environment, data roots, artifact roots, and commands. Classify all material before editing.
2. **Select source of truth.** Use provenance, imports, and tests—not directory names—to identify the active implementation.
3. **Write the architecture decision.** Classify data releases, model versions, tasks, evaluations, runs, and archive-only trees.
4. **Establish package and tests.** Add `pyproject.toml`, `src/`, tests, and thin commands before moving scientific logic. Preserve behavior first.
5. **Migrate in small compatibility-preserving steps.** Keep framework config/path semantics intact; extract pure logic; add regression tests before changing behavior.
6. **Archive only after promotion works.** Do not make archive trees imported by active code. Add an index and provenance record.
7. **Validate the active path.** Run targeted tests, full lint/build, CLI help, config validation, and an authorized small real-data smoke where applicable. State unavailable checks honestly.

## 8. Completion evidence

A completed architecture refactor records:

- selected framework mode and active source of truth;
- flat versus versioned decision and classifications of all apparent versions/runs;
- config/data/experiment/prediction namespaces and collision prevention;
- generated versus maintained file policy;
- archived trees and retained compatibility paths;
- exact validation commands/results and any blocked real-data checks; and
- a compatibility-gap ledger for framework migrations.

See `checklist.md` for the audit and acceptance gate.
