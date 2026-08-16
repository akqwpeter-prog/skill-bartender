# skill-bartender 🍸

**给 Agent 技能配一位调酒师：任务对味，技能配杯 —— 没尝过的技能不上桌。**

你的 agent 已经能看到技能目录（名字+一句话描述），但它常常「倒多了」：
一次加载一堆技能、加载错的那个、或漏掉那条本就编排好一切的 workflow 技能。
**skill-bartender** 就是修这件事的元技能：

- 🪜 **懒人阶梯** — 通用工具能干的零加载；恰好匹配的只加载一个；组合任务用
  workflow 技能，不手工拼原子技能；拿不准就不加载。
  （精神来源：[ponytail](https://github.com/DietrichGebert/ponytail)——
  最好的加载是没发生的加载。）
- 🍷 **路由表** — 任务→技能映射写在 references/policy.md，随你改。
- 🔐 **安全酒窖** — 需要但没装的技能：隔离区 → [SkillSpector](https://github.com/NVIDIA/SkillSpector)
  扫描 → **人工确认** → 才拷进技能目录。永不自动安装。
- 🧠 **学习** — 加载了没用上的技能会被记下来，下次同类任务跳过。

## 安装（一个文件，三平台通用）

    # DeepSeek Harness
    mkdir -p ~/.dsh/skills/skill-bartender
    cp skills/skill-bartender/SKILL.md ~/.dsh/skills/skill-bartender/
    cp -r skills/skill-bartender/references ~/.dsh/skills/skill-bartender/

    # Claude Code
    mkdir -p ~/.claude/skills/skill-bartender
    cp skills/skill-bartender/SKILL.md ~/.claude/skills/skill-bartender/

    # Codex
    mkdir -p ~/.codex/skills/skill-bartender
    cp skills/skill-bartender/SKILL.md ~/.codex/skills/skill-bartender/

之后喊一次「skill-bartender」，或把路由表粘进 AGENTS.md 常驻生效。

## 安全模型（必读）

- 技能是**指令**，指令可以被投毒（提示注入）。SkillSpector 是**过滤器，不是保证书**。
- 任何技能里的 scripts/ 都是**代码**——未经人工审查一律不执行。
- 每次安装都必须人工确认。没有静默安装，永远没有。

## 不重复造轮子

和生态**并用**，不是替代：
[DshMarket](https://github.com/dsh-market/dsh-market)（图形市场）、
[dsh-find-plugin](https://github.com/awesome-dsh-plugin/dsh-find-plugin)（对话找插件）、
[dsh-plugin-autoevo](https://github.com/klarkxy/dsh-plugin-autoevo)（带批准的插件自动安装）。
skill-bartender 补的是**路由策略**和**隔离-扫描-批准**这套纪律。

## 评测

路由策略自带黄金任务集：[docs/eval.md](docs/eval.md)。

## 许可证

MIT。ponytail（MIT）仅致敬引用，未打包。
