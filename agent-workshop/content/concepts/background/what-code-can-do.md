---
id: what-code-can-do
title: What code makes possible
themes: [text-formats]
related: [agent-vs-chat, inputs, outputs, tools]
blurb: Coding agents use executable code as a universal interface for research tasks, making text-based source formats and programmatic scripts far more reliable than manual GUI interactions.
---

Because a coding agent operates through the command line and programming languages ([Agent vs. chat](concept:agent-vs-chat)), its reach matches the reach of software: virtually any analytical, computational, or document-processing task that can be defined programmatically. In research, code is not merely software development—it is the primary medium for executing and recording empirical work.

![An AI agent at the centre, connected through executable code to data analysis, research, media generation, voice outreach and system automation.](image:code-as-universal-interface)

## Computational capabilities in research

| Research task | Programmatic action | Resulting research artifacts |
|---|---|---|
| **Data analysis** | Writes scripts to ingest, validate, and summarize raw records | Summary statistics, regression models, audit tables, and reproducible scripts |
| **Data visualization** | Renders publication plots using libraries like Matplotlib or Seaborn | Scalable vector graphics (SVG/PDF) and high-resolution raster figures |
| **Literature queries** | Interfaces with bibliographic APIs (e.g., PubMed, Crossref) | Structured query logs and validated BibTeX files |
| **Interactive reporting** | Compiles standalone dashboards using HTML, CSS, and JavaScript | Interactive visualization files viewable in any browser |
| **Document authoring** | Generates manuscripts in LaTeX or Markdown and compiles them | Publication-ready PDFs or reproducible document source files |
| **Web and API services** | Queries authenticated REST APIs or public databases | Raw responses parsed into structured tabular datasets |
| **Batch processing** | Loops across multi-gigabyte directories of records | Systematically cleaned, extracted, or normalized files |

Actions that publish data, incur financial costs, send external communications, or mutate sensitive infrastructure should always require explicit human approval ([Steering](concept:steering)).

## The advantage of text-based representations

Large language models process text tokens with high fidelity, reading, modifying, and generating structured source files with precision. In contrast, proprietary binary formats and visual documents require lossy conversion intermediaries that can drop structural metadata, formatting rules, or cell relationships.

| Recommended source format | Formats to avoid during processing | Key advantages |
|---|---|---|
| **LaTeX, Markdown** | PDF, DOCX | Clear syntactic hierarchy; diffable across revisions |
| **CSV, TSV, Parquet** | XLSX, XLS | Predictable schema parsing without formatting interference |
| **HTML, SVG** | PPTX, Keynote | Programmatic layout control and clean vector scaling |
| **JSON, YAML** | Unstructured images/screenshots | Native key-value parsing without OCR errors |

Adopting text-first formats during active analysis does not mean abandoning Word or Excel for final delivery: execute analytical pipelines in text formats and convert to presentation formats at the end of the workflow ([Inputs](concept:inputs), [Outputs](concept:outputs)).

## Programmatic code vs. graphical automation

Some AI systems interact with software visually by capturing screenshots and clicking virtual buttons ("computer use"). While visual automation is helpful when no programmatic interface exists, writing and running code provides distinct advantages for research:
- **Reproducibility:** A script can run again next month on new data with identical logic.
- **Inspectability:** Researchers can review the exact mathematical expressions and transformations applied.
- **Precision:** Refining an analysis requires only a concise clarification (e.g., *"adjust for patient age and clinic site"*), which the agent translates into precise code updates.

## Fundamental boundaries

Executable code automates operational steps, but cannot resolve methodological ambiguities:
- It cannot correct fundamentally biased or missing data.
- It cannot formulate a research hypothesis on its own.
- It cannot interpret the clinical or scientific meaning of an estimate; substantive interpretation remains the researcher's responsibility.

## Scoping task complexity

The scope of tasks an agent can solve autonomously continues to expand. The most dependable practice is to validate workflows on small, contained samples before running large pipelines ([Scoping work](concept:scoping-work)).

## Demo it

<!-- demos -->
