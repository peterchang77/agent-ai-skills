---
role: find-references
scenario: toy
starts_from: the `analyzed` checkpoint (or any folder)
produces: "`scripts/pubmed_refs.py`, `references.bib`, `refs/search-log.md`"
prompt:
  - label: Add the rule
    text: |
      Add this rule to AGENTS.md: Citations come only from retrieved PubMed records. Each entry in references.bib must contain a PMID.
      Never write a citation from memory.
  - label: Build the tool
    text: |
      Write a small command-line script, scripts/pubmed_refs.py, using only the Python standard library, with three commands. `search
      "query"` prints the PMID, year, title, first author and journal of each hit, and appends the query, the date and the results to
      refs/search-log.md. `add PMID...` fetches those records from PubMed and appends BibTeX entries that include the PMID to references.bib,
      skipping duplicates. `verify` re-fetches every entry in references.bib and reports any whose title or year differs. Use PubMed
      E-utilities and wait between requests. Test it, and show me the --help.
  - label: Search
    text: |
      Using scripts/pubmed_refs.py, search PubMed for telephone follow-up diabetes HbA1c. Show me the top 8 candidates with PMID, year and
      title, and wait for me to choose which to add.
  - label: Add and verify
    text: |
      Add PMIDs 20950378, 21092015, 15842446 and 26871245 to references.bib, then run verify and show me the result.
---

Run the prompts in order. Check that the tool works (the `--help` output and a passing test) before you search. The first prompt is the rule from the general page, saved where every future session will read it.

**What you should see.** A query such as `telephone follow-up diabetes HbA1c randomized` returned about 200 hits when this material was
prepared (the count will differ over time). Among the top results were these, which suit the background of the abstract:

| PMID | Year | Title (shortened) |
|---|---|---|
| 20950378 | 2010 | Telephone follow-up to improve glycaemic control in type 2 diabetes: systematic review and meta-analysis |
| 21092015 | 2010 | Effect of telephone follow-up on adherence to a diabetes therapeutic regimen |
| 15842446 | 2005 | Nurse follow-up of patients with diabetes: randomized controlled trial |
| 26871245 | 2016 | Does telephone follow-up and education affect self-care and metabolic control in diabetic patients? |

The same search also returns papers that are *not* relevant (a transition-of-care review, a text-message programme, postpartum follow-up).
Choosing is your job, and rejecting is part of the log. The last prompt names the four PMIDs from the table so that your result matches; with your own search, pick the candidates that suit your abstract instead.

**Fallback.** `scenarios/toy/extras/pubmed_refs.py` is a reference version of the script and `extras/references.bib` holds these four verified
entries. Running `python3 pubmed_refs.py verify --bib references.bib` should report `ok` for each.

**Your search will not match exactly.** Search results change as new papers appear, and the agent may phrase its query differently. The
workflow is what matters: retrieve, choose, record, verify.
