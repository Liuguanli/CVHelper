import importlib.util
import sys
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "watch" / "run_daily_watch.py"
spec = importlib.util.spec_from_file_location("run_daily_watch", MODULE_PATH)
watch = importlib.util.module_from_spec(spec)
assert spec is not None and spec.loader is not None
sys.modules[spec.name] = watch
spec.loader.exec_module(watch)


def _config() -> dict:
    return {
        "exclusion_keywords": ["designer", "marketing"],
        "role_keywords": ["software engineer", "database", "systems", "backend"],
        "strong_match_keywords": ["database", "query", "storage", "performance"],
        "early_career_keywords": ["new grad", "graduate", "intern"],
        "preferred_locations": ["united states", "australia", "remote"],
    }


def _job(company: str, idx: int) -> watch.Job:
    return watch.Job(
        company=company,
        source=f"source-{company}",
        title=f"{company} Role {idx}",
        url=f"https://example.com/{company.lower()}/{idx}",
        location="Remote",
        posted_or_updated="2026-05-08",
        score=60 - idx,
        priority="high-priority",
        category="Strong Match",
        resume_fit="High",
        research_fit="High",
        notes="Signals: backend, systems",
    )


def test_normalize_url_drops_trailing_slash_and_fragment() -> None:
    result = watch.normalize_url("https://example.com/jobs/", "./123/#details")
    assert result == "https://example.com/jobs/123"


def test_looks_like_real_job_title_filters_generic_pages() -> None:
    assert watch.looks_like_real_job_title("Software Engineer, Data Infrastructure")
    assert not watch.looks_like_real_job_title("Open Roles")


def test_score_job_exclusion_keyword_returns_zero() -> None:
    score, priority, category, *_ = watch.score_job(
        "Software Engineer", "This role is for product marketing.", _config()
    )
    assert score == 0
    assert priority == "skip"
    assert category == "Low Priority"


def test_score_job_early_career_category_is_detected() -> None:
    score, priority, category, *_ = watch.score_job(
        "Software Engineer, New Grad",
        "Backend systems role with database and remote option.",
        _config(),
    )
    assert score > 0
    assert category == "Early-Career / New Grad"
    assert priority == "early-career"


def test_build_job_returns_none_for_non_trackable_title() -> None:
    source = watch.Source(
        name="Example",
        company="ExampleCo",
        url="https://example.com/jobs",
        allow_domains=["example.com"],
    )
    job = watch.build_job(
        source,
        _config(),
        title="Open Roles",
        url="/jobs",
        text="Generic listing page",
        location="",
        posted_or_updated="",
    )
    assert job is None


def test_cleanup_seen_jobs_removes_failed_or_generic_entries() -> None:
    seen = {
        "https://example.com/jobs/1": {
            "title": "[Source fetch failed] Example",
            "url": "https://example.com/jobs/1",
        },
        "https://example.com/blog/abc": {
            "title": "Software Engineer",
            "url": "https://example.com/blog/abc",
        },
        "https://example.com/jobs/2": {
            "title": "Software Engineer, Backend",
            "url": "https://example.com/jobs/2",
        },
    }
    cleaned = watch.cleanup_seen_jobs(seen)
    assert list(cleaned.keys()) == ["https://example.com/jobs/2"]


def test_diversify_jobs_balances_companies_then_fills_total_limit() -> None:
    jobs = [
        _job("OpenAI", 1),
        _job("OpenAI", 2),
        _job("OpenAI", 3),
        _job("Databricks", 1),
        _job("Databricks", 2),
        _job("Google", 1),
    ]
    selected = watch.diversify_jobs(jobs, per_company_limit=2, total_limit=5)
    assert len(selected) == 5
    assert sum(1 for j in selected if j.company == "OpenAI") <= 2
    assert sum(1 for j in selected if j.company == "Databricks") <= 2
