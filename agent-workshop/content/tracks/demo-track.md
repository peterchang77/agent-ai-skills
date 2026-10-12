---
id: demo-track
title: Demo track
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

The demo track is **one worked example, step by step**. It shows how the ideas in the [concept track](../concepts/index.md) look when applied to real
files: reading mixed formats, cleaning data, running an analysis, finding references, writing a report, and packaging the work so you can repeat it.

Each step has the same layout:

1. **Background**, so you can follow the step without reading anything else.
2. **A general approach**, a prompt pattern you can reuse on your own data.
3. A **Workshop example** that uses the supplied dataset. Switch the scenario tab if you have more than one.
4. **What to check** and **Common problems**.
5. **Concepts behind this**, linking back to the concept track.

## The story

A small, synthetic clinic group has three sites and a handful of files: visit records, a spreadsheet of targets, a protocol, a newsletter, call logs and
visit notes. The work answers three questions and produces a report:

```text
raw files → profile → plan and clean → cohort → analysis → references → abstract
                             │
                             ├─→ dashboard, Word/Excel export
                             └─→ reusable tool and skill → Git
```

The questions are an operational one (which clinics meet their HbA1c target), a research one (was a follow-up call associated with a recheck, with
confounding to handle), and an optional one (did new Saturday hours reduce urgent visits).

## Doing a step on its own

You do not have to start at the beginning. Each step states a **starting state**, either the supplied data kit or a saved checkpoint with the earlier results,
and the [Setup](setup.md#restore-a-starting-point) page shows how to restore it. So you can, for example, open *Write a research abstract* directly.

## Kinds of step

| Kind | Meaning |
|---|---|
| Full step | A core step in the story |
| Quick step | Short, usually a single action |
| Optional detour | Useful and self-contained, but you can skip it |
| Advanced | Needs an API key, costs money, or both |

## Using your own data

The general part of each step works on any data. The example only shows what it looks like on the supplied files. If you do this on real data, read
[Privacy](concept:privacy) and [Secrets](concept:secrets) first.

## Contents

<!-- toc -->

## How this fits with the other tracks

- The [concept track](../concepts/index.md) explains the ideas each step uses.
- The [guided tutorial](../tutorial/index.md) interleaves the two in a fixed order.
