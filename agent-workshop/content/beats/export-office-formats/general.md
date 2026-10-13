---
role: export-office-formats
title: Export to Word and Excel for collaborators
kind: detour
summary: Convert plain-text source files into DOCX and XLSX deliverables for external collaborators, auditing formatting trade-offs and preserving master text sources.
time: 6 min
teaches: [outputs, text-formats]
needs: [write-abstract]
---

While plain-text source formats are optimal for version control and automated execution, institutional collaborators frequently require deliverables formatted as Microsoft Word documents or Excel workbooks. In this exercise, you convert text source files into `.docx` and `.xlsx` artifacts, evaluate formatting fidelity, and manage version synchronization.

**Before you start:** Completed plain-text research outputs, such as a LaTeX or Markdown manuscript and a structured CSV dataset ([Setup](setup:restore-a-starting-point)).

## Background

Maintain master files in structured text formats ([Outputs](concept:outputs)) and execute office conversions at the boundary of your research pipeline. This boundary conversion pattern ensures master analytical scripts remain clean, diffable, and programmatically regenerable.

| Source format | Target deliverable | Conversion utility | Common structural translation compromises |
|---|---|---|---|
| **Markdown / LaTeX** | Microsoft Word (`.docx`) | `pandoc` | Fine typographic layouts and complex LaTeX tables are simplified; mathematical equations convert to native Word equations |
| **CSV / TSV** | Microsoft Excel (`.xlsx`) | `pandas`, `openpyxl` | Numerical data transfers cleanly; explicit column widths, header formatting, and frozen panes must be applied programmatically |

Edits made by collaborators directly inside Word or Excel files do not automatically synchronize back to plain-text source code. Establish a clear directional convention: designate plain-text files as the single source of truth, incorporating external editorial feedback back into master text files.

## General methodology

Direct the agent to compile the plain-text source files into office formats, inspecting the resulting documents to identify any structural changes introduced during translation:

```text
Convert <source document> into a Microsoft Word document (<out/manuscript.docx>) using pandoc, resolving citations against the bibliography.
Convert <data.csv> into an Excel workbook (<out/data.xlsx>), configuring explicit column widths, formatted header rows, and frozen top panes.
Inspect both generated files and provide an audit detailing any layout or structural modifications introduced during the conversion.
```

<!-- example -->

## Verification criteria

- **Direct visual inspection:** Open the generated `.docx` and `.xlsx` files in standard office software rather than relying solely on conversational confirmations.
- **Citation continuity:** In-text citation keys and the bibliography section resolved cleanly into formatted text within the Word document.
- **Type integrity in spreadsheets:** Numerical columns parse as numbers rather than text strings, and dates parse as valid datetime objects.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Citations display as unformatted keys (e.g., `[@author2024]`) | Pandoc executed without linking the local bibliography file | Ensure the conversion command includes `--bibliography=references.bib` |
| Numbers are left-aligned and fail to compute in formulas | Values were written to Excel as string primitives | Direct the agent to cast columns to numeric types in `openpyxl`/`pandas` prior to export |
