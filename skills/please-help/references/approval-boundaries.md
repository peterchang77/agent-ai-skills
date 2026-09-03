# Approval Boundaries

Planning or inspecting is not approval to take a consequential action. Pause and ask for explicit approval before crossing one of these boundaries. State the specific action, target or destination, likely effect, main risk, and a safer or staged alternative where useful.

| Boundary | Examples | Default response |
| --- | --- | --- |
| Destructive or broad file changes | deletion, overwrite, recursive rename/move, broad permission changes | Show targets and a dry run/backup/reversible alternative; wait for approval. |
| Source or authoritative material | editing raw data, correcting records, changing a source document | Preserve it and create derived work; ask before changing the source. |
| External sharing or publication | email, chat message, issue comment, upload, website, social post | Draft locally and wait for approval of recipient/destination and content. |
| Network, credentials, and secrets | API calls, cloud storage, service login, environment credential use | Explain destination, data sent, cost/permission impact, and local alternative; wait for approval. |
| Cost or resource commitment | paid APIs, cloud resources, large model calls, bulk processing | Inventory the work, state resource drivers and a pilot; wait for budget/scope approval. |
| Private, sensitive, or production material | client data, personal data, health/financial records, production systems | Use authorized copies/test data when possible; confirm access and handling boundary first. |
| Dependencies and system changes | new packages, system packages, toolchain changes, services | Inspect existing tools; explain purpose and impact; wait when the change is material. |
| Git collaboration or history | push, PR creation/merge, branch deletion, reset, clean, force push | Show status/diff/target and safer alternatives; wait for approval. |

## Safe defaults

- Use fictional, public, synthetic, or authorized-copy data for examples and learning.
- Never request, show, log, commit, or paste secret values into chat.
- Prefer a small read-only inventory or pilot before a large operation.
- Preserve raw/source inputs and write outputs separately.
- When a boundary is crossed unexpectedly during execution, stop and return to a concise recommendation. Do not silently expand scope.

## Asking for approval plainly

> The next step would send these files to an external service and may use the configured account. I can instead run a local check first. Do you approve the external request to this destination?

> This would recursively change permissions under `project/`. I can first show the affected paths and test the change on a small directory. Do you approve that staged approach?
