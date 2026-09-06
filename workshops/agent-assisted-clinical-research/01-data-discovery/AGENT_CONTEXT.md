# Agent context: 01 — Safe data discovery

## Assignment

Create a small, inspectable command-line utility that safely explores the workshop’s assigned CheXpert Plus data resource and exports a **small metadata trial**. Begin by inspecting the current project and installed data-client documentation/API; do not assume that table or column names in this brief exactly match the deployed workspace.

## Why this matters

The full CheXpert Plus release is multi-terabyte scale. Data discovery must occur before export. The goal is not to download images or the complete dataset; it is to learn what is available and produce a bounded, documented metadata sample for the next exercise.

## Workspace facts

- The sandbox source used Stanford AIMI CheXpert Plus v1.0 through Redivis (`AIMI.chexpert_plus:5yyj`), with a main metadata table named `df_chexpert_plus_240401`. The cloud workspace may mount prepared data or use a different configured access route.
- Typical useful metadata fields include a de-identified patient ID, image path/ID, findings, impression, split, and potentially date-related fields. Inspect the real schema before choosing fields.
- Follow the cloud landing page for the actual dataset root, package, and authentication mechanism. If applicable, credentials are provided by the environment/client; never create, print, commit, or hard-code tokens.
- Try the supplied environment check with `bash workshop/tools/preflight.sh`. It reports only whether required values exist, never their values.

## Required outcome

Create a CLI with equivalent capabilities to:

```text
list-tables
list-columns TABLE
export TABLE --output PATH [--columns COLUMN ...] [--max-results N] [--csv]
```

It should use the approved client/configuration, require an explicit table and destination, refuse to overwrite output, and make a bounded trial easy. Parquet should be the default unless the user explicitly requests CSV. Its help and errors should make it difficult to accidentally issue an enormous export or leak credentials.

Run it to list available resources, inspect the actual metadata schema, and export at most ten rows into an ignored `data/` directory. Report commands, created paths, observed schema, validation evidence, assumptions, and limitations.

## Boundaries

Do not build bulk/image download behavior, export a full table by default, embed secrets, or infer temporal meaning from a field merely because its name contains `order` or `date`. The next exercise will establish whether temporal fields really support chronology.

## Definition of a credible result

A reviewer should be able to run `--help`, list resources, inspect columns, make a 10-row export, see the source table/row count, and observe that a repeat export does not overwrite an existing file. If data access is unavailable, diagnose it and stop rather than fabricating output.
