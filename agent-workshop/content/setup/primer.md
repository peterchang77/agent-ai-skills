---
title: Setup
---

This page gets you to a working folder with an agent running inside it. You do it once; the other pages assume it is done.
Each demo step also tells you which starting state it needs, so you can jump in anywhere ([Restore a starting point](#restore-a-starting-point)).

## 1. Install an agent

Install a coding-agent harness from the vendor's own instructions. Many are a one-line install script
(`curl ... | sh`). Read a script before running it, and install only from the vendor's site. For the choices and
trade-offs, see [Harnesses and models](concept:harnesses). Your institution may also restrict which tools and models
you may use with real data ([Privacy](concept:privacy)).

## 2. Make a project folder

An agent works in the folder where you start it, so start it in the right one.

```bash
mkdir -p ~/workshop-demo     # create the folder
cd ~/workshop-demo           # go into it
pwd                          # confirm where you are
```

`ls` lists what is here and `cd ..` goes up one level. For more on paths, permissions, and safe habits, see the
[Linux command line](guide:linux-command-line-for-coding-agents) guide.

## 3. Check the tools

```bash
uv --version         # Python environments and packages
pdflatex --version   # only needed for the PDF-report steps
pandoc --version     # only needed for the Word-export step
```

Anything missing can be installed by the agent when a step needs it ([Environment](concept:environment)); approve installs deliberately.

## 4. Add the data for your scenario

See the tabs under [Your scenario's data](#your-scenarios-data) below.

## Restore a starting point

Each demo step names the state it starts from, such as the data kit or a checkpoint. A checkpoint is a complete
project folder. To start a step cleanly, use an empty folder and copy the checkpoint into it:

```bash
rm -rf ~/workshop-demo && mkdir ~/workshop-demo      # only if you are sure this folder is disposable
cp -r <scenario folder>/checkpoints/<name>/. ~/workshop-demo/
cd ~/workshop-demo
```

Then start the agent in that folder. Keeping a pristine copy of the kit lets you reset between attempts, and
[version control](concept:version-control) gives you the same ability for your own work.

## If your agent gives different results

Live agents vary: a different route, different file names, slightly different wording. That is normal. Each step lists
what to check and the reference results, so you can judge whether your result is right even if the path differs.
