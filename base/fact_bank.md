# Fact Bank

这份文件是给 harness 的“真实信息来源”。之后改简历和写 cover letter 时，优先以这里和 `CV-ByteDance.tex` 为准。

## Identity

- Name: Guanli Liu
- Location: Melbourne, Australia
- Email: liuguanli22@gmail.com
- LinkedIn: https://www.linkedin.com/in/guanli-liu-11353058/
- GitHub: https://github.com/Liuguanli
- Open to: remote / relocation

## Target Role Themes

- Software Engineer
- Data Engineer / Data Infrastructure Engineer
- Data Scientist
- Backend Engineer
- Applied / Research Engineer for data systems, retrieval, or AI data infrastructure

## Core Narrative

- Software engineer and postdoctoral researcher with strong experience in backend systems, data infrastructure, indexing, benchmarking, and query processing.
- Built end-to-end systems involving ingestion, SQL parsing, indexing, retrieval, benchmarking, and performance evaluation.
- Comfortable across both research and engineering contexts.
- Earlier industry experience includes Software Engineer at Baidu, where he worked on the company's internal IM system, and Data Scientist at nftDb, a startup focused on NFT trading data.

## Experience Highlights

### University of Melbourne, PhD + Postdoc

- Worked on database benchmarking, indexing, query processing, and AI-driven data systems.
- Built a layout advisory system for data lake style datasets.
- Built DriftBench for evaluating performance stability under workload and data drift.
- Built benchmarking frameworks for spatial and learned indexes.
- Published or submitted work to venues including VLDB and ICDE.
- Supervised junior researchers and collaborated with academic and industry partners.

### nftDb, Data Scientist

- Worked at a startup focused on NFT trading data, market trend tracking, and multimodal search over digital assets.
- Built Python ingestion pipelines for blockchain transaction data.
- Worked with Kafka-style streaming and Airflow-orchestrated batch workflows.
- Used SQL and dbt for cleaning, normalizing, and modeling data.
- Queried large datasets in BigQuery for analytics and reporting.
- Built an internal RAG-based knowledge assistant.

### Baidu, Software Engineer

- Worked on Baidu's internal company IM system.
- Designed messaging protocols and message deduplication mechanisms.
- Improved database performance via profiling, query optimization, and backend tuning.

## Technical Skills

- Languages: Python, Java, SQL, some C++
- Data systems: SparkSQL, Apache Hudi, REST APIs, ingestion pipelines, batch and incremental processing
- Databases: PostgreSQL, PostGIS, pgvector, BigQuery
- AI / retrieval: RAG, vector databases, embedding-based retrieval
- Infra: Docker, Google Cloud Platform
- ML: PyTorch, Scikit-learn

## Evidence / Assets Worth Reusing

- GitHub projects for layout advisory, DriftBench, RL spatial benchmark, RSMI
- Publications in VLDB / ICDE / ADC / ICDEW related work
- Cross-over background: academic rigor plus production-oriented engineering

## Research Stories For STAR-Style Writing

### Story 1: Data Layout Advisory

- Situation / Problem:
  - Data lake style systems can perform very differently depending on how data is physically laid out.
  - Choosing a good layout is hard because it depends on both the dataset and the workload.
- Action:
  - Built a layout advisory system that supports dataset ingestion, workload ingestion, SQL workload parsing, and layout recommendation.
  - Developed methods for reasoning about layout quality and physical design trade-offs.
- Result:
  - Produced a concrete system, not only a paper idea.
  - Strong fit for roles involving physical optimization, storage structures, or performance-aware data systems.
- Venue cue:
  - Related work includes `VLDB 2025` and `VLDB 2026`.

### Story 2: DriftBench

- Situation / Problem:
  - Benchmark results often look good in static settings but become less reliable when workload or data changes.
- Action:
  - Built DriftBench, a framework for evaluating performance stability under workload and data drift.
  - Focused on benchmarking methodology, robustness, and careful system evaluation.
- Result:
  - Shows strength in systems evaluation, benchmarking, and evidence-driven performance reasoning.
- Venue cue:
  - `VLDB 2026`

### Story 3: Learned Index / Spatial Index Work

- Situation / Problem:
  - Efficient query processing over spatial or learned index structures requires strong trade-off thinking around speed, structure, and adaptability.
- Action:
  - Worked on learned index construction, learned spatial index structures, and recursive learned spatial indexes.
  - Built systems and experimental frameworks rather than only theoretical analysis.
- Result:
  - Strong fit for indexing, query processing, and storage structure discussions.
- Venue cue:
  - `VLDB 2020`, `ICDE 2023`, `ICDEW 2023`

## Research Writing Reminders

- When mentioning a paper, say the key idea first and the venue second.
- Use venue names to support credibility, not as the whole story.
- If speaking to HR, use one short line for the paper venue and spend more time on what problem was solved.

## Hard Boundaries

- Do not invent production scale numbers unless already documented elsewhere.
- Do not claim team leadership beyond what can be supported by the resume.
- Do not claim hands-on ownership of technologies not already evidenced.
- Do not present unpublished work as already accepted unless clearly confirmed.
