# SFCoT: Safer Chain-of-Thought via Active Safety Evaluation and Calibration

- **Category:** Cryptography
- **Date:** 2026-03-16
- **Link:** http://arxiv.org/abs/2603.15397v1

---
## SFCoT: Safer Chain-of-Thought via Active Safety Evaluation and Calibration

### Problem

Large Language Models (LLMs) are highly susceptible to jailbreak attacks that bypass their safety alignments, leading to harmful outputs. Existing defense mechanisms primarily rely on **post-hoc filtering**, which only evaluates and removes harmful content from the **final output**. This approach leaves intermediate **Chain-of-Thought (CoT) reasoning steps** unmonitored and vulnerable to adversarial manipulation, allowing harmful intent to propagate undetected until the final generation. This delayed response increases potential exposure to unsafe content and compromises the overall reliability of LLM safety mechanisms.

### Method

This paper proposes **SaFer Chain-of-Thought (SFCoT)**, a framework that proactively monitors and calibrates potential risks throughout the entire reasoning process in real time. SFCoT operates as follows:

1.  **CoT Parser:** Extracts structured reasoning steps (`t_i`) from the LLM's output stream.
2.  **Three-tier Safety Scoring System:** Each individual reasoning step (`t_i`) is evaluated by a comprehensive scoring system:
    *   **Lexical Level:** Rapid screening for explicit violations using sensitive lexicons and regex rules.
    *   **Semantic Level:** Utilizes a lightweight deep learning model to interpret the deeper meaning and identify implicit risks (e.g., evasive phrasing).
    *   **Policy Level:** Contextualizes the step within the broader CoT to detect advanced adversarial tactics like rule-circumvention or logical inconsistencies.
    *   A weighted fusion of these three levels yields a final safety score for each step.
3.  **Dynamic Intervention Module:** Based on the safety score, SFCoT takes targeted action:
    *   **Highly Safe:** Reasoning proceeds uninterrupted.
    *   **Explicitly Unsafe (below threshold):** The reasoning process is immediately **truncated** to halt further generation.
    *   **Gray Zone (ambiguous safety):** Triggers the **Multi-perspective Consistency Verification**.
4.  **Multi-perspective Consistency Verification:** For gray-zone steps, this module:
    *   Generates multiple semantically equivalent variants (paraphrases) of the suspicious step.
    *   Computes safety scores for these variants and assesses the variance.
    *   High variance suggests semantic instability or potential deceptiveness, prompting the Dynamic Intervention Module to perform **rewriting** of the step to redirect the reasoning trajectory.
    *   A fallback strategy is applied if multiple interventions fail.

This active evaluation and calibration at the CoT level allow for early detection and intervention, preventing harmful reasoning from fully developing.

### Impact

SFCoT demonstrates significant improvements in LLM safety and reliability:

*   **Reduced Attack Success Rate (ASR):** SFCoT drastically reduces the ASR from a baseline of **58.97% to 12.31%**. This represents a **79.1% improvement** over the original LLM and a **72.7% improvement** compared to a common post-hoc safety filtering scheme.
*   **Proactive Safety:** By intervening at intermediate reasoning steps, SFCoT prevents harmful outcomes from materializing, enhancing the trustworthiness of LLM deployments.
*   **Preserved Utility:** Despite robust safety enhancements, SFCoT preserves **91.2% of the base model’s general utility** across various benchmarks (MMLU, GSM8K, MBPP).
*   **Improved Output Quality:** The rewriting mechanism for gray-zone steps, as opposed to direct truncation, significantly maintains output quality, achieving an Output Quality Score of 4.6 compared to 2.1 for direct truncation, ensuring safety without sacrificing usefulness.
*   **Efficiency:** SFCoT establishes an effective and efficient LLM safety enhancement method at the Chain-of-Thought level.