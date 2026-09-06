# Reference prompt — annotation tool

Use this only after drafting your own request.

> Read `workshop/04-annotation-tool/{CONTEXT,CONTRACT,ACCEPTANCE}.md` and the exercise-03 schema. Propose a minimal local review interaction before implementing. Create one self-contained HTML file with inline CSS/JS and no build system, CDN, server, or network request. It must load user-selected local JSON/JSONL records, render prior/current impressions as escaped text plus the LLM proposal, navigate records, retain in-session reviewer edits, capture concept/state/decision/evidence/notes with an explicit uncertain option, and download JSON annotations keyed by `transition_id`. Explain the expected input shape in the page, show useful parse errors, and make keyboard-accessible controls. Test with fabricated input including HTML-like text and validate an export with `python -m json.tool`. Do not implement user accounts, upload, synchronization, diagnosis, or a database.

The desired outcome is a small inspectable artifact, not a generic web application.