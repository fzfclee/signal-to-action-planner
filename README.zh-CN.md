<div align="center">

# Signal-to-Action Planner

**把混乱的信号，变成有理由的下一步行动和可以验证的决策门槛。**

基于 CLEAR 的可移植 Markdown Skill，适合处理藏在长故事、会议记录、客户反馈、反复摩擦和不确定局面里的真实决策。

<p>
  <a href="https://github.com/fzfclee/signal-to-action-planner/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/fzfclee/signal-to-action-planner/validate.yml?branch=main&amp;style=for-the-badge&amp;label=validation" alt="Validation"></a>
  <a href="#clear-如何运行"><img src="https://img.shields.io/badge/framework-CLEAR-0f766e?style=for-the-badge" alt="CLEAR framework"></a>
  <a href="https://github.com/fzfclee/signal-to-action-planner/stargazers"><img src="https://img.shields.io/github/stars/fzfclee/signal-to-action-planner?style=for-the-badge" alt="GitHub stars"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Limited%20Use-2563eb?style=for-the-badge" alt="Limited Use license"></a>
</p>

[30 秒开始](#30-秒开始) · [CLEAR 如何运行](#clear-如何运行) · [输出示例](#输出示例) · [质量证据](#质量证据) · [English](README.md) · [O2V CLEAR](https://www.o2vframework.com/zh/personal/clear)

</div>

---

## 为什么需要它

很多难题不是以清晰的问题出现，而是以一大段混乱的经历出现：

- 事实、假设、情绪和转述混在一起；
- 把一个显眼事件误认为真正的信号；
- 一个“听起来合理”的解释过早变成结论；
- 列出很多行动，却没说明为什么它们值得优先做；
- 所谓验证只是“再看看”，没有明确决策门槛。

Signal-to-Action Planner 帮助 AI 从叙述走到有证据的行动，同时避免把每个问题都写成长篇咨询报告。

## 30 秒开始

### Codex

```powershell
git clone https://github.com/fzfclee/signal-to-action-planner.git "$env:USERPROFILE\.codex\skills\signal-to-action-planner"
```

新建任务后输入：

```text
$signal-to-action-planner
我需要判断这件事下一步该怎么办：
[粘贴经历、观察、会议记录、客户反馈或工作信号]
```

默认情况下，Skill 至少会问一个真正有用的澄清问题。如果速度比补充证据更重要，可以明确要求直接输出或跳过提问。

### 其他 AI Agent

把 [`SKILL.md`](SKILL.md) 放入项目指令或 Markdown Skill 目录。较小模型使用 [`minimal_SKILL.md`](minimal_SKILL.md)，上下文非常紧张时使用 [`ultra_minimal_SKILL.md`](ultra_minimal_SKILL.md)。

## CLEAR 如何运行

```mermaid
flowchart LR
    I["混乱输入"] --> C["C · 澄清事实"]
    C --> L["L · 找到信号"]
    L --> E["E · 揭示机会"]
    E --> A["A · 采取行动"]
    A --> R["R · 复核证据"]
```

| 步骤 | 决策问题 | 可见输出 |
|---|---|---|
| **C · Clarify the Facts** | 哪些是已知、推断、假设或缺失？ | 事实、假设、证据强度和决策焦点 |
| **L · Locate the Signal** | 什么反复变化、矛盾、行为或风险现在最重要？ | 关键优先信号和可信度 |
| **E · Expose the Opportunity** | 信号意味着什么？还有哪些竞争性解释？ | 影响和工作假设 |
| **A · Act with a Justified Next Move** | 什么行动可以改变局面或提高判断质量？ | 优先行动、Owner、时间和第一步 |
| **R · Review the Evidence** | 什么结果代表继续、调整或停止？ | 验证信号、行动路线和决策门槛 |

证据贯穿每一步，不是最后才做的文字检查。

## 适用场景

| 场景 | Planner 增加的价值 |
|---|---|
| 一大段经历掩盖了真正问题 | 明确决策焦点，区分事实和假设 |
| 客户反馈很好，但没有实际行动 | 区分礼貌性兴趣和真实承诺 |
| 职场或利益相关者局面不清楚 | 提出竞争性假设和下一次取证沟通 |
| 问题反复出现 | 找出信号模式、合理行动和复核门槛 |
| 多个行动看起来都合理 | 按决策影响、投入、信心和风险确定优先级 |
| 无法等到完全确定再行动 | 设计低后悔行动和判断更新方式 |

简单、低影响的问题直接回答就够了。只有当结构能实质提高行动、验证、风险判断或决策门槛时，才需要使用这个 Skill。

## 你会得到什么

默认报告包含七个可见部分：

1. 决策摘要；
2. C - 事实、假设和决策焦点；
3. L - 关键信号；
4. E - 影响和工作假设；
5. A - 有理由的下一步行动；
6. R - 验证计划和行动路线；
7. 风险与质量检查。

默认输出适合普通对话和较小模型。需要补充少量证据和执行细节时，可增加 `--detailed`；它仍然是一份决策简报，不是完整咨询底稿。

## 输出示例

**输入**

```text
几个潜在用户都说我的想法不错，但没有人愿意继续推进。
我不知道这是真需求，还是大家只是客气。
```

**精简输出**

```markdown
# CLEAR Signal-to-Action Quick Diagnostic Report

## 1. 决策摘要
- 核心判断：感兴趣还不是需求。
- 第一步：要求一个具体承诺，而不是继续收集意见。
- 决策门槛：两周内是否至少有两个人采取下一步行动。

## 2. C - 澄清事实
- 事实：几个人说想法有意思。
- 事实：没有人承诺继续推进。
- 缺失：紧迫性、预算、决策人和测试意愿。

## 3. L - 找到信号
- 强信号：口头认可没有转化为行为。

## 4. E - 揭示机会
- 假设 1：问题不够紧迫。
- 假设 2：使用场景太宽，或者下一步不清楚。

## 5. A - 采取行动
- 请 3–5 个人选择一个具体动作：测试、引荐决策人或预约沟通。

## 6. R - 复核证据
- 至少两个人承诺则继续；
- 继续夸赞但不行动，则缩小场景；
- 更窄的方案仍没有承诺，则降低优先级。

## 7. 风险与质量检查
- 主要风险：把礼貌当成需求。
- 证据信心：中。
```

更多案例见 [`examples.md`](examples.md)。

## 兼容环境

| Agent / 工具 | 推荐方式 |
|---|---|
| Codex | 本地 Skill 目录和 `$signal-to-action-planner` |
| Claude Code | 项目或个人 Markdown Skill |
| Claude Projects | Project Instructions |
| Cursor / Windsurf | 项目规则或可复用指令 |
| Hermes / 较小模型 | `minimal_SKILL.md` 或 `ultra_minimal_SKILL.md` |
| OpenClaw / WorkBuddy | Markdown Skill 目录或可复用指令 |

不需要 App、托管服务、外部 API 或额外运行依赖。

## 质量证据

本仓库明确区分结构校验和行为评估：

- **自动仓库校验：** 每次提交和 Pull Request 都检查必需资产、UTF-8、frontmatter、内部链接、CLEAR 顺序、输出约定和公共入口。
- **公开 Benchmark：** [`BENCHMARK.md`](BENCHMARK.md) 定义代表性案例、通过标准、失败模式和评分维度。
- **完整示例：** [`examples.md`](examples.md) 展示证据处理、优先级、验证和行动路线输出。
- **三种运行规模：** full、minimal 和 ultra-minimal 指令可用于不同上下文预算。
- **对话约定：** [`conversation_flow.md`](conversation_flow.md) 说明澄清、检查点和允许直接输出的条件。

本地运行结构校验：

```powershell
python scripts/validate_repo.py
```

## 仓库结构

| 文件 | 用途 |
|---|---|
| [`SKILL.md`](SKILL.md) | 完整公共运行指令 |
| [`minimal_SKILL.md`](minimal_SKILL.md) | 较小模型版本 |
| [`ultra_minimal_SKILL.md`](ultra_minimal_SKILL.md) | 紧上下文版本 |
| [`conversation_flow.md`](conversation_flow.md) | 交互和澄清流程 |
| [`output_templates.md`](output_templates.md) | 标准报告结构 |
| [`examples.md`](examples.md) | 完整案例 |
| [`BENCHMARK.md`](BENCHMARK.md) | 评估案例和评分 |
| [`ROADMAP.md`](ROADMAP.md) | 计划中的公共改进 |

## 与 O2V 的关系

Signal-to-Action Planner 是一个可独立使用的公共 CLEAR 实现，适合日常 AI Agent 场景。

CLEAR 可用于 [O2V Framework](https://www.o2vframework.com/zh) 的 Enterprise、Venture 和 Personal 三种配置。O2V 在信号和行动之后，进一步连接场景、角色、痛点、方案、验证、商业论证、可复用资产和价值故事。可以在 [O2V Personal](https://www.o2vframework.com/zh/personal/clear) 查看公共 CLEAR 介绍。

本仓库依据 [`LICENSE`](LICENSE) 中的条款提供，署名和方法论权利说明见 [`NOTICE.md`](NOTICE.md)。

## 参与贡献

欢迎提交匿名 Benchmark 案例、兼容性发现、失败样例和表达改进。提交 Pull Request 前请阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

方法论或咨询合作：

- 中文：微信 `lizhi_ch`
- 英文：[LinkedIn 联系 Zhi Li](https://www.linkedin.com/in/li-zhi/)

---

<div align="center">

**不要等待完全确定，先定义一个能让证据变得更好的下一步。**

如果 Planner 帮你把混乱的局面变成了行动，欢迎 Star，让更多人找到它。

</div>
