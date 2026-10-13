---
id: scoping-work
title: Scoping work — how much to ask per turn
short: Scoping work
themes: [context-discipline]
related: [steering, verification, context, costs]
blurb: Scope requests to sizes that can be independently verified. Require structured plans before executing complex multi-step pipelines.
---

Calibrating the scope of each request is a vital skill when collaborating with coding agents. Prompts that are too narrow lead to tedious, fragmented oversight; prompts that are too broad produce sprawling, multi-file codebases that defy thorough human review. Effective task scoping ensures that every unit of delegated work can be audited before compounding further steps.

## The spectrum of task granularity

| Granularity tier | Example research task | Supervisory requirements |
|---|---|---|
| **Atomic modification** | Adjusting a plot axis label or updating a column mapping | Quick glance at the unified diff |
| **Discrete script** | Developing a data-profiling script to identify outliers | Review the execution output and inspect the script logic |
| **Multi-stage pipeline** | Ingesting raw data, applying cleaning rules, and estimating a regression model | Evaluate each analytical phase sequentially; reconcile intermediate counts |
| **End-to-end project** | Defining a patient cohort, modeling outcomes, and compiling a manuscript | Formulate an explicit plan up front, establish intermediate checkpoints, and run peer reviews |
| **Autonomous execution** | Multi-hour batch processing or large-scale document classification | Strong environment sandboxing, detailed structured logging, and thorough post-hoc auditing |

## Balancing interactive steering and long-running execution

Short feedback loops—proposing an approach, reviewing code, and confirming results—keep the researcher in control, catching flawed assumptions while they are inexpensive to correct. In contrast, granting extended autonomy saves researcher attention but risks compounding errors: an incorrect filtering criteria applied at minute two can invalidate an entire hour of subsequent calculations.

**A practical rule of thumb:** A well-scoped unit of work is one you can verify in a few minutes. If you cannot explain how you will validate the output, break the task into smaller sub-tasks.

## The plan-first methodology

For non-trivial analytical tasks, instruct the agent to propose a structured **plan** before executing any commands or editing files. A well-constructed plan outlines the methodological strategy, candidate libraries, key assumptions, and open questions requiring researcher guidance. Many agent harnesses support dedicated *plan modes* that enforce read-only exploration until you explicitly approve execution ([Steering](concept:steering)).

```text
Before modifying any files or running scripts, formulate an analytical plan for <objective>.
Detail the computational steps, expected artifacts, methodological assumptions, and open questions.
Do not edit any files yet.
```

Requiring a planning phase ensures that scientific judgements—such as variable definitions, exclusion criteria, and statistical models—remain firmly in your hands before code is run.

## Structuring effective requests

An effective prompt provides three clear components:

1. **The objective:** The research question and the intended artifact (e.g., an audit table or publication plot).
2. **Operational boundaries:** Specific input datasets to use, files that must remain untouched, and required software dependencies.
3. **Verification standards:** The criteria by which correctness will be judged (e.g., expected row totals, specific reference benchmarks).

For a deeper exploration of prompt engineering and delegation patterns, refer to the [Introducing coding agents](guide:introducing-coding-agents) guide.

## Establishing checkpoints for complex workflows

Long-running workflows should be organized into distinct stages with intermediate data files saved to disk. Saving checkpoints prevents a late-stage failure from losing earlier progress and allows you to audit data transformations at stage boundaries rather than only at the conclusion.

## Indicators of excessive prompt scope

- The proposed plan is too complex to summarize in a couple of sentences.
- You cannot verify the final output against known data properties.
- Code modifications are scattered across dozens of files you have not inspected.

## Calibrating autonomy over time

Agent reasoning capabilities continue to improve. A complex analytical pipeline that failed on earlier models may succeed on newer architectures. The recommended practice is to start with modest task boundaries, evaluate output quality, and gradually increase delegated autonomy as confidence grows.

## Demo it

<!-- demos -->
