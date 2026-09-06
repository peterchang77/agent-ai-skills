# Contract: safe discovery CLI

The created utility is a discovery and small-export tool. It is not a general unrestricted downloader.

## Inputs

- An approved authentication mechanism provided by the data-client library or workspace.
- Exact table name for column inspection/export.
- Explicit output path for an export.
- Optional explicit list of columns.
- Optional explicit `max-results` / row limit.

## Required behavior

- Commands: `authenticate` if applicable, `list-tables`, `list-columns TABLE`, and `export TABLE --output PATH`.
- The tool must not hard-code credentials, tokens, home directories, or a participant-specific path.
- It must refuse to overwrite a destination.
- It must create the output parent directory only after input validation.
- It must show a clear error when access/authentication fails, without including secrets in the error.
- It must support Parquet by default and CSV only through an explicit option.
- The export help text must warn users to trial large resources with a row limit first.

## Out of scope

Full image download, bulk table export by default, cohort construction, report abstraction, and any automatic upload of data to a third party.
