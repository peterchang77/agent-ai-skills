---
id: what-code-can-do
title: What code makes possible
themes: [text-formats]
related: [agent-vs-chat, inputs, outputs, tools]
blurb: If a task can be done on a computer, an agent can usually do it by writing and running code. Text-based formats make that far more reliable.
---

Because an agent acts through code ([Agent vs. chat](concept:agent-vs-chat)), its reach is the reach of code: nearly
anything that can be done electronically. "Code" here does not only mean software. It is also a way to *do* work.

## A short gallery

| Task | What the agent actually does | You get |
|---|---|---|
| Analyse a dataset | Writes a script that loads, cleans, and summarises it | Tables, statistics, the script itself |
| Make figures | Plots from the data with a plotting library | Image or vector files |
| Review literature | Queries a bibliographic service, saves records | Search log, BibTeX file |
| Build a website or dashboard | Writes HTML, CSS, and JavaScript | A page you open in a browser |
| Produce a report | Writes LaTeX or Markdown and compiles it | A PDF or document |
| Call a web service | Writes code that calls an API with your key | Results saved to files |
| Process files in bulk | Loops over hundreds of files | Converted, renamed, or extracted outputs |
| Generate media | Calls image, audio, or video tools | Media files |

Anything that sends, publishes, spends money, or contacts a person needs your approval first ([Steering](concept:steering)).

## The format rule

The agent works best when the material is **text-based source**, because it can read, edit, and regenerate text
exactly. Binary and visual formats must first be converted, and the conversion can lose information.

| Prefer (text source) | Over |
|---|---|
| LaTeX or Markdown | PDF, Word |
| CSV | Excel |
| HTML website | PowerPoint |
| Plain text, JSON | Screenshots of text |

You do not need to give up Word or Excel: work in the text format and convert at the end ([Inputs](concept:inputs), [Outputs](concept:outputs)).

## Why code beats clicking

Agents can also operate graphical programs by looking at the screen ("computer use"), which is useful when no other
route exists. For most tasks code is better: it is **repeatable** (rerun it on next month's data), **inspectable**
(you can read exactly what it did), and **fixable with one sentence** ("use the median, not the mean").

## What code cannot fix

- Missing or poor-quality data.
- A question that is not yet clear.
- Judgement calls about what a result *means*, which stay with you.

## How far can it go?

What an agent can do on its own improves quickly, so a task that failed a few months ago may work now. The reliable habit is to try a small version of a task first and see ([Scoping work](concept:scoping-work)).

## Demo it

<!-- demos -->
