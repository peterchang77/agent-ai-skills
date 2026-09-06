# Reference prompt — data discovery

Use this only after drafting your own request.

> Read `workshop/01-data-discovery/{CONTEXT,CONTRACT,ACCEPTANCE}.md` and inspect the existing project before coding. Build a small Python CLI for the approved CheXpert Plus data client. It must list tables, list a named table’s columns, and export only an explicitly named table to a new CSV or Parquet file with optional columns and `--max-results`. Follow the workspace credential mechanism; never print or store credentials. Refuse overwrite, warn about large exports, and give actionable auth errors without secrets. Do not implement bulk/image downloading or cohort logic. Before implementation, briefly report the data-client API you found and the safe discovery plan. After implementation, run `--help`, list tables, inspect the metadata schema, and export at most ten rows. Report paths, commands, validation evidence, and remaining assumptions.

Why it is useful: the prompt says what artifact to make and how to verify it, but lets the agent inspect the client and choose ordinary implementation details.