---
id: demo-clinical
title: Demo · Clinical
track: demo
scenario: toy
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

This track follows one worked example for a clinical operations and quality-improvement audience: a three-clinic network wants to know which sites meet their glycemic (HbA1c) targets, and whether a follow-up call pilot at one site increased rechecks. You direct a coding agent through the same workflow used in the [imaging demo track](../demo-imaging/index.md): inspect the inputs, audit and clean them, define the study population, analyze, and write up, but the data are a mix of spreadsheet, document and database files and the analysis is an observational comparison.

You do not need programming experience to follow along. Each step explains the background, gives a prompt to paste, shows what a good result looks like, and lists what to check. Steps marked as optional or advanced can be skipped.

## Case study overview

The exercises follow a synthetic multi-site clinical dataset consisting of encounter logs, performance benchmark spreadsheets, a clinical trial protocol, staff newsletters, and unstructured triage notes:

```text
raw files → profile → plan and clean → cohort → analysis → references → abstract
                             │
                             ├─→ dashboard, Word/Excel export
                             └─→ reusable tool and skill → Git
```

The workflow addresses three clinical research questions: an operational audit (evaluating site adherence to glycemic targets), an observational study (measuring whether post-discharge outreach correlates with recheck visits while adjusting for confounders), and an optional policy analysis (assessing whether expanded clinic hours reduced emergency utilization).

## What is distinctive in this example

- **Many file formats.** Spreadsheets, Word and PDF documents, a web page and a database all need to be read, and each loses something in conversion.
- **Problems inside the records.** Mixed units, duplicates, spelling variants and bad dates are found by code, and the cleaning decisions are written down.
- **An observational analysis.** Crude and adjusted estimates, with a second agent reviewing the work.

All data in this example is synthetic.

<!-- include: demo-common -->

## Contents

<!-- toc -->

## Track navigation

<!-- track-nav -->
