---
id: demo-track
title: Demo track
track: demo
tagline: one worked example, step by step, each step self-contained
sections:
  - name: Start
    steps:
      - {setup: true}
      - {beat: orient-in-folder}
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

Follow the story from raw files to a reviewed result. Every step says which starting state it needs, so you can
begin anywhere, and each step links to the concepts behind it.
