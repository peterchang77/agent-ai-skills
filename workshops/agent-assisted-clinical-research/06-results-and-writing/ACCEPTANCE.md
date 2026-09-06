# Acceptance: analysis and writing

## Required checks

- Regenerate the table and figure from saved evaluation artifacts; confirm the values agree with the metrics file.
- Compile the LaTeX document when a TeX toolchain is supplied, for example:

```bash
latexmk -pdf methods-results.tex
```

- Inspect the PDF/log for unresolved citations, missing figures, and overfull/missing references.
- Confirm every numeric result in prose can be traced to an input artifact.
- Confirm every BibTeX entry was verified from a trusted supplied source.
- Search the draft for prohibited overclaim language and revise contextually:

```bash
rg -n -i 'diagnos|clinical (accuracy|performance|utility)|ground truth|detects disease|prove' methods-results.tex
```

## Review questions

- Does the report say what the metric actually measures?
- Are results selected on validation and held-out evaluation distinguished?
- Are limitations specific to the data/label/model pipeline rather than generic boilerplate?