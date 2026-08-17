# Routing guide

The routing table in `references/policy.md` is data, not prose. Rules:

1. **Task column names the trigger, not the feature.** "Generate image
   / poster / banner" beats "free image generation" — the catalog
   matcher reads the trigger.
2. **One row per decision**, concrete columns (pour / do not pour).
3. **URL-keyed families route by path pattern**, one skill per task.
4. **Workflow before atomic**: if a workflow skill composes the task,
   never hand-assemble atomics.
5. **`whenToUse` frontmatter** on any skill should be a short trigger
   phrase (e.g. `飞书审批`), not prose — dsh-skill-router matches it
   literally. Long prose never fires.
6. **The do-not-pour column is load-bearing**: it is what stops
   family-pack loading and same-domain duplicates.
