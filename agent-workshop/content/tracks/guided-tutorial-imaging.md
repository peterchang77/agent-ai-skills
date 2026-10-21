---
id: guided-tutorial-imaging
title: Tutorial · Imaging
track: tutorial
scenario: imaging
tagline: a structured path through the curriculum on one imaging example, alternating conceptual foundations with practical exercises
sections:
  - name: 1. Get started
    steps:
      - {setup: true}
  - name: 2. Meet your agent
    steps:
      - {concept: agent-vs-chat}
      - {beat: orient-in-folder}
      - {concept: what-code-can-do}
      - {concept: harnesses}
  - name: 3. Work safely
    steps:
      - {concept: privacy}
      - {concept: environment}
      - {beat: prepare-environment}
  - name: 4. Understand the inputs
    steps:
      - {concept: inputs}
      - {beat: read-text-files}
      - {beat: read-office-formats}
      - {beat: look-at-images}
      - {beat: first-look}
  - name: 5. Check and clean the images
    steps:
      - {concept: scoping-work}
      - {concept: verification}
      - {beat: profile-data}
      - {beat: review-images}
      - {concept: steering}
      - {beat: plan-cleaning}
      - {beat: clean-data}
      - {concept: memory}
      - {beat: add-agents-md}
  - name: 6. Evaluate the AI tool
    steps:
      - {concept: context}
      - {beat: build-cohort}
      - {beat: evaluate-detector}
      - {beat: review-with-second-agent}
  - name: 7. Write it up
    steps:
      - {concept: outputs}
      - {beat: find-references}
      - {beat: references-from-links}
      - {beat: write-abstract}
      - {beat: build-dashboard}
      - {beat: export-office-formats}
  - name: 8. Make it repeatable
    steps:
      - {concept: tools}
      - {beat: make-tool-and-skill}
      - {concept: version-control}
      - {beat: commit-work}
      - {concept: costs}
      - {beat: check-usage-and-compact}
  - name: Advanced
    steps:
      - {concept: secrets}
      - {concept: sandboxing}
      - {beat: use-secrets}
      - {beat: bulk-classify}
---

This guided tutorial follows the same structured path as the [tabular tutorial](../tutorial/index.md), on a radiology example: you direct a coding agent to audit and clean a set of chest radiographs, define a study population, and evaluate open-source AI tools that flag **pneumothorax**. Background concepts are placed just before the hands-on step that uses them, with direct links back to the reference pages.

You can complete it in one session or across several. Work from each stage is preserved as a restorable checkpoint, so you can pause, resume, or skip forward at any point ([Setup](setup.md#restore-a-starting-point)).

This is a toy demonstration on a small public image sample with planted data problems. Nothing here is evidence about any real tool.

## Learning outcomes

By completing this tutorial, you will produce:

- A configured local agent environment with safe data-handling and credential practices, including for images that carry patient information.
- A reproducible image-cleaning pipeline with a small offline viewer, a human review of what code cannot find, and an explicit audit trail of decisions.
- An evaluation of four AI models with intervals, paired comparisons and cautious subgroup analysis, independently reviewed by a second agent.
- A verified bibliography, an abstract with citations, and a self-contained results dashboard.
- A reusable command-line tool and agent skill tracked in Git, alongside a bulk report-classification workflow using an external API.

## Contents

<!-- toc -->

## Track navigation

- Consult the [concept track](../concepts/index.md) for a modular reference covering core ideas independently of hands-on steps.
- Use the [imaging demo track](../demo-imaging/index.md) to explore individual practical exercises or jump into specific checkpoints.
