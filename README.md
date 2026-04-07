# CV Harness Workspace

这个目录现在已经有一份 LaTeX 简历母版：`CV-ByteDance.tex`。

为了用 harness 高效完成“按岗位微调简历 + 生成可直接朗读的 cover letter / HR 视频稿”，建议把工作区固定成下面这个结构：

```text
CVHelper/
├── CV-ByteDance.tex                # 当前简历母版
├── base/
│   ├── fact_bank.md                # 事实库：经历、技能、亮点、不能乱写的边界
│   └── writing_rules.md            # 写作约束：真实性、语气、时长、风格
├── prompts/
│   ├── 01_analyze_job.md           # 先拆解岗位需求
│   ├── 02_tailor_resume.md         # 再改简历
│   └── 03_write_cover_letter.md    # 生成 cover letter 和视频稿
├── jobs/
│   ├── _template/
│   │   ├── job_posting.md
│   │   ├── company_notes.md
│   │   ├── targeting_notes.md
│   └── <job-slug>/
│       ├── job_posting.md
│       ├── company_notes.md
│       ├── targeting_notes.md
│       └── outputs/
│           └── <yyyymmdd>/
├── market_watch/
│   ├── README.md                   # 新发现的相似岗位放这里
│   ├── watch_targets.md            # 追踪范围和筛选规则
│   ├── discovered_roles.md         # 后续发现的新岗位清单
│   └── alerts.md                   # 值得优先看的岗位提醒
└── scripts/
    └── new_job.sh                  # 复制岗位模板
```

推荐工作流：

1. 运行 `scripts/new_job.sh company-role-date` 新建一个岗位目录。
2. 把 JD 粘贴到 `jobs/<job-slug>/job_posting.md`。
3. 把你对岗位的判断写到 `jobs/<job-slug>/targeting_notes.md`。
4. 先在 `jobs/<job-slug>/outputs/<yyyymmdd>/` 下生成岗位分析。
5. 再在同一个 dated 目录下生成简历、cover letter 和视频稿。
6. 最后补一轮评估输出：
   - ATS / 机器筛选打分
   - HR 视角 review
6. 每次新一轮修改，都新建一个 dated 目录，避免版本混在一起。

推荐文件命名：

- 分享给别人的最终文件，文件名里最好同时带上：
  - 你的名字
  - 文档类型
  - 公司或岗位名
  - 日期
- 推荐格式：
  - `guanli_liu_resume_<company>_<position>.pdf`
  - `guanli_liu_coverletter_<company>_<position>.pdf`
  - `guanli_liu_videoscript_<company>_<position>.pdf`
- 这样单独发文件时不会混淆，也方便你保留多个版本。

目录收纳原则：

- 每个岗位根目录只保留输入文件：`job_posting.md`、`company_notes.md`、`targeting_notes.md`
- 中间结果和最终结果统一放进 `outputs/<yyyymmdd>/`
- 不保留多余的占位输出文件
- LaTeX 编译垃圾文件会自动清理
- 每轮结果建议至少包含：
  - `job_analysis_<yyyymmdd>.md`
  - `resume_changes_<yyyymmdd>.md`
  - `ats_review_<yyyymmdd>.md`
  - `hr_review_<yyyymmdd>.md`
  - 简历 PDF
  - cover letter PDF
  - video script PDF

Git 管理建议：

1. 把 `base/`、`prompts/`、`jobs/`、`market_watch/`、`scripts/` 和简历母版纳入版本控制。
2. 忽略 LaTeX 编译中间文件、PDF、`.DS_Store` 等噪音文件。
3. 每新增一个岗位，尽量单独 commit，方便回看这次申请到底改了什么。
4. 如果某个岗位最后真的投递了，可以再打一个 tag 或单独建分支保存最终版本。
5. `market_watch/` 适合频繁小 commit，因为它本质上是持续更新的机会池。

几个关键建议：

- 简历只做“最小必要修改”，避免为了贴岗位而失真。
- cover letter 不要写成传统套话，应该更像 3 到 4 分钟的人话视频稿。
- 视频稿要能直接朗读，所以要短句、口语化、少从句。
- 任何没做过的事情都不要扩写成“我主导过”。

岗位追踪约定：

- 你已经决定要申请的岗位，放到 `jobs/`。
- 我后续发现的类似新岗位，先放到 `market_watch/discovered_roles.md`。
- 如果我判断某个岗位特别值得你尽快看，我会同时写进 `market_watch/alerts.md` 并在回复里直接提醒你。

如果后面你愿意，我可以下一步继续帮你把这个结构再升级成“输入一个 JD 就自动生成一套输出”的半自动脚本版本。
