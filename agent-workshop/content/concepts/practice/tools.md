---
id: tools
title: Tools — repeatable capabilities
short: Tools
themes: [recursive-ai, context-discipline]
related: [memory, secrets, costs, version-control]
blurb: Turning interactive prompts into parameterized scripts creates deterministic, testable tools that run identically on every execution.
---

In an agent workflow, a **tool** is any executable program, library, or network interface the agent can invoke to inspect the environment or modify state.

| Tool category | Examples | Key characteristics |
|---|---|---|
| **System & runtime utilities** | Python libraries, shell commands, LaTeX, Pandoc | Executes locally on the host; fast and deterministic |
| **External cloud APIs** | Bibliographic APIs, cloud databases, model endpoints | Interfaces with remote systems; requires authentication and network access |
| **Custom project scripts** | Tailored Python scripts with CLI arguments (`--help`) | Codifies custom analytical workflows; version-controlled within the project |

## Why programmatic tools outperform repeated prompts

Prompting an agent in natural language is well-suited for interactive data exploration, but natural language instructions remain probabilistic. A prompt may yield subtle variations in code logic, column naming, or floating-point formatting across repeated runs.

In contrast, codifying a procedure into a dedicated script provides distinct scientific advantages:
- **Determinism:** The script executes identical mathematical algorithms on every invocation.
- **Testability:** The tool can be benchmarked against synthetic datasets with known ground truth.
- **Decoupled execution:** The tool runs independently in standard terminal environments without requiring an active language model or incurring API token costs.

Transforming interactive workflows into durable tools represents the most reliable form of project memory ([Memory](concept:memory)).

## The workflow: from prompt exploration to validated tool

1. **Explore interactively:** Develop the analytical steps interactively with the agent, verifying intermediate tables.
2. **Package the script:** Direct the agent to synthesize the verified commands into a standalone Python script equipped with structured command-line arguments and standard help documentation (`--help`).
3. **Validate against baseline results:** Run the newly packaged script on the original dataset to confirm that output files match the interactive results.
4. **Implement automated assertion tests:** Add a unit test or validation script (e.g., using `pytest`) that asserts expected column names and summary totals against known benchmarks.
5. **Document and commit:** Add usage instructions to `README.md` and commit the script and test suite to version control ([Version control](concept:version-control)).

Using the agent to draft, refine, and test its own analytical scripts demonstrates the recursive application of AI to improve research software engineering.

## Integrating cloud APIs and batch model execution

When a research task involves processing hundreds or thousands of text records (e.g., classifying clinical notes or extracting structured entities), executing requests individually within an interactive chat session is inefficient. 

Instead, develop a standalone batch processing script that calls an API endpoint programmatically:
- **Validate on a representative pilot:** Test the classification prompt and parsing logic on 10 to 50 records before running the full dataset.
- **Estimate total API expenditure:** Calculate anticipated token volume and pricing before launching full-scale processing ([Costs](concept:costs)).
- **Implement rate limiting and checkpointing:** Incorporate retry logic with exponential backoff to handle transient API rate limits, and write partial outputs to disk so an interrupted run does not lose completed records.
- **Protect credentials and data:** Inject API keys via environment variables ([Secrets](concept:secrets)) and verify institutional authorizations for external data egress ([Privacy and data handling](concept:privacy)).

## Minimum documentation and testing standards

For any tool intended for ongoing research or collaboration, maintain a concise README section demonstrating an example invocation, an explanation of inputs and outputs, and an automated test against known reference values.

## Demo it

<!-- demos -->
