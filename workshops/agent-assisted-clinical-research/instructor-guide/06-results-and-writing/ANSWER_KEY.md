# Instructor answer key — 06 Results, LaTeX, citations

## Teaching point

Agents can convert saved artifacts into readable scientific outputs, but must not invent evidence or strengthen claims. Traceability and calibrated language are the desired deliverables.

## Suggested live flow

1. Ask agents to inventory existing result files and TeX availability before drafting.
2. Make them identify likely overclaims before writing.
3. Generate table/figure from saved outputs, then draft a short methods/results document.
4. Inspect traceability of one prose number and one citation.
5. Compile, inspect log/PDF, and revise language/limitations.

## Expected artifact and evidence

- Reproducible figure/table generation from saved aggregate metrics/predictions.
- `methods-results.tex`, verified `references.bib`, successful compile where TeX available.
- Statements of temporal cohort rule, patient-disjoint split/selection policy, weak-label/masking, baseline, support/metrics, and specific limitations.
- Mapping from every reported number/citation to source artifact/source metadata.

## Reference prompt

> Read the context and inventory saved outputs/toolchain before writing. Generate reproducible table/figure artifacts, then a concise LaTeX methods/results document and verified BibTeX. Trace every number to a saved result and each citation to a supplied trusted source. State methods, selection/test policy, support, weak-label semantics, and specific limitations; list likely overclaims first and avoid them. Compile/inspect the document and report all paths, commands, evidence, unresolved limitations. Do not invent numbers, intervals, p-values, or bibliography.

## Common errors and steering

- **Agent writes before examining results:** require artifact inventory and source paths first.
- **Invented citations:** use supplied citation metadata or stop; inspect BibTeX manually.
- **Calls agreement “clinical accuracy”:** revise terminology and explain exact target/metric.
- **Unsupported significance language:** remove unless prespecified saved calculation exists.
- **Static manually copied table:** require script/regeneration and check against source.
- **TeX unavailable:** retain source and describe a tested alternative/clear compile command; do not claim PDF was compiled.

## Reference materials

Sandbox `docs/report2delta-v2-methods-results.tex` and its `.bib` file are instructor comparison artifacts. Use them to discuss scope/claim language, not as a participant starting point.
