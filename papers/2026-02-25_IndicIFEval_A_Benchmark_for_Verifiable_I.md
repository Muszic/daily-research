# IndicIFEval: A Benchmark for Verifiable Instruction-Following Evaluation in 14 Indic Languages

- **Category:** NLP
- **Date:** 2026-02-25
- **Link:** http://arxiv.org/abs/2602.22125v1

---
Here's a summary of the research paper "IndicIFEval: A Benchmark for Verifiable Instruction-Following Evaluation in 14 Indic Languages" in Markdown:

---

### Problem

Large Language Model (LLM) instruction-following benchmarks are overwhelmingly English-centric, creating a critical evaluation gap for hundreds of millions of Indic language speakers. Existing methods like human evaluation are costly, and LLM-as-a-judge approaches can be inconsistent and biased. While automatically verifiable instruction benchmarks (e.g., IFEval) exist for English, LLMs exhibit significantly weaker performance in non-English languages for both generation and evaluation. There is a lack of comprehensive benchmarks for Indic languages that evaluate verifiable, rule-based constraints, especially considering their linguistic diversity, data scarcity, and distinct script systems. Previous multilingual efforts often rely solely on translation without proper localization or grounding in native content, and may not fully explore the impact of reasoning capabilities.

### Method

The authors introduce **INDICIFEV AL**, a benchmark designed to evaluate constrained generation of LLMs across 14 Indic languages (Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Nepali, Oriya, Punjabi, Sanskrit, Tamil, Telugu, Urdu, plus English as a baseline). It comprises approximately 800 human-verified examples per language, split into two complementary subsets:

1.  **INDICIFEV AL-TRANS**:
    *   Translated and localized prompts from the English IFEval benchmark.
    *   Underwent careful preprocessing, including manual inspection, localization of named entities (e.g., "President of USA" to "Prime Minister of India"), and addressing problematic translations (abbreviations, translationese).
    *   Keywords were extracted, individually translated, and re-inserted before full prompt translation to ensure accuracy.
    *   Automatic verification using regular expressions was performed, followed by human verification by native speakers for cultural suitability and translation quality.

2.  **INDICIFEV AL-GROUND**:
    *   Synthetically generated instructions grounded in native Indic content, addressing limitations of translation (e.g., unnatural keywords, grammatically infeasible constraints due to distinct Indic word order).
    *   Focused on six problematic constraint types: Keyword Inclusion/Prohibition/Frequency, Paragraph/Sentence Count, and First Word.
    *   Utilized context mining (TFIDF-based keyword extraction from the `sangraha-verified` corpus) and Gemini-2.5 for prompt generation, ensuring diversity in task types.
    *   Manually verified by native speakers to ensure validity and naturalness.

**Evaluation**:
*   A diverse suite of 20+ open-weight (Llama, Gemma, Aya, Qwen families) and proprietary (GPT-5, Gemini-3) models, ranging from 0.5B to 70B+ parameters, were evaluated.
*   Metrics included prompt-level and instruction-level loose accuracy, with a focus on prompt-level.
*   The original IFEval verification scripts were modified to integrate the **Indic NLP Library** for robust sentence segmentation and word tokenization across Indic scripts.
*   Evaluations were orchestrated using the Language Model Evaluation Harness with greedy decoding.

### Impact

*   **Released Benchmark**: INDICIFEV AL and its evaluation scripts are publicly released, providing a crucial resource to drive progress in multilingual constrained generation for Indic languages.
*   **Identified Cross-lingual Gap**: Evaluation consistently showed higher performance on English prompts compared to Indic languages, revealing a persistent cross-lingual gap in verifiable instruction following. This gap narrows for larger and more multilingual-oriented models but remains significant for smaller ones.
*   **Model Performance Trends**: Increasing model parameters generally improves performance, with gains plateauing around 12B-14B parameters, suggesting a minimum capacity for verifiable instruction adherence. The Gemma family consistently exhibited the smallest performance gap with English, while the Aya family showed the highest degradation. Hindi was identified as the most robust Indic language across model families.
*   **Constraint-Specific Struggles**: While models demonstrated strong adherence to **formatting constraints**, they struggled significantly with **lexical (keyword inclusion) and cross-lingual tasks**.
    *   Models were proficient at *avoiding* keywords (negative constraints) but struggled with *including* keywords (positive constraints or frequency), indicating a gap in generating precise lexical forms despite semantic understanding.
    *   Shifting the prompt language to Indic, even when an English output was requested, introduced a substantial performance gap, highlighting limitations in cross-lingual instruction-following despite strong English capabilities. Hindi, a high-resource Indic language, showed its maximum performance gap in this "English response from Indic prompt" category.
    *   Sanskrit showed the most significant performance degradation relative to English, especially for constraints requiring an English response.
*   **Framework for Expansion**: The research provides a comprehensive framework for extending verifiable instruction-following benchmarks to new languages, leveraging existing translation models, general-use LLMs, and local corpora.
*   **Overall Conclusion**: Despite progress in high-resource languages like Hindi, instruction-following across the broader Indic family significantly lags behind English, underscoring the need for continued research and development in this area.