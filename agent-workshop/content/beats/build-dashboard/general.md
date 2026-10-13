---
role: build-dashboard
title: Build a dashboard as a single web page
kind: full
summary: Compile an interactive, self-contained HTML research dashboard displaying aggregated metrics and audit counts without external runtime dependencies.
time: 7 min
teaches: [outputs, tools]
needs: [clean-data]
---

In this exercise, you direct the agent to develop a standalone, interactive research dashboard packaged as a single self-contained HTML file (`out/dashboard.html`). Paired with a reproducible generator script, this web-based asset can be inspected in any browser without requiring external server infrastructure.

**Before you start:** Cleaned data and a clear specification of the analytical questions and figures the dashboard should present ([Setup](setup:restore-a-starting-point)).

## Background

Web pages authored in plain HTML, CSS, and JavaScript represent an exceptional medium for research dissemination, often replacing static slide decks and complex spreadsheet workbooks ([Outputs](concept:outputs)).

A robust research dashboard embodies three design requirements:

- **Self-contained execution:** The HTML file embeds all necessary CSS, JavaScript, and aggregated data inline, operating entirely offline without making external CDN requests. This self-contained architecture enhances security and prevents tracking.
- **Programmatic reproducibility:** A dedicated Python script (`scripts/make_dashboard.py`) processes the dataset and compiles the HTML output, ensuring the dashboard can be regenerated whenever data is updated ([Tools](concept:tools)).
- **Aggregate data privacy:** Dashboards intended for dissemination must display only aggregated summary statistics, stratified rates, and cell counts—never embedding row-level patient or participant records ([Privacy and data handling](concept:privacy)).

## General methodology

Instruct the agent to write a generator script that ingests the cleaned dataset and compiles the self-contained dashboard:

```text
Write a reproducible generator script, scripts/make_dashboard.py, that reads <clean data> and outputs out/dashboard.html.
The dashboard must be a single, self-contained HTML file (making zero external network requests) featuring <specified figures or tables>.
Embed aggregated summary metrics only; do not include row-level patient records.
Ensure all chart axes and measurement units are explicitly labeled, and display the underlying sample sizes supporting each visualization.
Provide an overview explaining your choice of visualization components and layout hierarchy.
```

Open the generated file in your browser to inspect visual formatting, then refine elements using conversational directives (e.g., *"highlight clinic site B in contrasting blue"*, *"add horizontal benchmark target lines"*).

<!-- example -->

## Verification criteria

- **Zero external dependencies:** The HTML file makes no outbound network connections (verified by searching file contents for external `http://` or `https://` script tags).
- **Metric fidelity:** Plotted values and table figures match empirical numbers derived from the cleaned dataset.
- **Complete axis annotation:** Every figure displays explicit axis labels, measurement units, and supporting sample counts.
- **Privacy preservation:** The underlying HTML source contains strictly aggregated metrics, with zero identifiable row-level data.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Visualizations render as blank elements | External CDN charting libraries failed to load due to offline execution | Direct the agent to use inline SVG or embed a lightweight, self-contained charting script inline |
| Dashboard numbers diverge from statistical models | The generator script accidentally ingested raw uncleaned data rather than the cleaned dataset | Update the generator script to ingest exclusively from `data/clean/` |
