---
title: Setup
---

Before beginning the exercises, configure a dedicated project directory with an active coding agent. You only need to perform this setup once; subsequent tutorial modules assume this environment is in place.

Each demo step specifies its required starting state, allowing you to jump directly into any exercise ([Restore a starting point](#restore-a-starting-point)).

## Quickstart

An automated setup script installs the sample data and configures a coding agent (Kiro CLI). The script runs on Linux, macOS, and Windows via WSL:

```bash
curl -fsSL https://peterchang77.github.io/agent-ai-skills/install.sh | bash
```

The script performs the following actions:

- **Prompts for configuration preferences:** Confirms the destination directory (defaulting to `~/workshop-demo`), asks whether to download intermediate checkpoints, and checks whether to install the agent.
- **Retrieves the benchmark dataset:** Downloads the synthetic clinical dataset, verifies data integrity against SHA-256 checksums, and unpacks the archive into your chosen directory.
- **Configures the agent:** Downloads and runs the official agent installer after displaying the source URL. This step is skipped if an agent is already detected.
- **Ensures idempotent execution:** Re-running the script updates missing files without overwriting local modifications unless you explicitly pass the `--force` flag (which creates a timestamped backup before replacing files).

Once the script completes, change into the project directory and launch your agent:

```bash
cd ~/workshop-demo
```

If you chose a custom folder, use that path wherever this guide references `~/workshop-demo`. Advanced flags can be passed after `bash -s --` (for example, `bash -s -- --dir ~/my-folder --yes --checkpoints --no-agent`); pass `--help` to inspect all options.

> [!NOTE]
> Review network scripts before execution: you can inspect the installer source at [install.sh](https://peterchang77.github.io/agent-ai-skills/install.sh). The workshop dataset is completely synthetic; before using institutional or clinical data, consult [Privacy and data handling](concept:privacy).

## Custom setup

If you prefer to configure your workspace manually, use an alternative agent, or operate within a restricted computing environment, follow these steps:

### 1. Install an agent

Install your preferred agent harness following the vendor's official documentation. Most tools provide straightforward command-line installation instructions. Always review third-party scripts before execution. For architectural trade-offs between different harnesses, see [Harnesses and models](concept:harnesses). Verify institutional approval before analyzing sensitive or regulated datasets ([Privacy and data handling](concept:privacy)).

### 2. Create a project directory

An agent scopes its filesystem context to the directory where it is launched. Always initialize a dedicated folder for your project:

```bash
mkdir -p ~/workshop-demo     # create project directory
cd ~/workshop-demo           # enter directory
pwd                          # verify current path
```

Use `ls` to audit local contents. For additional guidance on permissions, directory navigation, and shell safety, refer to the [Linux command line](guide:linux-command-line-for-coding-agents) guide.

### 3. Verify local software dependencies

Check whether essential system utilities and compilers are available:

```bash
uv --version         # Python environment and package manager
pdflatex --version   # required for PDF report compilation
pandoc --version     # required for Word document conversion
```

During [Prepare your environment](beat:prepare-environment), the agent will audit these dependencies and propose installation commands for missing tools ([Environment](concept:environment)). Always inspect and approve system-level installations deliberately.

### 4. Populate scenario data

Consult the tabs under [Your scenario's data](#your-scenarios-data) below to unpack the required dataset files. (The automated quickstart performs this step automatically for the synthetic clinical scenario.)

## Restore a starting point

Each demo exercise defines the prerequisite state it expects, such as the raw data kit or an intermediate checkpoint representing earlier analytical progress. A checkpoint is a self-contained snapshot of the project directory.

To reset your workspace to a clean checkpoint:

```bash
rm -rf ~/workshop-demo && mkdir ~/workshop-demo      # ensure the target folder is disposable before removing
cp -r <scenario folder>/checkpoints/<name>/. ~/workshop-demo/
cd ~/workshop-demo
```

If you ran the quickstart with `--checkpoints`, snapshots are pre-downloaded to `~/workshop-demo-checkpoints/<name>/`, which replaces `<scenario folder>/checkpoints/<name>` in the snippet above.

After copying the files, start the agent inside that folder. Maintaining an untouched copy of the data archive allows quick resets between exercises, while [version control](concept:version-control) provides the same safety for your ongoing work.

## Expected variance in agent outputs

Large language models generate non-deterministic outputs. Two runs will frequently follow slightly different execution paths, generate different helper filenames, or format code uniquely. This variance is expected. Each demo module provides explicit validation criteria and reference benchmarks so you can verify that the final analytical result is correct regardless of the specific route taken.
