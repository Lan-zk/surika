<p align="center">
  <img src="skills/surika/assets/logo.png" alt="Surika 狐獴标识" width="96">
</p>

<h1 align="center">surika.</h1>
<p align="center">Learn to think. Not just to code.</p>

<p align="center"><a href="README.md">English</a> · 简体中文</p>

Surika 是面向 AI 编程者的学习 skill：在你使用 Coding Agent 做项目的过程中，帮助你理解代码、语言机制和设计取舍，逐步形成有依据、能验证和修正的判断。

从一个问题开始就够了。你可以要求直接解释、一起读源码、比较方案，或用图看清执行过程；随时跳过练习、换题、回到开发。Surika 提供教学工作流，不接管整个会话。

也可独立使用 [surika-knowledge](skills/surika-knowledge/SKILL.md) 提取、查询和修正专业记录。例如：“整理这次排障中我自己提出的判断，先给我看。”从本地安装时将下方命令中的 `--skill surika` 换成 `--skill surika-knowledge`，或手动复制整个 `skills/surika-knowledge/` 目录。两个入口默认从用户主目录的 `~/.surika/` 读取个人知识，换项目后仍可复用。

## 安装

安装内容是 [`skills/surika/`](skills/surika/) 整个目录，包括参考文档和品牌素材；无需构建应用、启动服务或配置单独的模型。模型、文件访问与执行工具由你的 Agent 提供。

需要 Node.js 22.20 或更新版本以及 npm。

### 从 GitHub 安装

在目标项目目录执行：

```bash
npx skills@latest add Lan-zk/surika --skill surika
```

同样支持 `-a codex`、`-a claude-code` 和 `-g`。可先用 `npx skills@latest add Lan-zk/surika --list` 确认远程能发现 `surika`。

安装选项与其他 Agent 的路径见 [Skills CLI 安装说明](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)和[支持的 Agent](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)。安装器支持某个 Agent，不代表 Surika 已在所有宿主中完成体验验证。

### 从本地源码安装

进入你希望使用 Surika 的项目目录，将下面的路径替换为本地 Surika 仓库的绝对路径：

```bash
npx skills@latest add /absolute/path/to/surika --skill surika
```

按提示选择 Agent。默认只安装到当前项目；添加 `-g` 可供多个项目使用。也可以直接指定 Agent：

```bash
# Codex：当前项目
npx skills@latest add /absolute/path/to/surika --skill surika -a codex

# Claude Code：用户级
npx skills@latest add /absolute/path/to/surika --skill surika -a claude-code -g
```

### 不使用安装器

将本地 `skills/surika/` **整个文件夹**复制到宿主的 skills 目录，保留 `references/`、`assets/` 和 `agents/`：

| Agent | 当前项目 | 用户级 |
|---|---|---|
| Codex | `.agents/skills/surika/` | `~/.agents/skills/surika/` |
| Claude Code | `.claude/skills/surika/` | `~/.claude/skills/surika/` |

例如在目标项目根目录执行（macOS / Linux；目标目录不存在时）：

```bash
mkdir -p .agents/skills
cp -R /absolute/path/to/surika/skills/surika .agents/skills/surika
```

已有同名安装时先检查其内容，避免覆盖自己的修改或复制出嵌套目录。同一 Agent 选择一种安装方式即可。

## 开始使用

安装后，在 Agent 中明确请求使用 Surika：

```text
使用 Surika 帮我理解：为什么这个函数里修改了参数，外面的变量却没有变化？先直接解释。
```

也可以在支持显式 skill 调用的宿主中选择 `surika`，例如 Codex 中输入 `$surika`。不需要先建学习档案或完成水平测试。

| 你想做什么 | 可以这样说 |
|---|---|
| 理解机制 | “使用 Surika，带我看这段代码里的值是怎样变化的。” |
| 阅读源码 | “使用 Surika，从这条请求路径解释模块之间为什么这样分工。” |
| 比较方案 | “使用 Surika，帮我分析这里用队列还是直接调用，各自依赖什么条件？” |
| 可视化 | “使用 Surika，做一个 HTML，让我看清缓存命中和未命中的两条路径。” |
| 自由切换 | “这里直接告诉我答案。”／“先停止教学，帮我完成这个修复。” |

可视化按问题现场生成，沿用 Surika 的品牌和[设计指导](skills/surika/references/DESIGN.md)。它应表达关系与变化，而不是把对话段落搬到页面；静态图也可以，不强制做题或互动。

## 从沉淀到学习

1. 在开发会话中说：“用 surika-knowledge 提取我在这次讨论中作出的技术判断，先给我看。”认可后说“保存”。也可以从“我想梳理自己参与过的迁移项目”开始对话。
2. 换到另一项目或会话后说：“用 Surika 结合我之前的迁移经历解释双写风险。”两个宿主需要能访问同一个个人目录。想检验理解时可以说“换一个条件，让我自己判断”；想保留新表现时说“把我刚才的判断和旧项目联系起来保存”。
3. 随时说“列出迁移相关记录”或“那次选型由同事负责，请修正”。也可直接用编辑器打开 `~/.surika/records/` 中的 Markdown 文件。

首次保存会初始化个人目录。在源码仓库运行 `python3 skills/surika-knowledge/scripts/knowledge.py search` 可浏览摘要，加检索词可缩小范围。命令行需要 Python 3.9+，支持查看、更新和删除；见[工具用法](skills/surika-knowledge/references/store.md)。

## 确认安装、更新与卸载

```bash
# 查看当前项目的安装；用户级安装加 -g
npx skills@latest list
npx skills@latest list -g

# 卸载当前项目的 Surika；用户级安装加 -g
npx skills@latest remove surika
```

从 GitHub 安装后，可用 `npx skills@latest update surika` 更新。使用本地源码安装时，更新源码后重新执行原来的 `add` 命令；手动复制的安装则重新复制完整目录。更新前保留自己修改过的内容。

若 Agent 未发现 skill，检查安装范围是否与当前项目一致、安装目录中是否直接包含 `SKILL.md`，然后重新打开会话或重启宿主。CLI 能列出文件不等于宿主已加载；以宿主的技能列表和实际调用为准。

## 学习记录与边界

技术背景和可复用的项目经验默认保存在 `~/.surika/`。仅属于当前项目的学习进度和材料保存在工作区的 `.surika/`。你可以指定其他目录。短问答无需保存，你也可以拒绝记录，或自行查看、修改与删除文件。记录不自动提交或上传；位于 Git 仓库时注意忽略规则。

Surika 区分技术依据、运行结果与推演，也区分你的表现和 Agent 代做的部分。它不提供独立执行沙箱、后台复习提醒或永久“掌握”评分。教学方法有研究参考，Surika 本身的长期学习效果仍待验证。

## 项目结构

```text
skills/surika/
├── SKILL.md                # 工作流与关键边界
├── references/
│   ├── learning.md         # 按需参考的教学活动
│   ├── memory.md           # 学习记录与续接
│   ├── DESIGN.md           # 品牌与可视化设计
│   └── methods.md          # 方法来源与证据边界
├── assets/logo.png         # 品牌素材
└── agents/openai.yaml      # Codex 展示信息
```

当前交付范围见 [ADR 0007](docs/adr/0007-skill-workflow-and-visual-design.md)。`docs/` 保留研究和历史决策，其中的桌面应用与固定模板方案不代表当前功能，也不需要随 skill 安装。

反馈时可在 [Issues](https://github.com/Lan-zk/surika/issues) 中描述使用的 Agent、希望理解的问题，以及哪里帮助了你或阻碍了探索。请省略私人学习记录和项目敏感信息。
