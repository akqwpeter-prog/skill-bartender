# Changelog

## 0.1.2 (2026-08-17)

- Docs: full README refresh to match the dsh-media-skills standard —
  banner header, tagline, badge matrix, TOC + language links, Why/What
  you get tables, quick start, how-it-works diagram, FAQ, layout tree,
  ecosystem section.
- Banner: AI-generated cocktail-bar background + gradient overlay
  (scripts/make-banner.py now composes docs/social-preview.png from
  docs/bg-raw.png via media-tools).
- New scripts/make-diagram.py: docs/screenshots/how-it-works.png.
- Chinese README synced to the new structure.

## 0.1.1 (2026-08-17)

- Add SkillSpector CI: every change under `skills/` is scanned; HIGH
  findings fail the build.
- Add SECURITY.md, routing guide, examples, contributor guide, and a
  local validation script.

## 0.1.0 (2026-08-16)

- Initial release: laziness ladder, routing table, quarantine-then-
  approve install flow.
- Verified SkillSpector commands; self-scan clean (0 findings).
- dsh.bundle manifest for `dsh plugin add`.
