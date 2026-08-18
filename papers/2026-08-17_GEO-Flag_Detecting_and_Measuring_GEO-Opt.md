# GEO-Flag: Detecting and Measuring GEO-Optimized Web Content

- **Category:** Machine Learning
- **Date:** 2026-08-17
- **Link:** http://arxiv.org/abs/2608.16824v1

---
Here's a summary of the research paper in Markdown:

### Problem

Generative Engine Optimization (GEO) involves modifying web content to improve its visibility and citation likelihood by generative search engines. This practice poses significant risks: it can give low-authority or irrelevant pages disproportionate visibility, potentially displacing reliable sources, and enable the propagation of weak or false information presented as well-supported. Unlike conventional search, generative search synthesizes direct answers, making it harder for users to assess source provenance and authority. Despite these concerns, systematic methods for detecting GEO-optimized content are largely underexplored, and existing detection methods exhibit substantial weaknesses, including poor generalization across different GEO strategies and reliance on human-vs-AI authorship cues rather than GEO-specific signals.

### Method

1.  **GEOFlagBench Benchmark:** Introduced a novel benchmark of 3,200 webpages across 400 queries, four domains (Health, Finance, Technology, Travel), and eight GEO optimizer families (including strategy-based rewriting, learned optimization, preference manipulation, and human GEO). This benchmark was used to systematically evaluate existing GEO detection methods (fine-tuned classifiers, zero-shot LLMs, feature-based models, and repurposed AI-text detectors).
2.  **Intervention-Paired Training (IPT):** Proposed a new training method to improve GEO detection. IPT supervises detector responses to content transformations using:
    *   **Positive Pairs:** Requires a higher GEO score for a page after a GEO intervention compared to its original version.
    *   **Zero Pairs:** Constrains GEO scores to remain close for an original page and its non-GEO AI-polished version, teaching the detector that LLM editing alone is not GEO evidence.
    This design encourages detectors to focus on GEO-specific changes, reducing reliance on static authorship or generic LLM-writing cues. IPT was applied to ModernBERT and Qwen3-0.6B models.
3.  **GEO-gated Agent System for Auditing:** Developed a system to assess the verifiability of Citation URLs on detected GEO pages. This system first applies the GEO detector, then uses deterministic parsing and retrieval to extract and collect evidence for Citation URLs. A constrained agent assigns a publisher Source Tier to each URL, and deterministic rules derive a Citation URL Verifiability label.
4.  **Empirical Prevalence Estimation:** Deployed the complete GEO detection and Citation URL audit pipeline on 10,095 pages associated with 1,000 real-user ORCAS queries from released Google Search and Gemini-grounded retrieval results.

### Impact

1.  **Revealed Detection Weaknesses:** Evaluation using GEOFlagBench demonstrated that while some existing methods achieve high aggregate F1 scores (up to 0.880), they suffer from significant method-level weaknesses (e.g., poor recall on sparsely modified or human-based GEO content) and potential reliance on original-authorship shortcuts (e.g., large false-positive rate gaps between AI- and human-authored non-GEO pages).
2.  **Improved Robust Detection:** Intervention-Paired Training (IPT) substantially improved GEO detection performance and robustness. For instance, on ModernBERT, IPT increased F1 from 0.862 to 0.944 and worst-group accuracy from 0.725 to 0.883, while reducing the authorship-conditioned false-positive-rate gap from 0.263 to 0.108.
3.  **Quantified Real-World GEO Prevalence:** The deployment pipeline estimated an overall GEO prevalence of 8.90% in real-world search results (8.14% for Google Search, 9.09% for Gemini). This prevalence shows a clear increasing trend, reaching an estimated 16.36% among pages modified in 2026.
4.  **Highlighted Citation Verifiability Risks:** The audit revealed that 69.34% of Citation occurrences on detected GEO pages received "LOW" verifiability labels, indicating a significant risk of strategically constructed or low-quality source support.
5.  **Established Foundation:** The research establishes a foundational framework and tools for systematically detecting, auditing, and measuring GEO in real-world search ecosystems.