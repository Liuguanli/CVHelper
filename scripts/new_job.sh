#!/usr/bin/env bash

set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: scripts/new_job.sh <job-slug>"
  exit 1
fi

job_slug="$1"
target_dir="jobs/${job_slug}"

if [ -e "$target_dir" ]; then
  echo "Directory already exists: $target_dir"
  exit 1
fi

mkdir -p "$target_dir/outputs"

cp jobs/_template/job_posting.md "$target_dir/job_posting.md"
cp jobs/_template/company_notes.md "$target_dir/company_notes.md"
cp jobs/_template/targeting_notes.md "$target_dir/targeting_notes.md"

echo "Created: $target_dir"
echo "Next step: paste the JD into $target_dir/job_posting.md"
