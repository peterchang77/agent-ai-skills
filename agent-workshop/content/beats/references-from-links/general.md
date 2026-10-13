---
role: references-from-links
title: Build references from links you provide
kind: detour
summary: Construct an auditable BibTeX bibliography from researcher-curated URLs, using DOI content negotiation and PMID lookups while barring model speculation.
time: 6 min
teaches: [inputs, verification, tools]
needs: [orient-in-folder]
---

In research workflows, investigators often accumulate specific URLs to articles, preprints, or bibliographic records during literature exploration. In this detour exercise, you direct the agent to fetch metadata directly from curated links, format the records as BibTeX, and audit extraction integrity.

**Before you start:** A project directory and a list of target URLs representing papers you intend to cite ([Setup](setup:)).

## Background

This exercise illustrates the **web as an analytical input pathway** ([Inputs](concept:inputs)). You supply publication links (PubMed entries, DOI URLs, preprint repositories, or publisher landing pages), and the agent retrieves each resource to extract titles, authors, publication years, and persistent identifiers.

Web interfaces vary significantly in how easily they yield bibliographic metadata:

| URL structure | Expected retrieval behavior | Optimal technical pathway |
|---|---|---|
| **DOI links** (`doi.org/...`) | High reliability; official DOI resolvers support HTTP content negotiation | Request `Accept: application/x-bibtex` headers to retrieve authoritative BibTeX directly |
| **PubMed records** | High reliability via API; standard web interfaces may block automated requests | Query PubMed E-utilities using the parsed PMID |
| **Preprint repositories** (arXiv, bioRxiv) | High reliability; open metadata headers and Dublin Core tags | Parse HTML `<meta>` tags or query repository APIs |
| **Commercial journal pages** | Variable; commercial firewalls or anti-bot protections frequently block scrapers | Fall back to DOI content negotiation or manual abstract pasting |

When an automated HTTP request fails (e.g., due to an institutional paywall or bot detection), language models are prone to fabricating missing citation fields from memory. **Explicitly prohibit guessing:** when a page cannot be retrieved, instruct the agent to declare the failure, fall back to identifier lookups, or request that you paste the metadata manually.

## General methodology

Direct the agent to resolve each link using official resolvers or metadata headers, mandating that the source channel be documented for every record:

```text
Here are links to <N> target publications: <url1> <url2> ...
For each link, retrieve official bibliographic metadata using DOI content negotiation, PubMed E-utilities, or publication metadata tags.
Append verified BibTeX entries to references.bib, ensuring each entry includes an active DOI or PMID.
If automated retrieval fails for any link, report the error explicitly; do not guess or fabricate missing fields from memory.
Finally, provide a summary table listing each entry alongside the exact retrieval mechanism used.
```

<!-- example -->

## Verification criteria

- **Complete link accounting:** Every provided URL is explicitly accounted for as successfully added or transparently reported as failed.
- **Persistent identifier presence:** All created BibTeX entries contain valid DOI or PMID attributes.
- **Empirical source verification:** Spot-check two or three entries against original article pages to confirm author lists and publication years match.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Extraction blocked by publisher website | Commercial anti-bot protections or institutional paywalls | Extract the DOI string from the URL and query the official `dx.doi.org` resolver directly |
| Fabricated author lists or journals | The agent encountered an extraction error and filled missing fields from pre-training memory | Explicitly mandate: *"Never guess missing fields; report extraction failures immediately"* |
| Duplicate entries in bibliography | Multiple URLs referenced the same underlying publication | Direct the agent to de-duplicate against existing DOI and PMID attributes prior to appending |
