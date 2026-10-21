---
id: tutorial-clinical
title: Tutorial · Clinical
track: tutorial
scenario: toy
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

This guided tutorial provides a structured, linear path through the workshop on a clinical operations example: you direct a coding agent to clean multi-site clinic data, analyze a follow-up call pilot, and write up the result. By sequencing conceptual background alongside practical exercises, it ensures you have the necessary context immediately before each hands-on task, with direct links back to the reference pages.

You can complete it in one session or across several. Work from each stage is preserved as a restorable checkpoint, so you can pause, resume, or skip forward at any point ([Setup](setup.md#restore-a-starting-point)).

This is a synthetic example; nothing here is a finding about a real population.

## Learning outcomes

By completing this tutorial, you will produce:

- A configured local agent environment with safe data-handling and credential practices.
- A reproducible data cleaning pipeline with an explicit audit trail of cleaning decisions.
- A statistical analysis featuring crude and adjusted estimates, independently reviewed by a second agent.
- A verified bibliography, an executive abstract with citations, and an interactive reporting dashboard.
- A reusable command-line tool and agent skill tracked in Git, alongside a bulk classification workflow using an external API.

<!-- include: tutorial-common -->

## Contents

<!-- toc -->

## Track navigation

<!-- track-nav -->
