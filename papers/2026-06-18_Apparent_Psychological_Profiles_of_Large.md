# Apparent Psychological Profiles of Large Language Models are Largely a Measurement Artifact

- **Category:** NLP
- **Date:** 2026-06-18
- **Link:** http://arxiv.org/abs/2606.20205v1

---
This research paper investigates the validity of assigning stable psychological profiles to Large Language Models (LLMs) using instruments designed for humans.

### Problem
The increasing practice of using human-designed psychological instruments to characterize LLMs with stable psychological profiles (e.g., personality, risk-preference) is problematic. These profiles are used to inform judgments about an LLM's usability, safety (e.g., propensity for risky behavior), and their potential as proxies for human participants in research. However, it is unclear whether these apparent profiles represent genuine, stable traits of the LLMs or are simply artifacts of the measurement process itself. Existing evidence suggests LLM responses can be sensitive to minor prompt changes, exhibit different factor structures than humans, and show weak correlations between self-reported traits and actual behavior, casting doubt on the validity of these borrowed instruments.

### Method
The researchers employed a formal psychometric framework to analyze LLM responses, specifically designed to distinguish between true latent traits and directional response biases.
1.  **Participants & Instruments:** They administered a battery of 29 psychological instruments (including the 300-item IPIP-NEO Big Five personality inventory and a comprehensive risk-preference battery spanning self-reports and behavioral tasks) to 56 instruction-tuned LLMs (46 open-source, 10 proprietary) and large human reference samples (N=20,993).
2.  **Key Concept:** The instruments varied in their "response orthogonality"—the proportion of items where the targeted trait and a potential response bias would lead to opposite response directions (e.g., comparing forward-keyed items like "I worry a lot" with reverse-keyed items like "I keep my cool" for Neuroticism).
3.  **Analysis:** They performed:
    *   A diagnostic test using forward-reverse item mean correlations to identify whether between-model variation was driven by trait or bias.
    *   Per-model decomposition of responses into a latent trait component ($\theta_i$) and a response-bias component ($b_i$).
    *   Analysis of how response bias correlates with model capability (size, proprietary vs. open-source).
    *   Examination of the relationship between an instrument's response orthogonality and the apparent internal consistency (reliability) of LLM responses.

### Impact
The study's findings demonstrate that the apparent psychological profiles of LLMs are predominantly artifacts of the measurement instruments, not inherent properties of the models:

*   **Bias, Not Trait, Drives LLM Differences:** Differences between LLMs on psychological instruments are primarily driven by a "directional response bias"—a tendency to consistently select one end of a scale or one labeled option, regardless of the item's content. This bias accounts for 81–90% of between-model variation in LLMs, compared to only 9–16% in humans, where trait variance dominates.
*   **Bias Persists Despite Capability:** While response bias slightly decreases with increased model capability (e.g., larger parameter count, proprietary models), it is not eliminated and remains significantly higher than human levels, even in the most advanced LLMs.
*   **Orthogonality Explains Apparent Reliability:** The apparent high reliability (internal consistency) observed in LLM responses on many instruments is spurious. It is almost entirely predicted by the instrument's lack of "response orthogonality" (correlation $r = -0.95$). Instruments with few reverse-keyed items show artificially high consistency due to bias, while instruments with high orthogonality reveal near-zero consistency, indicating that consistency is bias-driven, not trait-driven.
*   **Profiles are Manufacturable:** As a consequence, the specific psychological profile an LLM appears to possess can be manipulated or "manufactured" through the selection of items in the measurement instrument.

The study concludes that psychological instruments borrowed from human psychology lack validity for characterizing LLMs. It calls for the development of dedicated LLM assessment methodologies centered on "response orthogonality" to achieve a more accurate and meaningful understanding of machine behavior.