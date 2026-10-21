---
role: references-from-links
scenario: imaging
starts_from: any folder (an existing `references.bib` is optional)
produces: entries added to `references.bib`
prompt: |
  Here are links to two papers:
  https://pubmed.ncbi.nlm.nih.gov/34350409/
  https://doi.org/10.1177/08465371231220885
  For each, retrieve the metadata from the page or from its DOI or PMID record, and add a BibTeX entry to references.bib with the DOI or
  PMID. If you cannot retrieve a link, say so and do not guess any field. Then list the source you used for each entry.
---

**Links used.** Two papers on deep learning for pneumothorax: PMID 34350409 (a multicenter external validation study, 2021) and DOI 10.1177/08465371231220885 (a diagnostic test accuracy meta-analysis, 2024).

**What to expect.** Publisher pages and the PubMed web page often refuse automated access or return a bot-check page. A good agent:

1. reports which page it could not read directly,
2. falls back to the PubMed programmatic interface for the PMID and to the DOI service's BibTeX for the DOI, and
3. lists the source it used for each entry.

A poor agent writes both entries from memory. Your environment may behave differently; the principle is the same.

**Check.** Open one of the papers in a browser and compare the title, authors, and year with the entry. If you also have `pubmed_refs.py` from the previous step, run `verify`; it only checks entries that have a PMID.
