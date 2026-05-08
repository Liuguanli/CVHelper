# Prompt: Analyze Job

Analyze the role based on the input files below and write the result to `jobs/<job-slug>/outputs/job_analysis.md`.

Input files:

- `jobs/<job-slug>/job_posting.md`
- `jobs/<job-slug>/company_notes.md`
- `jobs/<job-slug>/targeting_notes.md`
- `base/fact_bank.md`
- `base/writing_rules.md`

Requirements:

1. Summarize in 3-5 sentences what kind of candidate this role is actually seeking.
2. List:
   - must-have requirements
   - nice-to-have requirements
   - likely pain points of the hiring team
3. Identify what should be emphasized most from my background.
4. Identify potential gaps between my background and the role, with honest framing suggestions.
5. Provide up to 8 concrete recommendations for resume tailoring.
6. Provide up to 6 concrete recommendations for cover letter / video script positioning.

Output format:

- `Role summary`
- `Must have`
- `Nice to have`
- `Likely team needs`
- `Best evidence from my background`
- `Potential gaps and honest framing`
- `Resume tailoring plan`
- `Cover letter / video plan`
