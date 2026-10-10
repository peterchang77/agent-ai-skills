---
role: find-references
scenario: toy
starts_from: the `analyzed` checkpoint (or any folder)
produces: "`scripts/pubmed_refs.py`, `references.bib`, `refs/search-log.md`"
prompt: |
  I need background references for an abstract about nurse telephone follow-up to improve HbA1c control or recheck in diabetes. Write
  scripts/pubmed_refs.py with three commands: search, add and verify (standard library only; log searches to refs/search-log.md; every entry in references.bib must carry a PMID). Then
  search PubMed for telephone follow-up diabetes HbA1c, show me the top 8 candidates, and wait for me to choose which to add.
---

**Rule for `AGENTS.md`** (add it first): *Citations come only from retrieved PubMed records. Each `references.bib` entry must contain a PMID.
Never write a citation from memory.*

**What you should see.** A query such as `telephone follow-up diabetes HbA1c randomized` returned about 200 hits when this material was
prepared (the count will differ over time). Among the top results were these, which suit the background of the abstract:

| PMID | Year | Title (shortened) |
|---|---|---|
| 20950378 | 2010 | Telephone follow-up to improve glycaemic control in type 2 diabetes: systematic review and meta-analysis |
| 21092015 | 2010 | Effect of telephone follow-up on adherence to a diabetes therapeutic regimen |
| 15842446 | 2005 | Nurse follow-up of patients with diabetes: randomized controlled trial |
| 26871245 | 2016 | Does telephone follow-up and education affect self-care and metabolic control in diabetic patients? |

The same search also returns papers that are *not* relevant (a transition-of-care review, a text-message programme, postpartum follow-up).
Choosing is your job, and rejecting is part of the log.

**Fallback.** `scenarios/toy/extras/pubmed_refs.py` is a reference version of the script and `extras/references.bib` holds these four verified
entries. Running `python3 pubmed_refs.py verify --bib references.bib` should report `ok` for each.

**Your search will not match exactly.** Search results change as new papers appear, and the agent may phrase its query differently. The
workflow is what matters: retrieve, choose, record, verify.
