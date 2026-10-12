---
id: inputs
title: Inputs — getting information to the agent
short: Inputs
themes: [text-formats]
related: [outputs, context, privacy, secrets, verification]
blurb: Everything the agent sees arrives as text. Choose the route and the format that keep as much structure as possible.
---

An agent can only work with what it can read, and it reads **text**. Choose how to hand something over based on the file type. For how to read specific file types, see [Read spreadsheets, documents, and PDFs](beat:read-office-formats).

## Routes

| Route | How | Good for | Notes |
|---|---|---|---|
| Paste | Copy text into the prompt | A few lines: an error message, a snippet | Tables lose their columns when pasted |
| Local file | Put it in the project folder and name it | Most work | The default choice |
| Website | Give a URL | Reference pages, public data | Save a local copy if you need to reproduce it |
| API | Give the agent an endpoint and a key | Live or large data | See below |
| Database | Give the agent a connection and a password | Structured records | See below |

**Rule of thumb:** paste a few lines; use a file for anything structured.

### APIs and databases

An agent is usually good at figuring out an interface from its documentation. Often the easiest start is simply to
give it the **endpoint URL and an API key** (or the **database URL and a password**) and ask it to explore what is
available. Two cautions: use a limited or read-only credential to begin with, and read [Secrets](concept:secrets)
before you paste anything sensitive. If the work has to be reproducible, ask the agent to save what it retrieved
(or the query that produced it) in the project.

## The format ladder

| Best: plain text | Fine: needs a library | Lossy: convert first |
|---|---|---|
| `.txt`, `.md`, `.csv`, `.json`, `.tex`, `.html` | `.xlsx`, `.docx` | scanned PDFs and images; `.pptx` |

Between those, **PDF** needs a distinction:

- A PDF with an **embedded text layer** (most PDFs) can have its text extracted, though tables and columns may come out jumbled.
- A **scanned PDF** is only pictures of pages. It has no text until it goes through OCR (optical character recognition), which is slower and makes mistakes.

If you have a choice, ask for the text version at the source: export Excel to CSV, Word to Markdown, slides to a web page. Conversion silently drops structure such as merged cells, tracked changes, footnotes, and table layout. See [what code makes possible](concept:what-code-can-do) for the wider rule.

## Dependencies are normal

Reading `.xlsx` or `.docx` needs a library; reading a PDF needs a text-extraction tool. Let the agent install what it
needs inside the project ([Environment](concept:environment)). Tell it *which file* you care about, not which library to use.

## Keep inputs organised

- Keep original files in one place (for example `data/raw/`) and **never modify them**; write results elsewhere.
- Put a **data dictionary** next to the data, saying what each column means and its units.
- For large files, do not ask the agent to read everything. Have it inspect the structure and a sample, then **process with code** and report ([Context](concept:context)).

## Before you hand it over

Check that the data is allowed to go to the model you are using ([Privacy](concept:privacy)).

## Common mistakes

- Pasting a table from a PDF or a web page and trusting the columns.
- Assuming the agent read all of a large file. Ask what it actually opened.
- Leaving out the data dictionary, so the agent guesses what columns mean.

## Demo it

<!-- demos -->
