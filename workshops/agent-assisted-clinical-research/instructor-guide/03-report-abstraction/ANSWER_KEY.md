# Instructor answer key — 03 Report abstraction

## Teaching point

A credible LLM abstraction workflow is a versioned, resumable data process—not merely a prompt plus parsed JSON. Structural validator checks support auditability but do not make labels clinically true.

## Suggested live flow

1. Ask participants to propose an agent request that delivers an extraction runner, not a one-off notebook.
2. Require agent inspection/planning: fixed prompt/schema/run config, protected raw storage, terminal record semantics, retry policy, resume behavior.
3. Run ten records only; inspect one raw response, one structured record, and one masked output.
4. Run resume and show zero resubmissions.
5. Feed malformed/unsupported cases and explain the masks.

## Expected artifact and evidence

- CLI with bounded initial run, environment-only endpoint configuration, fixed run metadata, raw/structured separation, terminal errors, bounded retry and resume.
- Per-concept validator enforcing allowed enums, certainty/alignment/current evidence and special bare-negative/isolated-opacity rules.
- Ten-record smoke result, resume evidence, invalid fixture evidence, masked modeling manifest.

## Reference prompt

> Read the context and inspect endpoint/client conventions. Propose fixed-run configuration, storage layout, and terminal retry/resume semantics before coding. Build the bounded abstraction CLI plus validator with raw artifacts in ignored protected paths and structured provenance records. Keep schema/prompt/model/decode config fixed; validate current-impression evidence, certainty, alignment, abstentions, bare-negative resolution, and isolated non-opacity. Run ten records, resume, and invalid fixtures. Report outputs, checks, and what validation cannot prove.

## Common errors and steering

- **Raw output in Git/ordinary logs:** stop and move to ignored protected directory.
- **Sends whole row/images/identifiers:** limit input to approved prior/current impressions and stable transition ID.
- **Retries successful calls:** define terminal state and demonstrate `--resume` skips it.
- **LLM output accepted blindly:** require parser/validator masks and keep raw response.
- **Claims ground truth:** correct language to weak pseudo-label/structural consistency.
- **Endpoint failure:** verify variables/health route with instructor; preserve error record rather than replacing output.

## Reference materials

Sandbox `scripts/run_report2delta_extraction.py`, fixed prompt/schema resources, and the label-audit document are instructor-only comparison material.
