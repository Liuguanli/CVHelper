from __future__ import annotations

import json
import html
import os
import re
import smtplib
import ssl
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urljoin, urlparse, urlunparse
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parent.parent
WATCH_DIR = ROOT / "watch"
STATE_DIR = WATCH_DIR / "state"
MARKET_WATCH_DIR = ROOT / "market_watch"
CONFIG_PATH = WATCH_DIR / "config.json"
SEEN_JOBS_PATH = STATE_DIR / "seen_jobs.json"
LATEST_DIGEST_PATH = STATE_DIR / "latest_digest.md"
DISCOVERED_ROLES_PATH = MARKET_WATCH_DIR / "discovered_roles.md"
ALERTS_PATH = MARKET_WATCH_DIR / "alerts.md"
DEFAULT_TIMEZONE = "Australia/Melbourne"


DATE_PATTERNS = [
    re.compile(r"Posted[:\s]+([A-Z][a-z]+ \d{1,2}, \d{4})"),
    re.compile(r"Posted on[:\s]+([A-Z][a-z]+ \d{1,2}, \d{4})"),
    re.compile(r"Updated[:\s]+([A-Z][a-z]+ \d{1,2}, \d{4})"),
]

GENERIC_TITLE_PATTERNS = [
    re.compile(r"^open roles?\b", re.IGNORECASE),
    re.compile(r"^search jobs?\b", re.IGNORECASE),
    re.compile(r"^open positions?\b", re.IGNORECASE),
    re.compile(r"^job details\b", re.IGNORECASE),
    re.compile(r"^microsoft research blog\b", re.IGNORECASE),
    re.compile(r"^about microsoft research\b", re.IGNORECASE),
    re.compile(r"^microsoft research podcast\b", re.IGNORECASE),
    re.compile(r"^microsoft research\b", re.IGNORECASE),
    re.compile(r"^programming languages and software engineering$", re.IGNORECASE),
    re.compile(r"^join us at the forefront of research at microsoft$", re.IGNORECASE),
    re.compile(r"^empower engineers\. inspire productivity\.$", re.IGNORECASE),
    re.compile(r"^careers?$", re.IGNORECASE),
    re.compile(r"^jobs?$", re.IGNORECASE),
]

GENERIC_URL_SNIPPETS = [
    "/blog/",
    "/podcast/",
    "/about/",
    "/search?",
    "/search/",
    "/company/careers",
    "/careers/open-positions/",
    "/research-area/",
    "/about-microsoft-research/",
    "/applications/jobs/results/ai",
    "/applications/jobs/results/dashboard",
    "/applications/jobs/results/how-we-hire",
    "/applications/jobs/results/students",
    "/applications/jobs/results/teams",
]

TITLE_ROLE_KEYWORDS = [
    "software engineer",
    "software development engineer",
    "research engineer",
    "research scientist",
    "applied scientist",
    "researcher",
    "member of technical staff",
    "data engineer",
    "data infrastructure",
    "database",
    "systems",
    "backend",
    "storage",
    "query",
    "platform engineer",
    "ml systems",
    "research fellow",
    "postdoctoral",
    "postdoc",
    "lecturer",
    "academic",
    "new grad",
    "graduate",
    "early career",
    "intern",
]

TITLE_REQUIRED_TOKENS = [
    "engineer",
    "scientist",
    "developer",
    "researcher",
    "intern",
    "graduate",
    "student",
    "architect",
    "fellow",
    "lecturer",
    "professor",
]

EARLY_CAREER_TITLE_KEYWORDS = [
    "early career",
    "new grad",
    "graduate",
    "university grad",
    "entry level",
    "intern",
    "internship",
    "student",
]

SENIORITY_TITLE_KEYWORDS = [
    "senior",
    "staff",
    "principal",
    "manager",
    "director",
    "head of",
    "lead ",
    "vp ",
    "vice president",
]

JOB_PAGE_SIGNALS = [
    "responsibilities",
    "qualifications",
    "minimum qualifications",
    "preferred qualifications",
    "about the job",
    "job description",
    "what you'll do",
    "what you will do",
    "about the role",
    "basic qualifications",
]

LOCATION_PATTERNS = [
    re.compile(r"(San Francisco, CA|Seattle, WA|New York City, NY|Mountain View, CA|Redmond, WA|Melbourne, Australia|Sydney, Australia|Remote-Friendly[^\\n]*)"),
    re.compile(r"(Menlo Park, CA|London, UK|Zürich, CH|Sydney, NSW, Australia|Melbourne, VIC, Australia)"),
]

AU_LOCATION_KEYWORDS = [
    "australia",
    "melbourne",
    "victoria",
    "vic",
    "sydney",
    "new south wales",
    "nsw",
    "brisbane",
    "queensland",
    "qld",
    "perth",
    "western australia",
    "wa",
    "canberra",
    "adelaide",
    "hobart",
    "darwin",
]


@dataclass
class Source:
    name: str
    company: str
    url: str
    allow_domains: list[str]
    source_type: str = "generic_html"
    board_token: str | None = None
    board_name: str | None = None
    search_queries: list[str] | None = None
    country_codes: list[str] | None = None
    result_limit: int | None = None


@dataclass
class Job:
    company: str
    source: str
    title: str
    url: str
    location: str
    posted_or_updated: str
    score: int
    priority: str
    category: str
    resume_fit: str
    research_fit: str
    notes: str


def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def load_seen_jobs() -> dict[str, dict]:
    if not SEEN_JOBS_PATH.exists():
        return {}
    return json.loads(SEEN_JOBS_PATH.read_text(encoding="utf-8"))


def save_seen_jobs(seen: dict[str, dict]) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    SEEN_JOBS_PATH.write_text(json.dumps(seen, indent=2, ensure_ascii=False), encoding="utf-8")


def request_headers(*, accept_json: bool = False) -> dict[str, str]:
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; CVHelperJobWatch/1.0; +https://github.com/)",
        # Avoid zstd responses because some Python environments here fail to decode them reliably.
        "Accept-Encoding": "gzip, deflate",
    }
    if accept_json:
        headers["Accept"] = "application/json"
    return headers


def fetch(url: str) -> str:
    response = requests.get(
        url,
        headers=request_headers(),
        timeout=30,
    )
    response.raise_for_status()
    return response.text


def fetch_json(url: str) -> dict[str, Any]:
    response = requests.get(
        url,
        headers=request_headers(accept_json=True),
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def normalize_url(base_url: str, href: str) -> str:
    joined = urljoin(base_url, href)
    parsed = urlparse(joined)
    path = parsed.path.rstrip("/") or "/"
    clean = parsed._replace(path=path, fragment="")
    return urlunparse(clean)


def is_job_like_link(url: str, text: str, source: Source) -> bool:
    lower_url = url.lower()
    lower_text = text.lower()
    normalized_source = normalize_url(source.url, "")
    if url == normalized_source:
        return False
    if not any(domain in lower_url for domain in source.allow_domains):
        return False
    if any(snippet in lower_url for snippet in GENERIC_URL_SNIPPETS):
        return False
    if "google.com/about/careers/applications/jobs/results/" in lower_url and not re.search(r"/results/\d", lower_url):
        return False
    if any(token in lower_url for token in ["/jobs/", "/job/", "/careers/details/", "/job_details/", "/applications/jobs/results/", "/careers/jobs/", "/careers/job/"]):
        return True
    if any(token in lower_text for token in TITLE_ROLE_KEYWORDS):
        return True
    return False


def extract_candidate_urls(source: Source, html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    urls: set[str] = set()
    for link in soup.find_all("a", href=True):
        text = " ".join(link.get_text(" ", strip=True).split())
        href = link["href"].strip()
        url = normalize_url(source.url, href)
        if is_job_like_link(url, text, source):
            urls.add(url)
    return sorted(urls)


def text_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    return soup.get_text("\n", strip=True)


def first_non_empty(values: Iterable[str]) -> str:
    for value in values:
        if value and value.strip():
            return value.strip()
    return ""


def extract_title(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    title = first_non_empty(
        [
            soup.find("h1").get_text(" ", strip=True) if soup.find("h1") else "",
            soup.title.get_text(" ", strip=True) if soup.title else "",
            "",
        ]
    )
    return re.sub(r"\s+", " ", title)


def looks_like_real_job_title(title: str) -> bool:
    normalized = re.sub(r"\s+", " ", title).strip()
    if len(normalized) < 10:
        return False
    if any(pattern.search(normalized) for pattern in GENERIC_TITLE_PATTERNS):
        return False
    lower_title = normalized.lower()
    return any(keyword in lower_title for keyword in TITLE_ROLE_KEYWORDS) or any(token in lower_title for token in TITLE_REQUIRED_TOKENS)


def is_trackable_job_title(title: str) -> bool:
    normalized = re.sub(r"\s+", " ", title).strip()
    if not normalized or normalized.startswith("[Source fetch failed]"):
        return False
    if any(pattern.search(normalized) for pattern in GENERIC_TITLE_PATTERNS):
        return False
    return looks_like_real_job_title(normalized)


def is_trackable_job_url(url: str) -> bool:
    lower_url = url.lower()
    return not any(snippet in lower_url for snippet in GENERIC_URL_SNIPPETS)


def looks_like_job_page(url: str, title: str, text: str) -> bool:
    lower_url = url.lower()
    lower_title = title.lower()
    lower_text = text.lower()
    if any(snippet in lower_url for snippet in GENERIC_URL_SNIPPETS):
        return False
    if any(pattern.search(title) for pattern in GENERIC_TITLE_PATTERNS):
        return False
    if not looks_like_real_job_title(title):
        return False
    has_job_url = any(token in lower_url for token in ["/jobs/", "/job/", "/careers/details/", "/job_details/", "/careers/job/"])
    has_job_signal = any(signal in lower_text for signal in JOB_PAGE_SIGNALS)
    has_title_role = any(token in lower_title for token in TITLE_REQUIRED_TOKENS)
    return (has_job_url or has_job_signal) and has_title_role


def html_fragment_to_text(content: str) -> str:
    if not content:
        return ""
    soup = BeautifulSoup(html.unescape(content), "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    return soup.get_text("\n", strip=True)


def format_iso_date(value: str | None) -> str:
    if not value:
        return "Not shown on page"
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return value
    return parsed.date().isoformat()


def build_job(
    source: Source,
    config: dict,
    *,
    title: str,
    url: str,
    text: str,
    location: str,
    posted_or_updated: str,
) -> Job | None:
    title = re.sub(r"\s+", " ", title).strip()
    url = normalize_url(source.url, url)
    if not is_trackable_job_title(title) or not is_trackable_job_url(url):
        return None
    score, priority, category, resume_fit, research_fit, notes = score_job(title, text, config)
    if score == 0:
        return None
    resolved_location = location or "Not shown on page"
    # Hard filter: keep only explicitly Australia-based roles.
    if not is_australia_location(resolved_location):
        return None

    return Job(
        company=source.company,
        source=source.name,
        title=title,
        url=url,
        location=resolved_location,
        posted_or_updated=posted_or_updated or "Not shown on page",
        score=score,
        priority=priority,
        category=category,
        resume_fit=resume_fit,
        research_fit=research_fit,
        notes=notes,
    )


def is_australia_location(location: str) -> bool:
    normalized = (location or "").lower()
    return any(keyword in normalized for keyword in AU_LOCATION_KEYWORDS)


def collect_greenhouse_jobs(source: Source, config: dict) -> list[Job]:
    if not source.board_token:
        return []
    data = fetch_json(f"https://boards-api.greenhouse.io/v1/boards/{source.board_token}/jobs?content=true")
    jobs: list[Job] = []
    for item in data.get("jobs", []):
        title = item.get("title", "")
        description = html_fragment_to_text(item.get("content", ""))
        department_text = ", ".join(dep.get("name", "") for dep in item.get("departments", []) if dep.get("name"))
        office_text = ", ".join(
            first_non_empty([office.get("location", ""), office.get("name", "")])
            for office in item.get("offices", [])
            if first_non_empty([office.get("location", ""), office.get("name", "")])
        )
        text = "\n".join(part for part in [title, description, department_text, office_text] if part)
        location = first_non_empty(
            [
                item.get("location", {}).get("name", ""),
                office_text,
            ]
        )
        job = build_job(
            source,
            config,
            title=title,
            url=item.get("absolute_url", ""),
            text=text,
            location=location,
            posted_or_updated=format_iso_date(item.get("updated_at")),
        )
        if job:
            jobs.append(job)
    return jobs


def format_ashby_location(item: dict[str, Any]) -> str:
    primary = item.get("location") or ""
    secondary = [
        loc.get("location", "")
        for loc in item.get("secondaryLocations", [])
        if loc.get("location")
    ]
    locations = [primary] + secondary
    locations = [loc for loc in locations if loc]
    if item.get("isRemote") and "remote" not in " ".join(locations).lower():
        locations.append("Remote")
    return ", ".join(dict.fromkeys(locations)) if locations else "Not shown on page"


def collect_ashby_jobs(source: Source, config: dict) -> list[Job]:
    if not source.board_name:
        return []
    data = fetch_json(f"https://api.ashbyhq.com/posting-api/job-board/{source.board_name}")
    jobs: list[Job] = []
    for item in data.get("jobs", []):
        if item.get("isListed") is False:
            continue
        title = item.get("title", "")
        text = "\n".join(
            part
            for part in [
                title,
                item.get("descriptionPlain", ""),
                item.get("department", ""),
                item.get("team", ""),
                item.get("employmentType", ""),
                item.get("workplaceType", ""),
                format_ashby_location(item),
            ]
            if part
        )
        job = build_job(
            source,
            config,
            title=title,
            url=item.get("jobUrl") or item.get("applyUrl") or source.url,
            text=text,
            location=format_ashby_location(item),
            posted_or_updated=format_iso_date(item.get("publishedAt")),
        )
        if job:
            jobs.append(job)
    return jobs


def collect_amazon_jobs(source: Source, config: dict) -> list[Job]:
    queries = source.search_queries or ["software engineer"]
    result_limit = source.result_limit or 100
    allowed_countries = set(source.country_codes or [])
    jobs: list[Job] = []

    for query in queries:
        search_url = (
            "https://www.amazon.jobs/en/search.json"
            f"?base_query={requests.utils.quote(query)}"
            f"&sort=recent&result_limit={result_limit}"
        )
        data = fetch_json(search_url)
        for item in data.get("jobs", []):
            country_code = item.get("country_code", "")
            if allowed_countries and country_code not in allowed_countries:
                continue

            title = item.get("title", "")
            description = html_fragment_to_text(item.get("description", ""))
            qualifications = html_fragment_to_text(item.get("basic_qualifications", ""))
            preferred = html_fragment_to_text(item.get("preferred_qualifications", ""))
            location = first_non_empty(
                [
                    item.get("normalized_location", ""),
                    item.get("location", ""),
                    f"{item.get('city', '')}, {country_code}".strip(", "),
                ]
            )
            text = "\n".join(
                part
                for part in [
                    title,
                    description,
                    qualifications,
                    preferred,
                    item.get("job_category", ""),
                    item.get("job_family", ""),
                    item.get("business_category", ""),
                    location,
                ]
                if part
            )

            job = build_job(
                source,
                config,
                title=title,
                url=urljoin("https://www.amazon.jobs", item.get("job_path", "")),
                text=text,
                location=location,
                posted_or_updated=item.get("posted_date") or item.get("updated_time") or "Not shown on page",
            )
            if job:
                jobs.append(job)

    deduped: dict[str, Job] = {}
    for job in jobs:
        existing = deduped.get(job.url)
        if existing is None or job.score > existing.score:
            deduped[job.url] = job
    return list(deduped.values())


def collect_google_jobs(source: Source, config: dict) -> list[Job]:
    listing_html = fetch(source.url)
    soup = BeautifulSoup(listing_html, "html.parser")
    candidate_urls: set[str] = set()
    for link in soup.find_all("a", href=True):
        url = normalize_url(source.url, link["href"].strip())
        if re.search(r"/applications/jobs/results/\d", url):
            candidate_urls.add(url)

    jobs: list[Job] = []
    for candidate_url in sorted(candidate_urls)[:120]:
        try:
            job_html = fetch(candidate_url)
        except Exception:
            continue
        text = text_from_html(job_html)
        title = extract_title(job_html)
        if not looks_like_job_page(candidate_url, title, text):
            continue
        job = build_job(
            source,
            config,
            title=title,
            url=candidate_url,
            text=text,
            location=extract_location(text),
            posted_or_updated=extract_date(text),
        )
        if job:
            jobs.append(job)
    return jobs


def collect_databricks_jobs(source: Source, config: dict) -> list[Job]:
    listing_html = fetch(source.url)
    soup = BeautifulSoup(listing_html, "html.parser")
    candidate_urls: set[str] = set()
    for link in soup.find_all("a", href=True):
        url = normalize_url(source.url, link["href"].strip())
        if re.search(r"/company/careers/.+-\d+$", url):
            candidate_urls.add(url)

    jobs: list[Job] = []
    for candidate_url in sorted(candidate_urls)[:120]:
        try:
            job_html = fetch(candidate_url)
        except Exception:
            continue
        text = text_from_html(job_html)
        title = extract_title(job_html)
        if not looks_like_job_page(candidate_url, title, text):
            continue
        job = build_job(
            source,
            config,
            title=title,
            url=candidate_url,
            text=text,
            location=extract_location(text),
            posted_or_updated=extract_date(text),
        )
        if job:
            jobs.append(job)
    return jobs


def collect_generic_jobs(source: Source, config: dict) -> list[Job]:
    jobs: list[Job] = []
    listing_html = fetch(source.url)
    for candidate_url in extract_candidate_urls(source, listing_html)[:120]:
        try:
            job_html = listing_html if candidate_url == source.url else fetch(candidate_url)
        except Exception:
            continue
        text = text_from_html(job_html)
        title = extract_title(job_html)
        if len(title) < 8:
            continue
        if not looks_like_job_page(candidate_url, title, text):
            continue
        job = build_job(
            source,
            config,
            title=title,
            url=candidate_url,
            text=text,
            location=extract_location(text),
            posted_or_updated=extract_date(text),
        )
        if job:
            jobs.append(job)
    return jobs


def extract_date(text: str) -> str:
    for pattern in DATE_PATTERNS:
        match = pattern.search(text)
        if match:
            return match.group(1)
    return "Not shown on page"


def extract_location(text: str) -> str:
    for pattern in LOCATION_PATTERNS:
        match = pattern.search(text)
        if match:
            return match.group(1)
    return "Not shown on page"


def score_job(title: str, text: str, config: dict) -> tuple[int, str, str, str, str, str]:
    content = f"{title}\n{text}".lower()
    lower_title = title.lower()

    if any(term in content for term in config["exclusion_keywords"]):
        return 0, "skip", "Low Priority", "Low", "Low", "Filtered by exclusion keywords"
    if not looks_like_real_job_title(title):
        return 0, "skip", "Low Priority", "Low", "Low", "Filtered as non-job page"
    required_location_keywords = config.get("required_location_keywords", [])
    if required_location_keywords and not any(term in content for term in required_location_keywords):
        return 0, "skip", "Low Priority", "Low", "Low", "Filtered by required location keywords"
    excluded_location_keywords = config.get("excluded_location_keywords", [])
    if any(term in content for term in excluded_location_keywords):
        return 0, "skip", "Low Priority", "Low", "Low", "Filtered by excluded location keywords"

    score = 0

    role_hits = [term for term in config["role_keywords"] if term in content]
    strong_hits = [term for term in config["strong_match_keywords"] if term in content]
    early_hits = [term for term in config["early_career_keywords"] if term in lower_title]
    location_hits = [term for term in config["preferred_locations"] if term in content]
    title_hits = [term for term in TITLE_ROLE_KEYWORDS if term in lower_title]
    has_early_title_signal = any(term in lower_title for term in EARLY_CAREER_TITLE_KEYWORDS)
    has_seniority_title_signal = any(term in lower_title for term in SENIORITY_TITLE_KEYWORDS)

    score += 6 * len(role_hits)
    score += 8 * len(strong_hits)
    score += 4 * len(location_hits)
    score += 3 * len(early_hits)
    score += 10 * len(title_hits)

    if any(term in content for term in ["phd", "research", "scientist", "systems", "database", "backend", "data infrastructure"]):
        score += 10

    if strong_hits:
        resume_fit = "High: " + ", ".join(strong_hits[:3])
        research_fit = "High: " + ", ".join(strong_hits[:3])
    elif role_hits:
        resume_fit = "Medium: " + ", ".join(role_hits[:3])
        research_fit = "Medium: " + ", ".join(role_hits[:3])
    else:
        resume_fit = "Low"
        research_fit = "Low"

    if has_early_title_signal and not has_seniority_title_signal:
        category = "Early-Career / New Grad"
    elif score >= 45:
        category = "Strong Match"
    elif score >= 28:
        category = "Stretch but Worth Trying"
    else:
        category = "Low Priority"

    if category == "Strong Match":
        priority = "high-priority"
    elif category == "Stretch but Worth Trying":
        priority = "worth-trying"
    elif category == "Early-Career / New Grad":
        priority = "early-career"
    else:
        priority = "low-priority"

    notes = "Signals: " + ", ".join((strong_hits or title_hits or role_hits or early_hits)[:4]) if (strong_hits or title_hits or role_hits or early_hits) else "General relevance only"
    return score, priority, category, resume_fit, research_fit, notes


def collect_jobs(config: dict) -> list[Job]:
    jobs: list[Job] = []
    for source_data in config["sources"]:
        source = Source(**source_data)
        try:
            if source.source_type == "greenhouse_api":
                source_jobs = collect_greenhouse_jobs(source, config)
            elif source.source_type == "ashby_api":
                source_jobs = collect_ashby_jobs(source, config)
            elif source.source_type == "amazon_jobs_json":
                source_jobs = collect_amazon_jobs(source, config)
            elif source.source_type == "google_careers":
                source_jobs = collect_google_jobs(source, config)
            elif source.source_type == "databricks_html":
                source_jobs = collect_databricks_jobs(source, config)
            else:
                source_jobs = collect_generic_jobs(source, config)
        except Exception as exc:
            jobs.append(
                Job(
                    company=source.company,
                    source=source.name,
                    title=f"[Source fetch failed] {source.name}",
                    url=source.url,
                    location="Unavailable",
                    posted_or_updated="Unavailable",
                    score=0,
                    priority="low-priority",
                    category="Low Priority",
                    resume_fit="Low",
                    research_fit="Low",
                    notes=f"Source fetch failed: {exc}",
                )
            )
            continue
        jobs.extend(source_jobs)

    deduped: dict[str, Job] = {}
    for job in jobs:
        existing = deduped.get(job.url)
        if existing is None or job.score > existing.score:
            deduped[job.url] = job
    company_rank = {name: idx for idx, name in enumerate(config.get("company_priority", []))}
    return sorted(
        deduped.values(),
        key=lambda job: (
            {"high-priority": 0, "worth-trying": 1, "early-career": 2, "low-priority": 3}.get(job.priority, 9),
            -job.score,
            company_rank.get(job.company, 999),
            job.title,
        ),
    )


def cleanup_seen_jobs(seen: dict[str, dict]) -> dict[str, dict]:
    cleaned: dict[str, dict] = {}
    for url, job in seen.items():
        title = str(job.get("title", ""))
        normalized_url = normalize_url(url, "")
        if not is_trackable_job_title(title):
            continue
        if not is_trackable_job_url(normalized_url):
            continue
        cleaned[normalized_url] = job | {"url": normalized_url}
    return cleaned


def diversify_jobs(jobs: list[Job], *, per_company_limit: int = 2, total_limit: int = 8) -> list[Job]:
    selected: list[Job] = []
    company_counts: dict[str, int] = {}

    for job in jobs:
        count = company_counts.get(job.company, 0)
        if count >= per_company_limit:
            continue
        selected.append(job)
        company_counts[job.company] = count + 1
        if len(selected) >= total_limit:
            break

    if len(selected) >= total_limit:
        return selected

    selected_urls = {job.url for job in selected}
    for job in jobs:
        if job.url in selected_urls:
            continue
        selected.append(job)
        selected_urls.add(job.url)
        if len(selected) >= total_limit:
            break

    return selected


def update_seen_jobs(jobs: list[Job], seen: dict[str, dict], today: str) -> tuple[list[Job], list[Job]]:
    new_jobs: list[Job] = []
    updated_jobs: list[Job] = []

    for job in jobs:
        if job.title.startswith("[Source fetch failed]"):
            continue
        current = asdict(job)
        previous = seen.get(job.url)
        if previous is None:
            current["first_seen"] = today
            current["last_seen"] = today
            seen[job.url] = current
            new_jobs.append(job)
            continue

        changed = any(
            previous.get(field) != current.get(field)
            for field in ["title", "location", "posted_or_updated", "priority", "category", "notes"]
        )
        merged = previous | current
        merged["last_seen"] = today
        seen[job.url] = merged
        if changed:
            updated_jobs.append(job)

    return new_jobs, updated_jobs


def render_discovered_roles(jobs: list[Job], today: str) -> str:
    discovered_jobs = [job for job in jobs if not job.title.startswith("[Source fetch failed]")]
    discovered_jobs = diversify_jobs(discovered_jobs, per_company_limit=3, total_limit=60)
    lines = [
        "# Discovered Similar Roles",
        "",
        f"Last updated: {today}",
        "",
        "This file records roles from the current watch run that are worth continued tracking.",
        "",
        "| Date Seen | Company | Role Title | URL | Posted / Updated | Location | Resume Fit | Research Fit | Priority | Notes |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for job in discovered_jobs[:60]:
        lines.append(
            f"| {today} | {job.company} | {job.title} | {job.url} | {job.posted_or_updated} | {job.location} | {job.resume_fit} | {job.research_fit} | {job.priority} | {job.notes} |"
        )
    return "\n".join(lines) + "\n"


def render_alerts(jobs: list[Job], new_jobs: list[Job], updated_jobs: list[Job], today: str) -> str:
    lines = [
        "# Alerts",
        "",
        f"Last updated: {today}",
        "",
    ]

    strong = diversify_jobs([job for job in jobs if job.priority == "high-priority"], per_company_limit=2, total_limit=10)
    early = diversify_jobs([job for job in jobs if job.priority == "early-career"], per_company_limit=2, total_limit=10)

    if new_jobs:
        lines.extend([f"## {today} - New Roles", ""])
        for job in diversify_jobs(new_jobs, per_company_limit=2, total_limit=10):
            lines.extend(
                [
                    f"### {job.company} - {job.title}",
                    f"- URL: {job.url}",
                    f"- Posted / Updated: {job.posted_or_updated}",
                    f"- Why it stands out: {job.notes}",
                    f"- Resume fit: {job.resume_fit}",
                    f"- Research fit: {job.research_fit}",
                    "",
                ]
            )

    if updated_jobs:
        lines.extend([f"## {today} - Updated Roles", ""])
        for job in diversify_jobs(updated_jobs, per_company_limit=2, total_limit=10):
            lines.extend(
                [
                    f"### {job.company} - {job.title}",
                    f"- URL: {job.url}",
                    f"- Posted / Updated: {job.posted_or_updated}",
                    f"- Why it stands out: {job.notes}",
                    "",
                ]
            )

    if strong:
        lines.extend([f"## {today} - Strong Match Snapshot", ""])
        for job in strong:
            lines.append(f"- {job.company}: {job.title} | {job.posted_or_updated} | {job.location}")
        lines.append("")

    if early:
        lines.extend([f"## {today} - Early-Career Snapshot", ""])
        for job in early:
            lines.append(f"- {job.company}: {job.title} | {job.posted_or_updated} | {job.location}")
        lines.append("")

    return "\n".join(lines)


def render_digest_change_list(title: str, jobs: list[Job], *, limit: int = 6) -> list[str]:
    section = [title, "-" * len(title)]
    bucket = diversify_jobs(jobs, per_company_limit=2, total_limit=limit)
    if not bucket:
        section.extend(["None", ""])
        return section

    for idx, job in enumerate(bucket, start=1):
        section.append(f"{idx}. {job.company} | {job.title}")
        section.append(f"   Posted / Updated: {job.posted_or_updated}")
        section.append(f"   Location: {job.location}")
        section.append(f"   Fit: {job.resume_fit} | {job.research_fit}")
        section.append(f"   Link: {job.url}")
    section.append("")
    return section


def render_digest_html_change_section(title: str, jobs: list[Job], *, limit: int = 6) -> str:
    bucket = diversify_jobs(jobs, per_company_limit=2, total_limit=limit)
    if not bucket:
        return f"<h2>{html.escape(title)}</h2><p>None</p>"

    items = []
    for job in bucket:
        items.append(
            "<li style='margin-bottom: 12px;'>"
            f"<strong>{html.escape(job.company)}</strong> - {html.escape(job.title)}<br>"
            f"Posted / Updated: {html.escape(job.posted_or_updated)}<br>"
            f"Location: {html.escape(job.location)}<br>"
            f"Fit: {html.escape(job.resume_fit)} | {html.escape(job.research_fit)}<br>"
            f"<a href=\"{html.escape(job.url)}\">Open role</a>"
            "</li>"
        )

    return f"<h2>{html.escape(title)}</h2><ul>{''.join(items)}</ul>"


def render_latest_digest(jobs: list[Job], new_jobs: list[Job], updated_jobs: list[Job], today: str) -> str:
    fetch_failures = [job for job in jobs if job.title.startswith("[Source fetch failed]")]
    tracked_jobs = [job for job in jobs if not job.title.startswith("[Source fetch failed]")]
    strong = diversify_jobs([job for job in tracked_jobs if job.category == "Strong Match"], per_company_limit=2, total_limit=4)
    stretch = diversify_jobs([job for job in tracked_jobs if job.category == "Stretch but Worth Trying"], per_company_limit=2, total_limit=4)
    early = diversify_jobs([job for job in tracked_jobs if job.category == "Early-Career / New Grad"], per_company_limit=2, total_limit=3)
    meaningful_count = len([job for job in tracked_jobs if job.category in {"Strong Match", "Stretch but Worth Trying", "Early-Career / New Grad"}])

    lines = [
        f"Daily Job Watch Digest - {today}",
        "=" * 36,
        f"New: {len(new_jobs)} | Updated: {len(updated_jobs)} | Tracked: {len(tracked_jobs)} | Failures: {len(fetch_failures)}",
        "",
    ]

    if not new_jobs and not updated_jobs:
        lines.extend(
            [
                "Today's Changes",
                "---------------",
                "No new or updated roles were detected today.",
                "",
            ]
        )
    else:
        lines.extend(render_digest_change_list("Today's New Roles", new_jobs))
        lines.extend(render_digest_change_list("Today's Updated Roles", updated_jobs))

    def clip(value: str, width: int) -> str:
        compact = re.sub(r"\s+", " ", value).strip()
        return compact if len(compact) <= width else compact[: width - 1] + "…"

    def render_plain_table(title: str, bucket: list[Job]) -> list[str]:
        section = [title, "-" * len(title)]
        if not bucket:
            section.extend(["None", ""])
            return section
        header = f"{'#':<2}  {'Company':<12}  {'Role':<42}  {'Date':<16}  {'Location':<24}"
        section.append(header)
        section.append("-" * len(header))
        for idx, job in enumerate(bucket, start=1):
            section.append(
                f"{idx:<2}  {clip(job.company,12):<12}  {clip(job.title,42):<42}  {clip(job.posted_or_updated,16):<16}  {clip(job.location,24):<24}"
            )
            section.append(f"    Link: {job.url}")
            section.append(f"    Fit: {job.resume_fit} | {job.research_fit}")
        section.append("")
        return section

    sections = [
        ("Snapshot: Strong Match", strong),
        ("Snapshot: Stretch but Worth Trying", stretch),
        ("Snapshot: Early-Career / New Grad", early),
    ]

    for header, bucket in sections:
        lines.extend(render_plain_table(header, bucket))

    if meaningful_count == 0:
        lines.extend(
            [
                "Run Notes",
                "---------",
                "No concrete job pages were extracted in this run.",
            ]
        )
        if fetch_failures:
            lines.append("")
            lines.append("Source fetch failures:")
            for job in fetch_failures[:10]:
                lines.append(f"- {job.company}: {job.notes}")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def render_latest_digest_html(jobs: list[Job], new_jobs: list[Job], updated_jobs: list[Job], today: str) -> str:
    fetch_failures = [job for job in jobs if job.title.startswith("[Source fetch failed]")]
    tracked_jobs = [job for job in jobs if not job.title.startswith("[Source fetch failed]")]
    strong = diversify_jobs([job for job in tracked_jobs if job.category == "Strong Match"], per_company_limit=2, total_limit=4)
    stretch = diversify_jobs([job for job in tracked_jobs if job.category == "Stretch but Worth Trying"], per_company_limit=2, total_limit=4)
    early = diversify_jobs([job for job in tracked_jobs if job.category == "Early-Career / New Grad"], per_company_limit=2, total_limit=3)
    meaningful_count = len([job for job in tracked_jobs if job.category in {"Strong Match", "Stretch but Worth Trying", "Early-Career / New Grad"}])

    def render_table(title: str, bucket: list[Job]) -> str:
        if not bucket:
            return f"<h2>{html.escape(title)}</h2><p>None</p>"
        rows = []
        for job in bucket:
            rows.append(
                "<tr>"
                f"<td>{html.escape(job.company)}</td>"
                f"<td>{html.escape(job.title)}</td>"
                f"<td>{html.escape(job.posted_or_updated)}</td>"
                f"<td>{html.escape(job.location)}</td>"
                f"<td>{html.escape(job.priority)}</td>"
                f"<td>{html.escape(job.resume_fit)}</td>"
                f"<td>{html.escape(job.research_fit)}</td>"
                f"<td><a href=\"{html.escape(job.url)}\">Open</a></td>"
                "</tr>"
            )
        return (
            f"<h2>{html.escape(title)}</h2>"
            "<table border='1' cellpadding='6' cellspacing='0' style='border-collapse: collapse; width: 100%;'>"
            "<thead><tr>"
            "<th>Company</th><th>Role</th><th>Date</th><th>Location</th><th>Priority</th><th>Resume Fit</th><th>Research Fit</th><th>Link</th>"
            "</tr></thead>"
            f"<tbody>{''.join(rows)}</tbody></table>"
        )

    sections = [
        render_table("Snapshot: Strong Match", strong),
        render_table("Snapshot: Stretch but Worth Trying", stretch),
        render_table("Snapshot: Early-Career / New Grad", early),
    ]

    if not new_jobs and not updated_jobs:
        changes_html = "<h2>Today's Changes</h2><p>No new or updated roles were detected today.</p>"
    else:
        changes_html = (
            render_digest_html_change_section("Today's New Roles", new_jobs)
            + render_digest_html_change_section("Today's Updated Roles", updated_jobs)
        )

    run_notes = ""
    if meaningful_count == 0:
        if fetch_failures:
            failure_items = "".join(
                f"<li><strong>{html.escape(job.company)}</strong>: {html.escape(job.notes)}</li>"
                for job in fetch_failures[:10]
            )
            run_notes = (
                "<h2>Run Notes</h2>"
                "<p>No concrete job pages were extracted in this run.</p>"
                f"<p>Source fetch failures:</p><ul>{failure_items}</ul>"
            )
        else:
            run_notes = "<h2>Run Notes</h2><p>No concrete job pages were extracted in this run.</p>"

    return (
        "<html><body style='font-family: Arial, sans-serif;'>"
        f"<h1>Daily Job Watch Digest - {html.escape(today)}</h1>"
        f"<p><strong>New:</strong> {len(new_jobs)} &nbsp; <strong>Updated:</strong> {len(updated_jobs)} &nbsp; <strong>Tracked:</strong> {len(tracked_jobs)} &nbsp; <strong>Failures:</strong> {len(fetch_failures)}</p>"
        + changes_html
        + "".join(sections)
        + run_notes
        + "</body></html>"
    )


def send_email(subject: str, body: str, html_body: str | None = None) -> None:
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")
    email_from = os.getenv("EMAIL_FROM")
    email_to = os.getenv("EMAIL_TO")

    required = [smtp_host, smtp_port, smtp_username, smtp_password, email_from, email_to]
    if not all(required):
        print("Email status: skipped (missing SMTP/EMAIL secret values).")
        return

    print(f"Email status: attempting send via {smtp_host}:{smtp_port} to {email_to}.")

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = email_from
    message["To"] = email_to
    message.set_content(body)
    if html_body:
        message.add_alternative(html_body, subtype="html")

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_host, int(smtp_port), context=context) as server:
            server.login(smtp_username, smtp_password)
            server.send_message(message)
        print("Email status: sent successfully.")
    except Exception as exc:
        print(f"Email status: failed ({type(exc).__name__}: {exc})")


def main() -> int:
    local_tz = ZoneInfo(os.getenv("WATCH_TIMEZONE", DEFAULT_TIMEZONE))
    today = datetime.now(timezone.utc).astimezone(local_tz).date().isoformat()
    config = load_config()
    seen = cleanup_seen_jobs(load_seen_jobs())
    jobs = collect_jobs(config)
    new_jobs, updated_jobs = update_seen_jobs(jobs, seen, today)
    save_seen_jobs(seen)

    discovered_text = render_discovered_roles(jobs, today)
    alerts_text = render_alerts(jobs, new_jobs, updated_jobs, today)
    digest_text = render_latest_digest(jobs, new_jobs, updated_jobs, today)
    digest_html = render_latest_digest_html(jobs, new_jobs, updated_jobs, today)

    DISCOVERED_ROLES_PATH.write_text(discovered_text, encoding="utf-8")
    ALERTS_PATH.write_text(alerts_text, encoding="utf-8")
    LATEST_DIGEST_PATH.write_text(digest_text, encoding="utf-8")

    send_email(
        subject=f"Daily Job Watch - {today}",
        body=digest_text,
        html_body=digest_html,
    )

    print(f"Collected {len(jobs)} roles, {len(new_jobs)} new, {len(updated_jobs)} updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
