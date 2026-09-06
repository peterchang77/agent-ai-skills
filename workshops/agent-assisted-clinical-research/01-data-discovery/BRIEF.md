# 01 — Data discovery

## Learning goal

Direct an agent to safely explore an unfamiliar data resource before downloading or analyzing it. The deliverable is a small, inspectable command-line utility—not a broad export script.

Read [`CONTEXT.md`](CONTEXT.md), [`CONTRACT.md`](CONTRACT.md), and [`ACCEPTANCE.md`](ACCEPTANCE.md). Then write your own request to the agent.

## Deliverable

Ask the agent to create a Python CLI under your participant project that can:

1. authenticate using the approved credential mechanism without printing credentials;
2. list accessible tables;
3. list columns of a named table; and
4. export an explicitly named, column-limited table to a new local CSV or Parquet file, with an optional row limit.

Do not ask it to download all images or all tables.

## Before implementation

Ask the agent to inspect the existing project conventions and the data-client documentation/API available in the workspace. Have it report the smallest safe discovery plan before it writes code.

## After implementation

Run a table-listing command and a small (`--max-results 10`) export. Read the produced schema and explain why the next exercise cannot safely use a row/order field as a date without verification.

## If you get stuck

Use the discovery reference prompt only after attempting the task: [`../reference-prompts/01-data-discovery.md`](../reference-prompts/01-data-discovery.md).
