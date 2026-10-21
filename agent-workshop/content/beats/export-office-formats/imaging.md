---
role: export-office-formats
scenario: imaging
starts_from: the `reported` checkpoint
produces: "`out/abstract.docx`, `out/cohort.xlsx`"
prompt: |
  Convert out/abstract.tex to out/abstract.docx using pandoc with references.bib as the bibliography (citeproc). Convert out/cohort.csv to
  out/cohort.xlsx with a header row, sensible column widths and a frozen header row. Open each result and tell me what changed or was lost compared
  with the source.
---

**Files used:** `out/abstract.tex`, `references.bib`, `out/cohort.csv`.

**What you should see.** The Word file keeps the section headings, the results table, and citations rendered as numbers or author-year with a reference list. LaTeX layout details (margins, the table style) are replaced by Word defaults. The spreadsheet contains 203 rows,
one per patient, with numeric age and score columns.

**Note.** `references.bib` sits at the project root while the abstract is in `out/`; the agent may need to pass the path to pandoc. If it fails, show it the error. Also consider whether the cohort file should leave the project at all: it holds a patient ID per row ([Privacy](concept:privacy)).
