# Agent context: 04 — Single-page abstraction review tool

## Assignment

Create one portable HTML file that lets a reviewer inspect a prior/current report pair and an optional LLM abstraction, record a review decision, and download annotations locally. First inspect the available abstraction output/schema and propose a minimal interaction design. Build the tool; do not build a general web platform.

## Scientific background

Reviewers need to compare the original prior/current impressions with a proposed report-derived weak label. A reviewer may agree, modify, reject, or mark the proposal uncertain. The interface must make uncertainty easy to capture and must not imply that either the LLM or reviewer establishes clinical ground truth.

## Available resources

- Input records should use a stable `transition_id`, `prior_impression`, `current_impression`, and optional LLM output from exercise 03.
- Develop using fabricated/approved sample content. Load real report content only inside the approved cloud environment.
- There is no need for a server, database, authentication, external library, or network call. Keep data local in the browser.

## Required outcome

Create a single `.html` file with inline CSS and JavaScript and no build step/CDN. A file picker must load local JSON or JSONL records and clearly report parse errors. Display stable ID/progress, prior impression, current impression, and LLM proposal as visibly distinct regions. Support previous/next navigation while retaining annotations in the current browser session.

The reviewer must be able to select a concept, select a state or explicit abstention/not-enough-information option, choose `agree`, `modify`, `reject`, or `uncertain`, record an evidence quote and optional notes, then download a JSON annotation file. Each exported item must retain its source transition ID and a timestamp. Escape report text when rendering: input text is not HTML.

Test using fabricated input, including HTML-like text, and validate the downloaded JSON with a standard parser.

## Boundaries

No network requests, upload, persistent server storage, user accounts, multi-user synchronization, image display, diagnosis, or clinical claims. Real review exports are protected derived data and must not be committed.

## Definition of a credible result

A reviewer can open the file directly in a browser, annotate several fabricated records without a server, navigate without losing edits, export valid JSON, and see that HTML-like report text is shown literally rather than executed/rendered.
