---
id: privacy
title: Privacy and data handling
themes: [recursive-ai]
related: [secrets, sandboxing, harnesses, inputs]
blurb: Anything the agent reads may be sent to a model provider. Decide whether your data may go there before deciding what the agent can do with it.
---

*General guidance only. Your institution's policies, agreements, and approvals determine what is actually allowed. This page helps you ask the right questions.*

## The first question

Everything an agent reads, plus your messages and its replies, is sent to the model. So the question "can the agent
do this?" comes second. The first is **"may this data go to this model, under this agreement?"**

## A decision in four steps

1. **Classify the data.** Public, internal, confidential, or regulated (for example health, student, or financial records).
2. **Find out what your institution approves.** Which model endpoints, accounts, and tools are sanctioned for that class of data? Who decides? (Often a security, privacy, or research-compliance office.)
3. **Choose the endpoint to match.** Use only approved routes for regulated data, whatever the convenience of another tool.
4. **Match the isolation and handling.** Where the files live, who can see transcripts, and what leaves the machine ([Sandboxing](concept:sandboxing)).

## What differs between options

| Question to ask | Why it matters |
|---|---|
| Are prompts and files **retained**? For how long? | Retention determines exposure if the provider is breached or compelled to disclose. |
| Are they used for **training**? | Often differs between free consumer products and business or API terms. |
| Is there a **data agreement** covering your data class? | Regulated data generally requires a specific agreement with the provider or platform. |
| Where is it **processed** and by whom? | Region and subprocessors can matter for some policies. |

Consumer, business, API, and cloud-platform offerings often carry different terms, so a model name alone tells you nothing about the data handling. Look up the terms of the *specific* route you are using.

## Cloud versus local models

- **Cloud (hosted) models** are the most capable. Data goes to the provider under its terms, which may be strong when an institutional agreement is in place.
- **Local models** keep data on your machine, which can simplify some approvals. At the time of writing they are generally less capable and need suitable hardware.

Neither is automatically right. The choice follows your data class and what your institution supports.

## Practical habits

- **Use the approved route for real data.** Many organisations provide endpoints approved for sensitive data; use those, and use them consistently.
- **Use synthetic or de-identified data when it is enough.** This is a convenience for demonstrations, sharing examples, and testing a method. It is not a replacement for approved real-data workflows when real data is the point.
- **Share the minimum.** Often the schema and a small sample are enough for the agent to write code that you then run on the full data.
- **De-identification is not automatic safety.** Free-text notes, small cell counts, and rare combinations of fields can re-identify people.
- **Mind the transcript.** Session records may be stored locally or by the provider. Keep [secrets](concept:secrets) and unnecessary identifiers out of anything the agent reads.
- **Keep sensitive data out of Git.** Version control keeps history, and a public repository exposes it ([Version control](concept:version-control)).

## The workshop data

The supplied example dataset is synthetic so that anyone can follow along without approvals. When you adapt the
steps to your own data, the examples on each page still apply, subject to the decision above.
