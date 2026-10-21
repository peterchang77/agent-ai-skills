---
id: demo-track
title: Demo · Tabular
track: demo
tagline: one worked example, from raw files to a cited report, in self-contained steps
sections:
  - name: Start
    steps:
      - {setup: true}
      - {beat: orient-in-folder}
      - {beat: prepare-environment}
  - name: 1. Understand the inputs
    steps:
      - {beat: read-text-files}
      - {beat: read-office-formats}
      - {beat: first-look}
  - name: 2. Clean the data
    steps:
      - {beat: profile-data}
      - {beat: plan-cleaning}
      - {beat: clean-data}
      - {beat: add-agents-md}
  - name: 3. Research analysis
    steps:
      - {beat: build-cohort}
      - {beat: analyze-pilot}
      - {beat: review-with-second-agent}
      - {beat: saturday-hours}
  - name: 4. References and writing
    steps:
      - {beat: find-references}
      - {beat: references-from-links}
      - {beat: write-abstract}
  - name: 5. Outputs for others
    steps:
      - {beat: build-dashboard}
      - {beat: export-office-formats}
  - name: 6. Make it repeatable
    steps:
      - {beat: make-tool-and-skill}
      - {beat: commit-work}
      - {beat: check-usage-and-compact}
  - name: Advanced
    steps:
      - {beat: use-secrets}
      - {beat: bulk-classify}
---

The demo track provides an end-to-end case study across modular, self-contained exercises. It translates the theoretical principles from the [concept track](../concepts/index.md) into concrete research tasks: ingesting mixed data formats, auditing and cleaning tabular records, conducting statistical analyses, retrieving literature citations, compiling a publication-ready abstract, and packaging the completed pipeline for long-term reproducibility.

Each demo module follows a standardized structure:

1. **Background**: Core context and prerequisites for the immediate task.
2. **General methodology**: Reusable prompt patterns and computational techniques applicable to any dataset.
3. **Workshop example**: A concrete demonstration using the provided benchmark dataset. (You can switch scenario tabs if exploring multiple configurations.)
4. **Verification criteria & common pitfalls**: Targeted guidance for evaluating outputs and troubleshooting discrepancies.
5. **Supporting concepts**: Direct references back to foundational principles in the concept track.

## Case study overview

The exercises follow a synthetic multi-site clinical dataset consisting of encounter logs, performance benchmark spreadsheets, a clinical trial protocol, staff newsletters, and unstructured triage notes:

```text
raw files → profile → plan and clean → cohort → analysis → references → abstract
                             │
                             ├─→ dashboard, Word/Excel export
                             └─→ reusable tool and skill → Git
```

The workflow addresses three clinical research questions: an operational audit (evaluating site adherence to glycemic targets), an observational study (measuring whether post-discharge outreach correlates with recheck visits while adjusting for confounders), and an optional policy analysis (assessing whether expanded clinic hours reduced emergency utilization).

## Modular progression and checkpoints

You do not need to execute the tutorial from start to finish in a single pass. Every exercise defines an explicit **starting state**, consisting of either the initial dataset or a saved checkpoint reflecting earlier results. The [Setup](setup.md#restore-a-starting-point) guide provides instructions for restoring any checkpoint, allowing you to jump directly into specific exercises such as statistical modeling or manuscript drafting.

## Exercise categories

| Category | Description |
|---|---|
| Full step | Core stages of the research pipeline |
| Quick step | Focused, high-leverage administrative or environment checks |
| Optional detour | Deep-dive tasks that enrich the analysis without blocking subsequent steps |
| Advanced | Exercises requiring external API credentials or cloud budget |

## Adapting to proprietary data

The general methodologies apply universally to empirical datasets. The workshop example demonstrates how these techniques operate on synthetic data with known answers. Before adapting these workflows to proprietary or sensitive institutional data, consult [Privacy and data handling](concept:privacy) and [Secrets](concept:secrets).

## Contents

<!-- toc -->

## Track navigation

- The [concept track](../concepts/index.md) provides theoretical foundations for the methods applied here.
- The [imaging version of this track](../demo-imaging/index.md) applies the same workflow to chest radiographs and the evaluation of an AI tool.
- The [guided tutorial](../tutorial/index.md) arranges these exercises and concepts into a continuous, interleaved curriculum.
