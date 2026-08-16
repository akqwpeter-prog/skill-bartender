---
name: skill-bartender
description: >
  Task-to-skill pairing with a laziness ladder and a safe install cellar. Use
  when a task may need specialized skills, when choosing among skills, when
  the user asks to find or install a skill, or to audit installed skill
  descriptions. Pairs the minimal set (usually one; zero when plain tools
  suffice), prefers workflow skills over hand-composed atomic ones, and never
  auto-installs: every downloaded SKILL.md is quarantined, scanned with
  SkillSpector, and installed only after explicit human approval.
---

# Skill Bartender

You are the bartender of agent skills: mix the right cocktail for the task,
and never pour an untasted bottle.

## The ladder — stop at the first rung that holds

0. **No skill.** read/grep/glob/bash/web_search handle the task — load nothing.
1. **One skill.** Exactly one skill in the catalog matches — load it.
2. **Workflow over atomic.** A workflow skill already composes the task
   (e.g. meeting-summary, standup-report) — load it, never hand-assemble
   atomic skills.
3. **Unsure — don't load.** A wrong body stays in history forever; a missed
   load only costs one tool round-trip. Miss beats false pour.

Never pre-load "just in case". One skill first; add a second only when the
first proves insufficient mid-task.

## Pour (matching)

- Read the task. Consult the available-skills list (name + description).
- Apply the routing table in references/policy.md — user-editable, it
  overrides these defaults.
- Prefer specific over general; route URL-keyed skill families
  (doc/drive/wiki/sheets/base/slides) by URL path pattern, one at a time.
- Never auto-load unless the user names them: agent-reach-*, lark-openapi-explorer, lark-skill-maker.

## Cellar (installing a missing skill)

When a task genuinely needs a skill that is not installed:

1. **Search**: GitHub topic dsh-plugin, awesome lists, marketplaces. Prefer
   repos with a license, recent commits, and plain SKILL.md files.
2. **Quarantine**: download the SKILL.md into a quarantine dir — never
   directly into a skills root.
3. **Taste**: scan with NVIDIA SkillSpector. Install once:
   `uv tool install git+https://github.com/NVIDIA/skillspector.git`
   then run `skillspector scan QUARANTINE_DIR --no-llm --format json --output report.json`.
   No uv? python3 -m venv + pip install from the same repo, or build the
   included Dockerfile locally and run the scan inside the container.
   If unavailable, run the manual checklist in references/policy.md.
4. **Scripts are code**: SkillSpector reads prompts, not scripts. Any
   scripts/ file is executable code — do not run it; show it to the human
   for review, default deny.
5. **Human approval**: present source URL, commit hash, scan verdict, and a
   one-paragraph summary. Wait for an explicit yes. A passing scan is a
   filter, not a guarantee — prompt injection survives static scans.
6. **Install**: copy the approved SKILL.md (plus reviewed assets) into the
   skills root (e.g. ~/.dsh/skills/NAME/), record source + commit + scan
   result + date in your notes.

## Learn (don't pour twice)

Track every loaded skill. If one goes unused by task end: note it, and skip
it for the same task type next time. Offer to remove chronic no-shows.

## Taste test (audit the cellar)

On request: list installed skills, and rewrite weak descriptions into
"when-to-use" sentences — a description that names the trigger beats a
feature list. Keep each under the catalog cap (500 chars in DSH).

## Boundaries

- Never auto-install. Never run downloaded scripts without explicit approval.
- This skill must itself be loaded once (user gesture or task match); it
  cannot self-trigger.
- Spirit: ponytail (github.com/DietrichGebert/ponytail) — the best load is
  the load never made.
