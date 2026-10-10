---
role: export-office-formats
title: Export to Word and Excel for collaborators
kind: detour
summary: Work in text formats, then convert last. See what survives the conversion to DOCX and XLSX.
time: 6 min
teaches: [outputs, text-formats]
needs: [write-abstract]
---

Colleagues often want Word or Excel. After this step you will know how to produce them from text sources, and what is lost in the conversion.

**Before you start:** a finished text-source output, such as a LaTeX or Markdown document and a CSV ([Setup](setup:restore-a-starting-point)).

## Background

Keep your master versions in text ([Outputs](concept:outputs)) and convert at the end, so the master can be regenerated and edited cleanly. Two common conversions:

| From | To | Tool | Expect to lose |
|---|---|---|---|
| Markdown or LaTeX | `.docx` | `pandoc` | Fine layout control; complex LaTeX (some tables, floats) simplifies |
| CSV | `.xlsx` | `pandas` and `openpyxl` | Nothing in the data; formatting and formulas have to be added deliberately |

Collaborators' edits made in Word or Excel do not flow back to your sources, so decide which copy is the master. Comments and tracked changes made in Word
can be read back (see the `docx` skill if installed), but it is easier to keep one direction of travel.

## General approach

```text
Convert <source> to a Word document <out/file.docx> using pandoc, with the bibliography. Convert <csv> to <out/file.xlsx> with a header row, column widths,
and a frozen header. Open each result and tell me what changed or was lost compared with the source.
```

<!-- example -->

## What to check

- Open both files in Word and Excel, not just the agent's description.
- Citations and the reference list survive in the Word document.
- Numbers in the spreadsheet are numbers, not text, and dates are dates.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| Citations appear as raw keys | The bibliography was not passed to pandoc | Add the bibliography option |
| Numbers left-aligned as text | Written as strings | Ask for numeric types |
