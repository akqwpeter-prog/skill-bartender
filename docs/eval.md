# Eval: gold task suite

> The routing policy ships with a benchmark. New rules must not break it.
> Method: run each task with and without the policy; compare the loaded skill
> set, total tokens, and first-response latency.

## Real tasks (mined from actual agent sessions)

| # | Task | Expected pour | Why |
|---|---|---|---|
| 1 | "Port the image skills from Codex to DSH" | none | porting = read source, no skill matches |
| 2 | "Generate a few test images" | media-tools | single clear match |
| 3 | "Confirm privacy & security, no keys" | none | audit = subagents + code scan |
| 4 | "Model can't read images, can we change that?" | none | mechanism research, read source |
| 5 | "Publish to GitHub, join dsh-plugin" | none | gh CLI + git, plain tools suffice |

> 4 of 5 real tasks expect **zero** loading — rung 0 is where the value is.

## Synthetic routing cases

| # | Task | Pour | Do not pour |
|---|---|---|---|
| 6 | "Summarize this week's meeting minutes" | lark-workflow-meeting-summary | lark-minutes, lark-vc |
| 7 | "What's on my plate today?" | lark-workflow-standup-report | lark-calendar + lark-task |
| 8 | "Check my approval todos" | lark-approval | lark-task |
| 9 | "Message Zhang San" | lark-im | lark-contact (add only if open_id needed) |
| 10 | "Import this table into Base" | lark-base | lark-sheets, lark-drive |
| 11 | "Find last Wednesday's meeting minutes" | lark-vc | lark-calendar |
| 12 | "Edit this doc: https://…/docx/…" | lark-doc | lark-drive, lark-wiki |

## Pass bar

- False pours = 0. Missed pours ≤ 2 (catalog still completes the task).
- Total tokens must not rise vs. no-policy baseline.
