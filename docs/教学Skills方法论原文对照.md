# 教学 Skills 方法论原文对照

研究日期：2026-11-15。对照的用途是为 Surika 选择、组合和落实成熟教学方法，不以独有或原创为目标。研究对象是作者的 SKILL.md 及其直接引用的教学规则；没有执行这些技能，也没有测量学习效果。下文“明确规定”只说明文本规定，不证明运行时稳定遵循；“未明写”仅限已读文件，不等于产品没有该能力。

## 结论先行

不能把现有教学 skills 概括为“生成教程、提问和记录进度”。样本中已经有：基于回答诊断执行模型、针对错误模型设计对照实验、根据失败退回前置概念、记录独立完成与所需帮助、变式迁移、跨会话记录和间隔复习。这些应成为 Surika 可直接借鉴的教学做法；反证用于纠正浅层比较，不是要求 Surika 避开已有方法。

尤其是“先听学习者的机制解释，设计能区分解释的最小实验，按结果调整，再检查迁移”与 programming-tutor 的现有规则高度重合，适合借鉴为编程练习流程。重点是把适用的方法连成可追溯、可纠正、跨会话稳定执行的学习流程，再检验是否促进独立理解、保留与迁移。多个 skill 采用同一做法是实践参考，仍不能代替该做法的研究依据或 Surika 自身的效果验证。

## 来源与版本

公开原文通过 GitHub 连接器读取；分支 HEAD 另用 `git ls-remote` 核验。以下固定提交链接便于复核。没有仅凭 README、聚合目录或星数作判断。

| 标记 | 实际读取的一手来源 | 版本定位 |
|---|---|---|
| T | 本机 [teach/SKILL.md](/Users/linzhikai/.agents/skills/teach/SKILL.md)，及同目录 [MISSION-FORMAT.md](/Users/linzhikai/.agents/skills/teach/MISSION-FORMAT.md)、[LEARNING-RECORD-FORMAT.md](/Users/linzhikai/.agents/skills/teach/LEARNING-RECORD-FORMAT.md)、[GLOSSARY-FORMAT.md](/Users/linzhikai/.agents/skills/teach/GLOSSARY-FORMAT.md)、[RESOURCES-FORMAT.md](/Users/linzhikai/.agents/skills/teach/RESOURCES-FORMAT.md) | 本机快照；SKILL SHA-256 `550482c2d674b085c9043b87bfdc14a8f2ec453c736119e7fcbb1e9332bffeba`；未核定上游版本 |
| R | 本机 [rederive/SKILL.md](/Users/linzhikai/.agents/skills/rederive/SKILL.md) | 本机快照；SHA-256 `87e18303c666563796c77f14869b466dd5d962a318b5019b11d0ffa6e22ca9f8`；未核定上游版本 |
| P | cdmorozov/claude-tutors：[programming-tutor/SKILL.md](https://github.com/cdmorozov/claude-tutors/blob/0a76e25d99de25c8f925974f26a8df1da8a33865/programming-tutor/SKILL.md)、[pedagogy.md](https://github.com/cdmorozov/claude-tutors/blob/0a76e25d99de25c8f925974f26a8df1da8a33865/programming-tutor/references/pedagogy.md)、[misconceptions.md](https://github.com/cdmorozov/claude-tutors/blob/0a76e25d99de25c8f925974f26a8df1da8a33865/programming-tutor/references/misconceptions.md) | `main` HEAD `0a76e25`；SKILL 无显式版本号 |
| C | Terryc21/tutorial-creator：[SKILL.md](https://github.com/Terryc21/tutorial-creator/blob/b159b40754856a9a3e9ac729ecfbef032b972ae5/skills/tutorial-creator/SKILL.md)、[VOCAB.md](https://github.com/Terryc21/tutorial-creator/blob/b159b40754856a9a3e9ac729ecfbef032b972ae5/skills/tutorial-creator/VOCAB.md)、[SCHEMAS.md](https://github.com/Terryc21/tutorial-creator/blob/b159b40754856a9a3e9ac729ecfbef032b972ae5/skills/tutorial-creator/SCHEMAS.md) | SKILL `2.1.2`；`main` HEAD `b159b407` |
| K | kevinnio/tutor：[SKILL.md](https://github.com/kevinnio/tutor/blob/f0ad1ee514a034b720a4af4a36b5767f473a5994/SKILL.md) | metadata `0.6`；`master` HEAD `f0ad1ee` |

## 对照：教学决策怎样发生

每行引用上表同标记原文。比较目标和决策规则，不按功能数量评分。

| 对象 | 目标能力与起点观察 | 下一步与帮助规则 | 跨会话证据、迁移和延迟 | 用户控制 |
|---|---|---|---|---|
| T：teach | 以真实 mission、可观察成功标准组织知识、技能和现实实践；读取 prior knowledge、学习记录，估计最近发展区 | 用户指定主题优先，否则按 mission 与已有理解选紧凑课；即时反馈；未设统一提示阶梯 | Learning Record 区分真正理解与仅覆盖内容；可记录 Evidence、误解纠正、旧记录被替代；明确 retrieval、spacing、技能 interleaving，但未规定统一复查时间表或必填帮助字段 | 修改 mission 须确认；偏好进 NOTES；尊重拒绝社区建议 |
| R：rederive | 从问题和约束重建仓库设计；先听根本需求及学习者方案 | 每次增加一个会使当前方案失效的约束；卡住给选项及代价；连续两错可提供不含缺失部分的图；即使请求也不直接揭示决策 | `.rederive/map.md` 与 `log.md` 持久化；明确记录卡点、什么帮助使其继续、独立想到的方案与仍不稳处；未明写延迟复测或新情境迁移调度 | 可换题、重置；更好的自创方案可被认可；对直接答案的控制较严格 |
| P：programming-tutor | 建立执行模型、推理、调试和设计能力；区分学习与交付；练习时看预测、手工追踪、尝试和错误证据 | 五模式；概念问题直接讲解；练习按提示阶梯；变式失败回到执行模型重新诊断；挫折时调整支架 | 明确重建、改变需求的迁移、边界案例、逐渐撤支架；所读文件未规定跨会话文件格式或延迟重测调度 | 概念讲解默认零问题，检查须自愿；坚持要代码时最终给代码并解释，再加变式；不把交付请求强变教学 |
| C：tutorial-creator | 阅读自己代码、应用概念、表达理解；配置经验水平，前测、词汇历史与 confused 状态提供起点信息 | daily 按未覆盖概念顺序推荐；gap-driven 按混淆历史选课，针对最近错误侧面；生成注释、前后测与答案 | `vocabulary.yaml`、PROGRESS 和会话记录；review 的日期/结果/来源驱动状态和下一轮；有间隔词汇复习；后测要求应用，但 applied_test_history 明确预留，不能当作已连通的应用测评历史 | 可选路径/概念/文件、跳过/停止复习、撤销；可重置 mastered；一般编辑命令不允许改测试历史，纠错需手改文件 |
| K：TuTor | 学习者亲自完成每一步；从实际文件、diff 和其运行过的测试核验进展 | 给一个行动，用户完成后核验；失败不前进；解释命令各部分；不写交付代码、不代运行交付物，仅允许不解决当前题的短通用示例 | 明确当前会话 checklist；所读 SKILL 未明写长期学习档案、迁移题或延迟复查；产物核验本身不能证明学习者理解 | 支持语言/术语水平调整；即使请求代做也拒绝；这是其教学契约，不等于所有用户场景都适合 |

## 必须保留的反证与限制

**1. 证据教学不始于 Surika。** T 的 Learning Record 原文要求 “Coverage is not learning. Wait for evidence.”，并把用户声称的既有知识与练习展示理解都作为记录入口；Evidence 是可选项，不能说它没有证据观，也不能说所有记录都有可回放的行为证据。R 的日志字段 `found on their own` 与 `struggled with` 已记录独立程度及起效的帮助。

**2. 机制假设、反例和教学调整已有明确程序。** P 的主文件要求让学习者预测错误规则处理不好的案例，再运行看矛盾；失败后重新诊断，而非重复讲解。其 misconceptions 的参数章节给出两种实验：重新绑定参数与修改传入对象，各自预测再运行，以差异暴露误解。pedagogy 的调试章节要求先提出假设、设计可证实或反驳的测试、一次改变一个变量；PRIMM 则由 Predict/Run/Investigate 到 Modify/Make。将 Surika 的差异只写成“最小实验区分正确机制和误解”会忽略这些直接反例。[P 原文](https://github.com/cdmorozov/claude-tutors/blob/0a76e25d99de25c8f925974f26a8df1da8a33865/programming-tutor/references/misconceptions.md)

这里仍有一个较窄的区别可研究：P 通常把错误表现解释为错误执行模型，未要求把教师的诊断也持久化为可撤销假设、同时记录多个备选解释。这是所读规范的缺口，不证明模型运行时不会这么做。

**3. 跨会话证据闭环与复习已有实例。** C 的 VOCAB 明确测试产生状态；三次连续正确可成为 mastered，最近三次至少两次 partial/wrong 为 confused；复习优先 confused，其次超过 14 天未测的 reviewing，再到近期 reviewing/new。SKILL 的 gap-driven 路径用测试历史选择针对性教程。因此不能把它说成静态教程生成器。[VOCAB 原文](https://github.com/Terryc21/tutorial-creator/blob/b159b40754856a9a3e9ac729ecfbef032b972ae5/skills/tutorial-creator/VOCAB.md)

同时要限制推断：其测试主要核对术语定义，不等于独立编程能力；所列复习 tiers 没有 mastered，三个正确也没有要求跨日间隔。SCHEMAS 的 `test_history` 只规范日期、结果、来源，不必填原始回答、提示条件或问题；`applied_test_history` 与后测评分字段明确预留。SKILL 的 gap-driven 却提到从历史中的问题判断具体弱点，规范之间存在信息落地不充分的张力。VOCAB 又同时描述“confused 一次答对便恢复”和“最近三次两错仍 confused”，在“错、错、对”上并不一致。这些是可检查的文本问题，不能未经运行就宣称系统必然失败。[SCHEMAS 原文](https://github.com/Terryc21/tutorial-creator/blob/b159b40754856a9a3e9ac729ecfbef032b972ae5/skills/tutorial-creator/SCHEMAS.md)

## 可借鉴的实施要求与验证方式

以下把已有做法转成待落实的产品要求。先检查是否执行到位，再检验是否促进学习；无须证明其他工具做不到。

| 实施要求 | 最小可观察承诺 | 如何检验实现与学习结果 |
|---|---|---|
| 可撤销的学习诊断 | 同一题保留学习者原话、预测、执行结果、教师解释与不确定性；新证据能替代旧判断，用户可纠正 | 用相反证据检查诊断能否修正，是否仍把一次错答当稳定能力标签；再检查针对性教学后能否独立解释和预测新案例 |
| 帮助条件贯穿证据 | 在下一题选择和学习记录中区分独立、提示后、示范后完成；不是只增加字段 | 用相同结果、不同帮助条件检查后续任务是否合理变化；逐渐减少帮助后，学习者是否仍能独立完成 |
| 延迟迁移进入同一闭环 | 得到同意后，在后续会话换情境、减少帮助重新检查；保留间隔与任务差异，不凭当场成功判长期掌握 | 核验复查实际发生且任务不只是改名字；分别记录即时、延迟与新情境表现，避免用当场正确代替长期学习证据 |

选择方法时应尊重适用情境：不能强迫 P 在概念问答时测验，也不能用 K 的“禁止代做”代表所有技能。实施验证检查流程遵循、诊断可追溯与用户可控；效果验证在可比较的任务、时间和帮助条件下检查即时、延迟与新情境表现。现有 skills 可以充当参考流程或实验基线，目的是找出什么帮助学习，而非制造差异。

## 访问及研究边界

所有指定 SKILL 均成功读取。kevinnio 的 `main` 路径首次返回 404；确认默认分支为 `master` 后读取成功，不是项目不可访问。T/R 仅本机快照，未验证上游作者归属；C 的长文件先完整抓取，再按教学相关段落复读，并补读 VOCAB/SCHEMAS。未穷尽各仓库所有附件，未运行示例、评估评分一致性或核实文件内引用的教育效果研究。作者关于某方法“最有效”等论断不在本报告的已验证结论内。
