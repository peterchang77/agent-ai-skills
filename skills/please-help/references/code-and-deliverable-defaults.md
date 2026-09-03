# Code and Deliverable Defaults

Use existing project conventions first. These defaults apply only when a user needs a new approach and no stronger local convention exists.

## New code: Python and `uv`

For a simple new local coding request—automation, data cleanup, file processing, report generation, small analysis, or a utility—recommend Python. Manage a new Python project with `uv` and use a project-local `.venv`; do not modify global Python packages by default.

Before creating anything:

1. inspect for an existing language, `pyproject.toml`, environment, package manager, test setup, scripts, or project instructions;
2. reuse the established approach if one exists; and
3. explain the smallest useful setup in plain language.

Match the setup to recurrence:

| Situation | Recommended starting point |
| --- | --- |
| Small one-off task | Small script, explicit inputs/outputs, minimal dependencies, and a clear command to run it. |
| Reusable or multi-file task | `pyproject.toml`, `uv`-managed project-local `.venv`, a locked dependency set, relevant checks, and a documented run command. |
| Existing project | Use its current language, package manager, environment, test system, and layout unless there is a clear reason to change them. |

Do not install packages or update dependencies silently. First inspect what is declared and available. Explain why a package is needed and seek approval when installation materially changes the environment, adds a substantial dependency, creates cost/security concerns, or needs network access.

A concise recommendation to a new user can be:

> I recommend a small Python tool in its own project-local environment, so it does not change your system-wide Python setup. I’ll first check whether this project already has a preferred language or environment.

## Deliverables: start simple, then choose the format for the audience

Choose the simplest format that serves the intended reader and workflow. Do not treat a richer format as automatically better.

| Need | Recommended starting point | Why |
| --- | --- | --- |
| Notes, plans, technical documentation, drafts, handoffs | Markdown or plain text | Easy to inspect, revise, compare, and keep in Git. |
| Data table or calculation output | CSV/Excel-compatible data plus a concise Markdown explanation | Keeps data and narrative independently reviewable. |
| Formal fixed-layout report or print-ready document | Reviewable source first, then PDF | Preserves a simple editable source and gives stable distribution layout. |
| Equations, citations, controlled academic typesetting, established TeX workflow | LaTeX source, then PDF | Fits work that genuinely needs precise typesetting or an existing LaTeX pipeline. |
| Editable organizational document, comments, tracked changes, existing template | Word (`.docx`) | Fits collaborative business workflows and required templates. |
| Presentation | Text/Markdown outline first, then slides | Separates content decisions from visual design. |

Markdown or text is the normal default for a new draft. Use a PDF when fixed layout or printing matters. Use LaTeX because the work needs equations, citations, controlled typesetting, or an existing LaTeX workflow—not simply because someone wants a PDF. Use Word when the audience needs an editable Word document, tracked changes, comments, or an organizational template.

When practical, retain a simple source artifact and generate richer deliverables from it. Inspect existing templates and output conventions before choosing a format.

Ask only the format questions that matter:

> Who will use the result, and what do they need to do with it? Do they need an editable Word file, a fixed-layout PDF, or is a reviewable Markdown/text draft enough to start? Are there templates I should inspect?

If the user is unsure, recommend the lowest-friction route:

> I recommend starting with a Markdown draft so we can review the content and keep a clear history. We can produce a PDF or Word document once the audience and layout needs are clear.
