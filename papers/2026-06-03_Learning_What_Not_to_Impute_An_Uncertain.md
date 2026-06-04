# Learning What Not to Impute: An Uncertainty-Aware Diffusion Framework for Meaningful Missingness

- **Category:** Machine Learning
- **Date:** 2026-06-03
- **Link:** http://arxiv.org/abs/2606.05073v1

---
This paper introduces Diff-Joint, a novel diffusion-based framework for "selective imputation" that addresses the often overlooked distinction between different types of missing values.

### Problem

Many real-world datasets contain missing entries (NAs) that are conventionally assumed to be unobserved regular values needing imputation. However, missingness can arise from two distinct sources:
1.  **Meaningfully Missing (MM):** Entries that are intrinsically absent, semantically valid, and should be preserved as 'na' (e.g., "not applicable" for a survey question). Imputing these can distort data, remove semantic information, and introduce bias.
2.  **Observation-Induced Missing:** Entries that are regular values but went missing due to data collection errors, transfer issues, or other observation processes, and *should* be imputed.

The core problem is that these two types of missingness appear identically as 'na' in observed data and are not directly distinguishable. The goal is to perform **selective imputation**: to jointly infer which observed NAs are meaningfully missing (and thus should be preserved) and which are observation-induced (and thus should be recovered/imputed).

### Method

Diff-Joint proposes an iterative, diffusion-based framework to jointly model tabular data (`x`) and a latent binary "meaningful missingness" mask (`c`).

1.  **Joint State Representation:** The method defines a joint diffusion state `(x, c)`, where `x` represents the completed tabular values and `c` is a binary mask indicating which entries are meaningfully missing (1 for MM, 0 for observation-induced).
2.  **Initialization:** All observed 'na' entries are initially treated as observation-induced missing, with their values randomly filled and the corresponding `c` mask set to 0.
3.  **Iterative Refinement Loop:** Diff-Joint alternates between two steps:
    *   **Model Update:** A diffusion model is trained on the current collection of estimated joint states `(x, c)`. This model learns the joint distribution of data values and meaningful-missingness patterns.
    *   **Latent State Update:** For each data point and each observed 'na' entry:
        *   **Conditional Sampling:** Multiple conditional samples `(x_k, c_k)` are drawn from the current diffusion model, conditioned on the observed entries.
        *   **Imputation of `x` (for observation-induced NAs):** The imputed value for `x` is updated by aggregating the `x_k` samples (e.g., mean for continuous, mode for discrete).
        *   **Updating `c` (Meaningful Missingness Mask):** This is the key innovation. An **uncertainty score** is computed for each 'na' entry based on the diversity of the `x_k` samples (empirical entropy for discrete, standard deviation for continuous).
            *   **High uncertainty** in the sampled `x_k` values suggests that the model is unsure how to impute, which is indicative of meaningful missingness (i.e., the 'na' state itself is the "correct" state).
            *   This uncertainty signal (identified via k-means clustering on uncertainty scores) is combined with a majority vote from the sampled `c_k` masks. An entry is classified as meaningfully missing if *either* the uncertainty pattern or the sampled `c_k` masks support the MM interpretation.
4.  **Final Output:** After several iterations, the model outputs the final imputed data (with observation-induced NAs filled) and the learned meaningful-missingness mask, preserving 'na' for identified MM entries.

### Impact

*   **Novel Problem Formulation:** Diff-Joint pioneers the formalization and practical solution to the "selective imputation" problem, moving beyond the traditional assumption that all missing data must be imputed.
*   **Effective Meaningfulness Identification:** The framework successfully distinguishes between meaningfully missing and observation-induced missing entries, as demonstrated on both synthetic Bayesian network data and a real-world clinical dataset (MIMIC-IV-ED).
*   **Competitive Imputation Accuracy:** While focusing on distinguishing missingness types, Diff-Joint maintains competitive accuracy for imputing observation-induced missing values.
*   **Improved Downstream Task Performance:** By correctly identifying and preserving meaningfully missing entries instead of inappropriately imputing them, the method prevents data distortion, reduces bias, and leads to improved performance on downstream predictive tasks.
*   **Robust Framework:** Ablation studies confirm that the iterative refinement, joint-state characterization, and uncertainty-aware aggregation are all crucial components contributing to its strong performance.