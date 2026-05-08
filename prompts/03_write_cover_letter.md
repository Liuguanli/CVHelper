# Prompt: Write Cover Letter And HR Video Script

Generate the following outputs from the input files below:

- `jobs/<job-slug>/outputs/cover_letter.md`
- `jobs/<job-slug>/outputs/hr_video_script.md`
- `jobs/<job-slug>/outputs/hr_review.md`

Input files:

- `base/fact_bank.md`
- `base/writing_rules.md`
- `jobs/<job-slug>/job_posting.md`
- `jobs/<job-slug>/company_notes.md`
- `jobs/<job-slug>/targeting_notes.md`
- `jobs/<job-slug>/outputs/job_analysis.md`
- `jobs/<job-slug>/outputs/resume_changes.md`

Requirements:

## Cover letter

- Use first person.
- Avoid generic template-style openings.
- Keep length within 250-400 words.
- Write as a concise and thoughtful statement of fit.
- Explicitly cover:
  - why this role is worth applying to
  - why my background matches current team needs
  - two to three most relevant examples
  - a natural closing
- If emphasizing research capability, do not only list paper titles.
- Prefer simplified STAR framing for research examples:
  - problem
  - what I built / proposed
  - why it mattered
  - venue or publication status
- If mentioning top venues, embed naturally (for example `VLDB 2025`, `ICDE 2023`, `submitted to VLDB 2026`).
- If a paper is not yet accepted, state that clearly.

## HR video script

- This is an HR self-intro script, not a line-by-line copy of the cover letter.
- Keep it conversational and directly speakable.
- Target 3-4 minutes; never exceed 5 minutes.
- Tone should be natural, confident, and not over-promotional.
- Prefer simple, direct, easy-to-read English.
- Suggested structure:
  1. `Hi, I am Guanli Liu.`
  2. Where I am from / where I am now
  3. Which role I am applying for
  4. Why I am applying for this role
  5. What I have been building recently
  6. Why my background matches this role
  7. What value I can bring
  8. Brief closing

Extra requirements:

- Both cover letter and video script must be concrete and avoid empty claims.
- Avoid overly written/formal long sentences in the video script.
- Use STAR-like ordering for project examples when possible, but keep it natural.
- If research is a selling point, explain the key idea first instead of just naming venues.
- If role information is incomplete, use conservative phrasing and avoid assumptions.

## HR review

- Review from a US HR/recruiter perspective.
- Focus on:
  - clarity of first impression
  - ease of understanding role fit
  - whether content feels too academic, too generic, or AI-written
  - whether cover letter and video script are memorable
  - where HR may hesitate
- Suggested output sections:
  - `HR Readout`
  - `What works well`
  - `What may worry HR`
  - `Would I move this candidate forward?`
  - `How to improve before sending`
