# Pretraining Data Can Be Poisoned through Computational Propaganda

- **Category:** Artificial Intelligence
- **Date:** 2026-07-16
- **Link:** http://arxiv.org/abs/2607.15267v1

---
Here's a summary of the research paper in Markdown format:

### Problem

Existing research on pretraining data poisoning for Language Models (LMs) has largely focused on limited, established data sources (e.g., Wikipedia) that do not represent the massive scale and heterogeneity of modern web-scale pretraining corpora (like Common Crawl). Consequently, it's unclear whether poisoning attacks are feasible in such large, diverse environments, and critically, whether malicious content can survive the complex web crawling, text extraction, and extensive data curation pipelines (deduplication, quality filtering) that precede LM training. This gap means the true risk of web-scale computational propaganda influencing LMs remains largely unquantified.

### Method

1.  **Novel Attack Vector Identification:** The paper identifies "third-party content injection" as a new, web-scale attack surface. Specifically, it focuses on **public discussion interfaces** (e.g., comment sections on websites) where an adversary can deploy automated tools to inject attacker-controlled text into webpages they do not own.
2.  **HALFLIFE Analysis Framework:** Introduces **HALFLIFE**, a novel probabilistic analysis, to estimate the end-to-end "poison inclusion" probability—the likelihood that injected adversarial content ultimately appears in a final LM training corpus. HALFLIFE decomposes this probability into three sequential stages:
    *   **S1 (Injectability):** Probability that a webpage is susceptible to content injection (e.g., has a public comment section). Estimated by scanning Common Crawl data.
    *   **S2 (Capture):** Probability that injected content is accurately scraped by web crawlers and survives text extraction into plain text. Simulated by injecting poison into identified comment sections and applying text extraction tools.
    *   **S3 (Survival):** Probability that captured content persists through standard LM data curation pipelines, including heuristic filtering, language identification, quality filtering, and deduplication.
3.  **Empirical Application & Comparison:** HALFLIFE is applied to analyze public comments as a poison vector. Its viability is contrasted with programmatic advertisements, which HALFLIFE determines are not a viable vector due to architectural incompatibility with text-based crawl pipelines.
4.  **Model Impact Evaluation:** Controlled experiments are conducted by training models with varying amounts of "comment-based" poisoned data. These models are evaluated on "belief-manipulation" tasks (e.g., biasing towards one entity over another) to demonstrate the impact of the included poison on downstream LM generations, using different content formats (e.g., Q/A, unlabeled text) to mimic naturalistic injections.

### Impact

*   **Quantified Web-Scale Vulnerability:** The research empirically demonstrates that poisoning pretraining data is feasible at web-scale through public discussion interfaces. HALFLIFE estimates a significant inclusion probability (e.g., 0.13% for comments), meaning even a relatively modest volume of injections (100k–1M webpages) can introduce enough poisoned documents to influence LMs. This scale of impact is greater than poisoning entire established sources like Wikipedia (0.067% of some corpora).
*   **Bypass of Data Curation:** It reveals that well-crafted, "naturalistic" adversarial injections can successfully bypass standard web crawling, text extraction, and robust LM data curation pipelines, including heuristic, language, and quality filters, without being detected or removed.
*   **Demonstrated Model Manipulation:** The study confirms that injected poisoned content, even in subtle formats, can effectively manipulate downstream language model behavior, leading them to generate specific claims, narratives, or recommendations (e.g., favoring one company over another).
*   **Essential Tool for Risk Assessment:** HALFLIFE is introduced as a crucial analytical framework for evaluating the practical viability of potential data poisoning vectors, highlighting the importance of considering the entire data preparation pipeline when assessing risks to LMs.