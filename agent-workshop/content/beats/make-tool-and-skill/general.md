---
role: make-tool-and-skill
title: Turn the analysis into a tool and a skill
kind: full
summary: Package proven analytical pipelines into tested, parameterized command-line tools and modular agent skills for persistent reproducibility.
time: 10 min
teaches: [tools, memory, verification]
needs: [add-agents-md, analyze-pilot]
---

In this exercise, you package an interactive multi-step analysis into a tested command-line script and author an agent skill that instructs future sessions when and how to invoke it. Codifying workflows into standalone tools represents the most durable form of project memory: executing future analyses requires a concise instruction rather than an extended exploratory conversation.

**Before you start:** A verified analysis script, input datasets, and output tables ([Setup](setup:restore-a-starting-point)).

## Background

Prompt-driven analytical sessions remain probabilistic: repeating an analysis via conversational prompts can introduce subtle discrepancies in column naming, statistical packages, or output formatting. 

In contrast, a **deterministic tool** (a Python script with explicit arguments and `--help` documentation) executes the exact same mathematical logic every time, runs independently of the language model, and can be validated with regression tests ([Tools](concept:tools)).

An **agent skill** is a modular instruction runbook housed in its own directory that specifies *when* the agent should invoke the tool and *how* to evaluate its output, eliminating the need to re-explain procedures in future sessions ([Memory](concept:memory)).

| Component | Responsibility | Technical properties |
|---|---|---|
| **Executable tool** | Analytical execution logic | Deterministic, parameterized, tested against reference data |
| **Tool documentation (`README.md`)** | Usage instructions, arguments, sample calls | Human-readable specification |
| **Agent skill (`SKILL.md`)** | Invocation criteria, exact CLI syntax, validation rules | Machine-readable runbook ingested dynamically by the harness |
| **Standing instructions (`AGENTS.md`)** | Repository-wide guardrails and directory paths | Ingested at session initialization across all tasks |

## General methodology

1. **Package into a parameterized script:**

```text
Consolidate data cleaning, cohort definition, and statistical modeling into an executable CLI tool: scripts/pilot_report.py.
Provide structured arguments for input datasets and output destination directories, with full --help documentation.
Ensure the tool does not modify input datasets. Provide a concise README.md detailing usage.
```

2. **Implement regression testing:** Execute the script on baseline data and confirm that generated metrics match previously verified results. Implement an automated validation test (via `pytest` or an assertion script) that verifies core statistical estimates against known benchmarks.

3. **Author the modular skill:**

```text
Create a custom skill in .agents/skills/pilot-report/SKILL.md (under 40 lines) specifying:
- Trigger criteria: when to invoke this tool.
- Exact CLI execution syntax and required arguments.
- Verification checks to execute on generated output files.
Do not duplicate tool README documentation; reference the script directly.
```

4. **Verify skill discovery:** Launch a clean agent session, request an updated report on the data, and verify that the agent autonomously discovers and executes the skill.

<!-- example -->

## Verification criteria

- **Numerical reproducibility:** The packaged tool reproduces earlier empirical point estimates and sample counts exactly.
- **Automated test assertions:** The test suite passes on valid data and fails if key numerical values or column schemas are altered.
- **Skill conciseness:** The `SKILL.md` file remains under 40 lines, providing targeted invocation guidelines without redundant documentation.
- **Credential hygiene:** The skill, tool, and documentation contain zero hardcoded secrets.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Agent fails to invoke the skill in fresh sessions | Skill file path does not match harness discovery conventions, or trigger description is vague | Verify your harness's expected skill directory path; clarify the description in `SKILL.md` |
| Tool outputs diverge from prior results | Data filtering or modeling logic was altered during script consolidation | Conduct step-by-step diff comparisons between the original exploratory script and the consolidated CLI script |
