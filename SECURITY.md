# Security

## Threat model

Skills are **instructions**, and instructions can be adversarial
(prompt injection). A downloaded SKILL.md is not trusted until it passes
the quarantine pipeline in `SKILL.md`: download to a quarantine dir,
scan with [SkillSpector](https://github.com/NVIDIA/SkillSpector), show
the human the verdict, and install only after explicit approval.

`scripts/` in any skill is **code**. It is never executed without human
review, regardless of scan results.

## Reporting a vulnerability

Open an issue with the `security` label, or contact the maintainer
directly. Do not include live secrets in the report.
