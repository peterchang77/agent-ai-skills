---
id: agent-vs-chat
title: Agent vs. chat
themes: [text-formats, recursive-ai]
related: [what-code-can-do, harnesses, verification]
blurb: A chat model answers from memory inside an empty box. An agent has a computer, so it can read your files, run code, and show evidence.
---

Most people first meet AI as a **chat**: you type a question, the model answers from what it learned in training. An
**agent** is the same kind of model connected to a computer. That connection changes what you can ask for and what
you must check.

![Chat compared with an agent. A chat model works only with text you paste in. An agent runs code in a local terminal, reads and writes local files, and fetches data from APIs and the web, inside an autonomous loop of acting, observing and fixing.](image:agent-vs-chat)

## The distinction, stated cleanly

| | Chat | Agent |
|---|---|---|
| Knowledge | Training data only | Training data **plus** your files, tools, and the web |
| Actions | None; you copy and paste | Reads, writes, runs, installs, fetches |
| Evidence | "Trust me" | Scripts, logs, and files you can inspect |
| Main risk | A confident wrong answer | The same, **plus** it can change things on your computer |
| Best for | Quick questions, brainstorming, drafting | Multi-step work on real files and data |

Real products blur this line somewhat, as the last section explains.

## How an agent acts on the world

An agent interacts with the world through **text**. It writes commands and code; a program called the
[harness](concept:harnesses) runs them and hands the output back as more text. That one mechanism is enough to
reach almost anything on a computer ([What code makes possible](concept:what-code-can-do)).

### The agent loop

![The agent loop. Starting from your directive, the agent observes the environment and files, acts by writing and running code, and evaluates the output and errors. It repeats until the result is verified, then returns artifacts and a summary.](image:agent-loop)

The loop explains two behaviours you will see constantly:

- **It can check its own work.** It runs the code, reads the error, and fixes it, so you often get working results rather than plausible text.
- **It can run up cost and time.** Each pass through the loop adds to the conversation ([Context](concept:context), [Costs](concept:costs)), and an agent that is stuck can loop for a long time.

## When to use which

- **Use chat** for a quick question, brainstorming, or editing a paragraph you paste in. It is faster, needs no setup, and exposes nothing on your computer.
- **Use an agent** when the work involves your files or data, several steps, running code, or producing files that must be reproducible.

## What stays the same

An agent is still a language model. It can be wrong, it can misread a file, and it can say a task is done when it is not. The difference is that an agent leaves *evidence* (scripts, logs, outputs) you can check, which is why [Verification](concept:verification) is a core habit.

## Where the line blurs

Some chat products already offer file upload, web search, or a code sandbox, and some agents are restricted to a single folder. A more accurate picture is a spectrum of **access** (your files, code execution, the web, your own computer) and **control** (what you approve). The agent end of the spectrum is where the
[approval modes](concept:steering) and [isolation choices](concept:sandboxing) matter.

## Demo it

<!-- demos -->
