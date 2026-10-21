---
role: review-images
title: Build a viewer and review the flagged images
kind: full
summary: Have the agent flag suspect images with code, build a small offline viewer, and confirm or reject each flag yourself before anything is changed.
time: 10 min
teaches: [verification, tools, privacy]
needs: [profile-data]
---

Some problems in image data cannot be found by code alone. Here you split the work: the agent flags candidates with measurable checks and builds a tool that lets a person review them, and **you** make the call. Only reviewed items are acted on later.

**Before you start:** A profile of the images, with the problems code could find ([Profile the data](beat:profile-data)).

## Background

Code can check metadata exhaustively and can check some pixel properties (size, brightness patterns, exact duplicates). It cannot reliably tell that a picture is mirrored, or that a picture is inverted when the file claims it is not. Those need a person looking. This is a **human-in-the-loop** pattern: the machine narrows hundreds of images to a handful, a person confirms them, and the decision is recorded in a file the agent reads back ([Verification](concept:verification)).

The viewer is a good first **tool** to build with an agent ([Tools](concept:tools)): small, offline, and reusable. A self-contained HTML page works on any machine with a browser and sends nothing over a network, which also matters for privacy: patient details can sit in the pixels as well as the header ([Privacy](concept:privacy)).

## General methodology

Ask for flags with a stated reason for each, then a viewer, then record your decisions and let the agent read them back:

```text
Write a script that scans <folder> and flags images that look wrong, writing <out/flags.csv> with columns file and flag (one row per flag). Use measurable checks
and say what each flag means. Then write a second script that builds one self-contained, offline HTML page showing a thumbnail for every image, a filter by flag,
a larger view with the header on click, and confirm / reject / unsure buttons that can be exported as <out/review.csv>. Do not embed any labels or model results.
Tell me how to open it.
```

Open the page, review the flagged images, then use the export button to save `review.csv`. Tell the agent where it is. Do not let the agent decide for you which flags are real.

<!-- example -->

## Verification criteria

- **Every flag has a reason** and a count, and the agent reports flags it could not test.
- **The page is offline and self-contained** (no web requests). Check the file for `http` links.
- **No answers in the page.** Labels, scores and other results are absent, so your review is not biased by them.
- **Decisions come from you.** The agent uses `review.csv` as given and reports any flag you left unreviewed.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| The page is very large or slow | Full-size images were embedded | Ask for downsampled thumbnails and a larger view at moderate size |
| Flags are trusted without review | The agent acted on its own detector | Insist: *"Only act on items I confirmed in review.csv"* |
| A problem was never flagged | No check can see it | Scan the whole sheet yourself; this step exists because code cannot find everything |
