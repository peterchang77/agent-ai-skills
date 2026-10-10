#!/usr/bin/env python3
"""Minimal PubMed reference helper (stdlib only). A *working example*, not a definitive tool.

  pubmed_refs.py search "query" [--max 8] [--log refs/search-log.md]
  pubmed_refs.py add PMID [PMID ...] [--bib references.bib]
  pubmed_refs.py verify [--bib references.bib]

Design points worth copying in your own workflow:
  * Every entry is built from a retrieved PubMed record, never from model memory.
  * Each entry keeps its PMID (and DOI if present) so it can be re-checked later.
  * Searches are logged (query, date, hits, what was added) so the search is reproducible.
  * `verify` re-fetches each PMID and compares title and year with the .bib entry.
  * Requests are spaced out: NCBI allows ~3 requests/second without an API key.
"""
import argparse, datetime as dt, json, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def _get(endpoint, **params):
    time.sleep(0.4)
    url = BASE + endpoint + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "workshop-refs/0.1"}), timeout=30) as r:
        return r.read().decode()

def fetch_records(pmids):
    root = ET.fromstring(_get("efetch.fcgi", db="pubmed", id=",".join(pmids), retmode="xml"))
    out = []
    for art in root.findall(".//PubmedArticle"):
        pmid = art.findtext(".//PMID")
        a = art.find(".//Article")
        title = "".join(a.find("ArticleTitle").itertext()).strip().rstrip(".")
        authors = []
        for au in a.findall(".//Author"):
            if au.findtext("LastName"):
                authors.append(f"{au.findtext('LastName')}, {au.findtext('ForeName') or au.findtext('Initials') or ''}".strip(", "))
        year = (a.findtext(".//JournalIssue/PubDate/Year") or (a.findtext(".//JournalIssue/PubDate/MedlineDate") or "")[:4] or "")
        doi = next((i.text for i in art.findall(".//ArticleId") if i.get("IdType") == "doi"), "")
        out.append(dict(pmid=pmid, title=title, authors=authors, year=year, doi=doi,
                        journal=a.findtext(".//Journal/Title") or "", volume=a.findtext(".//JournalIssue/Volume") or "",
                        pages=a.findtext(".//Pagination/MedlinePgn") or ""))
    return out

def to_bibtex(r):
    key = re.sub(r"\W", "", (r["authors"][0].split(",")[0] if r["authors"] else "anon")) + r["year"] + "_" + r["pmid"]
    f = [("title", "{" + r["title"] + "}"), ("author", " and ".join(r["authors"])), ("journal", r["journal"]),
         ("year", r["year"]), ("volume", r["volume"]), ("pages", r["pages"].replace("-", "--")),
         ("doi", r["doi"]), ("note", f"PMID: {r['pmid']}")]
    return f"@article{{{key},\n" + ",\n".join(f"  {k} = {{{v}}}" for k, v in f if v) + "\n}\n"

def cmd_search(a):
    res = json.loads(_get("esearch.fcgi", db="pubmed", term=a.query, retmax=a.max, retmode="json", sort="relevance"))["esearchresult"]
    ids = res["idlist"]; recs = fetch_records(ids) if ids else []
    for r in recs:
        print(f"PMID {r['pmid']} | {r['year']} | {r['title'][:100]} | {(r['authors'] or ['?'])[0].split(',')[0]} et al. | {r['journal']}")
    if a.log:
        with open(a.log, "a") as f:
            f.write(f"\n## {dt.date.today()} — `{a.query}`\n- hits: {res['count']}; shown: {len(ids)}; PMIDs: {', '.join(ids)}\n")
    print(f"\n{res['count']} total hits; showing {len(ids)}. Log: {a.log or 'none'}", file=sys.stderr)

def cmd_add(a):
    existing = open(a.bib).read() if _exists(a.bib) else ""
    new = [r for r in fetch_records(a.pmids) if f"PMID: {r['pmid']}" not in existing]
    with open(a.bib, "a") as f:
        for r in new: f.write(to_bibtex(r) + "\n")
    print(f"added {len(new)} of {len(a.pmids)} to {a.bib}")

def _exists(p):
    try: open(p).close(); return True
    except FileNotFoundError: return False

def cmd_verify(a):
    text = open(a.bib).read(); bad = 0
    entries = re.findall(r"@article\{(.*?),\n(.*?)\n\}", text, re.S)
    pm = {e[0]: re.search(r"PMID: (\d+)", e[1]) for e in entries}
    recs = {r["pmid"]: r for r in fetch_records([m[1] for m in pm.values() if m])}
    for key, body in entries:
        m = pm[key]; title = (re.search(r"title = \{(.*)\}", body) or [0, ""])[1].strip("{}"); year = (re.search(r"year = \{(\d+)\}", body) or [0, ""])[1]
        if not m or m[1] not in recs: print(f"FAIL {key}: no resolvable PMID"); bad += 1; continue
        r = recs[m[1]]; same = r["title"].lower() == title.lower() and r["year"] == year
        print(("ok   " if same else "DIFF ") + key); bad += (not same)
    sys.exit(1 if bad else 0)

p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
s = p.add_subparsers(dest="cmd", required=True)
x = s.add_parser("search"); x.add_argument("query"); x.add_argument("--max", type=int, default=8); x.add_argument("--log", default=None); x.set_defaults(f=cmd_search)
x = s.add_parser("add"); x.add_argument("pmids", nargs="+"); x.add_argument("--bib", default="references.bib"); x.set_defaults(f=cmd_add)
x = s.add_parser("verify"); x.add_argument("--bib", default="references.bib"); x.set_defaults(f=cmd_verify)
a = p.parse_args(); a.f(a)
