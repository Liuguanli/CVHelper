# Jobs Folder

Use one dedicated directory per role. Suggested naming:

- `company-role-yyyymm`
- Example: `databricks-data-engineer-202604`

Each role directory should contain only two categories:

- Inputs: JD, company context, your targeting direction
- Outputs: all generated artifacts under `outputs/<yyyymmdd>/`

Suggested minimum outputs per round:

- `job_analysis_<yyyymmdd>.md`
- `resume_changes_<yyyymmdd>.md`
- `ats_review_<yyyymmdd>.md`
- `hr_review_<yyyymmdd>.md`
- resume PDF
- cover letter PDF
- video script PDF

Current target-role table:

- `jobs/target_roles.md`

Benefits of this structure:

- No cross-contamination between different roles
- Easy reuse of proven wording from previous applications
- Easy path to later batching and automation
- Cleaner role root directories with less clutter
