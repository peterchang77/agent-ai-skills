---
role: write-abstract
scenario: toy
starts_from: the `referenced` checkpoint (results plus `references.bib`)
produces: "`out/abstract.tex`, `out/abstract.pdf`"
prompt: |
  Write a one-page structured abstract (Background, Methods, Results, Conclusions) as out/abstract.tex, for the leadership packet, about
  whether being reached by a follow-up call was associated with HbA1c recheck. Take every number from out/pilot_results.md and
  out/cohort_flow.md, and the cleaning counts from out/cleaning_flow.md. Cite only entries in references.bib, and do not add any other citation.
  Include one results table, state that this is a retrospective cohort and that the data is synthetic, and give the main limitation.
  Compile it to out/abstract.pdf with the bibliography and report any warnings. Then list each number and each citation with its source.
---

**Files used:** `out/pilot_results.md`, `out/cohort_flow.md`, `out/cleaning_flow.md`, `references.bib`.

**Reference result.** The reference abstract is `scenarios/toy/checkpoints/reported/out/abstract.pdf`, one page. Its key numbers:

| Item | Value |
|---|---|
| Cohort | 251 adult Hillcrest patients (from 819 adults with an HbA1c) |
| Reached / not reached | 92 / 159 |
| Rechecked | 45 of 92 (49%) vs. 47 of 159 (30%) |
| Unadjusted odds ratio | 2.28 (95% CI 1.34 to 3.88) |
| Adjusted odds ratio | 1.80 (95% CI 1.03 to 3.15) |
| Cleaning | 15 duplicates removed, 10 HbA1c values converted, 6 dates and 1 age corrected |

**Compare yours.** Your wording will differ. Check the numbers against this table and the citations against `references.bib`. In the reference, four
papers are cited in the Background to describe prior work on telephone follow-up.

**Check the citations by reading.** Ask: "For each citation, quote the sentence in the paper's abstract that supports the claim." If the agent
cannot, the citation is decoration.
