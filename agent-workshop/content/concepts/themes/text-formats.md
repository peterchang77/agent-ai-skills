---
id: text-formats
title: Theme — simple text formats win
short: Simple text formats win
blurb: Plain-text source formats maximize parsing accuracy and enable precise line-by-line editing and version control.
related: [what-code-can-do, inputs, outputs]
---

Because language models operate directly on tokenized text sequences, plain-text formats offer the highest processing fidelity and reliability across computational pipelines:

| Preferred text format | Formats to avoid during analysis | Key analytical advantages |
|---|---|---|
| **CSV / TSV** | Excel (`.xlsx`, `.xls`) | Transparent tabular structure without hidden workbook formulas, macros, or cell styles |
| **Markdown** | Word (`.docx`) | Human-readable markup; diffable in Git and converted cleanly via Pandoc |
| **LaTeX** | PDF | Inspectable mathematical markup that can be revised and re-compiled programmatically |
| **HTML / SVG** | PowerPoint (`.pptx`) | Standalone, interactive visualizations viewable in any browser without binary slide engines |

**Adopt a boundary conversion pattern:** Execute data transformations and authoring in structured plain-text formats, converting to presentation deliverables (DOCX, PDF, PPTX) at the boundary of your research pipeline ([Inputs](concept:inputs), [Outputs](concept:outputs), [What code makes possible](concept:what-code-can-do)).
