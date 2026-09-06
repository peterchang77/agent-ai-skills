# Acceptance: annotation tool

Open the file directly in a browser and load a fabricated local review file.

## Required manual checks

- No network request is needed to load, use, or export the tool.
- Reports render as text; an input containing `<b>text</b>` does not create bold markup.
- Navigation retains annotations for previously visited records.
- Every export record retains its source `transition_id` and reviewer fields.
- An explicit uncertain/abstain path is usable.
- The exported JSON can be parsed with `python -m json.tool`.
- Keyboard users can select controls and export without a mouse.

## Review questions

- Could a reviewer distinguish the LLM proposal from their own judgement?
- Does the interface accidentally force an answer when evidence is insufficient?
- Is this deliberately small tool easier to inspect than a framework application would be?