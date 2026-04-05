# Prompt: Tailor Resume

请基于以下输入文件，对现有 LaTeX 简历做“最小必要修改”，并产出：

- 一个岗位定制版 LaTeX 简历：`jobs/<job-slug>/outputs/tailored_resume.tex`
- 一个编译后的 PDF：`jobs/<job-slug>/outputs/tailored_resume.pdf`
- 一个改动说明：`jobs/<job-slug>/outputs/resume_changes.md`

输入文件：

- `CV-ByteDance.tex`
- `base/fact_bank.md`
- `base/writing_rules.md`
- `jobs/<job-slug>/job_posting.md`
- `jobs/<job-slug>/company_notes.md`
- `jobs/<job-slug>/targeting_notes.md`
- `jobs/<job-slug>/outputs/job_analysis.md`

硬性要求：

1. 保持真实，不新增没有证据支持的经历。
2. 尽量保持原有结构和排版稳定。
3. 修改优先级：
   - Profile 段落
   - Experience 中 bullet 的措辞和顺序
   - Skills 中的排序和强调
4. 如果岗位是偏 backend / data / infra，就优先强调：
   - scalable backend systems
   - data infrastructure
   - ingestion / pipelines
   - SQL / databases
   - benchmarking / performance / reliability
5. 如果岗位是偏 AI / retrieval / applied ML，就优先强调：
   - RAG
   - retrieval
   - vector / embedding related work
   - system building rather than pure theory
6. 不要让简历变成 JD 的关键词堆砌版本。
7. 不要让语言看起来像 AI 批量生成，避免空泛、过度包装、千篇一律的措辞。
8. 必须尽量通过 ATS。
9. ATS 友好的方式不是堆关键词，而是把 JD 里的关键术语自然地贴到真实经历上。
10. 所有措辞都必须经得起面试追问。

输出要求：

- `tailored_resume.tex` 应保持可编译。
- 生成 `.tex` 后，再使用仓库里的 `scripts/build_resume.sh` 编译出 `tailored_resume.pdf`。
- 如果某个 JD 关键词和你的经历不完全匹配，优先用接近但真实的表达，不要硬造。

`resume_changes.md` 请包含：

- `What changed`
- `Why it changed`
- `What was intentionally not changed`
- `Any remaining fit gaps`
