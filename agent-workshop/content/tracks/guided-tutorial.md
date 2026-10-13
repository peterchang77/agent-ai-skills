---
id: guided-tutorial
title: Guided tutorial
track: tutorial
tagline: a structured path through the curriculum, alternating conceptual foundations with practical exercises
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
      - {beat: first-look}
  - name: 5. Clean the data
    steps:
      - {concept: scoping-work}
      - {concept: verification}
      - {beat: profile-data}
      - {concept: steering}
      - {beat: plan-cleaning}
      - {beat: clean-data}
      - {concept: memory}
      - {beat: add-agents-md}
  - name: 6. Research analysis
    steps:
      - {concept: context}
      - {beat: build-cohort}
      - {beat: analyze-pilot}
      - {beat: review-with-second-agent}
      - {beat: saturday-hours}
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

The guided tutorial provides a structured, linear path through the entire workshop. By sequencing conceptual background alongside practical exercises, this track ensures you have the necessary context immediately before each hands-on task. While drawing from the same underlying material as the independent concept and demo tracks, this sequence organizes the workshop into a continuous progression with direct links back to the reference pages.

You can complete the workshop in a single session or across multiple sittings. Work from each stage is preserved as a restorable checkpoint, allowing you to pause, resume, or skip forward at any point ([Setup](../demo/setup.md#restore-a-starting-point)).

## Learning outcomes

By completing this tutorial, you will produce:

- A configured local agent environment with safe data-handling and credential practices.
- A reproducible data cleaning pipeline with an explicit audit trail of cleaning decisions.
- A statistical analysis featuring crude and adjusted estimates, independently reviewed by a second agent.
- A verified bibliography, an executive abstract with citations, and an interactive reporting dashboard.
- A reusable command-line tool and agent skill tracked in Git, alongside a bulk classification workflow using an external API.

## Prerequisites

- A computer with terminal access where you can install tools (or where an agent CLI is already configured). The initial step walks through setup.
- A dedicated working directory for workshop files.
- For the advanced section only: an active API key with a modest usage budget.

## Recommended approach

- **Review the concept page first**, then proceed to the demo exercise. Concept summaries are intentionally concise, providing the methodological grounding before you run commands.
- **Work through the benchmark dataset before using your own data.** The provided scenario includes known ground truth, making it straightforward to evaluate whether the agent's calculations are accurate before applying the patterns to novel data.
- **Adapt to your schedule.** Optional detours and advanced exercises are clearly labelled. If you have limited time, focus on the core "Full step" exercises listed in the [demo track](../demo/index.md).

## Contents

<!-- toc -->

## Track navigation

- Consult the [concept track](../concepts/index.md) for a modular reference covering core ideas independently of hands-on steps.
- Use the [demo track](../demo/index.md) to explore individual practical exercises or jump into specific checkpoints.
