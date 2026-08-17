<div align="center">

<img src="docs/social-preview.png" alt="skill-bartender — task-to-skill pairing for DeepSeek Harness" width="100%">

<br>

# 🍸 skill-bartender

### *Mix the right skill cocktail for every task — and never pour an untasted bottle.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![SkillSpector CI](https://github.com/akqwpeter-prog/skill-bartender/actions/workflows/scan.yml/badge.svg)](https://github.com/akqwpeter-prog/skill-bartender/actions/workflows/scan.yml)
[![DeepSeek Harness](https://img.shields.io/badge/DeepSeek%20Harness-Skill-4D6BFE)](https://github.com/topics/dsh-plugin)
[![Self-scan](https://img.shields.io/badge/SkillSpector-0%20findings-2EA44F)](docs/skillspector-report.json)
[![Laziness ladder](https://img.shields.io/badge/ladder-0%20skills%20when%20possible-8B5CF6)](README.md#-why)
[![Platforms](https://img.shields.io/badge/platforms-DSH%20·%20Claude%20Code%20·%20Codex-4D6BFE)](README.md#-quick-start)
[![Docs](https://img.shields.io/badge/docs-2%20languages-4D6BFE)](docs/lang/README_ZH.md)

<br>

Your agent already sees a catalog of skill names and descriptions — but it
**over-pours**: loads too many skills, loads the wrong ones, or misses the one
workflow skill that composes the task. **skill-bartender** is the meta-skill
that fixes the pour:

- 🪜 **Laziness ladder** — zero skills when plain tools suffice; one skill
  when one matches; workflow over hand-composed atomics; unsure → don't load.
- 🍷 **Routing table** — a user-editable task→skill map (`references/policy.md`)
  that overrides the defaults.
- 🔐 **Safe cellar** — a needed skill missing? Quarantine → SkillSpector scan
  → explicit human approval → install. Never auto-installs.
- 🧠 **Learn** — loaded-but-unused skills get logged and skipped next time.
- 🧪 **Taste test** — audit installed skills and rewrite weak descriptions
  into "when-to-use" sentences.

[Why](#-why) · [What you get](#-what-you-get) · [Quick start](#-quick-start) · [See it in action](#-see-it-in-action) · [Usage](#-usage) · [Security model](#-security-model-read-this) · [FAQ](#-faq) · [Examples](#-examples) · [Layout](#-layout) · [License](#-license)

[**English**](README.md) · [**简体中文**](docs/lang/README_ZH.md)

</div>

---

## 🤔 Why

Most agents treat the skill catalog as an all-you-can-eat buffet. `skill-bartender`
treats it as a bar with a taste test:

| | skill-bartender | Typical catalog behavior |
|---|---|---|
| Skills loaded per task | usually **one**; zero when plain tools suffice | whatever matches, however many |
| Workflow skills | ✅ preferred — never hand-assemble atomics | ❌ often missed or hand-composed |
| Unsure about a match | ❌ don't load (miss beats false pour) | ⚠️ loads "just in case" |
| Installing a missing skill | 🔐 quarantine → scan → **human approval** | ⚠️ downloads straight into the skills dir |
| Auto-install | ❌ never, by design | ⚠️ often silent |
| Learns from unused loads | ✅ logged, skipped next time | ❌ no memory |

**Why the "laziness ladder"?** A wrong skill body stays in conversation
history forever; a missed load only costs one tool round-trip. The best load
is the load never made (spirit: [ponytail](https://github.com/DietrichGebert/ponytail)).

## ✨ What you get

| Capability | What it does | Where |
|---|---|---|
| 🪜 Laziness ladder | Stop at the first rung that holds: 0 no skill → 1 one skill → 2 workflow skill → 3 unsure, don't load | all platforms |
| 🍷 Routing table | Task→skill map in `references/policy.md`; URL-keyed families (doc/drive/wiki/sheets/base/slides) routed by path pattern | all platforms |
| 🔐 Safe cellar | Missing skill: search → **quarantine dir** → SkillSpector scan → scripts shown to human (default deny) → explicit yes → install; source + commit hash + verdict recorded | DSH, Claude Code, Codex |
| 🧠 Learn | Unused loads logged and skipped for the same task type next time; chronic no-shows get offered for removal | DSH |
| 🧪 Taste test | On request: list installed skills, rewrite weak descriptions into trigger-phrase form (under the 500-char catalog cap) | on request |

## ⚡ Quick start

One file, three platforms:

```sh
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
```

Or install as a DeepSeek Harness bundle:

```sh
dsh plugin --profile web add github:akqwpeter-prog/skill-bartender
```

Then say "skill-bartender" once, or paste the routing table into your
AGENTS.md for always-on routing. Full examples: [docs/EXAMPLES.md](docs/EXAMPLES.md).

## 📸 See it in action

*The pour flow in one picture: stop at the first rung that holds, and never
install without a taste test.*

<img src="docs/screenshots/how-it-works.png" alt="How the pour works: laziness ladder (0 plain tools, 1 one match, 2 workflow, 3 unsure) plus the safe cellar (quarantine → SkillSpector scan → human approval → install)" width="100%">

## 🚀 Usage

Four ways to use it:

| Way | How | When |
|---|---|---|
| **A. Say the name** | In any session, just say "skill-bartender" | One-off or first-time setup |
| **B. Always-on routing** | Paste the routing table into AGENTS.md | Every task routes through the ladder |
| **C. Request a pour** | "Which skill fits this task?" | Choosing among skills |
| **D. Cellar audit** | "Audit my installed skills" | Taste test: weak descriptions get rewritten |

`skill-bartender` must itself be loaded once (user gesture or task match) —
it never self-triggers, and never pre-loads "just in case".

## 🔐 Security model (read this)

- Skills are **instructions**, and instructions can be adversarial (prompt
  injection). SkillSpector is a **filter, not a guarantee**.
- `scripts/` in any skill is **code** — never executed without human review.
- Human approval is mandatory for every install. **No silent installs, ever.**
- This skill scans itself clean: SkillSpector **0 findings** (score 0 / SAFE)
  — [docs/skillspector-report.json](docs/skillspector-report.json).
- Security policy: [SECURITY.md](SECURITY.md).

## ❓ FAQ

**Does it auto-install missing skills?**
No. Every download goes to a quarantine dir, gets scanned with SkillSpector,
and is copied into the skills root only after explicit human approval. A
passing scan is a filter, not a guarantee — prompt injection survives static
scans, so scripts are shown to the human and default-deny.

**What if SkillSpector isn't installed?**
`uv tool install git+https://github.com/NVIDIA/skillspector.git`, or run the
manual checklist in `references/policy.md`.

**Does it work with Claude Code and Codex?**
Yes — the same SKILL.md installs on all three platforms in ~15 seconds.

**How is this different from DshMarket / dsh-find-plugin / dsh-plugin-autoevo?**
They find, search, and auto-install plugins. skill-bartender adds the
**routing policy** (ladder + routing table) and the **quarantine-then-approve**
discipline. Use it *alongside* the ecosystem, not instead of it.

**How is it evaluated?**
The routing policy ships with a gold-task suite: [docs/eval.md](docs/eval.md).

## 🎁 Examples

- [docs/EXAMPLES.md](docs/EXAMPLES.md) — real routing cases, cellar installs, audits.
- [docs/ROUTING-GUIDE.md](docs/ROUTING-GUIDE.md) — how to write your own task→skill rules.
- [docs/eval.md](docs/eval.md) — gold-task suite for the routing policy.

## 🗺️ Layout

```
skill-bartender/
├── skills/
│   └── skill-bartender/
│       ├── SKILL.md             # the skill itself (one file, three platforms)
│       └── references/policy.md # user-editable routing table
├── docs/
│   ├── screenshots/how-it-works.png
│   ├── eval.md                  # gold-task suite
│   ├── EXAMPLES.md / ROUTING-GUIDE.md
│   ├── skillspector-report.json # self-scan: 0 findings
│   ├── social-preview.png       # banner (regenerate via scripts/)
│   └── lang/README_ZH.md        # 简体中文
├── scripts/
│   ├── make-banner.py           # composes docs/social-preview.png
│   ├── make-diagram.py          # composes the how-it-works diagram
│   └── validate.py              # local structure validation
├── cordis.patch.yml / index.js / package.json   # DSH bundle manifest
└── LICENSE (MIT)
```

## 🤝 Join the DSH plugin ecosystem

DeepSeek Harness developer preview is still in its testing phase for Harness
developers; core plugins and base APIs will keep iterating. We look forward
to exploring the upper limits of intelligence together with developers
worldwide, on top of open-source, open, reusable, and composable infrastructure.

- [dsh-plugin topic](https://github.com/topics/dsh-plugin)
- [Quickstart](https://deepseek-harness.github.io/deepseek-harness/guide/quickstart)
- [DeepSeek Harness repo](https://github.com/deepseek-ai/deepseek-harness)
- Companion executor: [dsh-skill-router](https://github.com/akqwpeter-prog/dsh-skill-router)

> This repo is tagged [`dsh-plugin`](https://github.com/topics/dsh-plugin) and
> listed in the [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin)
> curated list. PRs, issues and translations are welcome.

## 📄 License

[MIT](LICENSE). Ponytail (MIT) is referenced, not bundled — tribute in the SKILL.md.
