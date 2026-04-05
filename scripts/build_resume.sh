#!/usr/bin/env bash

set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: bash scripts/build_resume.sh <path-to-tex>"
  exit 1
fi

tex_file="$1"

if [ ! -f "$tex_file" ]; then
  echo "TeX file not found: $tex_file"
  exit 1
fi

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
tex_dir="$(cd "$(dirname "$tex_file")" && pwd)"
tex_name="$(basename "$tex_file")"

cd "$repo_root"

xelatex -interaction=nonstopmode -halt-on-error -output-directory="$tex_dir" "$tex_file"
xelatex -interaction=nonstopmode -halt-on-error -output-directory="$tex_dir" "$tex_file"

pdf_file="${tex_dir}/$(basename "${tex_name%.tex}.pdf")"
echo "Built PDF: $pdf_file"
