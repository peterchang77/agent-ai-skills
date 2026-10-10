---
role: build-dashboard
title: Build a dashboard as a single web page
kind: full
summary: Ask for one self-contained HTML file with charts and tables. It opens in any browser, needs no software, and can be regenerated from the data.
time: 7 min
teaches: [outputs, tools]
needs: [clean-data]
---

After this step you will be able to turn a dataset into an interactive-looking dashboard in one HTML file, with a generating script, that you can open
in any browser and share (if the data may be shared).

**Before you start:** cleaned data, and a clear idea of the two or three questions the dashboard should answer ([Setup](setup:restore-a-starting-point)).

## Background

A web page is a text file the agent can write well, and it replaces slides and spreadsheets for many purposes ([Outputs](concept:outputs)). Decide in
advance:

- **Self-contained.** One file with the data and chart code inside, so it works offline and cannot fetch anything from the network. This is also safer for sensitive data.
- **Generated.** A script reads the data and writes the page, so it can be regenerated next month ([Tools](concept:tools)).
- **Shareable only if the data may be shared.** Embedding patient-level data in a page you send around is a privacy decision ([Privacy](concept:privacy)). Prefer aggregated numbers in anything you distribute.

## General approach

```text
Write scripts/make_dashboard.py that reads <clean data> and writes out/dashboard.html: a single self-contained page (no external
network requests) with <the two or three charts or tables>. Use aggregated numbers only, not patient-level rows. Label axes and units,
and show the number of records behind each chart. Open question: tell me which parts you chose and why.
```

Open the file in your browser and look at it. Then iterate in plain language: "make Riverside's bar red", "add the target line".

<!-- example -->

## What to check

- The file has no external links (search it for `http`).
- Chart values match numbers you can reproduce from the data.
- Every chart has labelled axes, units, and a count.
- It contains only aggregated data.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| Blank charts | A charting library failed to load | Ask for a version with no external dependencies |
| Numbers differ from your analysis | The dashboard used raw instead of cleaned data | Point it at the cleaned file |
