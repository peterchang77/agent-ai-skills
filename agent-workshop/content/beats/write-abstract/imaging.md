---
role: write-abstract
scenario: imaging
starts_from: the `referenced` checkpoint (results plus `references.bib`)
produces: "`out/abstract.tex`, `out/abstract.pdf`"
prompt: |
  Write a one-page structured abstract (Background, Methods, Results, Conclusions) as out/abstract.tex, for the department's AI committee, about
  whether the open-source pneumothorax detectors are ready for a pilot. Take every number from out/evaluation.md and out/cohort_flow.md, and the cleaning counts from out/cleaning_flow.md. Cite only entries in references.bib,
  and do not add any other citation. Include one results table, state that this is a retrospective evaluation on a small public sample with synthetic data problems and that the models may have seen these images in training,
  and give the main limitation. Compile it to out/abstract.pdf with the bibliography and report any warnings. Then list each number and each citation with its source.
---

**Files used:** `out/evaluation.md`, `out/cohort_flow.md`, `out/cleaning_flow.md`, `references.bib`.

**Reference result.** The reference abstract is `scenarios/imaging/checkpoints/reported/out/abstract.pdf`, one page. Its key numbers:

| Item | Value |
|---|---|
| Images received / cleaned | 283 / 258 |
| Cohort | 203 adult patients, 59 with pneumothorax (PA 120, AP 83) |
| AUC of the primary model (`all`) | 0.78 (95% CI 0.72 to 0.84) |
| Other models | `chex` 0.72, `nih` 0.67, `pc` 0.69 |
| Primary minus `nih` / `pc` / `chex` | +0.11 (0.04 to 0.18) / +0.09 (0.01 to 0.16) / +0.06 (-0.02 to 0.15) |
| Primary at its published threshold | sensitivity 0.92, specificity 0.47 |
| Pilot bar (sens at least 0.85, spec at least 0.80) | Not met by any model |
| PA vs AP (exploratory) | AUC 0.85 vs 0.74, difference 0.11 (-0.03 to 0.26) |

**Compare yours.** Your wording will differ. Check the numbers against this table and the citations against `references.bib`. The conclusions should not claim more than the table does: no model met the bar, and the PA vs AP difference is not established.

**Check the citations by reading.** Ask: "For each citation, quote the sentence in the paper's abstract that supports the claim." If the agent cannot, the citation is decoration.
