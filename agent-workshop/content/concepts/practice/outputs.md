---
id: outputs
title: Outputs — getting results out
short: Outputs
themes: [text-formats]
related: [inputs, verification, steering, secrets]
blurb: Request text-based source files and compile them to presentation formats. Source files are inspectable, version-controlled, and reproducible.
---

Working with a coding agent yields different types of output: text responses in the conversation, persistent files generated on disk, and external system actions. Structuring how these outputs are produced ensures that research findings remain verifiable, reproducible, and ready for publication.

## Categories of agent outputs

| Output category | Examples | Evaluation and governance |
|---|---|---|
| **Conversational responses** | Analytical summaries, code explanations, synthesis | Evaluate claims against empirical results ([Verification](concept:verification)) |
| **Durable file artifacts** | Analysis scripts, cleaned datasets, figures, manuscripts | Inspect file contents, check units, and verify table values |
| **Operations with external side effects** | Submitting network requests, executing paid API calls, deleting files | Require dry-run previews before granting execution approval ([Steering](concept:steering)) |

## The source-first compilation pattern

To ensure long-term reproducibility, instruct the agent to generate human-readable **source files** first, then compile those sources into final distribution formats.

| Target deliverable | Recommended source format | Compilation utility | Key reproducibility benefits |
|---|---|---|---|
| **Manuscript or report** | LaTeX (`.tex`) or Markdown (`.md`) | `pdflatex`, `pandoc` | Text source can be tracked in Git and re-compiled automatically |
| **Presentation / Slide deck** | Web presentation (HTML/CSS) | Any standard browser | Bypasses binary slide templates; inspectable layout code |
| **Tabular dataset** | CSV or Parquet | `pandas`, `polars` | Flat schema without hidden workbook formulas or styling artifacts |
| **Collaborative Word document** | Markdown source | `pandoc` | Clean text editing during analysis; export to DOCX for external review |
| **Interactive dashboard** | Standalone HTML/JS | Any standard browser | Fully portable visualization without requiring server hosting |

Adopting a source-first pattern ensures that any deliverable can be updated with a concise directive (e.g., *"update Figure 2 with 95% confidence intervals"*), allowing the agent to modify the source code and recompile the output automatically.

When collaborators require Word or Excel files, author the work in Markdown or CSV and perform the conversion as the final step. Keep in mind that converting between formats may not preserve proprietary features such as embedded spreadsheet macros or tracked changes.

## Output storage conventions

- **Isolate generated artifacts:** Direct all output files to dedicated directories (e.g., `out/`, `figures/`, `reports/`) to prevent overwriting raw inputs.
- **Maintain clear file naming conventions:** Use descriptive, standardized filenames that reflect the analysis stage and date.
- **Preserve script provenance:** Store the script that produced an artifact alongside the generated output so any collaborator can rerun the pipeline from scratch.

## Inspecting generated artifacts directly

A conversational confirmation from an agent (e.g., *"I have generated the regression table and plot"*) is not proof that the analysis is correct. Always open the generated figure, PDF, or dataset to verify:

- Axis ranges, labels, and measurement units match the underlying data.
- Sample sizes and degrees of freedom in tables match the cohort definitions.
- Outliers or missing data points are handled consistently with the research protocol.

## Managing side-effecting operations

Actions that modify remote infrastructure, incur financial charges, or delete files must be approached with care:

1. Require a **dry-run preview** detailing the exact files affected or API parameters called.
2. Verify that credentials are not printed into exported files or dashboards ([Secrets](concept:secrets)).
3. Grant approval only after verifying the intended action ([Steering](concept:steering)).

## Demo it

<!-- demos -->
