---
role: read-text-files
title: Read and summarize text files
kind: full
summary: Direct the agent to inspect and synthesize project-local text files, validating source provenance and avoiding copy-paste truncation.
time: 5 min
teaches: [inputs, verification]
needs: [orient-in-folder]
---

Structured plain text is the most reliable medium for language model ingestion. In this exercise, you direct the agent to read local text files directly from the filesystem, synthesize key findings, and attribute claims to specific source files.

**Before you start:** A project directory containing text-based documents or data files ([Setup](setup:)).

## Background

Plain-text formats, including Markdown (`.md`), CSV (`.csv`), JSON (`.json`), LaTeX (`.tex`), and HTML (`.html`), are parsed directly as structured token sequences without requiring translation libraries ([Inputs](concept:inputs)). 

Directing the agent to inspect files via relative filesystem paths is far superior to pasting excerpts into the chat window: it eliminates manual copy-paste errors, preserves tabular column alignments, and ensures the original file remains the definitive source of truth.

## General methodology

Specify the target files and the extraction objective explicitly, instructing the agent to attribute each summary point to its source document.

```text
Read <file1> and <file2>. Synthesize <analytical objective>. For each key finding, cite the specific source file and section.
```

Requiring explicit file citations transforms conversational claims into an auditable evidence trail ([Verification](concept:verification)). If the files contain confidential or regulated records, verify that your model endpoint is authorized for that data tier ([Privacy and data handling](concept:privacy)).

<!-- example -->

## Verification criteria

- **Verified file access:** Confirm that the agent executed read commands against each named file in the session transcript.
- **Traceable citations:** Every claim or numerical parameter in the summary cites a specific file.
- **Content fidelity:** The summary accurately reflects the text without omitting critical caveats or extrapolating unsupported claims.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Overly generalized summary | The extraction directive was underspecified | Clarify the research objective and specify the required structural format (e.g., bulleted list or markdown table) |
| Unsupported claims | The model hallucinated details from pre-training memory | Direct the agent to quote the exact supporting sentences from the source text and excise unverified points |
