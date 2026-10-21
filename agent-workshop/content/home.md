<div class="wk-hero" markdown>

# Coding Agents for Research

### Navigating Code, Tools, and Reproducible Science

A practical course for researchers ready to put AI coding agents to work on empirical data. You’ll learn how to collaborate with assistants that read your files, execute code, and show their work, focusing on the critical habits that keep your findings verifiable and reproducible.

</div>

## Core competencies

- **Differentiate agentic workflows from conversational chat**, selecting harnesses and models tailored to your security requirements.
- **Master context management**, structuring inputs and outputs to prevent attention degradation and excessive token consumption.
- **Implement rigorous verification practices**, validating computational steps using independent execution, automated tests, and multi-agent peer reviews.
- **Execute end-to-end data analyses**, transforming raw observational data into cleaned datasets, statistical models, verified citations, and reproducible reports.
- **Codify workflows into durable assets**, packaging scripts into deterministic command-line tools and version-controlled agent skills while managing credentials securely.

<div class="grid cards" markdown>

-   :material-lightbulb-on-outline: **Concept track**

    ---

    Modular explorations of core principles, designed for sequential reading or reference.

    [:octicons-arrow-right-24: Explore concepts](concepts/index.md)

-   :material-flask-outline: **Demo track**

    ---

    An end-to-end empirical case study structured into modular, restorable exercises.

    [:octicons-arrow-right-24: Clinical](demo-clinical/index.md) · [:octicons-arrow-right-24: Imaging](demo-imaging/index.md)

-   :material-map-marker-path: **Guided tutorial**

    ---

    A unified, step-by-step curriculum pairing theoretical background with hands-on practice.

    [:octicons-arrow-right-24: Clinical](tutorial-clinical/index.md) · [:octicons-arrow-right-24: Imaging](tutorial-imaging/index.md)

</div>

## Track comparison

| Track | Primary focus | Recommended usage |
|---|---|---|
| **Concept track** | Methodological principles and guardrails | Gaining foundational understanding and looking up specific topics |
| **Demo track** | Practical execution on realistic files | Observing hands-on patterns and adapting code templates to your data |
| **Guided tutorial** | Integrated, progressive workflow | Following a complete, end-to-end path without managing navigation |

All tracks utilize the same core modules. Each concept page links directly to corresponding practical steps, and each demo exercise references supporting theory, enabling seamless movement between tracks.

## Choosing your starting point

| If your immediate priority is... | Recommended path |
|---|---|
| Building a comprehensive understanding from scratch | Guided tutorial: [Clinical](tutorial-clinical/index.md) or [Imaging](tutorial-imaging/index.md) |
| Running code immediately with an existing agent | Demo track: [Clinical](demo-clinical/index.md) (clinic data) or [Imaging](demo-imaging/index.md) (chest radiographs) |
| Reviewing architecture, safety, and operational patterns | [Concept track](concepts/index.md) |
| Ensuring compliance before handling proprietary data | [Privacy and data handling](concept:privacy) and [Secrets](concept:secrets) |
| Solving a specific data or coding task | The relevant exercise in the [Clinical](demo-clinical/index.md) or [Imaging](demo-imaging/index.md) demo, followed by its supporting concepts |
| Instructing students or research colleagues | The guided tutorial ([Clinical](tutorial-clinical/index.md) or [Imaging](tutorial-imaging/index.md)), using each step's example as a classroom exercise |

## Two worked examples

The demo and tutorial tracks come in two parallel versions that follow the same steps and teach the same concepts. Each exercise provides a generalized approach suitable for any research domain alongside a concrete **Workshop example** from the version you chose. Pick the one closer to your work, or do both.

| | Clinical | Imaging |
|---|---|---|
| **Story** | A three-clinic network: target attainment and a follow-up call pilot | An AI tool for pneumothorax on chest radiographs: is it ready for a pilot? |
| **Data** | Synthetic visits, spreadsheet, Word, PDF, HTML and database files | A public sample of real chest radiographs (DICOM), model scores and reports, with synthetic problems added |
| **Distinctive** | Many file formats; an observational analysis with confounding | Pixel-level checks and a viewer; evaluating an AI model with intervals |

## Also in this repository

- [Introducing coding agents](guide:introducing-coding-agents)
- [Linux command line for coding agents](guide:linux-command-line-for-coding-agents)
- [Git and GitHub for coding agents](guide:git-and-github-for-coding-agents)
