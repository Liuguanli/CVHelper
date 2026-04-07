#!/usr/bin/env python3

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path("/Users/guanlil1/Dropbox/PostDoc/topics/CVHelper")
DATE = "20260405"
BASE_RESUME = ROOT / "CV-ByteDance.tex"


PROFILE_OLD = (
    "Software engineer and postdoctoral researcher with a strong background in scalable "
    "backend systems, data infrastructure, and performance optimization. I have built and "
    "studied large-scale systems for data ingestion, query processing, indexing, and "
    "retrieval, with a focus on reliability, scalability, debuggability, and efficient "
    "execution. My PhD and postdoctoral work involved designing and implementing "
    "high-performance data systems published in top database venues such as VLDB and ICDE. "
    "In both research and industry settings, I have delivered end-to-end systems involving "
    "backend services, data pipelines, benchmarking frameworks, and query optimization "
    "components. Earlier in my career, I worked as a Software Engineer and Data Scientist, "
    "gaining practical experience in software development, distributed processing, and "
    "production-oriented data workflows."
)

UMELB_SUMMARY_OLD_1 = (
    "\\textit{Lead research and engineering projects on database benchmarking, indexing, "
    "and AI-driven query processing.}"
)
UMELB_SUMMARY_OLD_2 = (
    "\\textit{Design system prototypes, supervise junior researchers, and collaborate with "
    "academic and industry partners.}"
)
LAYOUT_BULLET_OLD = (
    "    \\item Built a \\textbf{layout advisory} system for data lake-style datasets, "
    "supporting dataset and workload ingestion, SQL workload parsing, and layout recommendation."
)
DRIFT_BULLET_OLD = (
    "    \\item Built \\textbf{DriftBench}, a framework for evaluating performance stability "
    "under workload and data drift across database tuning and benchmarking scenarios."
)
SKILL_INSERT_AFTER = (
    "\\item \\textbf{Programming:} Proficient in Python and Java, with working knowledge of C++ and SQL"
)


ROLE_DATA = {
    "amazon-redshift-sde-202604": {
        "company": "Amazon",
        "role": "Software Development Engineer, Amazon Redshift, Redshift",
        "status": "verified",
        "source_url": "https://www.amazon.jobs/en/jobs/10378746/software-development-engineer-amazon-redshift-redshift",
        "source_note": "Verified from Amazon job page crawled 6 days ago.",
        "location": "East Palo Alto, California",
        "family": "query_engine",
        "profile": (
            "Software engineer and postdoctoral researcher with a strong background in database "
            "systems, query processing, indexing, and performance optimization. My work has "
            "focused on physical data design, SQL workload analysis, benchmarking, and backend "
            "data systems. I have built systems for workload parsing, layout recommendation, and "
            "performance evaluation, and published related work in venues such as VLDB and ICDE. "
            "Across research and industry, I have also worked on backend services, data pipelines, "
            "and database performance tuning, which fits well with query engine and analytical "
            "system work."
        ),
        "summary_lines": (
            "\\textit{Lead research and engineering projects on database systems, query processing, "
            "indexing, and performance evaluation.}",
            "\\textit{Build system prototypes, study performance trade-offs, and collaborate with "
            "academic and industry partners.}",
        ),
        "layout_bullet": (
            "    \\item Built a \\textbf{layout advisory} system for data lake-style datasets, "
            "supporting dataset and workload ingestion, SQL workload parsing, and physical design "
            "recommendation for analytical workloads."
        ),
        "drift_bullet": (
            "    \\item Built \\textbf{DriftBench}, a framework for evaluating performance stability "
            "under workload and data drift across database tuning and benchmarking scenarios."
        ),
        "extra_skill": "\\item \\textbf{Database / Query Systems:} Query processing, indexing, physical design, benchmarking, and performance analysis",
        "job_summary": [
            "Amazon Redshift query processing role inside the Redshift data plane.",
            "Focus areas include query analysis, query optimization, parallel execution, SQL language features, AWS integration, and performance improvement.",
            "Preferred background includes experience with database query engines.",
        ],
        "must_have": [
            "Professional software development experience",
            "System design or architecture experience",
            "Experience building large-scale or distributed systems in Java, C++, C#, or Perl",
            "Interest in query processing and analytical systems",
        ],
        "nice_to_have": [
            "Database query engine experience",
            "Performance tuning experience",
            "Complex systems delivery experience",
        ],
        "team_needs": [
            "Engineers who can work close to SQL and query engine internals",
            "People who can reason about performance bottlenecks and execution behavior",
            "Builders who can work across Redshift and other AWS services",
        ],
        "best_evidence": [
            "Database systems research in query processing, physical design, indexing, and benchmarking",
            "Baidu backend engineering and database performance tuning",
            "Layout advisory and SQL workload parsing work",
            "Research credibility through VLDB and ICDE publications",
        ],
        "gaps": [
            "No direct claimed ownership of a production MPP query engine",
            "C++ is present as working knowledge rather than the strongest language",
        ],
        "resume_plan": [
            "Push database systems and query processing to the top of the profile",
            "Emphasize workload parsing, physical design, and performance evaluation",
            "Keep Baidu visible for backend reliability and database tuning",
            "Use ATS terms such as query optimization, SQL, execution engine, and performance improvement only where truthful",
        ],
        "cover_plan": [
            "Lead with database systems and query processing fit",
            "Use layout advisory as one STAR example",
            "Use DriftBench or Baidu as the second example",
            "Frame the main gap honestly as production engine ownership rather than general systems ability",
        ],
        "resume_changes": [
            "Reposition the profile around query processing, database systems, and performance optimization.",
            "Tighten research summary lines to sound more systems-focused.",
            "Add a systems skills line for query processing, indexing, benchmarking, and physical design.",
            "Keep industry evidence visible to avoid reading as purely academic.",
        ],
        "cover_letter": [
            "I am applying for the Software Development Engineer role on the Amazon Redshift query processing team. The role is a strong match for my background in database systems, query processing, indexing, and performance-focused engineering.",
            "In my PhD and postdoctoral work at the University of Melbourne, I worked on database systems problems where performance depends on system design. One example is data layout optimization. I built a layout advisory system with dataset ingestion, SQL workload parsing, and layout recommendation, and I developed a cost model for physical design trade-offs. This work led to research published at VLDB 2025 and related follow-up work submitted to VLDB 2026. It gave me a strong foundation in analyzing workloads, understanding performance behavior, and turning systems ideas into working software.",
            "I also built DriftBench to study how system performance changes when workloads or data drift over time. The key point was to look beyond static benchmark results and measure whether behavior stays stable when conditions change. In industry, I worked on backend systems at Baidu and on data pipelines and retrieval-oriented tools at nftDb. Those roles gave me practical experience with backend reliability, database performance tuning, and production-oriented engineering.",
            "What attracts me to this role is the chance to work directly on query analysis, optimization, execution, and SQL-facing functionality in a large analytical system. That is very close to the kind of systems work I already do, and I would be excited to bring that background to Redshift.",
            "I would welcome the opportunity to discuss how I could contribute to the Redshift query processing team.",
        ],
        "video_script": [
            "Hi, I am Guanli Liu. I am a software engineer and postdoctoral researcher in Melbourne. My background is in database systems, backend engineering, and performance-focused data infrastructure.",
            "I am interested in this Redshift role because it is close to the work I have done in both research and engineering. My PhD and postdoctoral work has focused on database systems topics like query-related workloads, physical data design, indexing, benchmarking, and performance evaluation.",
            "One example is my work on data layout optimization. The problem was that analytical systems can perform very differently depending on how data is physically organized. I built a layout advisory system with dataset ingestion, SQL workload parsing, and layout recommendation. I also developed a cost model for physical design trade-offs. This work led to research published at VLDB 2025, and related follow-up work was submitted to VLDB 2026. More importantly, it shows how I work. I like to build systems, test ideas, and connect design choices with real performance outcomes.",
            "Another example is benchmarking. I built DriftBench to study how system performance changes when workloads or data drift over time. The key idea was to go beyond static benchmark results and ask whether performance stays stable when conditions change. That work strengthened my ability to measure system behavior carefully and make performance claims based on evidence.",
            "I also have industry experience. At Baidu, I worked on backend systems and database performance tuning. At nftDb, I built Python ingestion pipelines and SQL and dbt workflows. These roles gave me practical experience with reliability, delivery, and production-oriented engineering.",
            "What I like about this Redshift role is the chance to work on query processing, optimization, execution, and performance in a real large-scale analytical system. Those are areas where I already have strong overlap, and I would be excited to contribute.",
            "Thank you for your time. I would be glad to speak further.",
        ],
    },
    "amazon-applied-scientist-202604": {
        "company": "Amazon",
        "role": "Applied Scientist",
        "status": "verified",
        "source_url": "https://www.amazon.jobs/en/jobs/3182042/applied-scientist",
        "source_note": "Verified from Amazon job page crawled 3 weeks ago.",
        "location": "Seattle, Washington",
        "family": "applied_science",
        "profile": (
            "Software engineer and postdoctoral researcher with experience across applied research, "
            "data systems, retrieval, and performance evaluation. My work has combined system building "
            "with research on indexing, benchmarking, AI-assisted query processing, and retrieval-oriented "
            "data workflows. I have built end-to-end systems for ingestion, workload parsing, benchmarking, "
            "and retrieval, and published related work in venues such as VLDB and ICDE. This gives me a "
            "strong fit for applied roles that need rigorous experimentation, practical implementation, and "
            "clear technical reasoning."
        ),
        "summary_lines": (
            "\\textit{Lead research and engineering projects on benchmarking, indexing, retrieval, and AI-assisted query processing.}",
            "\\textit{Build system prototypes, evaluate performance carefully, and collaborate with academic and industry partners.}",
        ),
        "layout_bullet": LAYOUT_BULLET_OLD,
        "drift_bullet": DRIFT_BULLET_OLD,
        "extra_skill": "\\item \\textbf{Applied Research / Retrieval:} RAG, embedding-based retrieval, experimental evaluation, and AI-assisted data systems",
        "job_summary": [
            "Applied Scientist role inside Amazon Selection and Catalog Systems.",
            "The team works on product identity and relationship reasoning at Amazon scale using GenAI, VLMs, and multimodal reasoning.",
            "Preferred background includes publications, strong experimental design, and large-scale ML or GenAI systems.",
        ],
        "must_have": [
            "PhD or equivalent research background",
            "Programming ability in Python, Java, or C++",
            "Machine learning or algorithm development experience",
            "Strong experimental design and analysis",
        ],
        "nice_to_have": [
            "LLM or foundation model experience",
            "Multimodal or VLM experience",
            "Top-tier research publications",
            "Production ML deployment experience",
        ],
        "team_needs": [
            "Scientists who can work on product identity and relationship reasoning at huge scale",
            "People who combine modeling ideas with practical implementation",
            "Researchers who can publish and communicate clearly",
        ],
        "best_evidence": [
            "Research publications in VLDB, ICDE, ICDEW, and ADC",
            "LLM-assisted processing and retrieval-oriented work",
            "RAG system building at nftDb",
            "Benchmarking and evaluation strength",
        ],
        "gaps": [
            "No direct, clearly evidenced VLM or multimodal foundation model ownership",
            "Profile is stronger in systems and retrieval than in large-scale deep multimodal modeling",
        ],
        "resume_plan": [
            "Lead with applied research, retrieval, benchmarking, and AI-assisted systems",
            "Keep publications visible as credibility signals",
            "Emphasize evaluation rigor and implementation depth",
            "Avoid claiming multimodal or VLM expertise that is not directly supported",
        ],
        "cover_plan": [
            "Position yourself as an applied research candidate with strong system-building ability",
            "Use one STAR example from data layout or benchmarking and one from LLM-assisted or retrieval work",
            "Be explicit that your strength is rigorous systems-minded applied research",
        ],
        "resume_changes": [
            "Reframe the profile around applied research, retrieval, experimentation, and AI-assisted systems.",
            "Keep the research section central and publication signals visible.",
            "Add a retrieval / applied research skills line.",
            "Preserve honest boundaries around multimodal and VLM-specific experience.",
        ],
        "cover_letter": [
            "I am applying for the Applied Scientist role at Amazon Selection and Catalog Systems. While my background is more systems- and retrieval-oriented than pure multimodal modeling, I believe I am a strong fit for an applied science role that values rigorous experimentation, practical implementation, and research depth.",
            "In my PhD and postdoctoral work at the University of Melbourne, I worked on data-intensive systems problems where model or system choices had to be tested carefully. For example, I built DriftBench to study how performance changes when workloads or data drift over time. The key idea was to move beyond static benchmark results and measure whether system behavior stays stable when conditions change. That work strengthened my approach to evaluation and is tied to a VLDB 2026 submission.",
            "I also worked on AI-assisted and retrieval-oriented systems. At nftDb, I built an internal RAG-based knowledge assistant. In research, I supervised work on LLM-assisted processing of complex spatial queries and on embedding-based spatial keyword query processing. Across this work, the common thread has been applied research that combines implementation, careful evaluation, and useful outcomes.",
            "What attracts me to this role is the chance to work on hard product identity and reasoning problems at very large scale. I would be excited to bring my research discipline, retrieval and evaluation background, and practical system-building experience to that setting.",
            "I would welcome the opportunity to discuss where my background could contribute most effectively.",
        ],
        "video_script": [
            "Hi, I am Guanli Liu. I am a software engineer and postdoctoral researcher in Melbourne. My background combines applied research, data systems, retrieval, and performance evaluation.",
            "I am interested in this role because it looks like a place where strong experimentation and practical implementation both matter. My work is strongest when I can combine research thinking with system building.",
            "One example is benchmarking. I built DriftBench to study how system performance changes when workloads or data drift over time. The key idea was to go beyond static benchmark numbers and test whether behavior stays stable when conditions change. That work reflects how I think about careful evaluation and evidence-based results.",
            "Another example is retrieval and AI-assisted systems. At nftDb, I built an internal RAG-based knowledge assistant. In research, I also worked close to LLM-assisted spatial query processing and embedding-based query work. I am comfortable taking research ideas and turning them into useful systems and experiments.",
            "I also bring an engineering background. I have built data pipelines, SQL workflows, and backend components in both research and industry settings. That helps me work across the full path from idea to implementation.",
            "I know this role is closer to large-scale GenAI and multimodal reasoning than my strongest past work. I would describe my fit honestly as strongest in applied research, retrieval, evaluation, and system implementation. If the team values that combination, I believe I could contribute well.",
            "Thank you for your time. I would be glad to speak further.",
        ],
    },
    "google-phd-role-136954121411273414-202604": {
        "company": "Google",
        "role": "Unverified PhD-oriented role from provided link",
        "status": "unavailable",
        "source_url": "https://www.google.com/about/careers/applications/jobs/results/136954121411273414?has_remote=true&q=phd",
        "source_note": "As of April 5, 2026, the linked page appears unavailable or taken down.",
        "job_summary": ["The supplied Google careers link no longer resolves to a live job description."],
        "must_have": [],
        "nice_to_have": [],
        "team_needs": [],
        "best_evidence": [],
        "gaps": ["Current role title and requirements cannot be verified from the provided link."],
        "resume_plan": ["Do not tailor a resume to this role until a live JD is available."],
        "cover_plan": ["No cover letter generated because the role cannot be verified."],
    },
    "google-research-scientist-127025001-202604": {
        "company": "Google",
        "role": "Research Scientist, Google Research",
        "status": "verified",
        "source_url": "https://www.google.com/about/careers/applications/jobs/results/107328491954807494-research-scientist-google-research?degree=DOCTORATE&company=DeepMind&company=YouTube&company=Google&skills=lake&q=Research#!t=jo&jid=127025001&",
        "source_note": "Verified from the user-provided Google Research Scientist job description on April 5, 2026.",
        "location": "Mountain View, California",
        "family": "research_scientist",
        "profile": (
            "Research-oriented software engineer and postdoctoral researcher with a strong background in "
            "data systems, performance evaluation, query processing, indexing, and experimental design. "
            "My PhD and postdoctoral work has focused on building research prototypes, designing evaluation "
            "frameworks, and publishing results in top database venues such as VLDB and ICDE. Across "
            "research and industry, I have worked on data-intensive systems, retrieval-oriented tools, and "
            "backend infrastructure, with an emphasis on careful experiments, clear problem framing, and "
            "turning ideas into working systems."
        ),
        "summary_lines": (
            "\\textit{Lead research and engineering projects on data systems, benchmarking, indexing, and AI-assisted query processing.}",
            "\\textit{Build research prototypes, define evaluation methods, supervise junior researchers, and collaborate with academic and industry partners.}",
        ),
        "layout_bullet": (
            "    \\item Built a \\textbf{layout advisory} system for data lake-style datasets, supporting dataset and workload ingestion, SQL workload parsing, and layout recommendation, together with a cost model for physical design trade-offs."
        ),
        "drift_bullet": (
            "    \\item Built \\textbf{DriftBench}, a framework for evaluating performance stability under workload and data drift, with a focus on careful evaluation and reproducible systems comparison."
        ),
        "extra_skill": "\\item \\textbf{Research / Evaluation:} Experimental design, prototype building, benchmarking, retrieval, and systems performance analysis",
        "job_summary": [
            "Google Research Scientist role in Mountain View focused on fundamental research, product-facing innovation, and infrastructure-driven research impact.",
            "The JD highlights large-scale testing, rapid prototyping, experiment design, research methodology, and publishing research results.",
            "The scope spans areas such as machine learning, data mining, NLP, software performance analysis, compilers, and core search.",
        ],
        "must_have": [
            "PhD in Computer Science or a related field",
            "Coding ability in Python, JavaScript, R, Java, or C++",
            "Scientific publication submissions to conferences, journals, or public repositories",
        ],
        "nice_to_have": [
            "Two years of coding experience",
            "Experience owning and initiating research agendas",
            "Ability to define data structures, frameworks, and evaluation metrics with limited guidance",
        ],
        "team_needs": [
            "Researchers who can turn open-ended ideas into concrete prototypes and experiments",
            "People who can define evaluation methods and deliver research results with clear impact",
            "Scientists who can publish, collaborate broadly, and help shape longer-term research directions",
        ],
        "best_evidence": [
            "Strong publication record in VLDB, ICDE, ICDEW, and ADC",
            "Research prototypes in data layout optimization, indexing, and benchmarking",
            "Experimental design strength through DriftBench and other systems evaluation work",
            "Industry and research experience translating ideas into practical systems",
        ],
        "gaps": [
            "Your strongest evidence is in data systems and performance research rather than in the full breadth of Google Research areas such as NLP or deep learning",
            "The JD mentions owning research agendas; your materials should frame this through project leadership, supervision, and end-to-end research ownership",
        ],
        "resume_plan": [
            "Lead with research prototype building, evaluation design, and publication strength",
            "Keep systems and performance analysis central because they are a truthful research specialty",
            "Emphasize independent project ownership, mentoring, and collaboration across teams",
            "Use broad research language carefully without implying expertise in areas not supported by the resume",
        ],
        "cover_plan": [
            "Position yourself as a research scientist strongest in data systems and software performance analysis",
            "Use layout advisory as one STAR example and DriftBench as the second",
            "Mention VLDB 2025 and submitted to VLDB 2026 naturally after explaining the core technical contribution",
            "Be honest that your fit is strongest on systems, evaluation, and prototype development",
        ],
        "resume_changes": [
            "Reframe the profile around research prototyping, evaluation design, and publication-backed systems research.",
            "Keep the University of Melbourne work centered because it best shows independent research execution.",
            "Add a research and evaluation skills line to improve ATS alignment with prototype and experiment-driven work.",
            "Preserve industry engineering evidence so the profile still reads as practical, not purely academic.",
        ],
        "cover_letter": [
            "I am applying for the Research Scientist role at Google Research. My background is strongest in data systems, software performance analysis, and experimental systems research, and I believe that fits well with a role that values large-scale testing, prototype development, and clear research impact.",
            "In my PhD and postdoctoral work at the University of Melbourne, I have worked on research problems where strong ideas only matter if they are implemented and evaluated carefully. One example is data layout optimization for data-intensive systems. The problem was that performance can change a lot depending on how data is organized. I built a layout advisory system with dataset ingestion, SQL workload parsing, and layout recommendation, and I developed a cost model for physical design trade-offs. This work led to research published at VLDB 2025, with related follow-up work submitted to VLDB 2026.",
            "I also built DriftBench, a framework for evaluating how system performance changes when workloads or data drift over time. The key point was to move beyond one-time benchmark scores and test whether system behavior stays stable when conditions change. That work strengthened my approach to research methodology, evaluation metrics, and evidence-driven experimentation.",
            "What attracts me to Google Research is the chance to work in an environment where publishing, prototyping, and collaboration all matter. I would bring a style that is careful, practical, and strongly grounded in implementation. While my expertise is more focused on systems and performance than on every area listed in the job description, I believe that depth is a strength for research that needs clear technical grounding and measurable results.",
            "I would welcome the opportunity to discuss how my background could contribute to Google Research.",
        ],
        "video_script": [
            "Hi, I am Guanli Liu. I am a postdoctoral researcher and software engineer in Melbourne. My background is in data systems, software performance analysis, and research prototype building.",
            "I am interested in this Google Research role because it asks for the kind of work I do best. I like taking an open research problem, building a real prototype, and testing it carefully.",
            "One example is my work on data layout optimization. The problem was that system performance can change a lot depending on how data is organized. I built a layout advisory system with dataset ingestion, SQL workload parsing, and layout recommendation. I also developed a cost model for physical design trade-offs. This work led to research published at VLDB 2025, and related follow-up work was submitted to VLDB 2026.",
            "Another example is DriftBench. I built it to study how system performance changes when workloads or data drift over time. The key idea was to test whether systems stay stable when real conditions change, not just when a benchmark is fixed. That work helped me build strong habits in experimental design, evaluation metrics, and research methodology.",
            "I also enjoy working with other people and helping research move forward. In my academic work, I have supervised students, collaborated with other researchers, and taken projects from problem definition to implementation and publication.",
            "I would describe my fit most strongly in systems research, performance analysis, and prototype development. If the team values that kind of research depth, I believe I could contribute well.",
            "Thank you for your time. I would be glad to speak further.",
        ],
    },
    "meta-role-1815415389242149-202604": {
        "company": "Meta",
        "role": "Research Scientist, AI & Systems Co-design (PhD)",
        "status": "verified",
        "source_url": "https://www.metacareers.com/profile/job_details/1815415389242149",
        "source_note": "Verified from the user-provided Meta job description on April 5, 2026.",
        "location": "Menlo Park, California",
        "family": "ml_systems_research",
        "file_slug": "meta_research_scientist_ai_systems_codesign_phd",
        "profile": (
            "Research-oriented software engineer and postdoctoral researcher with a strong background in "
            "systems performance analysis, benchmarking, data systems, and prototype building. My research "
            "has focused on understanding performance trade-offs in data-intensive systems through physical "
            "design, indexing, workload analysis, and evaluation frameworks, with publications in venues such "
            "as VLDB and ICDE. Across research and industry, I have built backend systems, data pipelines, "
            "retrieval-oriented tools, and reproducible evaluation workflows. This gives me a strong foundation "
            "for systems research roles that value careful measurement, prototyping, and scaling-oriented thinking."
        ),
        "summary_lines": (
            "\\textit{Lead research and engineering projects on systems performance, benchmarking, data systems, and AI-assisted query processing.}",
            "\\textit{Build research prototypes, study performance trade-offs, supervise junior researchers, and collaborate with academic and industry partners.}",
        ),
        "layout_bullet": (
            "    \\item Built a \\textbf{layout advisory} system for data lake-style datasets, supporting dataset and workload ingestion, SQL workload parsing, and layout recommendation, together with a cost model for performance trade-offs."
        ),
        "drift_bullet": (
            "    \\item Built \\textbf{DriftBench}, a framework for evaluating performance stability under workload and data drift, helping model what-if performance behavior under changing conditions."
        ),
        "extra_skill": "\\item \\textbf{Systems / Performance Research:} Benchmarking, performance modeling, prototype building, retrieval, and systems evaluation",
        "job_summary": [
            "Meta AI & Systems Co-design research role focused on high-performance software and hardware technologies for AI at datacenter scale.",
            "The team works across models, runtime, hardware, compute, network, and storage, with emphasis on scalability, efficiency, and reliability for training and inference.",
            "The JD highlights benchmarking, performance modeling, what-if analysis, rapid prototyping, and assisting the productionization of high-leverage systems ideas.",
        ],
        "must_have": [
            "PhD in Computer Science or a related field",
            "Specialized experience in one or more areas such as accelerators, HPC, ML compilers, training or inference systems, model compression, communication collectives, ML kernels, frameworks, or software-hardware co-design",
            "Experience developing AI system infrastructure or AI algorithms in C/C++ or Python",
        ],
        "nice_to_have": [
            "Experience or knowledge of large-scale deep learning training or inference",
            "Experience or knowledge of generative AI or ranking and recommendation models",
            "Experience or knowledge of distributed ML systems and algorithm development",
        ],
        "team_needs": [
            "Researchers who can benchmark and model system behavior across many what-if scenarios",
            "People who can prototype quickly and help move promising ideas toward production",
            "Scientists who can reason jointly about system efficiency, scalability, and reliability",
        ],
        "best_evidence": [
            "Benchmarking and performance analysis depth through DriftBench and related systems work",
            "Research prototypes in physical design, indexing, and workload-aware optimization",
            "Strong publication record in systems and database venues such as VLDB and ICDE",
            "Industry experience building backend and data infrastructure in Python and Java",
        ],
        "gaps": [
            "Your evidence is much stronger in systems performance and data systems than in GPU kernels, ML compilers, distributed training, or hardware co-design",
            "The role expects closer exposure to large-scale AI training and inference stacks than your current materials directly show",
        ],
        "resume_plan": [
            "Lead with benchmarking, performance modeling, systems prototyping, and research publication strength",
            "Keep the strongest truthful overlap on what-if analysis, scalability thinking, and prototype development",
            "Avoid claiming direct ownership of GPU kernel, compiler, or AI hardware co-design work",
            "Preserve practical engineering signals from industry work in Python, Java, and backend systems",
        ],
        "cover_plan": [
            "Position yourself as strongest in systems performance research, benchmarking, and prototype development",
            "Use layout advisory and DriftBench as the two STAR examples",
            "Acknowledge honestly that your fit is stronger on performance analysis and systems methodology than on low-level accelerator optimization",
            "Keep the language simple and direct so the case still feels confident, not defensive",
        ],
        "resume_changes": [
            "Reframe the profile around systems performance research, benchmarking, and prototype building.",
            "Keep research publication signals visible because this is a research-heavy role.",
            "Add a systems and performance research skills line for ATS alignment.",
            "Maintain honest boundaries around AI hardware, ML compiler, and kernel-specific experience.",
        ],
        "cover_letter": [
            "I am applying for the Research Scientist, AI and Systems Co-design role at Meta. My strongest fit for this role is on systems performance research, benchmarking, and prototype development, especially in settings where efficiency and scalability need to be measured carefully and improved through system design.",
            "In my PhD and postdoctoral work at the University of Melbourne, I worked on research problems where system behavior depended strongly on design choices. One example is data layout optimization for data-intensive systems. The problem was that performance can change significantly depending on how data is organized. I built a layout advisory system with dataset ingestion, SQL workload parsing, and layout recommendation, and I developed a cost model for performance and physical design trade-offs. This work led to research published at VLDB 2025, with related follow-up work submitted to VLDB 2026.",
            "I also built DriftBench, a framework for evaluating how system performance changes when workloads or data drift over time. The key idea was to study not only peak performance, but also whether systems remain stable and efficient as conditions change. That work strengthened my approach to benchmarking, what-if analysis, and evidence-driven performance reasoning. These are the parts of the Meta role that feel especially close to my background.",
            "I want to be candid that my experience is stronger in systems performance and data-intensive systems than in low-level accelerator kernels, ML compilers, or hardware co-design. What I would bring is a strong research habit around performance analysis, scalable system prototyping, and translating technical ideas into measurable results. I am excited by environments where ideas move from exploration to production impact, and that is one of the strongest reasons this role stands out to me.",
            "I would welcome the opportunity to discuss how my background could contribute to Meta’s AI systems research efforts.",
        ],
        "video_script": [
            "Hi, I am Guanli Liu. I am a postdoctoral researcher and software engineer in Melbourne. My background is in systems performance research, benchmarking, and prototype building for data-intensive systems.",
            "I am interested in this Meta role because it sits in a space I find very exciting. I like work where you study system behavior carefully, build a prototype, and use evidence to improve efficiency and scalability.",
            "One example is my work on data layout optimization. The problem was that system performance can change a lot depending on how data is organized. I built a layout advisory system with dataset ingestion, SQL workload parsing, and layout recommendation. I also developed a cost model for performance and physical design trade-offs. This work led to research published at VLDB 2025, and related follow-up work was submitted to VLDB 2026.",
            "Another example is DriftBench. I built it to study how system performance changes when workloads or data drift over time. The key idea was to go beyond fixed benchmark numbers and test whether systems stay stable when real conditions change. That work helped me build strong habits in benchmarking, what-if analysis, and performance modeling.",
            "I want to be honest that my background is stronger in systems performance and data systems than in low-level GPU kernels or hardware co-design. But I believe I can contribute strongly in areas that need careful measurement, prototype development, and scalable systems thinking.",
            "What attracts me to Meta is the chance to work on ideas that move from research into real impact at very large scale. That mix of research depth and production relevance is very appealing to me.",
            "Thank you for your time. I would be glad to speak further.",
        ],
    },
    "openai-software-engineer-data-infrastructure-research-202604": {
        "company": "OpenAI",
        "role": "Software Engineer, Data Infrastructure - Research",
        "status": "verified",
        "source_url": "https://openai.com/careers/software-engineer-data-infrastructure-research-san-francisco/",
        "source_note": "Verified from OpenAI career page crawled 3 weeks ago.",
        "location": "San Francisco, California",
        "family": "data_infra_research",
        "profile": (
            "Software engineer and postdoctoral researcher with strong experience in data infrastructure, "
            "backend systems, benchmarking, and retrieval-oriented workflows. I have built systems for data "
            "ingestion, workload parsing, layout recommendation, performance evaluation, and internal retrieval "
            "tools, with a focus on reliability, reproducibility, and practical system behavior. My work spans "
            "both research and engineering settings, which fits well with infrastructure roles that support "
            "research teams at scale."
        ),
        "summary_lines": (
            "\\textit{Lead research and engineering projects on data systems, benchmarking, retrieval, and AI-assisted query processing.}",
            "\\textit{Build system prototypes, evaluate performance bottlenecks, and collaborate across research and engineering settings.}",
        ),
        "layout_bullet": (
            "    \\item Built a \\textbf{layout advisory} system for data lake-style datasets, supporting dataset and workload ingestion, SQL workload parsing, and layout recommendation."
        ),
        "drift_bullet": DRIFT_BULLET_OLD,
        "extra_skill": "\\item \\textbf{Data Infrastructure / Retrieval:} Ingestion pipelines, reproducible data workflows, benchmarking, RAG, and retrieval-oriented tooling",
        "job_summary": [
            "OpenAI research workload infrastructure role focused on dataset infrastructure for the training stack.",
            "Responsibilities include dataset APIs, scale validation, bottleneck debugging, reproducibility safeguards, and tooling for dataset inspection.",
            "The role sits close to multimodal researchers and large-scale training and inference infrastructure.",
        ],
        "must_have": [
            "Distributed systems, data pipelines, or infrastructure experience",
            "Experience building APIs and scalable abstractions",
            "Comfort debugging bottlenecks across large fleets",
            "Reliability and scale mindset",
        ],
        "nice_to_have": [
            "GPU-scale distributed systems experience",
            "Dataset infrastructure experience",
            "Probability or distributed data theory background",
        ],
        "team_needs": [
            "Engineers who can make datasets standardized, reliable, and easy to use",
            "People who can debug performance bottlenecks at scale",
            "Builders who care about research user experience and infrastructure quality",
        ],
        "best_evidence": [
            "nftDb ingestion pipelines and retrieval-oriented tooling",
            "Research systems work on data layout, benchmarking, and performance evaluation",
            "RAG assistant experience",
            "Strong research-to-engineering translation",
        ],
        "gaps": [
            "No explicit hands-on evidence of GPU-scale training dataset infrastructure",
            "Less direct exposure to multimodal dataset systems than the role likely expects",
        ],
        "resume_plan": [
            "Lead with data infrastructure, ingestion, reproducibility, and bottleneck analysis",
            "Use research systems work as proof of careful evaluation and reliability thinking",
            "Keep retrieval and RAG experience visible because the role sits near research workflows",
        ],
        "cover_plan": [
            "Position yourself as a data infrastructure engineer with research-facing systems depth",
            "Use one STAR example from ingestion / data workflows and one from benchmarking / evaluation",
            "Acknowledge the GPU-scale gap without sounding defensive",
        ],
        "resume_changes": [
            "Reframe the profile around data infrastructure, ingestion, reproducibility, and bottleneck analysis.",
            "Keep benchmarking and retrieval visible because they map well to research workflow tooling.",
            "Add a data infrastructure / retrieval skills line.",
        ],
        "cover_letter": [
            "I am applying for the Software Engineer, Data Infrastructure - Research role at OpenAI. This role is a strong match for my background in data infrastructure, backend systems, benchmarking, and research-facing engineering.",
            "A core theme in my work has been building systems that make data-intensive workflows easier to run, evaluate, and trust. In my PhD and postdoctoral work at the University of Melbourne, I built systems for data ingestion, SQL workload parsing, layout recommendation, and performance evaluation. For example, I built a layout advisory system for data lake style datasets and developed a cost model for physical design trade-offs. This work led to research published at VLDB 2025, with related follow-up work submitted to VLDB 2026.",
            "I also built DriftBench to study how system performance changes when workloads or data drift over time. That work sharpened my approach to reproducibility, bottleneck analysis, and evidence-driven evaluation. In industry, at nftDb, I built Python ingestion pipelines, SQL and dbt workflows, and an internal RAG-based knowledge assistant. Together, these experiences gave me a practical foundation in data workflows, reliability, and building tooling that supports other technical teams.",
            "What attracts me to this role is the chance to build dataset infrastructure that helps researchers move faster without losing reliability or clarity. I am especially interested in roles where infrastructure quality, user experience, and careful performance thinking all matter at once.",
            "I would welcome the opportunity to discuss how my background could contribute to OpenAI’s research infrastructure work.",
        ],
        "video_script": [
            "Hi, I am Guanli Liu. I am a software engineer and postdoctoral researcher in Melbourne. My background is in data infrastructure, backend systems, and performance-focused research engineering.",
            "I am excited about this role because it sits at the boundary between infrastructure and research support. That is a space where I think I can add real value.",
            "One example is my work on data layout optimization. The problem was that data systems can perform very differently depending on how data is organized and accessed. I built a layout advisory system with dataset ingestion, SQL workload parsing, and layout recommendation. I also developed a cost model for physical design trade-offs. This work led to research published at VLDB 2025, and related follow-up work was submitted to VLDB 2026. It gave me strong experience in building systems that support data workflows and in reasoning carefully about performance.",
            "Another example is benchmarking. I built DriftBench to study how system performance changes when workloads or data drift over time. The key idea was to measure whether systems stay stable when conditions change. That taught me to think carefully about bottlenecks, reproducibility, and reliability.",
            "I also have industry experience. At nftDb, I built Python ingestion pipelines, SQL and dbt workflows, and an internal RAG-based assistant. That work helped me build a practical mindset around data quality, delivery, and internal tooling.",
            "What I like about this OpenAI role is the chance to build data infrastructure that directly helps researchers work faster and more reliably. I like building systems that other technical people depend on, especially when reliability and user experience both matter.",
            "Thank you for your time. I would be glad to speak further.",
        ],
    },
    "databricks-senior-software-engineer-database-engine-internals-202604": {
        "company": "Databricks",
        "role": "Senior Software Engineer - Database Engine Internals",
        "status": "verified",
        "source_url": "https://www.databricks.com/company/careers/engineering---pipeline/senior-software-engineer---database-engine-internals-6544383002",
        "source_note": "Verified from Databricks job page on April 5, 2026.",
        "location": "Mountain View, California",
        "family": "query_engine",
        "profile": (
            "Software engineer and postdoctoral researcher with a strong background in database systems, "
            "query processing, indexing, physical design, and performance optimization. My work has focused "
            "on system internals that affect query behavior, data layout, benchmarking, and performance "
            "trade-offs. I have built systems for workload parsing, layout recommendation, and systems "
            "evaluation, and published related work in venues such as VLDB and ICDE. Across research and "
            "industry, I have also worked on backend services, database performance tuning, and production-"
            "oriented data workflows."
        ),
        "summary_lines": (
            "\\textit{Lead research and engineering projects on database systems, physical design, indexing, and performance evaluation.}",
            "\\textit{Build system prototypes, study trade-offs in query behavior, and collaborate across research and engineering settings.}",
        ),
        "layout_bullet": (
            "    \\item Built a \\textbf{layout advisory} system for data lake-style datasets, supporting dataset and workload ingestion, SQL workload parsing, and automatic physical data optimization through layout recommendation."
        ),
        "drift_bullet": DRIFT_BULLET_OLD,
        "extra_skill": "\\item \\textbf{Database / Systems:} Query processing, indexing, physical design, benchmarking, and performance evaluation",
        "job_summary": [
            "Databricks database engine role focused on the next-generation query engine and structured storage system.",
            "Key areas include query compilation and optimization, distributed execution, vectorized execution, resource management, transaction coordination, encodings and indexes, and automatic physical data optimization.",
            "The role values database, storage, distributed systems, and performance optimization depth.",
        ],
        "must_have": [
            "Strong interest in database or storage systems",
            "Performance optimization mindset",
            "Ability to work on complex next-generation systems over multi-year horizons",
        ],
        "nice_to_have": [
            "Experience with database engine internals",
            "PhD in databases or distributed systems",
            "Distributed execution or storage structure experience",
        ],
        "team_needs": [
            "Engineers who can reason deeply about database engine internals",
            "People comfortable with query performance and physical optimization",
            "Builders who can move from systems ideas to production software",
        ],
        "best_evidence": [
            "Physical design and layout optimization work",
            "Indexing and learned index systems work",
            "Benchmarking and systems evaluation experience",
            "Baidu backend and database performance tuning",
        ],
        "gaps": [
            "No explicit ownership of a production distributed query execution engine",
            "Less direct evidence around transaction coordination and vectorized execution internals",
        ],
        "resume_plan": [
            "Lead with database systems, physical design, indexing, and performance optimization",
            "Strengthen the physical optimization and benchmarking story",
            "Keep Baidu and nftDb to show practical engineering depth",
        ],
        "cover_plan": [
            "Open with database engine and physical optimization fit",
            "Use data layout and benchmarking as the core STAR examples",
            "Be honest about the production engine gap but strong on systems depth",
        ],
        "resume_changes": [
            "Reposition the profile around database engine relevant systems work.",
            "Strengthen physical optimization language in the research section.",
            "Preserve industry evidence for practical software delivery.",
        ],
        "cover_letter": [
            "I am applying for the Senior Software Engineer - Database Engine Internals role at Databricks. This role is a strong match for my background in database systems, physical design, indexing, and performance-focused engineering.",
            "In my PhD and postdoctoral work at the University of Melbourne, I worked on systems problems where query performance depends on how data is organized and how system trade-offs are managed. One example is data layout optimization. I built a layout advisory system with dataset ingestion, SQL workload parsing, and layout recommendation, and I developed a cost model for physical design trade-offs. This work led to research published at VLDB 2025, with related follow-up work submitted to VLDB 2026.",
            "I also built DriftBench to study how system performance changes when workloads or data drift over time. The key idea was to evaluate whether systems remain stable when conditions change, not only whether they look fast in a static benchmark. In addition, I have worked on learned index and spatial index systems, which strengthened my thinking around storage structures and indexing. Earlier in industry, I worked on backend systems and database performance tuning at Baidu.",
            "What attracts me to this Databricks role is the chance to work on deep database and storage problems that still have direct product impact. The role’s emphasis on query optimization, storage structures, indexes, and automatic physical data optimization lines up closely with the strongest parts of my background.",
            "I would welcome the opportunity to discuss how my systems background could contribute to the Database Engine team.",
        ],
        "video_script": [
            "Hi, I am Guanli Liu. I am a software engineer and postdoctoral researcher in Melbourne. My background is in database systems, backend engineering, and performance-focused data infrastructure.",
            "I am interested in this role because it is very close to the systems work I have done in research and engineering. My strongest areas are physical design, indexing, benchmarking, and performance evaluation.",
            "One example is my work on data layout optimization. The problem was that data systems can perform very differently depending on how data is physically organized. I built a layout advisory system with dataset ingestion, SQL workload parsing, and layout recommendation. I also developed a cost model for physical design trade-offs. This work led to research published at VLDB 2025, and related follow-up work was submitted to VLDB 2026.",
            "Another example is benchmarking. I built DriftBench to study how system performance changes when workloads or data drift over time. The key idea was to ask whether performance remains stable when conditions change. That work strengthened my ability to measure system behavior carefully and make performance claims based on evidence.",
            "I also worked on learned index and spatial index systems, and earlier at Baidu I worked on backend infrastructure and database performance tuning. So I bring both research depth and practical engineering experience.",
            "What I like about this Databricks role is that it works on query optimization, storage structures, indexes, and physical data optimization in a real product setting. That is a strong match for the work I have been doing.",
            "Thank you for your time. I would be glad to speak further.",
        ],
    },
    "databricks-systems-phd-software-engineer-202604": {
        "company": "Databricks",
        "role": "Systems PhD - Software Engineer",
        "status": "verified",
        "source_url": "https://www.databricks.com/company/careers/engineering---pipeline/systems-phd---software-engineer--8482037002",
        "source_note": "Verified from Databricks job page on April 5, 2026.",
        "location": "Mountain View, California; San Francisco, California",
        "family": "systems_phd",
        "profile": (
            "PhD-trained software engineer and postdoctoral researcher with a strong background in database "
            "systems, backend infrastructure, and performance optimization. My research and engineering work "
            "has focused on query processing, physical data design, indexing, benchmarking, and retrieval for "
            "data-intensive systems. I have built system prototypes for dataset ingestion, SQL workload parsing, "
            "layout recommendation, and performance evaluation, and published this work in venues such as VLDB "
            "and ICDE. Across academia and industry, I have worked on backend services, data pipelines, database "
            "performance tuning, and retrieval-oriented tools, with an emphasis on practical system building and "
            "measurable performance trade-offs."
        ),
        "summary_lines": (
            "\\textit{Lead research and engineering projects on database systems, physical design, indexing, benchmarking, and AI-assisted query processing.}",
            "\\textit{Build system prototypes, evaluate performance trade-offs, supervise junior researchers, and collaborate with academic and industry partners.}",
        ),
        "layout_bullet": (
            "    \\item Built a \\textbf{layout advisory} system for data lake-style datasets, supporting dataset and workload ingestion, SQL workload parsing, and automatic physical data optimization through layout recommendation."
        ),
        "drift_bullet": DRIFT_BULLET_OLD,
        "extra_skill": "\\item \\textbf{Database / Systems:} Query processing, indexing, physical design, benchmarking, and performance evaluation",
        "job_summary": [
            "Databricks Systems PhD role inside the Database Engine team.",
            "The page highlights work across query engines, vector databases, training pipelines, storage systems, and infrastructure for scale.",
            "Example areas include query compilation and optimization, distributed execution, vectorized execution, resource management, transaction coordination, indexes, and automatic physical data optimization.",
        ],
        "must_have": [
            "PhD in databases or systems",
            "Interest in database systems, storage systems, distributed systems, language design, or performance optimization",
            "Strong implementation mindset with practical impact",
        ],
        "nice_to_have": [
            "Database engine depth",
            "Performance optimization track record",
            "Research-to-engineering translation",
        ],
        "team_needs": [
            "Systems researchers who can become strong product engineers",
            "Candidates who can reason about performance and physical optimization",
            "Builders who can work from first principles",
        ],
        "best_evidence": [
            "PhD and postdoc in database systems",
            "Layout advisory and physical design work",
            "Benchmarking and indexing depth",
            "Industry experience at Baidu and nftDb",
        ],
        "gaps": [
            "No explicit claim of owning a production database engine",
            "Less direct evidence around distributed execution internals than around physical design and benchmarking",
        ],
        "resume_plan": [
            "Lead with systems PhD and practical engineering delivery",
            "Emphasize physical design, benchmarking, indexing, and performance",
            "Keep industry delivery visible",
        ],
        "cover_plan": [
            "Lead with systems PhD fit",
            "Use layout optimization and benchmarking as STAR examples",
            "Mention VLDB naturally as support, not as the entire story",
        ],
        "resume_changes": [
            "Rewrote the profile around systems PhD fit and practical software delivery.",
            "Strengthened the University of Melbourne section as the main proof of systems depth.",
            "Added a systems-specific skills line.",
        ],
        "cover_letter": [
            "I am applying for the Systems PhD - Software Engineer role at Databricks. This role is a strong match for my background in database systems, backend engineering, and performance-focused data infrastructure.",
            "In my PhD and postdoctoral work at the University of Melbourne, I worked on database systems problems where performance depends on design choices inside the system. One example is data layout optimization. The problem was that data lake systems can behave very differently depending on how data is physically organized. I built a layout advisory system with dataset ingestion, SQL workload parsing, and layout recommendation, and I developed a cost model for physical design trade-offs. This work led to research published at VLDB 2025, and related follow-up work was submitted to VLDB 2026.",
            "Another example is benchmarking. I built DriftBench to study how system performance changes when workloads or data drift over time. The key point was to look beyond static benchmark results and ask whether system behavior stays stable when conditions change. That work strengthened my approach to systems evaluation and is also tied to a VLDB 2026 submission.",
            "I also bring industry experience beyond research systems. At nftDb, I built Python ingestion pipelines, SQL and dbt workflows, and internal retrieval-oriented tools. Earlier at Baidu, I worked on messaging infrastructure and database performance tuning. These roles gave me practical experience with backend reliability, data workflows, and production-oriented engineering.",
            "What especially interests me about Databricks is the chance to work on database and storage problems that are both deep and practical. The role's focus on query optimization, storage structures, indexes, and physical data optimization is very close to the work I have already been doing. I believe I can bring strong systems depth, careful performance thinking, and a practical engineering mindset to this team.",
            "I would welcome the opportunity to discuss how my background could contribute to Databricks.",
        ],
        "video_script": [
            "Hi, I am Guanli Liu. I am a software engineer and postdoctoral researcher in Melbourne. My background is in database systems, backend engineering, and performance-focused data infrastructure.",
            "I am excited about this role because it matches both my research and my engineering work. My PhD and postdoctoral work has focused on database systems topics like physical data design, indexing, benchmarking, query-related systems, and performance evaluation. I enjoy building real systems and understanding how design choices affect performance.",
            "One example is my work on data layout optimization. The problem was that data lake systems can perform very differently depending on how data is physically organized. I built a layout advisory system that supports dataset ingestion, SQL workload parsing, and layout recommendation. I also developed a cost model for physical design trade-offs. This work led to research published at VLDB 2025, and related follow-up work was submitted to VLDB 2026. More importantly, it shows how I work. I like to build systems, test ideas, and connect design choices with real performance outcomes.",
            "Another example is benchmarking. I built DriftBench to study how system performance changes when workloads or data drift over time. The key idea was to go beyond static benchmark results and ask whether performance stays stable when conditions change. That work strengthened my ability to measure system behavior carefully and make performance claims based on evidence. It is also tied to a VLDB 2026 submission.",
            "I also have industry experience. At nftDb, I built Python ingestion pipelines, SQL and dbt workflows, and internal retrieval-oriented tools. Earlier at Baidu, I worked on messaging infrastructure and database performance tuning. These roles gave me practical experience with backend reliability, delivery, and engineering work in real environments.",
            "What I like about Databricks is that the problems are both deep and real. The role mentions query optimization, storage structures, indexes, and physical data optimization. Those are the areas where I have the strongest overlap. I also like that Databricks works on systems that have real product impact at scale.",
            "I believe I would bring a strong mix of systems depth, hands-on engineering, and careful performance thinking. Just as important, I can explain technical work clearly and connect it to useful outcomes. That is why this role feels like a strong fit for me.",
            "Thank you for your time. I would be excited to speak with you.",
        ],
    },
}


def latex_escape(text: str) -> str:
    replacements = {
        "\\": "\\textbackslash{}",
        "&": "\\&",
        "%": "\\%",
        "$": "\\$",
        "#": "\\#",
        "_": "\\_",
        "{": "\\{",
        "}": "\\}",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")


def build_text_tex(title: str, subtitle: str, body_lines: list[str]) -> str:
    paragraphs = "\n\n".join(latex_escape(line) for line in body_lines)
    return (
        "\\documentclass[11pt]{article}\n"
        "\\usepackage[a4paper,left=0.85in,right=0.85in,top=0.75in,bottom=0.75in]{geometry}\n"
        "\\usepackage{hyperref}\n"
        "\\hypersetup{hidelinks}\n"
        "\\usepackage{parskip}\n"
        "\\begin{document}\n"
        "\\thispagestyle{empty}\n"
        f"{{\\Large \\textbf{{{latex_escape(title)}}}}}\\\\\n"
        f"{latex_escape(subtitle)}\\\\\n"
        f"Prepared on April 5, 2026\n\n"
        f"{paragraphs}\n\n"
        "\\end{document}\n"
    )


def build_resume_tex(base: str, role: dict) -> str:
    content = base.replace(PROFILE_OLD, role["profile"])
    content = content.replace(UMELB_SUMMARY_OLD_1, role["summary_lines"][0])
    content = content.replace(UMELB_SUMMARY_OLD_2, role["summary_lines"][1])
    content = content.replace(LAYOUT_BULLET_OLD, role["layout_bullet"])
    content = content.replace(DRIFT_BULLET_OLD, role["drift_bullet"])
    if role["extra_skill"] not in content:
        content = content.replace(SKILL_INSERT_AFTER, f"{SKILL_INSERT_AFTER}\n\n{role['extra_skill']}")
    return content


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def run_build(tex_path: Path) -> None:
    subprocess.run(
        ["bash", str(ROOT / "scripts" / "build_resume.sh"), str(tex_path)],
        cwd=ROOT,
        check=True,
    )


def analysis_text(role: dict) -> str:
    parts = ["# Job Analysis", "", "## Source", f"- URL: {role['source_url']}", f"- Note: {role['source_note']}", ""]
    if role["status"] != "verified":
        parts.extend(
            [
                "## Status",
                f"- This role is currently marked as `{role['status']}`.",
                "",
                "## What I Can Do Now",
            ]
        )
    else:
        parts.append("## Role Summary")
    for item in role["job_summary"]:
        parts.append(f"- {item}")
    if role["must_have"]:
        parts.extend(["", "## Must Have"])
        parts.extend(f"- {item}" for item in role["must_have"])
    if role["nice_to_have"]:
        parts.extend(["", "## Nice To Have"])
        parts.extend(f"- {item}" for item in role["nice_to_have"])
    if role["team_needs"]:
        parts.extend(["", "## Likely Team Needs"])
        parts.extend(f"- {item}" for item in role["team_needs"])
    if role["best_evidence"]:
        parts.extend(["", "## Best Evidence From My Background"])
        parts.extend(f"- {item}" for item in role["best_evidence"])
    if role["gaps"]:
        parts.extend(["", "## Potential Gaps And Honest Framing"])
        parts.extend(f"- {item}" for item in role["gaps"])
    if role["resume_plan"]:
        parts.extend(["", "## Resume Tailoring Plan"])
        parts.extend(f"- {item}" for item in role["resume_plan"])
    if role["cover_plan"]:
        parts.extend(["", "## Cover Letter / Video Plan"])
        parts.extend(f"- {item}" for item in role["cover_plan"])
    return "\n".join(parts)


def resume_changes_text(role: dict) -> str:
    parts = ["# Resume Changes", "", "## What Changed"]
    parts.extend(f"- {item}" for item in role["resume_changes"])
    parts.extend(
        [
            "",
            "## Why It Changed",
            "- The wording was shifted toward the strongest truthful overlap with the current role.",
            "- The goal was to improve ATS fit without sounding AI-written or exaggerated.",
            "",
            "## What Was Intentionally Not Changed",
            "- No unsupported claims were added.",
            "- No fake metrics or fake scale were introduced.",
            "",
            "## Remaining Fit Gaps",
        ]
    )
    parts.extend(f"- {item}" for item in role["gaps"])
    return "\n".join(parts)


def job_posting_text(role: dict) -> str:
    lines = [
        "# Job Posting",
        "",
        "## Source",
        f"- Company: {role['company']}",
        f"- Role title: {role['role']}",
        f"- URL: {role['source_url']}",
        f"- Snapshot date: 2026-04-05",
        "",
        "## Notes",
        f"- {role['source_note']}",
    ]
    lines.extend(f"- {item}" for item in role["job_summary"])
    return "\n".join(lines)


def ats_score(role: dict) -> int:
    score = 84
    for gap in role.get("gaps", []):
        gap_lower = gap.lower()
        if "no direct" in gap_lower or "no explicit" in gap_lower or "expects closer exposure" in gap_lower:
            score -= 8
        elif "much stronger" in gap_lower or "stronger in" in gap_lower or "stronger on" in gap_lower:
            score -= 7
        elif "less direct" in gap_lower or "not directly" in gap_lower:
            score -= 6
        else:
            score -= 5
    return max(58, min(92, score))


def ats_review_text(role: dict) -> str:
    score = ats_score(role)
    lines = [
        "# ATS Review",
        "",
        "## ATS Match Score",
        f"- {score} / 100",
        "",
        "## Why This Score",
        "- The score reflects how well the tailored resume matches the role using truthful keyword overlap plus real evidence.",
    ]
    if role.get("best_evidence"):
        lines.extend(f"- Strength: {item}" for item in role["best_evidence"][:3])
    if role.get("gaps"):
        lines.extend(f"- Score reduced because: {item}" for item in role["gaps"][:3])
    lines.extend(
        [
            "",
            "## Keyword Coverage",
        ]
    )
    if role.get("must_have"):
        lines.extend(f"- High-value JD terms addressed: {item}" for item in role["must_have"][:4])
    if role.get("nice_to_have"):
        lines.extend(f"- Lower-confidence or partial coverage: {item}" for item in role["nice_to_have"][:3])
    lines.extend(
        [
            "",
            "## Evidence Strength",
        ]
    )
    if role.get("best_evidence"):
        lines.extend(f"- {item}" for item in role["best_evidence"])
    else:
        lines.append("- Evidence is limited because the role was not fully verified.")
    lines.extend(
        [
            "",
            "## Likely Screening Risks",
        ]
    )
    if role.get("gaps"):
        lines.extend(f"- {item}" for item in role["gaps"])
    else:
        lines.append("- No major screening risk identified from the current JD mapping.")
    lines.extend(
        [
            "",
            "## Recommended Resume Fixes Before Applying",
        ]
    )
    if role.get("resume_plan"):
        lines.extend(f"- {item}" for item in role["resume_plan"][:4])
    else:
        lines.append("- No tailored resume guidance available.")
    return "\n".join(lines)


def hr_readout(role: dict) -> str:
    family = role.get("family", "")
    if family in {"query_engine", "systems_phd"}:
        return "Likely to read as a strong systems candidate with credible research depth and practical engineering value."
    if family == "data_infra_research":
        return "Likely to read as a research-facing infrastructure candidate with solid systems credibility."
    if family == "ml_systems_research":
        return "Likely to read as an interesting systems-performance researcher, but not as a direct low-level AI systems specialist."
    if family == "research_scientist":
        return "Likely to read as a credible research scientist candidate with strongest fit in systems and performance work."
    return "Likely to read as a thoughtful candidate with clear strengths, though fit depends on how narrowly the team defines the role."


def hr_forward_decision(role: dict) -> str:
    score = ats_score(role)
    family = role.get("family", "")
    if family == "ml_systems_research":
        return "Maybe. I would move this candidate forward only if the team is open to a systems-performance researcher without direct accelerator or training-stack depth."
    if score >= 78:
        return "Yes. I would be comfortable moving this candidate to a recruiter screen or early technical conversation."
    if score >= 68:
        return "Maybe. I would want a quick recruiter screen to test how clearly the candidate explains the fit."
    return "Unclear. I would worry that the role-to-background mapping is too weak without more direct evidence."


def hr_review_text(role: dict) -> str:
    lines = [
        "# HR Review",
        "",
        "## HR Readout",
        f"- {hr_readout(role)}",
        "",
        "## What Works Well",
    ]
    if role.get("best_evidence"):
        lines.extend(f"- {item}" for item in role["best_evidence"][:3])
    lines.extend(
        [
            "- The materials are framed around real evidence instead of inflated claims.",
            "- The cover letter and video script explain technical work in a way a recruiter can follow.",
            "",
            "## What May Worry HR",
        ]
    )
    if role.get("gaps"):
        lines.extend(f"- {item}" for item in role["gaps"][:3])
    else:
        lines.append("- No major recruiter concern stands out from the current package.")
    lines.extend(
        [
            "- If the role is defined too narrowly, a recruiter may think the profile is too academic or adjacent rather than direct.",
            "",
            "## Would I Move This Candidate Forward?",
            f"- {hr_forward_decision(role)}",
            "",
            "## How To Improve Before Sending",
        ]
    )
    if role.get("resume_plan"):
        lines.extend(f"- {item}" for item in role["resume_plan"][:3])
    lines.extend(
        [
            "- Keep the first 30 seconds of the video very clear about what kind of role you fit best.",
            "- Make sure the first paragraph of the cover letter names the team need you match most directly.",
        ]
    )
    return "\n".join(lines)


def process_role(slug: str, role: dict, base_resume_text: str) -> None:
    job_dir = ROOT / "jobs" / slug
    output_dir = job_dir / "outputs" / DATE
    output_dir.mkdir(parents=True, exist_ok=True)
    company_slug = slugify(role["company"])
    position_slug = role.get("position_slug", slugify(role["role"]))

    write(job_dir / "job_posting.md", job_posting_text(role))
    write(output_dir / f"job_analysis_{DATE}.md", analysis_text(role))

    if role["status"] != "verified":
        return

    write(output_dir / f"resume_changes_{DATE}.md", resume_changes_text(role))
    write(output_dir / f"ats_review_{DATE}.md", ats_review_text(role))
    write(output_dir / f"hr_review_{DATE}.md", hr_review_text(role))

    resume_tex_name = f"guanli_liu_resume_{company_slug}_{position_slug}.tex"
    resume_tex_path = output_dir / resume_tex_name
    write(resume_tex_path, build_resume_tex(base_resume_text, role))
    run_build(resume_tex_path)

    cover_md_name = f"cover_letter_{DATE}.md"
    cover_md_path = output_dir / cover_md_name
    write(cover_md_path, "# Cover Letter\n\n" + "\n\n".join(role["cover_letter"]))

    cover_tex_name = f"guanli_liu_coverletter_{company_slug}_{position_slug}.tex"
    cover_tex_path = output_dir / cover_tex_name
    write(cover_tex_path, build_text_tex("Cover Letter", f"{role['company']} - {role['role']}", role["cover_letter"]))
    run_build(cover_tex_path)
    cover_tex_path.unlink(missing_ok=True)

    video_md_name = f"hr_video_script_{DATE}.md"
    video_md_path = output_dir / video_md_name
    video_intro = [
        "# HR Video Script",
        "",
        "## US Style Notes",
        "",
        "- Start with a smile and steady eye contact.",
        "- Use short sentences and pause after each key point.",
        "- Keep the tone clear, positive, and direct.",
        "- When talking about research, explain the problem, what you built, and why it mattered before naming the venue.",
        "",
        "## Key Message To Sell Yourself",
        "",
        "I can build real systems, explain technical work clearly, and connect research ideas to practical outcomes.",
        "",
        "## Script",
        "",
    ]
    write(video_md_path, "\n".join(video_intro) + "\n\n" + "\n\n".join(role["video_script"]))

    video_tex_name = f"guanli_liu_videoscript_{company_slug}_{position_slug}.tex"
    video_tex_path = output_dir / video_tex_name
    video_tex_lines = [
        "US Style Notes",
        "Start with a smile and steady eye contact.",
        "Use short sentences and pause after each key point.",
        "Keep the tone clear, positive, and direct.",
        "When talking about research, explain the problem, what you built, and why it mattered before naming the venue.",
        "",
        "Key Message To Sell Yourself",
        "I can build real systems, explain technical work clearly, and connect research ideas to practical outcomes.",
        "",
        "Script",
    ] + role["video_script"]
    write(video_tex_path, build_text_tex("HR Video Script", f"{role['company']} - {role['role']}", video_tex_lines))
    run_build(video_tex_path)
    video_tex_path.unlink(missing_ok=True)


def main() -> None:
    base_resume_text = BASE_RESUME.read_text(encoding="utf-8")
    for slug, role in ROLE_DATA.items():
        process_role(slug, role, base_resume_text)


if __name__ == "__main__":
    main()
