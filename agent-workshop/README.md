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
- **Demo tracks** (`/demo-<scenario>/…`): one worked example per scenario (`demo-clinical`, `demo-imaging`). Each step states the starting state it needs, so it can be done alone.
- **Guided tutorials** (`/tutorial-<scenario>/…`): one long path per scenario that interleaves concept pages and demo steps in a sensible order.

Scenarios are parallel: each has `content/setup/<scenario>.md`, `content/tracks/demo-<scenario>.md` and `content/tracks/tutorial-<scenario>.md`. The header shows Demo and Tutorial as dropdowns with one entry per scenario. Shared track text lives in `content/snippets/`. The internal id of the clinical scenario is `toy`.

The validator checks every link between concepts, beats and tracks, and that each beat's prerequisites come earlier in the demo track.

## Adding a scenario

Add `content/setup/<scenario>.md` (with a `label`, `own_track: true` and `dir`), a demo and a tutorial track page with `scenario:`, and, for each beat in the track, `content/beats/<role>/<scenario>.md` with `starts_from`, `produces`, and `prompt`. A scenario track may only include beats that have an example for it.

## The toy scenario

`scenarios/toy/` holds a deterministic generator (`uv run build_kit.py`) for a synthetic three-clinic dataset with planted data problems and planted effects, a reference solution under `reference/`, and restorable `checkpoints/` (`python3 reference/make_checkpoints.py`). The planted truth is in `reference/truth.json`, outside the kit. All data is synthetic.

## Installers

`assets/install.sh` and `assets/install.ps1` take `--scenario clinical|imaging` (`-Scenario` in PowerShell). Clinical downloads the published `toy-kit` and `toy-checkpoints` zips. Imaging downloads the small published `imaging-tools` zip (the build scripts), uses `uv` to build the 74 MB kit locally from the public image sample (and optionally the checkpoints), and copies the result into the project folder without overwriting your changes. `scripts/build.py` publishes the zips under `docs/downloads/`. Test locally with `python3 -m http.server` in `docs/` and `WORKSHOP_BASE_URL=http://127.0.0.1:PORT`.
