# Coding Agents for Research

> **Navigating Code, Tools, and Reproducible Science**

A modular curriculum on navigating coding agents in empirical research. Concepts are written once and are scenario-independent; each demo step has a **general** part (reusable on any data) and a labelled **Workshop example** for a scenario.

```text
content/concepts/<group>/<id>.md      concept pages (background, setup, practice, themes, reference)
content/beats/<role>/general.md       the reusable part of one demo step
content/beats/<role>/<scenario>.md    the scenario-specific example for that step
content/setup/                        generic setup primer + one page per scenario
content/tracks/                       the three tracks: concepts, demo, guided tutorial
scenarios/<name>/                     data kit, generator, reference solutions, checkpoints
scripts/build.py                      validate references; generate docs/ and mkdocs.yml
```

## Build and preview

```bash
uv run scripts/build.py                               # validate + generate docs/ and mkdocs.yml
uvx --with "mkdocs<2" --with mkdocs-material==9.7.7 mkdocs serve -a 127.0.0.1:8000
```

`docs/` and `mkdocs.yml` are generated; edit `content/` and `mkdocs.base.yml`.

## Tracks

- **Concept track** (`/concepts/…`): the ideas, each ending with links to the demo steps that apply it.
- **Demo track** (`/demo/…`): one worked example. Each step states the starting state it needs, so it can be done alone.
- **Guided tutorial** (`/tutorial/…`): one long path that interleaves concept pages and demo steps in a sensible order.

The validator checks every link between concepts, beats and tracks, and that each beat's prerequisites come earlier in the demo track.

## Adding a scenario

Add `content/setup/<scenario>.md` (with a `label`) and, for each beat, `content/beats/<role>/<scenario>.md` with `starts_from`, `produces`, and `prompt`. Beats missing a scenario simply show no tab for it.

## The toy scenario

`scenarios/toy/` holds a deterministic generator (`uv run build_kit.py`) for a synthetic three-clinic dataset with planted data problems and planted effects, a reference solution under `reference/`, and restorable `checkpoints/` (`python3 reference/make_checkpoints.py`). The planted truth is in `reference/truth.json`, outside the kit. All data is synthetic.
