# Agent-Assisted Clinical Research Workshop

This archive is a small set of research briefs for a live, agent-assisted workshop. Each exercise has one participant-visible file, `AGENT_CONTEXT.md`. It provides the domain facts, resource locations, safety boundary, and desired outcome that a researcher would otherwise have to explain repeatedly to an agent.

## Participant workflow

1. Open the exercise’s `AGENT_CONTEXT.md`.
2. Write your own request to your agent. Ask it to read that context and inspect the workspace before making assumptions.
3. Review the agent’s proposed approach, direct implementation, run its checks, and inspect the resulting artifact.
4. Iterate when evidence exposes a flaw.

The context is not a ready-made prompt or implementation plan. You decide how to request, scope, and review the work.

| Exercise | Artifact the agent should create |
|---|---|
| [01 Data discovery](01-data-discovery/AGENT_CONTEXT.md) | a safe small-export/discovery CLI |
| [02 Cohort curation](02-cohort-curation/AGENT_CONTEXT.md) | an auditable chronological cohort manifest |
| [03 Report abstraction](03-report-abstraction/AGENT_CONTEXT.md) | a resumable LLM extraction/validation pipeline |
| [04 Annotation tool](04-annotation-tool/AGENT_CONTEXT.md) | a single-file local review interface |
| [05 Modeling](05-modeling/AGENT_CONTEXT.md) | a simple selected-and-locked baseline evaluation |
| [06 Results and writing](06-results-and-writing/AGENT_CONTEXT.md) | figures, a LaTeX results report, and verified citations |

## Instructor workflow

The answer keys, live-demo prompts, reference implementations, common failure modes, and troubleshooting material must be provisioned **outside this checkout**—for example, in a separate private instructor repository or a separately mounted directory. Do not hide them in a dot directory within the participant workspace: an agent that can access them can read them.

Project the answer key during the demonstration or share it only after independent work. Participants can either work along with their agents or review the demonstrated result.

## What this archive includes

The `tools/` directory contains setup helpers only. It intentionally does not contain the primary artifacts participants are meant to ask agents to build. The cloud environment supplies approved data access, a local/institutional LLM endpoint, and its deployment-specific documentation.

## Data handling

CheXpert Plus data and derived artifacts remain subject to the applicable data-use agreement. Do not commit raw reports, images, exports, endpoint logs, credentials, signed URLs, or tokens. Use only instructor-approved data locations and endpoints. This workshop produces report-derived weak pseudo-labels and agreement metrics; it does not establish clinical ground truth, diagnostic performance, or clinical utility.
