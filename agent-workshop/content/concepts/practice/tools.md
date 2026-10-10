---
id: tools
title: Tools — repeatable capabilities
short: Tools
themes: [recursive-ai, context-discipline]
related: [memory, secrets, costs, version-control]
blurb: A tool is anything the agent can run. When a task will recur, turn it into a script so it behaves the same way every time.
---

A **tool** is anything the agent can run to get something done.

| Kind | Examples |
|---|---|
| Local software | Commands, Python libraries, LaTeX, `pandoc` |
| Cloud services | A web API, a database, an LLM API |
| Tools you write | A script with a command-line interface (`--help`) |

## Why a tool beats a prompt for repeatable work

A prompt is interpreted differently each time. A script runs the same way, can be **tested** against known answers, runs
without the model, and costs nothing per use. This is why a tool is the strongest form of [memory](concept:memory).

## Turn a task into a tool

1. Do the task once with the agent, interactively.
2. Ask it to turn the steps into a script with arguments and `--help`.
3. Run it on the same input and confirm the output matches.
4. Test it against a case where you know the answer.
5. Document it in the `README.md` and keep it in [version control](concept:version-control).

Using the agent to build the tool, and then reviewing the tool, is the "use AI recursively" pattern in practice.

## Cloud APIs and bulk LLM calls

For hundreds or thousands of items (classifying notes, extracting fields), write a script that calls an LLM API for each
item rather than working through them in chat. A few things to plan for:

- **Test on a handful first**, then estimate the total cost before running everything ([Costs](concept:costs)).
- **Handle rate limits and retries**, and **save partial results** so a failure does not lose everything.
- **Validate the outputs** against a labelled sample.
- **Use credentials safely** ([Secrets](concept:secrets)), and check that your data is allowed to go to that endpoint ([Privacy](concept:privacy)).

## Trust requires documentation and tests

A short README with an example run, and a check against known answers, is the minimum for a tool you or others will rely on.

## Demo it

<!-- demos -->
