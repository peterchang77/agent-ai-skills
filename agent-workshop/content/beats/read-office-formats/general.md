---
role: read-office-formats
title: Read spreadsheets, documents, and PDFs
kind: full
summary: The same request works for XLSX, DOCX, and PDF. The agent installs a reader and converts to text first, and each format loses something different.
time: 7 min
teaches: [inputs]
needs: [orient-in-folder, prepare-environment]
---

Spreadsheets, Word documents, and PDFs are the formats most people already have, but they are not plain text. After this step
you will be able to get any of the three read reliably, know what each conversion tends to lose, and know when to ask for a text
version instead. This matters because everything an agent works from arrives as text: if structure such as a table or a merged
cell is lost in conversion, the answer can be wrong without any visible error.

**Before you start:** a project folder containing the files you want read, with your agent started inside it ([Setup](setup:)).

## Background

An agent cannot look at a file the way you do. It runs a program that extracts text and then reads that output. The quality of the
answer depends on that extraction step.

| Format | What is inside | Typical reader | What is often lost or confusing |
|---|---|---|---|
| `.xlsx` | Cells in one or more sheets, plus formatting | `openpyxl`, `pandas` | Title rows above the header, merged cells, hidden sheets, formulas vs. values |
| `.docx` | Paragraphs with styles, tables, comments | `python-docx`, `pandoc` | Tracked changes, comments, text boxes, table layout |
| `.pdf` with text | Positioned text | `pdftotext` | Column order, tables, footnotes |
| `.pdf` scanned | Only images of pages | OCR (for example `ocrmypdf`) | Everything, until OCR; OCR then makes its own mistakes |

You do not need to choose the tool. Name the file and the task, and the agent picks a reader and installs it if needed
([Environment](concept:environment)). For the wider picture of input routes and the format ladder, see [Inputs](concept:inputs).

## General approach

A prompt that works for any of these formats:

```text
Read <file>. Tell me which tool you used and anything that was hard or lossy to extract (merged cells, tables, images, scanned
pages). Then <what you actually want>.
```

Asking for the tool and the problems in the same prompt as the task keeps the extraction step visible. If the result will be
reused, add: "Save a plain-text version in `text/` (CSV for spreadsheets, Markdown for documents)." Reading the converted
file is faster and more reliable than parsing the original every time.

What the agent will typically run (you do not have to write this, but it helps to recognise it):

```python
# XLSX: look at every sheet and the merged ranges before assuming a header row
from openpyxl import load_workbook
wb = load_workbook("file.xlsx", data_only=True)        # data_only: stored values, not formulas
for ws in wb.worksheets:
    print(ws.title, ws.dimensions, ws.merged_cells.ranges)
    for row in ws.iter_rows(values_only=True):
        print(row)
```

```python
# DOCX: paragraphs (with style names) and tables are stored separately
from docx import Document
doc = Document("file.docx")
for p in doc.paragraphs:
    print(p.style.name, "|", p.text)
for table in doc.tables:
    for row in table.rows:
        print([cell.text for cell in row.cells])
```

```bash
# PDF: -layout keeps columns in reading order better; "-" prints to the terminal
pdftotext -layout file.pdf -
# Word to Markdown in one line:
pandoc file.docx -t markdown
```

<!-- example -->

## What to check

- The agent named the tool it used for each file.
- It noticed structure problems (a title row, merged cells, a table) rather than treating row 1 as the header.
- Numbers in its answer match what you see when you open the original file yourself.
- Every sheet was read, not only the first.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| "Module not found" or a missing command | Reader not installed | Let the agent install it in the project environment |
| PDF extraction returns nothing | Scanned PDF: no text layer | Ask for OCR, or get the source file |
| Table columns run together | PDF layout lost | Retry with `-layout`, or ask for the original `.docx` or `.xlsx` |
| Wrong numbers from a spreadsheet | A formula read as empty, or the wrong header row | Ask it to show the first 10 raw rows and the header it chose |
