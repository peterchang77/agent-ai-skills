Each demo module follows a standardized structure:

1. **Background**: Core context and prerequisites for the immediate task.
2. **General methodology**: Reusable prompt patterns and computational techniques applicable to any dataset.
3. **Workshop example**: A concrete demonstration using this track's benchmark dataset.
4. **Verification criteria & common pitfalls**: Targeted guidance for evaluating outputs and troubleshooting discrepancies.
5. **Supporting concepts**: Direct references back to foundational principles in the concept track.

## Modular progression and checkpoints

You do not need to execute the demo from start to finish in a single pass. Every exercise defines an explicit **starting state**, consisting of either the initial dataset or a saved checkpoint reflecting earlier results. The [Setup](setup.md#restore-a-starting-point) guide provides instructions for restoring any checkpoint, allowing you to jump directly into specific exercises.

## Exercise categories

| Category | Description |
|---|---|
| Full step | Core stages of the research pipeline |
| Quick step | Focused, high-leverage administrative or environment checks |
| Optional detour | Deep-dive tasks that enrich the analysis without blocking subsequent steps |
| Advanced | Exercises requiring external API credentials or cloud budget |

## Adapting to proprietary data

The general methodologies apply universally to empirical datasets. The workshop example demonstrates how these techniques operate on data with known answers. Before adapting these workflows to proprietary or sensitive institutional data, consult [Privacy and data handling](concept:privacy) and [Secrets](concept:secrets).
