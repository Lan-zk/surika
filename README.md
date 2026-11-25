<p align="center">
  <img src="skills/surika/assets/logo.png" alt="Surika meerkat logo" width="96">
</p>

<h1 align="center">surika.</h1>
<p align="center">Learn to think. Not just to code.</p>

<p align="center">English · <a href="README-zh.md">简体中文</a></p>

Surika is a learning skill for people who build software with AI. It helps you understand code, language mechanisms, and design tradeoffs while working with a coding agent—developing judgments you can explain, test, and revise.

Start with a question. Ask for a direct explanation, read source code together, compare approaches, or visualize how a program runs. Skip exercises, change topics, or return to development whenever you want. Surika provides a teaching workflow without taking over the conversation.

Use [surika-knowledge](skills/surika-knowledge/SKILL.md) independently to capture, look up, or correct professional experience. For example, “Show me the judgments I contributed to this debugging session.” To install it locally, replace `--skill surika` below with `--skill surika-knowledge`, or copy the entire `skills/surika-knowledge/` directory. Both skills use `~/.surika/` in your home directory for personal knowledge across projects by default.

## Installation

Install the entire [`skills/surika/`](skills/surika/) directory, including its references and brand assets. There is no application to build, service to start, or separate model to configure. Your agent provides the model, file access, and execution tools.

Requires Node.js 22.20 or later and npm.

### From GitHub

Run from your target project:

```bash
npx skills@latest add Lan-zk/surika --skill surika
```

The same `-a codex`, `-a claude-code`, and `-g` options apply. Run `npx skills@latest add Lan-zk/surika --list` first to check whether the remote repository exposes `surika`.

See the [Skills CLI installation reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add) and [supported agents](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) for more options and installation paths. Installer support does not mean Surika has been tested in every host.

### From local source

Open the project where you want to use Surika, then replace the path below with the absolute path to your local Surika repository:

```bash
npx skills@latest add /absolute/path/to/surika --skill surika
```

Select your agent when prompted. Installation is project-scoped by default; add `-g` to use it across projects. You can also select an agent directly:

```bash
# Codex: current project
npx skills@latest add /absolute/path/to/surika --skill surika -a codex

# Claude Code: user-wide
npx skills@latest add /absolute/path/to/surika --skill surika -a claude-code -g
```

### Without an installer

Copy the **entire** local `skills/surika/` folder into your host's skills directory, preserving `references/`, `assets/`, and `agents/`:

| Agent | Current project | User-wide |
|---|---|---|
| Codex | `.agents/skills/surika/` | `~/.agents/skills/surika/` |
| Claude Code | `.claude/skills/surika/` | `~/.claude/skills/surika/` |

For example, from the target project root on macOS or Linux, when the destination does not already exist:

```bash
mkdir -p .agents/skills
cp -R /absolute/path/to/surika/skills/surika .agents/skills/surika
```

If a same-named installation already exists, inspect it first to avoid overwriting your changes or creating a nested directory. Choose one installation method per agent.

## Getting started

After installation, explicitly ask your agent to use Surika:

```text
Use Surika to help me understand why changing a parameter inside this function leaves the variable outside unchanged. Start with a direct explanation.
```

You can also select `surika` in hosts that support explicit skill invocation—for example, enter `$surika` in Codex. No learning profile or placement test is required.

| What you want to do | Try asking |
|---|---|
| Understand a mechanism | “Use Surika to walk me through how values change in this code.” |
| Read source code | “Use Surika to explain the division of responsibilities along this request path.” |
| Compare approaches | “Use Surika to compare a queue with a direct call here. What conditions drive the choice?” |
| Visualize a process | “Use Surika to create an HTML visualization of the cache-hit and cache-miss paths.” |
| Switch freely | “Just tell me the answer here.” / “Pause teaching and help me finish this fix.” |

Visualizations are generated for the question at hand, following Surika's brand and [design guidance](skills/surika/references/DESIGN.md). They should show relationships and changes rather than move chat paragraphs onto a page. Static diagrams are welcome; exercises and interaction are optional.

## Check, update, and uninstall

```bash
# List project installations; use -g for user-wide installations
npx skills@latest list
npx skills@latest list -g

# Remove Surika from the current project; add -g for a user-wide installation
npx skills@latest remove surika
```

For GitHub installations, update with `npx skills@latest update surika`. For local-source installations, update the source and repeat the original `add` command. For manual installations, copy the complete folder again. Preserve any personal edits before updating.

If your agent does not discover the skill, check that the installation scope matches your current project and that the installed folder directly contains `SKILL.md`. Then open a new conversation or restart the host. A CLI listing confirms files are present, not that the host has loaded them; check the host's skill list and actual invocation.

## Capture and reuse knowledge

Ask surika-knowledge to preview your own technical decisions from a conversation, then ask it to save the ones you want. In another project with access to the same home directory, ask Surika to explain a new topic using that experience. You can ask to try a changed constraint and save your reasoning with a link to the earlier record.

Browse or correct records through the agent or edit the Markdown in `~/.surika/records/`. The directory is created on the first write. From this checkout, run `python3 skills/surika-knowledge/scripts/knowledge.py search` to list summaries. The bundled CLI requires Python 3.9+; see the [record commands and format](skills/surika-knowledge/references/store.md).

## Learning records and boundaries

Technical background and reusable project experience default to `~/.surika/` in your home directory. Project-specific learning progress and materials stay in the workspace’s `.surika/`. You can choose another directory. Short questions need no record. You can decline saving or inspect, edit, and delete the files yourself. Records are not automatically committed or uploaded; check ignore rules when working inside a Git repository.

Surika distinguishes technical evidence, observed execution, and hypothetical reasoning, as well as your own work and work done by the agent. It does not provide an execution sandbox, background review reminders, or permanent “mastery” scores. Its teaching methods have research references; Surika's long-term learning outcomes remain unverified.

## Project structure

```text
skills/surika/
├── SKILL.md                # Workflow and key boundaries
├── references/
│   ├── learning.md         # Teaching activities, consulted as needed
│   ├── memory.md           # Learning records and continuity
│   ├── DESIGN.md           # Brand and visualization design
│   └── methods.md          # Method sources and evidence limits
├── assets/logo.png         # Brand asset
└── agents/openai.yaml      # Codex display metadata
```

See [ADR 0007](docs/adr/0007-skill-workflow-and-visual-design.md) for the current scope. `docs/` retains research and historical decisions; its desktop application and fixed-template proposals do not describe current features and are not needed for installation.

To share feedback, open an [issue](https://github.com/Lan-zk/surika/issues) with your agent, the question you wanted to understand, and what helped or got in the way. Leave out private learning records and sensitive project information.
