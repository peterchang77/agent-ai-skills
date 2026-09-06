# Instructor answer key — 01 Data discovery

## Teaching point

A useful agent request specifies a bounded deliverable and validation, but the agent must inspect the deployed data client/schema before it can implement safely. “Download the dataset” is neither a safe scope nor an adequate requirement.

## Suggested live flow

1. Project the participant `AGENT_CONTEXT.md`; ask audience members to write a request for two minutes.
2. Demonstrate a request such as: “Read the context, inspect the workspace/client documentation, propose a safe plan before code, then implement and run the requested bounded smoke test.”
3. Pause after the agent’s inspection/planning output. Ask: Which table is metadata? Which columns actually exist? What would a dangerous default be?
4. Let the agent implement the CLI, then run help, list tables, list columns, and a 10-row export.
5. Demonstrate overwrite refusal and explain why a row/order field is not yet validated chronology.

## Expected artifact and evidence

- A client-specific CLI with table listing, column inspection, and explicit bounded export.
- No embedded credentials, no default bulk/image download, overwrite refusal.
- Commands/output showing metadata schema and at most ten exported rows.
- A short report naming source table, fields, output path, assumptions, and limitations.

## Reference prompt

> Read the exercise context and inspect current project/client conventions before implementation. Build the requested safe discovery CLI. Require a named table/output, optional columns and row limit, refuse overwrite, use environment/client credentials only, and do not implement full/image export. Run help, resource/column discovery, and a 10-row metadata export. Report paths, commands, output schema, validation evidence, and limitations.

## Common errors and steering

- **Agent exports all data or images:** stop it; require `--max-results` for workshop trial and make broad export an explicit later approval.
- **Hard-coded API token/home path:** ask it to use the configured client/environment and scan source/Git status.
- **Invented columns/table names:** ask it to inspect actual schema first and revise CLI/help/test command.
- **Only code, no execution:** ask it to run the smallest live smoke test and explain what it found.
- **Data access fails:** demonstrate diagnostic behavior; do not fabricate a result. Check cloud credentials/mount with instructor.

## Reference implementation

The original sandbox’s `scripts/redivis_chexpert_plus.py` is a suitable private comparison artifact. Do not mount it in participant workspaces before their attempt.
