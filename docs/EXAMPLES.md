# Examples

## Worked routings

| Task | Pour | Why |
|---|---|---|
| 整理本周会议纪要成周报 | lark-workflow-meeting-summary | workflow composes it; never lark-minutes + lark-vc by hand |
| 帮我查一下审批待办 | lark-approval | single atomic match; lark-task is not approval |
| 生成一张海报 | media-tools | single match; vision-review is for reading, not making |
| 编辑 https://x.feishu.cn/docx/abc | lark-doc | URL path routing, one skill |
| 今天天气怎么样 | *(none)* | false-positive guard: no scheduling signal, pour nothing |

## Install log (fill after every install)

    skill: NAME
    source: REPO-URL @ COMMIT
    scanned: SkillSpector VERSION | manual checklist
    verdict: clean | notes
    human: approved by WHO on DATE
