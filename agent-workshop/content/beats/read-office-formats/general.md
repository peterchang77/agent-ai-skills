---
role: read-office-formats
title: Read spreadsheets, documents, and PDFs
kind: full
summary: Ingest XLSX, DOCX, and PDF containers, auditing structural extraction compromises such as merged cells, table boundaries, and OCR artifacts.
time: 7 min
teaches: [inputs]
needs: [orient-in-folder, prepare-environment]
---

Spreadsheets, Word documents, and PDFs are ubiquitous across research institutions, but they represent compound binary or presentation formats rather than plain text. In this exercise, you direct the agent to extract information from all three formats, audit the structural compromises inherent in each extraction pipeline, and evaluate when converting to plain text at the source is preferable.

Understanding parsing trade-offs is essential: because language models operate strictly on extracted text streams, any table misalignment or merged-cell distortion introduced during extraction can produce silent calculation errors.

**Before you start:** A project directory containing office or PDF files, with an active agent session ([Setup](setup:)).

## Background

An agent cannot inspect visual layouts directly in a terminal. It executes specialized parsing programs to convert binary files into raw text strings before evaluating them. The reliability of subsequent analyses depends directly on this conversion step.

| Format | Internal structure | Standard extraction utility | Common parsing vulnerabilities |
|---|---|---|---|
| **`.xlsx`** | Multi-sheet XML cells, formulas, formatting | `openpyxl`, `pandas` | Unhandled title blocks above headers, merged cell ranges, hidden sheets, formula strings vs. evaluated values |
| **`.docx`** | Paragraph trees, style runs, embedded tables | `python-docx`, `pandoc` | Tracked changes, margin comments, floating callout boxes, nested tables |
| **`.pdf` (Digital)** | Explicit 2D glyph coordinates | `pdftotext`, `pypdf` | Disrupted multi-column reading order, unaligned table columns, fragmented footnotes |
| **`.pdf` (Scanned)** | High-resolution raster images | OCR tools (e.g., `ocrmypdf`, `tesseract`) | Character recognition noise, table structure erasure, high compute latency |

You do not need to manually research extraction utilities. State the target file and research question; the agent will select and install the necessary libraries within the project environment ([Environment](concept:environment)). For the broader representation hierarchy, consult [Inputs](concept:inputs).

## General methodology

Use a prompt pattern that couples the extraction task with an explicit structural audit:

```text
Inspect <file>. Report the extraction utility used and flag any structural complexities or lossy conversions (e.g., merged cells, multi-column layouts, images, or scanned pages).
Then address the following analytical objective: <objective>.
```

Requiring the agent to declare its extraction tool and report structural anomalies ensures potential parsing errors remain transparent. When data will be analyzed repeatedly across a project, instruct the agent to export an intermediate plain-text snapshot to a `text/` directory (CSV for tabular sheets, Markdown for text documents). Reading structured plain text is faster, cheaper, and more dependable than re-parsing binary containers on every turn.

Representative scripts executed by the agent (for reference):

```python
# XLSX: Audit sheet names, dimensions, and merged cells before assuming header locations
from openpyxl import load_workbook
wb = load_workbook("file.xlsx", data_only=True)  # data_only evaluates formulas to stored numbers
for ws in wb.worksheets:
    print(ws.title, ws.dimensions, ws.merged_cells.ranges)
    for row in ws.iter_rows(values_only=True):
        print(row)
```

```python
# DOCX: Extract paragraphs and tabular cell matrices separately
from docx import Document
doc = Document("file.docx")
for p in doc.paragraphs:
    print(p.style.name, "|", p.text)
for table in doc.tables:
    for row in table.rows:
        print([cell.text for cell in row.cells])
```

```bash
# PDF: Extract positioned text preserving layout order
pdftotext -layout file.pdf -

# DOCX to Markdown conversion using Pandoc
pandoc file.docx -t markdown
```

<!-- example -->

## Verification criteria

- **Declared extraction tool:** The agent explicitly identifies the parser or command line utility used to read the file.
- **Structural anomaly audit:** The agent flags layout irregularities (such as descriptive banner rows above column headers or merged cell spans) rather than blindly assuming row 1 represents column headers.
- **Numerical consistency:** Extracted values match the underlying cells when inspected in standard spreadsheet software.
- **Comprehensive sheet coverage:** For multi-sheet workbooks, the agent verifies each relevant worksheet rather than inspecting only the default sheet.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| `"ModuleNotFoundError"` during script execution | Parser library is not installed in the virtual environment | Authorize the agent to install the missing package via `uv` |
| PDF extraction returns empty output | Document is a scanned image lacking a digital text layer | Instruct the agent to run an OCR pipeline or obtain the digital source file |
| Table columns merge into unaligned text | Complex multi-column layout parsed linearly | Re-run `pdftotext` with the `-layout` flag, or export the original table to CSV |
| Erroneous spreadsheet totals | Formulas read as null, or header rows offset | Instruct the agent to print the first 10 raw rows and explicitly verify the active header offset |
