# LangChoiceBench: Measuring and Explaining Programming-Language Choice in LLMs

- **Category:** NLP
- **Date:** 2026-08-06
- **Link:** http://arxiv.org/abs/2608.06041v1

---
This research paper introduces a new benchmark to systematically measure and explain programming-language choices made by Large Language Models (LLMs) when generating project-level code.

## Problem

*   LLMs exhibit a strong preference for Python when generating project-level code, even in scenarios where Python is a suboptimal choice.
*   There is a lack of systematic methods and dedicated benchmarks to measure this behavior, assess its consistency, and understand its underlying causes across various LLM models.
*   Poor programming language choices in software projects can have significant long-term negative impacts on maintainability, security, performance, and robustness, and are difficult to reverse.
*   Prior work identified this Python bias and recommendation-implementation inconsistency but lacked systematic variation of project areas, task requirements, prompt wording, investigation of newer reasoning models, or a reproducible benchmark.

## Method

*   **Introducing LANGCHOICEBENCH:** The authors developed a novel, dedicated project-level code-generation benchmark to measure Python preference, recommendation–implementation consistency, and language diversity in LLMs.
*   **Benchmark Design:**
    *   Covers 28 projects across seven distinct software areas where Python is often a poor default (e.g., Embedded, Enterprise, Frontend, Games, Low latency, Mobile, Systems).
    *   Each area includes four realistic, concise, and language-agnostic project tasks.
    *   For each task, three wording variants were created for both "implementation prompts" (asking for code) and "recommendation prompts" (asking for language suggestions).
*   **Evaluation Protocol:**
    *   Evaluated 25 diverse LLMs, including state-of-the-art frontier models and smaller open-weight models, with a focus on modern reasoning models.
    *   Used a default model-generation setting, generating 20 samples per implementation prompt variant and 5 samples per recommendation prompt variant (2,100 responses per model).
    *   Responses were parsed using regular expressions to extract code blocks and infer the primary implementation language, and custom tags (`<language>...</language>`) for recommendations.
*   **Metrics:**
    *   **Python Preference:** Python Implementation Rate (PyIR) and Python Recommendation Rate (PyRR).
    *   **Recommendation–Implementation Alignment:** Recommendation–Implementation Rate (RIR - proportion of implementations using a top-three recommended language) and Recommendation–Implementation Alignment (RIA - Spearman rank correlation between recommendation and implementation language rankings).
    *   **Language Diversity:** Effective Language Diversity (ELD - exponential entropy of the implementation-language distribution within each area).
*   **Reasoning Trace Analysis:** Analyzed 9,826 reasoning traces from Python implementations to understand models' justifications for their choices.

## Impact

*   **Pervasive Python Over-selection:** LLMs heavily over-select Python for project implementations (average PyIR of 35.3%) even in suboptimal contexts, while explicitly recommending it much less often (average PyRR of 10.7%). PyIR was higher than PyRR for every evaluated model.
*   **Low Consistency:** Recommendation–implementation consistency is generally low (average RIR of 48.8%), meaning less than half of implementations use one of the model's own top-three recommended languages. Alignment across full language rankings (RIA) is also weak (mean 0.17).
*   **Model Size and Specialization Effects:** Smaller open-weight models generally exhibit stronger Python preference and lower language diversity. Code-specialized models also show strong Python-heavy tendencies, indicating that specialization doesn't remove this bias, and can even reinforce it.
*   **Reasons for Poor Choice (Reasoning Trace Analysis):**
    *   **Automatic/Ease-driven:** Most Python choices are automatic (69.8%) or driven primarily by ease (20.5%), rather than explicit consideration of project requirements.
    *   **Phantom Evidence:** In 7.8% of cases, models fabricate contextual support for choosing Python, a failure mode termed "phantom evidence."
    *   **Inconsistency:** In 1.9% of cases, models explicitly select another language in their reasoning but then produce Python code.
*   **Contributions:**
    *   Release of **LANGCHOICEBENCH**, the first dedicated benchmark for evaluating project-level programming-language choice in LLMs, including prompts, data, and evaluation tools.
    *   A broad empirical evaluation of 25 diverse LLMs, providing insights into Python preference, recommendation–implementation consistency, and language diversity.
    *   Detailed analysis of reasoning traces that explains why models make suboptimal language choices, highlighting issues like missing deliberation, fabricated evidence, and output inconsistency.