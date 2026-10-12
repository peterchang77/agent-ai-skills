---
role: write-abstract
title: Write a research abstract as LaTeX, with citations
kind: full
summary: Have the agent write the abstract as LaTeX from your results file and bibliography, compile it, and trace every number and claim back to its source.
time: 9 min
teaches: [outputs, verification]
needs: [analyze-pilot]
---

After this step you will be able to turn saved results and a verified bibliography into a compiled PDF abstract, and to check that every number
and citation in it is supported.

**Before you start:** a results file, a `references.bib` whose entries were retrieved (not recalled), and a LaTeX installation
([Setup](setup:)). If LaTeX is missing, the agent can usually help install it ([Environment](concept:environment)), or you can ask for Markdown and
convert with `pandoc`.

## Background

Write the **source** and render it ([Outputs](concept:outputs)). LaTeX produces a clean PDF with automatic numbering and a reference list generated from
`references.bib`. Because the PDF is built from text, a correction is one edit and one rebuild.

Two rules keep the abstract trustworthy:

- **Numbers come from the results file**, not from the agent's recollection of the conversation. Tell it to copy them from the file.
- **Citations come only from `references.bib`.** It may not add a reference that is not already there ([Verification](concept:verification)).

A structured abstract has a fixed shape: Background, Methods, Results, Conclusions. Keep the conclusions to what the design supports.

## General approach

```text
Write a one-page structured abstract (Background, Methods, Results, Conclusions) as out/abstract.tex, with a results table and citations
from references.bib only. Take every number from <results file> and <flow table>. Do not add any citation that is not in references.bib. State
the study design and its main limitation. Compile it to out/abstract.pdf and report any warnings. Then list each number and each citation
in the abstract with where it came from.
```

The final sentence gives you a checklist. Work through it.

<!-- example -->

## What to check

- Each number matches the results file.
- Each citation key exists in `references.bib`, and the cited paper supports the sentence it is attached to (read the abstract of the paper).
- The conclusion uses language of association if the design is observational.
- The PDF compiled with no unresolved references (no `?` or `[?]`).
- If the data is synthetic, the abstract says so.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| `[?]` in the text | The bibliography step did not run | Rerun LaTeX, BibTeX, then LaTeX twice |
| Missing package | A LaTeX package is not installed | Let the agent install it, or use a simpler template |
| A claim the cited paper does not support | The citation was attached to the wrong sentence | Ask for the supporting statement from the paper, or remove the citation |
| Runs onto a second page | Too much text or spacing | Ask it to tighten the text and margins |
