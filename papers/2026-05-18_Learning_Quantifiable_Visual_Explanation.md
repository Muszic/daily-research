# Learning Quantifiable Visual Explanations Without Ground-Truth

- **Category:** Machine Learning
- **Date:** 2026-05-18
- **Link:** http://arxiv.org/abs/2605.18681v1

---
This research paper addresses the challenges of evaluating and generating high-quality visual explanations for deep learning models without relying on ground-truth annotations.

---

### Problem

*   **Difficulty in XAI Evaluation:** Modern deep learning models are "black boxes," and while Explainable AI (XAI) techniques (e.g., saliency maps) exist to provide human-interpretable explanations, their quality is difficult to quantify due to the lack of meaningful ground-truth to compare against.
*   **Limitations of Existing Metrics:** Current fidelity-based perturbation metrics (e.g., MoRF, LeRF) often fail to align with human intuition of explanation quality. They struggle with:
    *   **Large, irrelevant masks:** Giving high scores to explanations that highlight more information than necessary.
    *   **Multiple plausible explanations:** Penalizing masks that correctly identify one of several valid attribution pathways.
*   **Dependence on Ground-Truth for Learning:** Existing methods for learning explanations often rely on auxiliary supervision or proxy ground-truth signals, which are typically unavailable.

### Method

The paper proposes a dual contribution: a novel quantifiable metric and a self-supervised explanation generation technique.

1.  **Minimality-Sufficiency Integration (MSI) Metric:**
    *   **Purpose:** A new perturbation-based metric to quantify the quality of XAI methods, designed to favor explanations that are simultaneously specific (minimal) and sufficient (relevant).
    *   **Components:** MSI combines a `BaseScore` and a `MaskPenalty`.
        *   **`BaseScore`**: Measures the sufficiency and discriminative quality of an explanation. It compares the model's predictive performance when retaining only "relevant" pixels (above a threshold $\alpha_{min}$) versus retaining only "non-relevant" pixels (below $\alpha_{min}$), indicating a strong separation. It also integrates the Area Under Curve (AUC) from truncated perturbation curves (similar to MoRF-Insertion and MoRF-Deletion, but only integrating above $\alpha_{min}$). This addresses scenarios with multiple valid explanations.
        *   **`MaskPenalty`**: Penalizes explanations that highlight an unnecessarily large proportion of input pixels (i.e., pixels with values above $\alpha_{min}$), thus enforcing minimality and compactness.
    *   **Calculation:** `MSI = BaseScore - MaskPenalty`. The metric is sensitive to the $\alpha_{min}$ hyperparameter, which can be optimized for a given model and dataset.

2.  **Learnable Adapter eXplanation (LAX) Method:**
    *   **Purpose:** A novel, self-supervised XAI technique to generate explanations for any black-box model.
    *   **Approach:** LAX trains an "adapter module" on top of an existing pre-trained model. This adapter learns to output causal explanations (saliency maps).
    *   **Supervision:** Crucially, LAX is trained *without ground-truth annotations* for explanations. Instead, it uses a differentiable approximation of the proposed MSI metric as its supervision signal, inspired by the Information Bottleneck (IB) framework. This allows the model to inherently learn to generate explanations that satisfy the criteria of minimality and sufficiency.
    *   **Integration:** The adapter module works by fine-tuning a model to generate these explanations.

### Impact

*   **Quantifiable XAI Evaluation:** The proposed MSI metric provides a robust, quantifiable way to evaluate XAI methods. It "aligns better with human intuitions of explanation quality than do existing metrics," especially in cases of overly large masks or multiple valid explanations.
*   **High-Quality Explanation Generation:** The LAX method generates explanations that "outperform those of competing XAI techniques according to a number of quantifiable metrics."
*   **Ground-Truth Free Learning:** LAX addresses a significant challenge by learning to produce high-quality explanations in a self-supervised manner, without requiring costly and often unavailable ground-truth saliency maps.
*   **Non-Degrading Performance:** The LAX adapter module generates explanations "without degrading model performance" of the original black-box model.
*   **Causal Explanations:** The method aims to output causal explanations of the model's decision process.