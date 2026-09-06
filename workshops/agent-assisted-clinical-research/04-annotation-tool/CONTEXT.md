# Context: local report-review interface

Reviewers need to compare prior and current impressions, inspect a proposed structured abstraction, and record a human decision. The interface should make uncertainty and disagreement easy to record rather than forcing a binary correction.

The tool operates entirely in the browser. A reviewer selects a local JSON or JSONL file; no data is uploaded anywhere. The input must use fabricated examples during repository development and may use approved workspace data only in the cloud environment. Exported annotations remain local downloads and must be handled as protected data if derived from real reports.

Each displayed record should have a stable `transition_id`, prior/current impression strings, and an optional LLM output that follows `../03-report-abstraction/schema.json`. A useful annotation records the selected concept, reviewer state or abstention, evidence quote/notes, reviewer decision (`agree`, `modify`, `reject`, `uncertain`), and timestamp.

This is a teaching tool. It does not adjudicate radiology findings or decide which report is correct.