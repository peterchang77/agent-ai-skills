# Choosing a Web Shape

Choose the smallest approach that meets the real use case. Inspect the repository first; an established, appropriate project stack outweighs these defaults.

## Prefer one standalone HTML file

Use a single self-contained page when the goal is quick testing, a temporary or local dashboard, a project summary, a data/analysis viewer, a small review or annotation task, or a result that one person or a few trusted users will open directly.

It is especially effective when the page can be generated from a script, kept with an analysis artifact, opened offline, or served from a headless machine without installing a web stack.

A single page is still a good choice when it has modest interaction: filters, sortable tables, charts, image controls, section navigation, a small form, browser-local drafts, and explicit export downloads.

## Use a fuller platform deliberately

Recommend a maintained application/platform when one or more of these are core requirements:

- a public-facing product expected to grow over time;
- many users, user accounts, permissions, authentication, or sensitive-access controls;
- authoritative shared state, server-side submission, audit trails, or multi-user annotation and conflict handling;
- a large or frequently changing dataset that should not be embedded or loaded into the browser at once;
- durable APIs, background jobs, scheduled refreshes, notifications, payments, or integrations;
- complex multi-page navigation, reusable components, or an established organization-wide frontend/backend stack; or
- reliable deployment, monitoring, backups, accessibility review, and security ownership beyond an ad hoc local tool.

Do not jump straight to a framework. First say which requirement makes a platform necessary, what operational responsibilities it adds, and whether a static prototype can reduce uncertainty. A static single-page prototype often clarifies the workflow before backend commitments are made.

## Data and output choices

| Situation | Starting choice |
| --- | --- |
| Small approved data, portable report, offline use | Embed data/assets in a standalone page if size and sensitivity allow. |
| Local files likely to change during exploration | Keep data separate and generate/rebuild the HTML from a script. |
| Large tables, images, or sensitive material | Keep data out of the page where possible; use controlled local storage/access and avoid public hosting. |
| One reviewer, no central record required | Local browser state plus an explicit downloaded JSON/CSV export can be enough. |
| Shared review, durable record, or access control | Design a backend and governance workflow; a page alone is insufficient. |

## Practical examples

- A data scientist needs to inspect summary metrics and a few plots from one run: generate one HTML report.
- A team needs a temporary visual review of a small selected sample: generate a local standalone review page and export annotations explicitly.
- A user needs to browse a remote project directory, Markdown notes, or generated reports: run a loopback-only Python static server and use an SSH tunnel.
- A repository’s central purpose is a public data exploration tool with growing users and datasets: prototype the views if useful, then use the project’s supported web platform with deployment, authentication, and operations planned from the start.
