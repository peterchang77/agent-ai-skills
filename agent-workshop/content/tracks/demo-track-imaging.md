---
id: demo-track-imaging
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

This track follows one worked example for a radiology and imaging-informatics audience: a department wants to know whether an open-source
AI tool that flags **pneumothorax** (a collapsed lung from air leaking into the chest) on chest radiographs is ready for a pilot. You
direct a coding agent through the same workflow used in the [tabular demo track](../demo/index.md): inspect the inputs, audit and clean
them, define the study population, and analyze, but the data are DICOM images, the cleaning involves pixels as well as headers, and the
analysis is the evaluation of an AI model.

You do not need programming experience to follow along. Each step explains the background, gives a prompt to paste, shows what a good
result looks like, and lists what to check. Steps marked as optional or advanced can be skipped.

Each step defines its **starting state** (the original kit or a saved checkpoint), so you can begin at any step. See [Setup](setup.md#restore-a-starting-point).

```text
DICOM files → look → profile → review in a viewer → plan and clean → cohort → evaluate → references → abstract
                                      │                                              │
                                      └─→ a person confirms what numbers      ├─→ dashboard, Word/Excel export
                                          cannot show                         └─→ reusable tool and skill → Git
```

## What this track adds to the tabular track

- **Two kinds of data problems.** Header problems (IDs, units, missing fields) are found by code. Some pixel problems (a mirrored or
  inverted image) are not, so a person has to look. You build a small viewer for this.
- **Privacy at the pixel level.** Patient details can sit in the header *and* be burned into the image.
- **Evaluating an AI tool honestly.** Intervals, comparing models on the same patients, and treating subgroup differences with care.

This is a toy demonstration with a small public image sample. Nothing here is evidence about any real tool.

## Contents

<!-- toc -->

## Track navigation

- The [concept track](../concepts/index.md) gives the principles behind the methods used here.
- The [tabular demo track](../demo/index.md) covers the same workflow on spreadsheet-style data.
- The [imaging guided tutorial](../tutorial-imaging/index.md) arranges these exercises and the concepts into one continuous path.
