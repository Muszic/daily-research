# WiC is Not WSD: A Study on LLMs and Lexical Ambiguity Resolution

- **Category:** NLP
- **Date:** 2026-09-17
- **Link:** http://arxiv.org/abs/2609.20593v1

---
Here's a summary of the research paper in Markdown format:

---

## WiC is Not WSD: A Study on LLMs and Lexical Ambiguity Resolution

### Problem

Large Language Models (LLMs) continue to struggle with the Word-in-Context (WiC) task, where they must determine if a target word is used in the same meaning in two different sentences. This is puzzling given their progress on other lexical-semantic tasks. The authors hypothesize that this difficulty stems not just from comparing two contextual uses, but primarily from **the absence of an explicit sense inventory** and **an unspecified level of semantic granularity** in WiC. Unlike traditional Word Sense Disambiguation (WSD), WiC forces LLMs to implicitly infer the appropriate sense distinctions, often leading them to make overly fine-grained judgments that do not align with human annotations.

### Method

The study evaluates open LLMs (Llama3, Mistral, DeepSeek, in large and small variants) on WiC and WSD tasks under comparable settings.

1.  **Tasks and Datasets:**
    *   **Coarse-grained WiC:** Converted from the CWSD-20 dataset.
    *   **Fine-grained WiC:** A new dataset constructed from WordNet 3.1 to avoid contamination issues, focusing on more subtle sense distinctions.
    *   **Coarse-grained WSD:** Using the CWSD-20 dataset.
2.  **Prompting Strategies:**
    *   **Options+ / Options-**: Experiments were run with (`Options+`) and without (`Options-`) providing explicit candidate senses to the models, aiming to mimic the WSD setting for WiC.
    *   **CoT+ / CoT-**: Chain-of-Thought (CoT) prompting was also applied, both with (`CoT+`) and without (`CoT-`) explicit reasoning steps.
3.  **Analysis:**
    *   Direct comparison of WiC performance with and without explicit sense options.
    *   Comparison of WiC and WSD performance using the same sense inventory.
    *   "WiC through WSD" setting: Models first performed WSD on each sentence independently, then their two predicted senses were compared to derive a WiC label.
    *   Human evaluation of LLM errors to categorize sources of failure (e.g., inability to identify sense, failure to compare, mismatch in sense granularity).

### Impact

1.  **Explicit Sense Granularity Drastically Improves WiC:** Providing candidate senses (`Options+`) significantly enhances WiC performance across all models and settings (e.g., from 78.5% to 84.9% mean accuracy in coarse-grained WiC with CoT+). This strongly supports the hypothesis that the ambiguity of sense granularity is a primary challenge in WiC for LLMs.
2.  **LLMs Overthink Fine-Grained Distinctions:** While LLMs show strong lexical-semantic knowledge in WSD (averaging 92.7% accuracy), a substantial performance gap remains when moving to WiC, even with explicit options (e.g., 84.9% in coarse-grained WiC). Human evaluation confirmed that many WiC errors are not due to a lack of understanding, but rather **label ambiguity or mismatches between model and annotator sense boundaries**. LLMs frequently "over-disambiguate," focusing on overly fine-grained distinctions not intended by the dataset annotators.
3.  **Chain-of-Thought is Granularity-Dependent:** CoT prompting improves performance in coarse-grained WiC but can hinder it in fine-grained WiC. This suggests that without explicit granularity guidance, CoT can amplify subtle contextual differences, leading models to draw excessively fine-grained boundaries.
4.  **WiC is a Test of Granularity Alignment:** The study concludes that WiC is a more complex task than WSD, acting as a test of how well an LLM's latent sense representations align with human judgments of appropriate sense granularity. Future WiC dataset design should consider providing explicit guidance on the expected level of semantic distinction.