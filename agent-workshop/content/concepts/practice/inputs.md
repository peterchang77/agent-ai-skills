---
id: inputs
title: Inputs — getting information to the agent
short: Inputs
themes: [text-formats]
related: [outputs, context, privacy, secrets, verification]
blurb: Language models process information as text. Selecting appropriate ingestion pathways and source formats preserves data structure and prevents extraction errors.
---

An agent operates strictly on the data provided to its context window or accessible via its environment tools. Because language models process sequences of text tokens, how information is formatted directly determines parsing accuracy and analytical fidelity. For practical exercises reading diverse formats, see [Read spreadsheets, documents, and PDFs](beat:read-office-formats).

## Data ingestion pathways

| Ingestion pathway | Mechanism | Optimal use case | Key considerations |
|---|---|---|---|
| **Prompt insertion** | Pasting snippets directly into the prompt | Brief error logs, short configuration snippets | Tabular columns often lose alignment; fills context quickly |
| **Local filesystem** | Placing files within the project working tree | Primary empirical data files, source code, protocols | Standard approach; preserves file structure and relative paths |
| **Web retrieval** | Providing a URL for HTTP fetching | Public documentation, regulatory guidance, preprints | Archive retrieved copies locally to maintain computational reproducibility |
| **REST APIs** | Providing an endpoint URL and scoped credential | Live data feeds, dynamic queries, bulk records | Store credentials securely ([Secrets](concept:secrets)); record API query parameters |
| **Databases** | Providing a connection string or SQL client | Enterprise data warehouses, relational records | Use read-only credentials; persist query extracts to disk for reproducibility |

**General guideline:** Paste short excerpts of unstructured text directly into the prompt; maintain structured data and multi-page documents as local files within the project.

### Connecting to APIs and relational databases

Coding agents excel at writing integration code when provided with interface documentation. A common pattern is to provide an API endpoint or database connection string and ask the agent to inspect the schema:

1. Provision a scoped, read-only credential to safeguard production systems.
2. Store credentials in environment variables rather than prompts ([Secrets](concept:secrets)).
3. Require the agent to persist extracted records (and the exact query used) into a local data directory to ensure research reproducibility.

## The representation hierarchy

| Format category | Extensions | Processing behavior | Structural preservation |
|---|---|---|---|
| **High fidelity (Plain text)** | `.csv`, `.tsv`, `.json`, `.md`, `.tex`, `.yaml` | Parsed directly as structured text tokens | High: Preserves tabular rows, hierarchical keys, and semantic tags exactly. |
| **Intermediate (Office containers)** | `.xlsx`, `.docx` | Requires extraction libraries (`openpyxl`, `python-docx`) | Moderate: Extracts values reliably; may drop macros, cell formatting, and revision marks. |
| **Lossy (Visual & compound)** | Scanned `.pdf`, raster images, `.pptx` | Requires OCR engines or layout-heuristic parsers | Low: Column order, table structures, and complex formatting are frequently distorted. |

### Understanding PDF extraction challenges

PDF documents present distinct analytical challenges depending on their internal structure:
- **Digital PDFs with text layers:** Standard extraction utilities can extract the underlying text stream, but multi-column layouts, footnotes, and complex tables can be merged out of order.
- **Scanned image PDFs:** Contain only raster graphics without character streams. Extracting text requires Optical Character Recognition (OCR), which is slower, computationally intensive, and susceptible to character-recognition errors.

Where possible, obtain data directly in structured plain-text formats at the source (e.g., exporting Excel sheets to CSV, or pulling raw database tables).

## Dependency management for input processing

Ingesting non-text formats requires specialized libraries: reading `.xlsx` files requires spreadsheet parsers, while extracting text from PDFs requires command-line utilities. Rather than manually researching and installing these tools, allow the agent to install what it needs within the project virtual environment ([Environment](concept:environment)).

## Data organization and management hygiene

- **Enforce read-only raw data stores:** Maintain immutable original records in a dedicated directory (such as `data/raw/`) and instruct the agent never to modify them. All cleaning scripts should write to separate output folders.
- **Provide comprehensive data dictionaries:** Accompany datasets with a schema definition detailing column definitions, expected types, and measurement units to prevent hallucinated interpretations.
- **Inspect schemas before loading records:** For large datasets, direct the agent to inspect column headers and sample rows first, then execute data transformations using standalone scripts rather than dumping complete datasets into working memory ([Context](concept:context)).

## Ethical and privacy governance

Ensure all ingested data complies with institutional research approvals and privacy policies before exposing it to cloud-hosted agents ([Privacy and data handling](concept:privacy)).

## Demo it

<!-- demos -->
