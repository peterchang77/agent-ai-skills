---
name: single-page-web
description: Create a reviewable standalone HTML page for small dashboards, data views, analysis, annotation, or project summaries, and choose a fuller web platform only when its operational needs justify one.
---

# Single-Page Web

Use this skill when a user needs a quick, local, inspectable interface for a summary, dashboard, spreadsheet/data view, analysis result, annotation task, or project status page. Default to one standalone HTML file with inline CSS and JavaScript when it can meet the need. It is easy to share locally, archive with an analysis run, open on a headless machine through a simple server, and inspect without a build system.

Do not assume a web platform is better merely because the result is interactive. Read [choosing a web shape](references/choosing-a-web-shape.md) when deciding whether a single page is sufficient.

## Decide the smallest useful interface

Before building, establish only what changes the design:

- Who will use it, for what decision or task, and how many people need access?
- Is it a temporary/local artifact, a recurring internal workflow, or a public tool expected to grow?
- What data may appear, where will it come from, and may it leave the machine or be embedded in the page?
- Does the user need local interaction only, downloadable results, durable shared annotations, authentication, or multi-user coordination?

Inspect existing project tools, examples, data size, templates, and output conventions first. Reuse them when they meet the need.

## Default: a standalone page

For a one-off or small-user workflow, create a single `*.html` page with:

- semantic HTML, a useful title, a viewport tag, and a clear visible purpose;
- inline CSS sized for desktop and narrow screens;
- inline JavaScript only for the interaction actually needed (filtering, sorting, navigation, chart controls, image adjustments, or local annotation);
- an explicit data/provenance note, generated timestamp when relevant, and interpretation limits;
- clear empty, loading, error, and no-results states where applicable; and
- a separate named output path that does not overwrite source material.

Prefer simple tables, summaries, filters, and native browser controls over a framework or a custom component system. Keep the page usable without network access whenever practical. For a fully self-contained artifact, embed small approved data/assets; do not embed large, private, sensitive, or routinely changing data merely for convenience.

When dynamic text comes from files, users, or data, avoid string-built HTML. Insert it with DOM APIs such as `textContent`, or properly escape it. Treat a page containing data or annotations as an artifact with its own privacy and retention boundary.

## Annotation and review pages

A standalone page can support local review well: render the material, collect structured fields, save temporary work in browser storage if appropriate, and offer an explicit JSON/CSV download for the reviewer to hand back.

Be explicit about what is and is not durable:

- browser storage is local to one browser/profile and can be cleared;
- downloading an export is not the same as shared submission or audit storage;
- multi-user assignments, shared state, access control, conflict handling, or authoritative records require a designed backend/workflow.

Never silently upload annotations or data. Preserve source material, use separate derived outputs, and require approval before external services, credentials, or sensitive material are involved.

## View on a headless machine

For local or remote inspection, use Python's built-in static server; it requires no new dependency. From the directory containing the page or artifacts:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/` in a browser on that machine. It also provides a quick directory listing for HTML, Markdown, images, CSV files, and other artifacts; Markdown is served as the raw file, not rendered as a documentation site.

On a remote headless machine, keep the server bound to loopback and tunnel it from the viewing machine:

```bash
ssh -L 8000:127.0.0.1:8000 <user>@<remote-host>
```

Then open `http://127.0.0.1:8000/` locally. Read [headless serving](references/headless-serving.md) before changing the bind address or serving sensitive content.

## Validate and hand off

Open the page in a browser or headless browser when available. Check representative narrow and wide layouts, controls, keyboard use, data counts/labels, empty/error states, and download behavior. Confirm that displayed summaries match the source and that no protected data or secrets are embedded or staged for Git.

Report the output path, source/provenance, interaction and persistence limits, checks performed, and the command for local viewing. If the page no longer fits the single-page boundary, explain why and propose the smallest platform route rather than growing an accidental application.
