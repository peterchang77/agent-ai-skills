---
role: orient-in-folder
scenario: imaging
starts_from: the imaging kit copied into an empty folder
produces: nothing new; this step only reads
prompt: |
  What files and folders are in this folder? Describe each in one line, say how many files are in images/, and tell me which things you could not read as plain text.
---

**What you should see.** One folder, `images/`, holding 283 `.dcm` (DICOM) files, plus seven top-level files: `labels.csv`, `model_scores.csv`,
`radiology_reports.csv`, `radiology_reports_labeled_sample.csv`, `data_dictionary.md`, `radiology_notes.txt`, and `eval_protocol.docx`. The CSV, Markdown and
text files are readable directly. The agent should flag the `.dcm` files (they need a DICOM reader) and `eval_protocol.docx` (it needs a Word reader) as
needing special handling. The next steps deal with each.
