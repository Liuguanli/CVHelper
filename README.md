# CV Harness Workspace

## Overview

This repository helps you run a practical end-to-end workflow for:

- Role-specific resume tailoring (LaTeX based)
- Cover letter and HR self-intro video script generation
- Daily automated job watch with GitHub Actions
- CI/CD practice on a real personal productivity project

### Key points

- Resume source of truth: `CV-ByteDance.tex`
- Evidence source of truth: `base/fact_bank.md`
- Per-role isolation: each role has its own folder under `jobs/`
- Daily watch automation: updates are proposed via PR (not direct push)
- CI baseline: lint + tests on every PR/push

---

## Repository structure

```text
CVHelper/
├── CV-ByteDance.tex
├── base/
│   ├── fact_bank.md
│   ├── writing_rules.md
│   └── iteration_playbook.md
├── prompts/
│   ├── 01_analyze_job.md
│   ├── 02_tailor_resume.md
│   └── 03_write_cover_letter.md
├── jobs/
│   ├── _template/
│   └── <job-slug>/
│       ├── job_posting.md
│       ├── company_notes.md
│       ├── targeting_notes.md
│       └── outputs/<yyyymmdd>/
├── market_watch/
│   ├── watch_targets.md
│   ├── discovered_roles.md
│   └── alerts.md
├── watch/
│   ├── config.json
│   ├── run_daily_watch.py
│   └── state/
├── scripts/
│   ├── new_job.sh
│   └── build_resume.sh
└── .github/workflows/
    ├── ci.yml
    └── job_watch.yml
```

---

## Quick start

### 1) Create a role workspace

```bash
scripts/new_job.sh company-role-yyyymm
```

### 2) Fill role inputs

- `jobs/<job-slug>/job_posting.md`
- `jobs/<job-slug>/company_notes.md`
- `jobs/<job-slug>/targeting_notes.md`

### 3) Generate outputs

Use prompts in `prompts/` to produce:

- `job_analysis_<yyyymmdd>.md`
- `resume_changes_<yyyymmdd>.md`
- `ats_review_<yyyymmdd>.md`
- `hr_review_<yyyymmdd>.md`
- tailored resume `.tex` and `.pdf`
- cover letter and HR video script

### 4) Compile LaTeX resume

```bash
bash scripts/build_resume.sh jobs/<job-slug>/outputs/<yyyymmdd>/tailored_resume.tex
```

---

## Detailed usage

### A. Resume + application material workflow

1. Analyze the role (`prompts/01_analyze_job.md`)
2. Tailor resume with minimal necessary edits (`prompts/02_tailor_resume.md`)
3. Generate cover letter + HR script + HR review (`prompts/03_write_cover_letter.md`)
4. Save each iteration in a new dated output folder

Design rules:

- Stay truthful and interview-defensible
- Prefer natural JD-term mapping over keyword stuffing
- Keep structure stable unless a role-specific reason requires change

### B. Daily job watch workflow

`watch/run_daily_watch.py` collects roles from configured sources and updates:

- `market_watch/discovered_roles.md`
- `market_watch/alerts.md`
- `watch/state/seen_jobs.json`
- `watch/state/latest_digest.md`

Optional email digest is sent when SMTP secrets are configured.

Required secrets (GitHub):

- `SMTP_HOST`
- `SMTP_PORT`
- `SMTP_USERNAME`
- `SMTP_PASSWORD`
- `EMAIL_FROM`
- `EMAIL_TO`

---

## CI/CD setup in this repo

### CI (`.github/workflows/ci.yml`)

Runs on `push`/`pull_request`:

- install dependencies
- `ruff check watch tests`
- `pytest -q`

### CD-style automation (`.github/workflows/job_watch.yml`)

Runs daily and on manual dispatch:

1. executes `watch/run_daily_watch.py`
2. creates/updates an automation PR with watch output changes
3. after merge, changes become part of `main`

This avoids direct bot pushes and keeps change history reviewable.

---

## How to ensure you always see the latest work

### On GitHub

1. Check **Actions** for the latest `Daily Job Watch` run status
2. Check open PRs for a PR titled `chore(job-watch): update daily snapshot`
3. Review and merge that PR to publish the latest watch output to `main`

### Locally

1. Pull latest main:

```bash
git pull
```

2. Confirm freshness in:

- `watch/state/latest_digest.md`
- `market_watch/discovered_roles.md`

3. Use `Last updated: <date>` in generated markdown to verify recency.

If no new PR is created on a run, it usually means no meaningful watch changes were detected.

---

## Practical CI/CD practice path (recommended)

1. Break a small test intentionally, open PR, and verify CI fails.
2. Fix test and verify CI turns green.
3. Trigger `Daily Job Watch` manually (`workflow_dispatch`) and verify automation PR appears.
4. Merge PR and verify latest digest files update on `main`.
5. Pull locally and verify you can see the newest watch snapshot.

