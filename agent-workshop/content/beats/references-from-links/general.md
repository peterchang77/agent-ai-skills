---
role: references-from-links
title: Build references from links you provide
kind: detour
summary: A simpler workflow. You collect the links; the agent reads them and writes the BibTeX. Know when this works and when it fails.
time: 6 min
teaches: [inputs, verification, tools]
needs: [orient-in-folder]
---

Sometimes the quickest way to build a reference list is to paste the links to papers you have already found. After this step you will know how to
do that, what to expect from different kinds of links, and how to check the result.

**Before you start:** a project folder and a few links you have chosen ([Setup](setup:)).

## Background

This is the **web as an input** ([Inputs](concept:inputs)). You supply URLs (PubMed pages, DOI links, publisher pages, preprint servers) and the agent
fetches each one and extracts the title, authors, year, journal, and identifier.

Links behave very differently:

| Link type | What usually happens |
|---|---|
| A DOI | The DOI service can return BibTeX directly (via content negotiation), which is the most reliable route |
| PubMed record | Best through PubMed's programmatic interface using the PMID; the ordinary web page may refuse automated requests |
| Publisher article page | Often blocks automated requests or sits behind a paywall |
| Preprint server | Usually open and easy to read |

When a page cannot be fetched, the agent may be tempted to fill in the details from memory. **Forbid that explicitly.** The safe fallbacks are to
fetch metadata by identifier, or for you to paste the abstract or the citation text yourself.

## General approach

```text
Here are links to <n> papers: <url1> <url2> ... For each, retrieve the metadata from the page or from its DOI or PMID record. Add a BibTeX
entry to references.bib with the DOI or PMID in it. If you cannot retrieve a link, say so and do not guess any field. Then list, for each
entry, the source you used.
```

Check the list the agent returns: a source for every entry is your evidence that nothing was invented.

<!-- example -->

## What to check

- Every link is accounted for: added, or reported as failed.
- Each entry has an identifier and a stated source.
- Titles, years, and authors match the page when you open two or three yourself.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| Some links failed | Paywall or bot protection | Use the DOI or PMID route, or paste the details |
| Plausible but wrong details | The agent filled gaps from memory | Forbid guessing; ask for the source of each field |
| Duplicates of papers already in the file | Different links to the same paper | Compare identifiers before adding |
