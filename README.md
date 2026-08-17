# skill-bartender 🍸

[![License](https://img.shields.io/github/license/akqwpeter-prog/skill-bartender)](LICENSE)
[![SkillSpector CI](https://github.com/akqwpeter-prog/skill-bartender/actions/workflows/scan.yml/badge.svg)](https://github.com/akqwpeter-prog/skill-bartender/actions/workflows/scan.yml)
[![dsh-plugin](https://img.shields.io/badge/topic-dsh--plugin-2ea44f)](https://github.com/topics/dsh-plugin)

**Task-to-skill pairing with a laziness ladder and a safe install cellar.**

Your agent already sees a catalog of skill names and descriptions — but it
over-pours: loads too many skills, loads the wrong ones, or misses the one
workflow skill that composes the task. **skill-bartender** is the meta-skill
that fixes the pour:

- 🪜 **Laziness ladder** — zero skills when plain tools suffice; one skill
  when one matches; workflow over hand-composed atomics; unsure → don't load.
  (Spirit: [ponytail](https://github.com/DietrichGebert/ponytail) — the best
  load is the load never made.)
- 🍷 **Routing table** — a user-editable task→skill map (references/policy.md).
- 🔐 **Safe cellar** — when a needed skill is missing: quarantine →
  [SkillSpector](https://github.com/NVIDIA/SkillSpector) scan → **explicit
  human approval** → copy into the skills dir. Never auto-installs.
- 🧠 **Learn** — loaded-but-unused skills get logged and skipped next time.

## Install (one file, three platforms)

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

Then say "skill-bartender" once, or paste the routing table into your
AGENTS.md for always-on routing.

Or install as a DeepSeek Harness bundle:

    dsh plugin --profile web add github:akqwpeter-prog/skill-bartender

## Self-scan

This skill scans itself clean: SkillSpector **0 findings** (score 0 / SAFE).
Report: [docs/skillspector-report.json](docs/skillspector-report.json).

## Security model (read this)

- Skills are **instructions**, and instructions can be adversarial (prompt
  injection). SkillSpector is a **filter, not a guarantee**.
- scripts/ in any skill is **code** — never executed without human review.
- Human approval is mandatory for every install. No silent installs, ever.

## Not reinventing the wheel

Use skill-bartender *alongside* the ecosystem, not instead of it:
[DshMarket](https://github.com/dsh-market/dsh-market) (GUI marketplace),
[dsh-find-plugin](https://github.com/awesome-dsh-plugin/dsh-find-plugin)
(conversational search), [dsh-plugin-autoevo](https://github.com/klarkxy/dsh-plugin-autoevo)
(plugin auto-install with approval). skill-bartender adds the **routing
policy** and the **quarantine-then-approve** discipline for skills.

## Eval

The routing policy ships with a gold-task suite: [docs/eval.md](docs/eval.md).

## License

MIT. Ponytail (MIT) is referenced, not bundled — tribute in the SKILL.md.
