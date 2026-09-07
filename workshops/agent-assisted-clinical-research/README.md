# From Data to Evidence with Research Agents

A hands-on workshop in using coding agents to move from an unfamiliar research resource to a reproducible analysis and written result.

This repository is a reusable workshop framework. The instructor chooses the dataset, research question, data-access method, and example artifacts for a particular offering. Participants use a prepared workspace and an agent to create real, reviewable work rather than merely execute a prebuilt notebook.

## What participants practice

Participants learn how to:

- give an agent durable project context without repeatedly dictating setup details;
- turn a broad research task into a specific artifact an agent can build and validate;
- ask an agent to inspect data, APIs, documentation, and existing code before making assumptions;
- define inputs, outputs, constraints, and evidence of completion;
- use an LLM for structured data abstraction and review its output;
- build small purpose-built tools when they are more useful than a large application;
- create a simple analysis or model with a reproducible evaluation workflow; and
- turn saved artifacts into figures, tables, LaTeX, and verified citations.

The central skill is directing and reviewing an agent: deciding what the agent should do, what information it needs, what must be checked, and how to respond when evidence calls for a revision.

## Workshop structure

The six stages form a general research workflow. Their concrete content is supplied by the dataset and exercise selected for a workshop offering.

| Stage | Typical artifact created by an agent | Participant practice |
|---|---|---|
| [01. Data discovery](01-data-discovery/AGENT_CONTEXT.md) | A small data-access or inspection utility | Exploring an unfamiliar resource before using it |
| [02. Data curation](02-cohort-curation/AGENT_CONTEXT.md) | A documented analytic dataset or cohort manifest | Turning inclusion, exclusion, linkage, and split decisions into auditable code |
| [03. Structured abstraction](03-report-abstraction/AGENT_CONTEXT.md) | An LLM-assisted extraction and validation workflow | Schemas, provenance, reviewable outputs, and restartable processing |
| [04. Annotation tool](04-annotation-tool/AGENT_CONTEXT.md) | A compact local review interface | Requesting a narrow, inspectable tool for a real task |
| [05. Analysis or modeling](05-modeling/AGENT_CONTEXT.md) | A reproducible baseline analysis and evaluation | Defining a selection and evaluation workflow before interpreting results |
| [06. Results and writing](06-results-and-writing/AGENT_CONTEXT.md) | Figures, a LaTeX report, and citations | Connecting written claims to saved evidence |

Stages can be run in sequence or adapted independently. An instructor may use the full workflow, demonstrate selected stages, or substitute a different example while retaining the same learning pattern.

## Participant workflow

Each stage has one participant-facing `AGENT_CONTEXT.md`. It is a compact project brief containing the information a researcher would otherwise need to explain repeatedly: available resources, relevant background, required output, and practical boundaries.

For each stage:

1. Read `AGENT_CONTEXT.md`.
2. Write a request to your agent in your own words.
3. Ask the agent to inspect the workspace and propose an approach before implementation.
4. Review the plan, direct the work, and ask the agent to run relevant checks.
5. Inspect the resulting artifact and steer a revision as needed.

The context file is not a prewritten prompt or implementation recipe. Participants choose how to frame, sequence, and evaluate the agent’s work.

## Instructor guide and answer keys

[`instructor-guide/`](instructor-guide/) contains one answer key per stage. Each key provides a suggested live flow, expected artifacts, a reference prompt, common errors, recovery ideas, and reference-material locations.

It supports two teaching styles:

- **Work-along:** participants try a stage with their own agents, then compare their approach with the instructor guide.
- **Demonstration/review:** the instructor works through a stage live while participants inspect the decisions, artifacts, and validation.

### Sharing the guide or withholding it during an exercise

The instructor guide is intentionally included in this repository so it can be shared, reviewed, and reused. An agent that can access this checkout can also read it.

When you want participants to work without answer-key access, create a participant-only copy before launching their sessions:

```bash
bash tools/make-participant-copy.sh /path/to/participant-workshop
```

The generated copy excludes `instructor-guide/`. Use the full checkout for instruction and give participants/agents only the generated copy. Do not rely on a hidden directory as an access boundary.

## Preparing a workshop offering

Before the session, the instructor provides:

- a documented data source, data mount, or download route;
- an authenticated workspace with the necessary software and packages;
- any required API or model-endpoint configuration;
- an exercise-specific input resource suitable for the selected stages;
- a writable project directory for each participant; and
- any reference artifacts used in the live demonstration.

The included preflight helper checks for `uv`, Python, and the configured LLM environment-variable names:

```bash
bash tools/preflight.sh
```

It reports only whether a variable is set, never its value. Adapt or replace it when an offering does not use an LLM endpoint.

## Repository layout

```text
01-data-discovery/AGENT_CONTEXT.md
02-cohort-curation/AGENT_CONTEXT.md
03-report-abstraction/AGENT_CONTEXT.md
04-annotation-tool/AGENT_CONTEXT.md
05-modeling/AGENT_CONTEXT.md
06-results-and-writing/AGENT_CONTEXT.md
instructor-guide/<stage>/ANSWER_KEY.md
tools/preflight.sh
tools/make-participant-copy.sh
```

The `tools/` directory contains setup and distribution helpers. The primary exercise artifacts are not prebuilt: participants direct their agents to create them. The existing context files and answer keys provide one concrete example that instructors can adapt, replace, or extend for another dataset or research workflow.

## Using this framework for another topic

To adapt the workshop, replace a stage’s `AGENT_CONTEXT.md` with a brief that states:

- the available data, documentation, and workspace resources;
- the artifact to create;
- the scientific or operational background needed to make good decisions;
- the required outputs and evidence of completion; and
- the scope of the exercise.

Then update the corresponding instructor answer key with the intended live flow, a reference prompt, expected outputs, common mistakes, and useful recovery prompts. This preserves the workshop’s core experience while allowing the example to change.
