---
role: add-agents-md
title: Make the agent remember with AGENTS.md
kind: full
summary: Start a fresh session and watch the agent forget your decisions; then write the rules to a short file it reads every time.
time: 8 min
teaches: [memory, context, steering]
needs: [clean-data]
---

An agent forgets everything between sessions, so every new session starts by re-asking questions you already answered. After this
step you will know how to fix that with a short instructions file, and you will have seen the fix work.

**Before you start:** a project in which you have already made decisions you do not want to repeat, such as cleaning rules
([Setup](setup:restore-a-starting-point) if you need a starting state).

## Background

When a session ends, the conversation is gone ([Context](concept:context)). What persists is **files**. An **`AGENTS.md`** file in the
project folder is read automatically at the start of each session, which makes it the cheapest form of memory
([Memory](concept:memory)). It should be short and specific: where things are, what the rules are, and what never to do. Everything in
it is loaded into context every time, so length has a cost.

## General approach

1. **See the problem.** Start a new session in the project and ask a question that depends on your earlier decisions. Notice what the agent has to ask or guesses wrong.
2. **Write the rules.** Ask the agent to draft the file from what you have decided, then review it.

```text
Create AGENTS.md in this folder, under 25 lines, capturing: where the data and data dictionary live; the decisions we made and why;
where outputs go; what must never be modified; and how to report numbers. Be specific. Leave out anything you could work out from the code.
```

3. **Test it.** Start another new session and repeat the question from step 1. The agent should now apply the rules without asking.
4. **Improve it.** Ask: "Review AGENTS.md and remove anything vague or redundant." Using the agent to improve its own instructions is a habit worth keeping ([steering](concept:steering)).

<!-- example -->

## What to check

- The file is short, specific, and consistent with your actual decisions.
- It contains no secrets and no sensitive data ([Secrets](concept:secrets)).
- In the test session, the agent cited or followed the file.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| The agent ignores the file | It is not named or placed where the harness looks | Check your harness's convention for the filename and location |
| A long, generic file | The prompt did not ask for specifics | Cut it to the rules that would have prevented a real mistake |
| Rules that contradict the data | The file was drafted before decisions were final | Reconcile it with `notes/cleaning-decisions.md` |
