---
id: what-code-can-do
title: What code makes possible
themes: [text-formats]
related: [agent-vs-chat, inputs, outputs, tools]
blurb: Coding agents use executable code as a universal interface for research tasks, making text-based source formats and programmatic scripts far more reliable than manual GUI interactions.
---

Because a coding agent operates through the command line and programming languages ([Agent vs. chat](concept:agent-vs-chat)), its reach matches the reach of software: virtually any analytical, computational, or document-processing task that can be defined programmatically. In research, code is not merely software development—it is the primary medium for executing and recording empirical work.

![An AI agent at the centre, connected through executable code to data analysis, research, media generation, voice outreach and system automation.](image:code-as-universal-interface)

## An intuitive analogy: code as an executable lab protocol

In physical laboratory science, no investigator would accept a published paper where the methods section states: *"I clicked around in a graphical spreadsheet, adjusted some sliders, and copied the resulting chart."* That process has zero verifiable provenance—it cannot be audited, and no colleague can reproduce it.

Instead, empirical science relies on explicit **laboratory protocols**: precise, step-by-step records documenting every reagent volume, incubation temperature, and measurement time. 

**Executable code is the digital equivalent of a laboratory protocol:**
- Every data transformation, filtering threshold, and statistical formula is written in human-readable text.
- Running the script reproduces the exact analytical output from raw records.
- Any colleague or peer reviewer can inspect the code to see exactly how variables were derived.

When an agent works through code, it does not leave behind ephemeral opinions—it leaves an auditable, executable protocol that belongs to you.

## Code as the universal computational adapter

Why is code such an effective medium for an agent? Because operating systems expose almost all computational capabilities through text-based programming interfaces:
- Filesystems are traversed with shell commands (`bash`).
- Data cleaning and modeling are executed with numerical libraries (`Python`, `R`).
- Relational databases are queried with structured syntax (`SQL`).
- Scientific typesetting is compiled from markup (`LaTeX`).

By writing and running code, the agent possesses a **universal adapter** to interact with files, calculate statistics, generate high-resolution figures, and compile publications without needing a human to click through software menus.

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

## Text formats as open blueprints vs. binary black boxes

Large language models process text tokens with high fidelity, reading, modifying, and generating structured source files with precision. Understanding the difference between text source formats and binary containers is critical:

- **Text formats (`.csv`, `.md`, `.tex`, `.json`):** Function like **open architectural blueprints**. Every character, formula, and table delimiter is transparent, diffable in Git, and directly inspectable by both human eyes and model tokens.
- **Binary office containers (`.xlsx`, `.docx`, `.pdf`):** Function like **sealed black boxes**. They pack data alongside styling engines, proprietary XML schemas, or fixed page coordinates. Reading them requires complex parsing libraries that can silently drop cell formulas, unalign table columns, or lose revision histories.

| Recommended source format | Formats to avoid during processing | Key advantages |
|---|---|---|
| **LaTeX, Markdown** | PDF, DOCX | Clear syntactic hierarchy; diffable across Git revisions |
| **CSV, TSV, Parquet** | XLSX, XLS | Predictable schema parsing without formatting interference |
| **HTML, SVG** | PPTX, Keynote | Programmatic layout control and clean vector scaling |
| **JSON, YAML** | Unstructured images/screenshots | Native key-value parsing without OCR errors |

Adopting text-first formats during active analysis does not mean abandoning Word or Excel for final delivery: execute analytical pipelines in text formats and convert to presentation formats at the boundary of the workflow ([Inputs](concept:inputs), [Outputs](concept:outputs)).

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

## Next step: who runs the code?

If an agent operates by proposing code, how does that code actually execute safely on your machine? What prevents an agent from running a destructive command, and who coordinates the feedback loop? 

In the next concept, [Harnesses and models](concept:harnesses), we deconstruct the system architecture: distinguishing the reasoning model from the software harness that manages your tools and enforces security boundaries.

## Demo it

<!-- demos -->
