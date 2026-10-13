---
id: privacy
title: Privacy and data handling
themes: [recursive-ai]
related: [secrets, sandboxing, harnesses, inputs]
blurb: Data read by an agent is transmitted to the model provider as context. Determining whether data is permitted to leave your infrastructure must precede deciding what tasks to delegate.
---

## The primary governance question

In empirical and clinical research, institutional compliance policies determine how data may be processed. Before asking what an agent can accomplish, researchers must first address the foundational compliance question: **Is this dataset authorized for transmission to this specific model endpoint under current institutional data agreements?**

Because agent harnesses transmit file excerpts, terminal logs, and prompt instructions to the model provider during execution, analyzing a file with a cloud-backed agent constitutes external data egress.

## A four-step compliance workflow

1. **Classify data sensitivity:** Categorize the dataset according to institutional governance tiers (e.g., public, internal, confidential, or regulated data such as Protected Health Information or student records).
2. **Verify institutional authorizations:** Identify which model providers, enterprise agreements, and cloud tenants are approved for that data tier by institutional privacy, security, and research compliance boards.
3. **Select matching endpoints:** Use strictly approved enterprise endpoints for sensitive data, avoiding personal or consumer-tier accounts regardless of convenience.
4. **Enforce local environmental boundaries:** Restrict where data files reside locally, control access to session transcripts, and isolate network interfaces ([Sandboxing](concept:sandboxing)).

## Key evaluation criteria for model providers

| Governance criterion | Analytical implications |
|---|---|
| **Data retention periods** | Identifies whether the provider logs prompt payloads or intermediate files, and for how long. Short retention windows reduce exposure risks. |
| **Model training policies** | Distinguishes whether customer inputs are excluded from future model training. Enterprise and business contracts typically prohibit model training on customer data. |
| **Business Associate / Data Use Agreements** | Confirms whether formal legal protections (such as a HIPAA Business Associate Agreement or GDPR Data Processing Agreement) cover the endpoint. |
| **Data residency and regional routing** | Establishes where inference servers and data processing pipelines physically operate, which is critical for jurisdiction-specific compliance. |

Terms of service differ dramatically between consumer web interfaces, commercial API endpoints, and enterprise cloud agreements. A model's brand name does not define its data handling terms—always verify the legal agreement governing your specific account.

## Cloud vs. local models

- **Cloud-hosted models:** Offer cutting-edge reasoning and programming capabilities. Data leaves the local machine under terms specified by the provider agreement, which can meet strict compliance standards when enterprise contracts are established.
- **Locally deployed models:** Keep all data within the local workstation or institutional cluster. While local models reduce data egress concerns, they require specialized hardware and currently offer lower reasoning capability on complex analytical tasks.

The optimal approach depends on your data classification tier and institutional policy.

## Practical habits for research workflows

- **Adhere strictly to sanctioned pathways:** Use institutional enterprise endpoints when analyzing proprietary research data.
- **Prototype workflows using synthetic or de-identified data:** Use synthetic benchmarks to develop pipelines safely, transitioning to real data only within approved environments.
- **Minimize exposed context:** Rather than loading complete datasets into the agent session, provide schemas and representative samples for script generation, then run the resulting scripts locally on the full data.
- **Recognize re-identification risks:** Structured de-identification does not guarantee anonymity. Free-text clinical notes, low cell counts, or rare demographic combinations can lead to re-identification.
- **Audit local session logs:** Agent harnesses maintain local transcripts of conversations and terminal outputs. Ensure session history directories do not inadvertently store unredacted records or [secrets](concept:secrets).
- **Exclude datasets from version control:** Never commit sensitive datasets or patient identifiers to Git repositories ([Version control](concept:version-control)).

## Workshop benchmark data

The dataset supplied in this workshop is entirely synthetic, allowing participants to practice workflows without compliance concerns. When adapting these patterns to institutional research, apply the compliance framework detailed above.
