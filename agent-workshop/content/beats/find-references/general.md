---
role: find-references
title: Find references from a bibliographic database
kind: full
summary: Retrieve real papers from PubMed with a small script, build a BibTeX file from the retrieved records, and verify it. Never cite from the model's memory.
time: 9 min
teaches: [tools, verification, memory]
needs: [orient-in-folder]
---

Language models can produce plausible citations that do not exist. After this step you will have a repeatable way to find real references,
keep them in a BibTeX file, record how you searched, and check that every entry is genuine.

**Before you start:** a project folder and network access. A fallback is available if you cannot reach the network ([Setup](setup:)).

## Background

A safe reference workflow has four properties, which matter more than the particular tool:

1. **Retrieve, do not recall.** Every entry comes from a record returned by a bibliographic service, never from the model's memory.
2. **Keep identifiers.** Each entry carries a PMID or DOI, so it can be re-checked later.
3. **Log the search.** Record the query, date, number of hits, and what you kept or rejected, so the search is reproducible.
4. **Verify before use.** Re-fetch each entry and compare the title and year. Anything that does not resolve is flagged.

This is a *working example* of such a workflow, not a definitive one. [PubMed](https://pubmed.ncbi.nlm.nih.gov/) offers a free programmatic
interface (E-utilities): one call finds record IDs for a query, another fetches the records. It allows a few requests per second without an
account; space your calls out.

A `references.bib` file is plain text: the agent edits it and the LaTeX build reads it, so it works as project memory
([Memory](concept:memory)). Put the rule in `AGENTS.md`: "Citations come only from retrieved records; each must have a PMID or DOI."

## General approach

Ask the agent to build a small tool, then use it ([Tools](concept:tools)):

```text
Write a small command-line script, scripts/pubmed_refs.py, using only the Python standard library, with three commands: `search "query"`
(prints PMID, year, title, first author, journal, and appends the query and results to refs/search-log.md), `add PMID...` (fetches
records and appends BibTeX entries with the PMID to references.bib, skipping duplicates), and `verify` (re-fetches each entry and
reports any whose title or year differs). Use PubMed E-utilities and wait between requests. Test it, and show me the --help.
```

Then use it:

```text
Search PubMed for <topic>. Show me the candidates; I will choose which to add. Then add them and run verify.
```

You choose what to add: relevance is a judgement. Read each abstract before citing a paper for a claim.

<!-- example -->

## What to check

- Every `references.bib` entry has a PMID or DOI, and `verify` passes.
- `refs/search-log.md` shows the query, the date, and what you kept or rejected.
- You have read the abstract of each paper you will cite.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| Few or irrelevant hits | The query is too narrow or too broad | Adjust terms; combine intervention and condition terms |
| Rate-limit errors | Requests too fast | Add a delay between calls; use an API key for heavier use |
| Entries missing a DOI | Some records have none | Keep the PMID; it is sufficient to re-check |
| No network | Offline or blocked | Use the bundled `pubmed_refs.py` and `references.bib` in the extras folder |
