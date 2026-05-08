# Prompt: Tailor Resume

Based on the input files below, apply minimal necessary edits to the current LaTeX resume and produce:

- Role-tailored LaTeX resume: `jobs/<job-slug>/outputs/tailored_resume.tex`
- Compiled PDF: `jobs/<job-slug>/outputs/tailored_resume.pdf`
- Change log: `jobs/<job-slug>/outputs/resume_changes.md`
- ATS screening review: `jobs/<job-slug>/outputs/ats_review.md`

Input files:

- `CV-ByteDance.tex`
- `base/fact_bank.md`
- `base/writing_rules.md`
- `jobs/<job-slug>/job_posting.md`
- `jobs/<job-slug>/company_notes.md`
- `jobs/<job-slug>/targeting_notes.md`
- `jobs/<job-slug>/outputs/job_analysis.md`

Hard requirements:

1. Keep everything truthful; do not add unsupported experience.
2. Keep structure and layout as stable as possible.
3. Prioritize edits in this order:
   - Profile paragraph
   - Wording and ordering of bullets in Experience
   - Ordering and emphasis in Skills
4. For backend/data/infra roles, prioritize emphasis on:
   - scalable backend systems
   - data infrastructure
   - ingestion / pipelines
   - SQL / databases
   - benchmarking / performance / reliability
5. For AI/retrieval/applied ML roles, prioritize emphasis on:
   - RAG
   - retrieval
   - vector / embedding-related work
   - system building over pure theory
6. Do not turn the resume into JD keyword stuffing.
7. Avoid AI-mass-generated tone: no vague, over-packaged, repetitive phrasing.
8. Maximize ATS compatibility.
9. ATS-friendly writing means natural mapping of JD terms to real experience, not brute-force keyword repetition.
10. Every line must be defensible in interviews.

Output requirements:

- `tailored_resume.tex` must remain compilable.
- After generating `.tex`, compile `tailored_resume.pdf` via `scripts/build_resume.sh` in this repository.
- If a JD keyword is not a perfect match to your experience, use the closest truthful phrasing; do not fabricate.

`resume_changes.md` should include:

- `What changed`
- `Why it changed`
- `What was intentionally not changed`
- `Any remaining fit gaps`

`ats_review.md` should include:

- `ATS Match Score`: 0-100
- `Why this score`
- `Keyword Coverage`
- `Evidence Strength`
- `Likely Screening Risks`
- `Recommended Resume Fixes Before Applying`

Scoring principles:

- Aim for conservative, practical, actionable scoring, not inflated numbers.
- Evaluate keyword coverage by real mapping quality, not mechanical matching.
- If there is a clear gap between JD and experience, lower the score and state why.
