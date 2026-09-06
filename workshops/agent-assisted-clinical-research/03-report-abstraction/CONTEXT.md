# Context: constrained report-to-change abstraction

For each valid prior/current transition, extract change for four concept families: `pleural_effusion`, `pulmonary_edema`, `lung_opacity`, and `support_devices`. The allowed temporal states are `new`, `worsened`, `improved`, `stable`, `resolved`, plus explicit non-target/abstention states.

Use only the **prior and current impressions**. The prior is context; usable temporal evidence must appear in the current impression. Do not send image pixels or identifiers to the LLM endpoint. The endpoint is supplied through `WORKSHOP_LLM_BASE_URL`, `WORKSHOP_LLM_API_KEY`, and `WORKSHOP_LLM_MODEL`; credentials must never appear in code, output, or Git.

The sandbox used one frozen prompt/schema/model/decode configuration across a cohort. Its validator masked a concept when the output was malformed, uncertain, unaligned, contradictory, unsupported by the current impression, a bare negative falsely called `resolved`, or isolated atelectasis/scar/nodule/mass was used as the only lung-opacity evidence.

The endpoint call can fail or be interrupted. A robust program preserves raw response/request metadata in ignored storage, writes structured records separately, and resumes only records without a terminal outcome. It must never resubmit completed records merely to seek a preferable label.

Read the shared safety boundary before prompting an agent: [`../shared/data-and-llm-safety.md`](../shared/data-and-llm-safety.md).