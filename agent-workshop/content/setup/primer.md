---
title: Setup
---

Get a working folder with an agent running inside it. You do this once, and the other pages assume it is done.
Each demo step also tells you which starting state it needs, so you can jump in anywhere ([Restore a starting point](#restore-a-starting-point)).

## Quickstart

One command downloads the practice data and installs a coding agent (Kiro CLI), so you can start the demo straight away. It works on Linux, macOS and
Windows with WSL:

```bash
curl -fsSL https://peterchang77.github.io/agent-ai-skills/install.sh | bash
```

What it does:

- **Asks a few questions.** Where to put the data (default `~/workshop-demo`), whether to also download the checkpoints, and whether to install the agent.
- **Downloads the data.** It fetches the toy dataset, checks it arrived intact, and unpacks it into that folder.
- **Installs the agent.** It runs the vendor's installer after showing you the address, and skips this if the agent is already installed.
- **Is safe to repeat.** Files that are already up to date are not downloaded again. Files you have changed are kept, and only replaced if you add `--force`, which first copies the old versions into a sibling backup folder.

When it finishes, start the agent inside that folder:

```bash
cd ~/workshop-demo
```

If you chose a different folder, use it wherever the other pages say `~/workshop-demo`. Options go after `bash -s --`, for example `bash -s -- --dir ~/my-folder --yes --checkpoints --no-agent`; run it with `--help` to see them all.
Because the script is fetched from the internet, you can read it first at
[install.sh](https://peterchang77.github.io/agent-ai-skills/install.sh), and your institution may restrict which tools you can install.
The practice data is synthetic. Before you use your own data, read [Privacy](concept:privacy).

## Custom setup

Prefer to do it yourself, use a different agent, or work on a managed machine? These steps do the same job by hand.

### 1. Install an agent

Install a coding-agent harness from the vendor's own instructions. Many are a one-line install script
(`curl ... | sh`). Read a script before running it, and install only from the vendor's site. For the choices and
trade-offs, see [Harnesses and models](concept:harnesses). Your institution may also restrict which tools and models
you may use with real data ([Privacy](concept:privacy)).

### 2. Make a project folder

An agent works in the folder where you start it, so start it in the right one.

```bash
mkdir -p ~/workshop-demo     # create the folder
cd ~/workshop-demo           # go into it
pwd                          # confirm where you are
```

`ls` lists what is here and `cd ..` goes up one level. For more on paths, permissions, and safe habits, see the
[Linux command line](guide:linux-command-line-for-coding-agents) guide.

### 3. Check the tools

```bash
uv --version         # Python environments and packages
pdflatex --version   # only needed for the PDF-report steps
pandoc --version     # only needed for the Word-export step
```

The [Prepare your environment](beat:prepare-environment) step has the agent check these and install what is missing ([Environment](concept:environment)); approve installs deliberately.

### 4. Add the data for your scenario

See the tabs under [Your scenario's data](#your-scenarios-data) below. (The quickstart has already done this for the toy dataset.)

## Restore a starting point

Each demo step names the state it starts from, such as the data kit or a checkpoint. A checkpoint is a complete
project folder. To start a step cleanly, use an empty folder and copy the checkpoint into it:

```bash
rm -rf ~/workshop-demo && mkdir ~/workshop-demo      # only if you are sure this folder is disposable
cp -r <scenario folder>/checkpoints/<name>/. ~/workshop-demo/
cd ~/workshop-demo
```

If you used the quickstart with `--checkpoints`, they are in `~/workshop-demo-checkpoints/<name>/`, which replaces `<scenario folder>/checkpoints/<name>` above.

Then start the agent in that folder. Keeping a pristine copy of the kit lets you reset between attempts, and
[version control](concept:version-control) gives you the same ability for your own work.

## If your agent gives different results

Live agents vary: a different route, different file names, slightly different wording. That is normal. Each step lists
what to check and the reference results, so you can judge whether your result is right even if the path differs.
