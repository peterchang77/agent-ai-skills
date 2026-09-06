# Contract: single-file annotation tool

## Functional requirements

- One portable `.html` file with inline CSS and JavaScript; no build step, server, CDN, or external analytics.
- A file picker accepts local `.json` or `.jsonl` records and reports parse errors clearly.
- Previous/next navigation shows progress and a stable transition identifier.
- Clearly separate prior impression, current impression, and LLM proposal.
- Permit a concept selection, proposed/reviewer state, decision (`agree`, `modify`, `reject`, `uncertain`), evidence quote, and optional notes.
- Include explicit abstain/not-enough-information choices; never require a clinical label.
- Export a JSON file containing the original transition ID, annotations, and export timestamp.
- Treat input/output as text, not HTML: escape report content to prevent injected markup.

## Quality requirements

Use semantic labels and keyboard-accessible controls. Explain the expected input shape in the page. Preserve existing annotations during navigation in the same browser session.

## Out of scope

Network requests, persistence to a server, account management, diagnosis, image display, or any claim that reviewer decisions establish ground truth.