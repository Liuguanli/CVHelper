# Job Watch Automation

This folder contains the daily job-watch script used by GitHub Actions.

Design goals:

- Automatically fetch one round of job pages every day
- Keep only roles relevant to your background
- Write results back to the repository so local `git pull` is enough
- Send an email digest at the same time
- Prefer HTML table formatting in email for fast scanning

## Where results are stored

After GitHub Actions completes, it updates:

- `market_watch/discovered_roles.md`
- `market_watch/alerts.md`
- `watch/state/seen_jobs.json`
- `watch/state/latest_digest.md`

In other words:

- Email acts as a reminder
- `market_watch/` and `watch/state/` are your persisted archive

Locally, you only need:

```bash
git pull
```

to sync the latest generated snapshot.

## Required GitHub Actions secrets

In your GitHub repository:

`Settings -> Secrets and variables -> Actions`

Add these secrets:

- `SMTP_HOST`
- `SMTP_PORT`
- `SMTP_USERNAME`
- `SMTP_PASSWORD`
- `EMAIL_FROM`
- `EMAIL_TO`

For Gmail, recommended setup:

- Enable 2-factor authentication
- Create an App Password
- Store it in `SMTP_PASSWORD`

Common Gmail values:

- `SMTP_HOST=smtp.gmail.com`
- `SMTP_PORT=465`

## Run modes

- Scheduled daily run: automatic via GitHub Actions
- Manual test: click `Run workflow` in the GitHub Actions UI

## Current implementation notes

- This is a minimal but runnable implementation
- It prioritizes official careers pages and job boards
- It already includes additional APAC/Australia-related sources such as Atlassian, Canva, MongoDB, Microsoft, Oracle, Telstra, Airwallex, Xero, and SafetyCulture
- Page structures vary heavily by company, so parsing is best-effort
- If posting dates are unavailable, output explicitly shows `Not shown on page`
- Dedicated parsers can be added incrementally for Databricks / OpenAI / Amazon / Google
