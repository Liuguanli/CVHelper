# Job Watch Automation

这个目录是给 GitHub Actions 用的“每日岗位巡检”脚本。

设计目标：

- 每天自动抓一轮岗位页
- 只保留和你的背景相关的岗位
- 把结果写回仓库，方便你本地 `git pull`
- 同时发一封邮件摘要给你
- 邮件正文优先用 HTML 表格展示，方便快速浏览

## 结果存在哪里

GitHub Actions 跑完之后，会更新这些文件：

- `market_watch/discovered_roles.md`
- `market_watch/alerts.md`
- `watch/state/seen_jobs.json`
- `watch/state/latest_digest.md`

也就是说：

- 邮件是“提醒”
- 仓库里的 `market_watch/` 和 `watch/state/` 是“持久化存档”

你本地只需要：

```bash
git pull
```

就能把 GitHub Actions 生成的最新结果同步下来。

## GitHub Actions 需要的 Secrets

在 GitHub 仓库页面：

`Settings -> Secrets and variables -> Actions`

添加这些 secrets：

- `SMTP_HOST`
- `SMTP_PORT`
- `SMTP_USERNAME`
- `SMTP_PASSWORD`
- `EMAIL_FROM`
- `EMAIL_TO`

如果你用 Gmail，推荐：

- 开启两步验证
- 创建一个 App Password
- 把 App Password 放进 `SMTP_PASSWORD`

常见 Gmail 配置：

- `SMTP_HOST=smtp.gmail.com`
- `SMTP_PORT=465`

## 运行方式

- 每天定时：GitHub Actions 自动跑
- 手动测试：在 GitHub Actions 页面点 `Run workflow`

## 当前实现说明

- 这是一个“最小可运行版”
- 它优先抓官方 careers 页面和 job boards
- 已额外纳入部分澳洲技术公司来源，例如 Atlassian、Canva、Airwallex、Xero、SafetyCulture
- 不同公司页面结构差异很大，所以解析是 best-effort
- 如果某些页面抓不到发布日期，结果里会明确写 `Not shown on page`
- 后面可以逐步为 Databricks / OpenAI / Amazon / Google 单独做更强的解析器
