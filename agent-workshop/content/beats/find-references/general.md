---
role: find-references
title: Find references from a bibliographic database
kind: full
summary: Build a verified BibTeX bibliography via programmatic API retrieval (PubMed E-utilities), establishing a reproducible search log and eliminating hallucinated citations.
time: 9 min
teaches: [tools, verification, memory]
needs: [orient-in-folder]
---

Large language models frequently fabricate plausible-sounding academic citations when prompted from training memory. In this exercise, you implement a programmatic reference retrieval workflow that queries PubMed via external APIs, saves verified records to a BibTeX bibliography, documents search parameters, and validates metadata against upstream registries.

**Before you start:** A project directory and active network access. (A local fallback archive is available if network access is restricted; see [Setup](setup:)).

## Background

A dependable scientific bibliographic pipeline adheres to four core methodological principles:

1. **Programmatic retrieval over memory recall:** Every citation entry must be ingested directly from an authoritative bibliographic database, never generated from model parameters.
2. **Persistent identifier tracking:** Every entry must store a persistent digital identifier (PMID or DOI) enabling automated re-verification.
3. **Reproducible query auditing:** The search string, execution date, total hits returned, and explicit inclusion/exclusion decisions are preserved in an audit log (`refs/search-log.md`).
4. **Upstream metadata validation:** Metadata fields (authors, title, publication year) are systematically validated against registry records before citing.

This exercise uses the National Library of Medicine's [PubMed E-utilities](https://pubmed.ncbi.nlm.nih.gov/) API: an open programmatic interface where an `esearch` query retrieves matching PMIDs and an `esummary` call retrieves structured metadata.

The generated `references.bib` file acts as durable project memory ([Memory](concept:memory)), readable by both the agent and LaTeX compilation engines. Establish a standing rule in `AGENTS.md`: *"All academic citations must be programmatically retrieved and include a valid PMID or DOI; never generate citations from memory."*

## General methodology

Direct the agent to develop a lightweight, standard-library Python utility to search, append, and verify records:

```text
Create a Python CLI utility, scripts/pubmed_refs.py, using only the Python standard library, supporting three subcommands:
1. `search "<query>"`: Queries PubMed E-utilities, prints candidate PMIDs with publication year, title, first author, and journal, and appends the query and result counts to refs/search-log.md.
2. `add <PMID...>`: Fetches official metadata for the specified PMIDs and appends formatted BibTeX entries to references.bib, preventing duplicates.
3. `verify`: Re-queries PubMed for each PMID in references.bib and asserts that local titles and publication years match official records.
Incorporate polite rate limiting between API requests. Test the utility and display its --help documentation.
```

Execute the workflow interactively:

```text
Search PubMed for <research topic>.
Display candidate papers with titles and abstracts. Pause so I can select which records to include.
Then add the selected PMIDs to references.bib and run the verification audit.
```

The human researcher must make the final selection: relevance to your research question requires scientific judgement. Always read candidate abstracts before citing papers in your manuscripts.

<!-- example -->

## Verification criteria

- **Persistent identifier presence:** Every entry in `references.bib` contains a valid PMID or DOI, and running `scripts/pubmed_refs.py verify` exits without error.
- **Auditable search log:** The file `refs/search-log.md` records the exact search query, execution timestamp, and rationale for selected records.
- **Abstract verification:** The researcher has inspected the abstract for every cited paper to verify that findings support the intended manuscript claims.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| HTTP 429 Too Many Requests | Script exceeded PubMed's unauthenticated request rate limits (typically 3 requests/second) | Add explicit sleep pauses (`time.sleep(0.4)`) between API calls |
| Hallucinated reference fields | The agent supplemented missing metadata fields from internal memory | Mandate that all BibTeX attributes originate strictly from parsed API response payloads |
| Duplicate bibliography keys | The same paper was added under multiple query variations | Enforce uniqueness checks on PMIDs and DOIs prior to appending entries |
