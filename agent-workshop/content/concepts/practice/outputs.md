---
id: outputs
title: Outputs — getting results out
short: Outputs
themes: [text-formats]
related: [inputs, verification, steering, secrets]
blurb: Ask for a text-based source file, then render it. The source is editable, diffable, and regenerable; the rendered file is just a view.
---

## Three kinds of output

| Kind | Example | Care needed |
|---|---|---|
| An answer in the conversation | A summary or an explanation | Check it ([Verification](concept:verification)) |
| Files | A report, a figure, a cleaned dataset | Review the artifact itself |
| Actions with side effects | Sending an email, publishing a page, calling a paid API, deleting files | Preview first, then explicit approval ([Steering](concept:steering)) |

## Ask for the source, then render it

Have the agent write the **text source**, and render that to the format you need.

| You want | Ask for the source | Rendered with |
|---|---|---|
| A PDF report | LaTeX (`.tex`) or Markdown | `pdflatex`, `pandoc` |
| A slide deck | A web page (HTML) | any browser |
| A spreadsheet | CSV (or XLSX if required) | `pandas`, `openpyxl` |
| A Word document | Markdown, then convert | `pandoc`, `python-docx` |
| A dashboard | A single-page website | any browser |
| A shared document | A structured document pushed through the service's API | the service (needs credentials) |

Why this works: a `.tex` or `.html` file can be reviewed as text, kept in version control, regenerated from new
data, and fixed with one sentence ("make the table narrower"). A hand-built file cannot. For presentations, prefer a website over PowerPoint.

When a collaborator needs Word or Excel, work in Markdown or CSV and **convert last**. Expect to lose some features
(comments, tracked changes, formulas) on the way.

## Where outputs go

- Write to a separate folder such as `out/`. Never overwrite inputs.
- Use predictable names so later steps can find them.
- Keep the **script that produced** a file next to it, so the output can be regenerated.

## Review the artifact, not the transcript

Open the PDF, the figure, or the web page and look at it. "The agent said it made a chart" is not evidence that the chart is right. Check axes, labels, units, and a few values against the data.

## Websites as outputs

A single HTML file is an excellent output: it needs no software to view, can hold charts and tables, and works as a
dashboard. Opening the file locally is safe; before you share one, check that it contains no sensitive data or credentials ([Privacy](concept:privacy)).

## Actions with side effects

Anything that sends, publishes, spends money, or deletes should be a **draft first**: ask the agent to show exactly
what it will do, approve it, and only then run it. Never put credentials in the output ([Secrets](concept:secrets)).

## Demo it

<!-- demos -->
