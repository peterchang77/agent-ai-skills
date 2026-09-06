# Instructor answer key — 04 Annotation tool

## Teaching point

Agents can create bespoke research tools quickly when the scope is narrow. A single self-contained HTML file is inspectable, portable, and adequate for a local review workflow.

## Suggested live flow

1. Ask participants to request a minimal design proposal before coding.
2. Discuss the indispensable review distinctions: prior/current source text, LLM proposal, reviewer decision, uncertainty.
3. Have the agent build one file and open it directly in a browser.
4. Load fabricated JSON/JSONL; include an HTML-like report string to test safe rendering.
5. Navigate, annotate, export, and validate the JSON.

## Expected artifact and evidence

- One HTML file, inline JS/CSS, no server/build/CDN/network request.
- Local file loader; source ID/progress; separate report/proposal views; in-session retained edits.
- Concept/state/decision/evidence/notes and explicit uncertain path; local JSON export with source IDs/timestamp.
- Literal rendering of HTML-like input and valid parseable export.

## Reference prompt

> Read the context and propose a minimal local review interaction. Build one self-contained no-network HTML file that imports selected local JSON/JSONL, safely displays report text/proposal, navigates records while retaining edits, captures review/uncertainty/evidence/notes, and exports annotations keyed by transition ID. Test fabricated HTML-like input and parse the export. Do not add upload, database, accounts, synchronization, diagnosis, or frameworks.

## Common errors and steering

- **Starts React/Vite/server:** restate no build/server and require a portable one-file artifact.
- **Uses `innerHTML`:** require text-node/`textContent` rendering and injection fixture test.
- **Forces label:** add abstain/not-enough-information and uncertain decision.
- **Forgets source ID/provenance:** require in every export record.
- **Adds backend:** stop; the teaching goal is local inspectability.

## Reference materials

The prior repository revision includes an optional single-file `review-tool.html` reference. Keep it in the instructor presentation workspace, not the participant mount before their attempt.
