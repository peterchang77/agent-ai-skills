# Acceptance: safe discovery CLI

Review the agent's implementation before treating it as complete.

## Required checks

```bash
# Adapt the filename/entry point produced by the agent.
uv run python path/to/discover_data.py --help
uv run python path/to/discover_data.py list-tables
uv run python path/to/discover_data.py list-columns df_chexpert_plus_240401
uv run python path/to/discover_data.py export df_chexpert_plus_240401 \
  --columns deid_patient_id path_to_image findings impression split \
  --max-results 10 --output data/raw/metadata-trial.parquet
```

Then verify:

- `metadata-trial.parquet` exists and has at most 10 rows;
- its output prints the exact source table and row count;
- re-running the export to the same location fails rather than overwriting it;
- the source code and Git status contain no credential/token;
- the agent documented the actual available columns rather than inventing them.

## Human review questions

- Did the agent explore the endpoint before selecting an export?
- Does its code make a costly export difficult to perform accidentally?
- Did it confuse an endpoint/table name with a validated data schema?
