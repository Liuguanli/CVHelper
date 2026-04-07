# Prompt: Write Cover Letter And HR Video Script

请基于以下输入文件生成两份内容：

- `jobs/<job-slug>/outputs/cover_letter.md`
- `jobs/<job-slug>/outputs/hr_video_script.md`
- `jobs/<job-slug>/outputs/hr_review.md`

输入文件：

- `base/fact_bank.md`
- `base/writing_rules.md`
- `jobs/<job-slug>/job_posting.md`
- `jobs/<job-slug>/company_notes.md`
- `jobs/<job-slug>/targeting_notes.md`
- `jobs/<job-slug>/outputs/job_analysis.md`
- `jobs/<job-slug>/outputs/resume_changes.md`

要求：

## Cover letter

- 用第一人称。
- 不要写传统模板腔开头。
- 长度控制在 250 到 400 词。
- 更像一封简洁、有判断力、能体现匹配度的说明信。
- 明确写出：
  - 为什么这个岗位值得我申请
  - 为什么我的背景和他们当前需求匹配
  - 我最相关的两到三个例子
  - 一个自然的收尾
- 如果要强调 research 能力，不要只列论文名。
- 优先用简化版 STAR 方法来讲研究项目：
  - problem
  - what I built / proposed
  - why it mattered
  - venue or publication status
- 如果提到顶会，请自然嵌入，比如 `VLDB 2025`、`ICDE 2023`、`submitted to VLDB 2026`。
- 如果论文还未正式接收，必须明确说明。

## HR video script

- 这是给 HR 的自我介绍视频稿，不是逐字照搬 cover letter。
- 口语化，要能直接朗读。
- 控制在 3 到 4 分钟，绝对不能超过 5 分钟。
- 风格要自然、自信、不过度推销。
- 尽量用简单、直接、好读的英文，不要用太难读的词。
- 内容结构：
  1. `Hi, I am Guanli Liu.`
  2. 我来自哪里 / 我现在在哪里
  3. 我申请的是哪个岗位
  4. 我申请这个岗位的原因
  5. 我最近做的东西
  6. 我跟这个岗位 match 的点
  7. 我能带来什么
  8. 简短结束语

额外要求：

- cover letter 和视频稿都必须具体，避免空话。
- 视频稿要避免太书面化的长句。
- 视频稿中的项目例子尽量按 STAR 顺序展开，但要自然，不要机械。
- 如果 research 是卖点，要讲清楚论文最关键的点，而不是只报刊物名。
- 如果岗位信息不足，就明确使用保守表达，不要脑补。

## HR review

- 用“美国 HR / recruiter”的视角审这套材料。
- 重点看：
  - 第一印象是否清楚
  - 是否容易理解你适合什么岗位
  - 会不会觉得太学术、太泛、太像 AI 写的
  - cover letter 和视频稿是否有记忆点
  - 哪些地方可能让 HR 犹豫
- 输出格式建议包含：
  - `HR Readout`
  - `What works well`
  - `What may worry HR`
  - `Would I move this candidate forward?`
  - `How to improve before sending`
