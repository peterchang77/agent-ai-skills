---
role: write-abstract
title: Write a research abstract as LaTeX, with citations
kind: full
summary: Author a structured scientific abstract in LaTeX from empirical results files and a verified bibliography, compiling a publication PDF and tracing numerical claims to their source.
time: 9 min
teaches: [outputs, verification]
needs: [analyze-pilot]
---

In this exercise, you direct the agent to synthesize empirical results and verified bibliographic citations into a publication-ready structured scientific abstract in LaTeX (`out/abstract.tex`), compile the document to PDF, and trace every numerical claim back to underlying data tables.

**Before you start:** A results file from statistical analysis, a verified `references.bib` containing retrieved citations, and a local LaTeX compiler environment ([Setup](setup:)). If LaTeX is absent, the agent can configure it ([Environment](concept:environment)), or compile via Markdown and Pandoc.

## Background

Adopting a **source-first compilation pattern** ensures maximum reproducibility ([Outputs](concept:outputs)). LaTeX generates clean, standardized typography with automated section numbering and bibliographic citation formatting resolved against `references.bib`. Because the final PDF is compiled programmatically from plain text, updating estimates or refining prose requires only a concise source edit and recompilation.

Two mandatory guardrails maintain scientific integrity:

- **Numerical claims derive strictly from results files:** Every percentage, odds ratio, and sample size must be extracted directly from `out/results.md` and flow tables, rather than recalled from conversational memory.
- **Citations derive strictly from `references.bib`:** The agent is prohibited from introducing external citations that do not exist within the local bibliography ([Verification](concept:verification)).

A structured scientific abstract adheres to standard sections: Background, Methods, Results, and Conclusions. Ensure the concluding interpretation aligns strictly with what the observational design mathematically supports.

## General methodology

Direct the agent to draft the structured abstract, embed citations from the verified bibliography, compile the document, and provide an explicit provenance checklist for every number:

```text
Draft a single-page structured abstract (Background, Methods, Results, Conclusions) as out/abstract.tex.
Incorporate an embedded results summary table and citations drawn exclusively from references.bib.
Extract all numerical estimates, denominators, and confidence intervals directly from <results file> and <flow table>.
Do not fabricate or introduce any citation key absent from references.bib.
State the study design clearly, noting primary observational limitations.
Compile the document to out/abstract.pdf and report any LaTeX compiler warnings.
Finally, provide a provenance checklist mapping every number and citation key in the abstract to its specific source table or reference record.
```

<!-- example -->

## Verification criteria

- **Numerical concordance:** Every statistic, sample size, and confidence interval in the PDF matches underlying results tables exactly.
- **Bibliographic validity:** All citation keys resolve cleanly against `references.bib` without missing reference warnings (`?` or `[?]`), and cited papers substantiate their corresponding assertions.
- **Epistemic calibration:** The conclusions section discusses observed statistical associations without overreaching into unverified causal claims.
- **Synthetic data disclosure:** If analyzing the workshop benchmark dataset, the abstract explicitly discloses that the findings derive from synthetic data.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Unresolved citations (`[?]`) | The bibliography engine did not execute the full compile cycle | Recompile using the standard sequence: `pdflatex`, `bibtex`, followed by two passes of `pdflatex` |
| Missing LaTeX package errors | Required style packages are absent from the host LaTeX distribution | Authorize the agent to install missing packages via the system package manager, or simplify the LaTeX preamble |
| Disconnected citations | The model attached a legitimate citation to an unrelated claim | Direct the agent to cite the supporting sentence from the cited paper's abstract, or remove the reference |
| Document spills onto a second page | Preamble geometry or margins exceed single-page limits | Instruct the agent to adjust geometry margins or tighten section spacing |
