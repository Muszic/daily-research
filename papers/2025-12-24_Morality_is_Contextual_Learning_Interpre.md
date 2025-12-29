# Morality is Contextual: Learning Interpretable Moral Contexts from Human Data with Probabilistic Clustering and Large Language Models

- **Category:** NLP
- **Published:** 2025-12-24
- **Source:** [Original ArXiv Link](http://arxiv.org/abs/2512.21439v1)

---

## 🧐 Problem

The increasing integration of AI into social, economic, and moral interactions necessitates ethical supervision and alignment with human ethical standards. A significant challenge lies in the **profound context-dependency of human moral cognition**, where identical actions elicit divergent moral judgments based on situational, cultural, or psychological nuances. Existing rigid ethical frameworks and traditional AI alignment methods, including those based on Large Language Models (LLMs) trained with human feedback, struggle to capture this flexible, context-sensitive nature of human morality.

Specifically:
*   **Contextual Variability:** AI systems need to adapt to morally complex situations highly sensitive to context.
*   **Limitations of Rigid Frameworks:** Current ethical frameworks often fail to account for the dynamic, context-dependent nature of human morality.
*   **Opaque AI Systems:** It is difficult to ensure value alignment and explainability in opaque AI systems like end-to-end LLMs, which lack real reasoning abilities and guarantees of truth value.
*   **Lack of Empirical Grounding:** Synthetic datasets used for training moral AI often lack ecological validity and reproducibility, failing to reflect real human moral behavior and cultural diversity.

## 🛠️ Method

The paper introduces **COMETH (Contextual Organization of Moral Evaluation from Textual Human inputs)**, a novel framework designed to model how context shapes the acceptability of ambiguous actions by integrating empirical moral judgment data with a probabilistic context learning architecture.

COMETH's pipeline consists of four main components:

1.  **Empirical Data Collection:**
    *   A dataset of **300 high-ambiguity moral scenarios** was curated, based on Gert's common morality framework, focusing on six core actions (e.g., euthanasia, lying for support, stealing).
    *   **Ternary moral judgments** (Blame/Neutral/Support) were collected from **N=101 participants** for each scenario via an online survey.

2.  **LLM-based Pre-processing:**
    *   An LLM filter (e.g., Qwen-80B, Mistral-7B, Llama-3.1) extracts the principal action from each scenario into a uniform "to + verb + complement" format.
    *   These actions are then embedded using MiniLM-L6-v2 and clustered with K-means to produce **robust "Core Action" categories**, ensuring semantic consistency.

3.  **Probabilistic Context Learner:**
    *   Inspired by Model-Based Reinforcement Learning (MBRL), this module autonomously infers and refines **moral contexts** by clustering scenarios based on their human-derived ternary judgment distributions.
    *   An **adding module** uses Kullback-Leibler (KL) divergence to assign new scenarios to existing contexts or create new ones if the scenario's judgment distribution is sufficiently different.
    *   A **merging module** uses a semi-weighted Jensen-Shannon divergence (swJS) to consolidate similar contexts, preventing redundancy and maintaining diverse representations.

4.  **Generalization Module:**
    *   An LLM extracts **concise, non-evaluative binary contextual features** for each scenario within a cluster (e.g., "explicit consent only").
    *   These features are used to learn **feature importance weights** in a transparent likelihood-based model.
    *   This module predicts the moral judgment of new scenarios by assigning them to the most probable cluster based on their features, while also providing **interpretability** by revealing which features drive the predictions.

## 📊 Impact

COMETH demonstrates significant improvements in modeling context-sensitive human moral judgments and offers an interpretable alternative to opaque end-to-end LLM approaches:

*   **Doubled Alignment with Human Judgments:** Empirically, COMETH roughly **doubles the alignment rate** with majority human judgments compared to end-to-end LLM prompting (achieving approximately **60% vs. 30%** on average). This highlights the benefit of grounding predictions in structured feature representations rather than direct LLM outputs.
*   **Enhanced Interpretability and Explainability:** The Generalization module explicitly reveals **which contextual features drive moral predictions** by assigning weights to them. This provides a transparent framework for understanding *why* certain actions are judged a particular way in specific contexts, addressing a key limitation of black-box LLMs.
*   **Reproducible and Empirically Grounded Pipeline:** The research contributes:
    *   An **empirically grounded moral-context dataset** of 300 scenarios with human judgments.
    *   A **reproducible pipeline** that effectively combines human judgments, model-based context learning, and LLM semantic abstraction.
*   **Robustness and Scalability:** COMETH reduces variability in predictions across different LLMs and prompts, producing more stable clusters. It also suggests that semantic structuring can mitigate scale disparities, making robust moral prediction feasible even with lighter LLMs.
*   **Dynamic Context Learning:** The probabilistic context learner dynamically creates, updates, and merges moral contexts as new data is observed, adapting to the nuanced and evolving nature of human moral reasoning.
