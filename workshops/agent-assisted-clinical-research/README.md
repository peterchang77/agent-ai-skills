# Agent-Assisted Clinical Research Workshop

A workshop seed for learning to direct, inspect, and revise coding-agent work in a small longitudinal imaging study. Participants use a prepared CheXpert Plus workspace and an approved local LLM endpoint to build real artifacts. This repository supplies the research context and review contracts; it intentionally does **not** supply the implementations participants are meant to create.

## Learning outcome

By the end, a participant should be able to give an agent a bounded research-engineering request, inspect its assumptions and implementation, run meaningful validation, and revise the request when evidence exposes a problem. The scientific thread is a report-derived temporal-change target for serial chest radiographs. Outputs are weak pseudo-labels and agreement metrics, **not** clinical ground truth or diagnostic performance.

## Start here

1. Open [`00-orientation/README.md`](00-orientation/README.md) and set up the supplied cloud workspace.
2. Work through the exercise folders in order. Start each task from its `BRIEF.md`; do not open reference prompts until after your first attempt.
3. Use `CONTEXT.md`, `CONTRACT.md`, and `ACCEPTANCE.md` to improve your own agent request and review its work.
4. Compare with `reference-prompts/` or a `reference/` artifact only after an attempt or when recovering from a blocked exercise.

| Exercise | Participant asks an agent to create | Key lesson |
|---|---|---|
| [01 Data discovery](01-data-discovery/BRIEF.md) | a safe dataset-inspection/download utility | inspect before exporting; make cost and scope explicit |
| [02 Cohort curation](02-cohort-curation/BRIEF.md) | cohort construction and temporal-pair validation | an executable pipeline can still encode an invalid study definition |
| [03 Report abstraction](03-report-abstraction/BRIEF.md) | resumable LLM extraction and structural validation | constrain weak labels; retain evidence and provenance |
| [04 Annotation tool](04-annotation-tool/BRIEF.md) | a single-file review/annotation application | agents can build small, inspectable research tools |
| [05 Modeling](05-modeling/BRIEF.md) | a simple baseline, selection workflow, and evaluation | choose on validation; protect the held-out partition |
| [06 Results and writing](06-results-and-writing/BRIEF.md) | figures/tables and a concise LaTeX report | report what the analysis supports, including limitations |

## What is intentionally pre-built

- Data locations, endpoint conventions, and environment-variable names.
- Scientific definitions, fixed data/output contracts, and acceptance criteria.
- Small valid/invalid abstraction examples and a finished annotation-tool example.
- Optional reference prompts and reference implementations, separated from the default path.

## What participants should build

The download/inspection utility, date-pairing/cohort code, LLM abstraction runner, validator, annotation UI, baseline training/evaluation program, plots, and LaTeX results artifact. Agents should do real work; participants remain responsible for study decisions and review.

## Instructor setup

The cloud image must provide the approved CheXpert Plus data or a documented download path, an approved OpenAI-compatible LLM endpoint, and a Python environment. Put deployment-specific values in the workspace environment, never in Git. See [`shared/workspace-contract.md`](shared/workspace-contract.md).

## Data handling

CheXpert Plus and all derived artifacts remain subject to the applicable data-use agreement. Do not commit credentials, raw protected reports/images, unrestricted exports, or endpoint logs containing protected content. The endpoint must be approved for the report text it receives. See [`shared/data-and-llm-safety.md`](shared/data-and-llm-safety.md).

## Suggested timing

A 110-minute first session: orientation (10 min), discovery (15), curation (20), abstraction plus annotation (30), modeling (20), and results/writing (15). An instructor may demonstrate the completed full pipeline between participant tasks, but each exercise should run independently.
