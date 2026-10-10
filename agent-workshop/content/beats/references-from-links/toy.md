---
role: references-from-links
scenario: toy
starts_from: any folder (an existing `references.bib` is optional)
produces: entries added to `references.bib`
prompt: |
  Here are links to two papers:
  https://pubmed.ncbi.nlm.nih.gov/20950378/
  https://doi.org/10.1111/j.1742-7924.2010.00146.x
  For each, retrieve the metadata from the page or from its DOI or PMID record, and add a BibTeX entry to references.bib with the DOI or
  PMID. If you cannot retrieve a link, say so and do not guess any field. Then list the source you used for each entry.
---

**Links used.** Two papers on telephone follow-up in diabetes: PMID 20950378 (a systematic review and meta-analysis, 2010) and DOI
10.1111/j.1742-7924.2010.00146.x (a 2010 trial of telephone follow-up and adherence).

**What happens when this material was prepared.** The PubMed web page returned a short bot-check page instead of the record, and the publisher's page
for the DOI refused automated access. The DOI service's BibTeX response, however, returned a complete entry. A good agent therefore:

1. reports that the PubMed page could not be read directly,
2. falls back to the PubMed programmatic interface with PMID 20950378, and
3. uses the DOI's BibTeX for the second paper,

and lists these sources. A poor agent writes both entries from memory. Your environment may behave differently; the principle is the same.

**Check.** Open one of the papers in a browser and compare the title, authors, and year with the entry. If you also have `pubmed_refs.py` from the
previous step, run `verify`; it only checks entries that have a PMID.
