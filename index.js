/**
 * Bundled `skill-bartender` skill provider.
 *
 * Ships the task-to-skill pairing meta-skill for DeepSeek Harness:
 * - laziness ladder (zero loading when plain tools suffice)
 * - user-editable routing table (references/policy.md)
 * - quarantine -> SkillSpector scan -> human approval install flow
 *
 * The plugin registers one provider on `ctx.skills`. The skill body lives
 * under `skills/skill-bartender/SKILL.md`. No keys, no network, no side
 * effects beyond the registration.
 *
 * @module skill-bartender
 */

import { readFile } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'

const PROVIDER_NAME = 'skill-bartender'

const SKILL = {
  name: 'skill-bartender',
  description:
    'Task-to-skill pairing with a laziness ladder and a safe install cellar. Use when a task may need specialized skills, when choosing among skills, when the user asks to find or install a skill, or to audit installed skill descriptions. Pairs the minimal set (usually one; zero when plain tools suffice), prefers workflow skills over hand-composed atomic ones, and never auto-installs: every downloaded SKILL.md is quarantined, scanned with SkillSpector, and installed only after explicit human approval.',
  invocation: { modelInvocable: true, userInvocable: true },
  provider: PROVIDER_NAME,
  source: 'bundled',
  resourceBase: {
    kind: 'directory',
    path: fileURLToPath(new URL('./skills/skill-bartender/', import.meta.url)),
  },
  rank: 600,
  locator: new URL('./skills/skill-bartender/SKILL.md', import.meta.url),
}

const provider = {
  name: PROVIDER_NAME,
  list: () => Promise.resolve([SKILL]),
  async get(candidate) {
    const raw = await readFile(candidate.locator, 'utf8')
    const content = raw.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n?/, '')
    return {
      name: candidate.name,
      description: candidate.description,
      invocation: candidate.invocation,
      provider: candidate.provider,
      source: candidate.source,
      resourceBase: candidate.resourceBase,
      content,
    }
  },
}

/** Cordis plugin name. */
export const name = 'skill-bartender'
/** Service required by the bundled provider. */
export const inject = ['skills']

/** Register the bundled skill. */
export async function apply(ctx) {
  ctx.skills.registerProvider(() => provider)
}

