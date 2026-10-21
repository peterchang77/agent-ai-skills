---
id: demo-imaging
title: Demo · Imaging
track: demo
scenario: imaging
tagline: evaluating an AI tool on chest radiographs, from raw DICOM files to an interval-backed answer
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
      - {beat: look-at-images}
      - {beat: first-look}
  - name: 2. Check and clean the images
    steps:
      - {beat: profile-data}
      - {beat: review-images}
      - {beat: plan-cleaning}
      - {beat: clean-data}
      - {beat: add-agents-md}
  - name: 3. Evaluate the AI tool
    steps:
      - {beat: build-cohort}
      - {beat: evaluate-detector}
      - {beat: review-with-second-agent}
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

This track follows one worked example for a radiology and imaging-informatics audience: a department wants to know whether an open-source AI tool that flags **pneumothorax** (a collapsed lung from air leaking into the chest) on chest radiographs is ready for a pilot. You direct a coding agent through the same workflow used in the [clinical demo track](../demo-clinical/index.md): inspect the inputs, audit and clean them, define the study population, analyze, and write up, but the data are DICOM images, the cleaning involves pixels as well as headers, and the analysis is the evaluation of an AI model.

You do not need programming experience to follow along. Each step explains the background, gives a prompt to paste, shows what a good result looks like, and lists what to check. Steps marked as optional or advanced can be skipped.

## Case study overview

The exercises follow a small public sample of chest radiographs (real images, with synthetic data problems added) together with model scores, a Word evaluation protocol, a request memo and short radiology reports:

```text
DICOM files → look → profile → review in a viewer → plan and clean → cohort → evaluate → references → abstract
                                      │                                              │
                                      └─→ a person confirms what numbers      ├─→ dashboard, Word/Excel export
                                          cannot show                         └─→ reusable tool and skill → Git
```

The workflow addresses five questions: how well the primary model separates pneumothorax from none, whether it is really better than three alternatives, whether it works equally well across views, sexes and ages, whether any model meets the pilot bar, and (separately) how to sort 200 radiology reports.

## What is distinctive in this example

- **Pixels as well as headers.** Header problems are found by code; some pixel problems (a mirrored or inverted image) are not, so a person has to look. You build a small viewer for this.
- **Privacy at the pixel level.** Patient details can sit in the header *and* be burned into the image.
- **Evaluating an AI tool honestly.** Intervals, comparing models on the same patients, and treating subgroup differences with care.

This is a toy demonstration with a small public image sample. Nothing here is evidence about any real tool.

<!-- include: demo-common -->

## Contents

<!-- toc -->

## Track navigation

<!-- track-nav -->
