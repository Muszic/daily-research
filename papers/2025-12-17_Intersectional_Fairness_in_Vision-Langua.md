# Intersectional Fairness in Vision-Language Models for Medical Image Disease Classification

- **Category:** Artificial Intelligence
- **Published:** 2025-12-17
- **Source:** [Original ArXiv Link](http://arxiv.org/abs/2512.15249v1)

---

## 🧐 Problem

Medical artificial intelligence (AI) systems, particularly multimodal Vision-Language Models (VLMs), exhibit significant **intersectional biases**. These models are systematically less confident in diagnosing marginalized patient subgroups, leading to:
*   **Higher rates of inaccurate and missed diagnoses**, exacerbated by demographically skewed training data.
*   **"Certainty gaps"**: Even if aggregate accuracy seems fair, models often show systematic disparities in diagnostic confidence, leaving underrepresented groups in an "uncertainty grey zone" susceptible to misclassification.
*   **Exacerbation of existing health disparities**: AI, when not accounting for population bias, can worsen disparities, as seen in melanoma (racial disparities in survival) and glaucoma (higher prevalence/blindness rates in Black and Hispanic populations).

Current fairness interventions have limitations:
*   They frequently **focus on single demographic attributes** (e.g., race, gender, age in isolation), failing to address the compounding nature of **intersectional biases**.
*   They often lead to a **"levelling down" effect**, achieving statistical parity by degrading overall diagnostic performance for all groups, which is ethically untenable in clinical practice.
*   They fail to directly address the **diagnostic certainty gap** that undermines trust and reliability.

## 🛠️ Method

The authors developed **Cross-Modal Alignment Consistency via Maximum Mean Discrepancy (CMAC-MMD)**, a training framework designed to standardize diagnostic certainty across intersectional patient subgroups.

Here's how CMAC-MMD works:
1.  **Base Architecture:** It builds upon Contrastive Language-Image Pre-training (CLIP) frameworks, utilizing image and text encoders to create shared embeddings.
2.  **Quantifying Diagnostic Certainty (Alignment Score):** For each patient sample, CMAC-MMD computes a scalar "alignment score." This score represents the margin by which the model prefers the *correct* diagnosis over its *most compelling incorrect* alternative. A higher score indicates greater diagnostic confidence, while scores near zero signify uncertainty.
3.  **Enforcing Distributional Fairness:** Instead of debiasing high-dimensional feature representations, CMAC-MMD targets the model's decision-level outputs. Its core premise is that for a model to be fair, the *entire distribution* of these alignment scores must be consistent across all intersectional subgroups.
4.  **Maximum Mean Discrepancy (MMD) Loss:** The framework uses MMD, a kernel-based statistical test, to measure and minimize the distance between the alignment score probability distributions of different intersectional subgroups. This **`LCMAC`** loss penalizes the model when diagnostic certainty distributions differ among groups.
5.  **Total Training Objective:** The final objective combines the standard CLIP contrastive loss (`L_CLIP`) with the CMAC-MMD fairness regularisation term (`λ_CMAC * LCMAC`).

**Key advantages and experimental setup:**
*   **Privacy-Preserving:** During clinical inference, CMAC-MMD **does not require sensitive demographic data** as model input. Demographic attributes are used *only during training* to compute the fairness loss.
*   **Evaluation:** The method was evaluated retrospectively using two clinical domains:
    *   **Dermatology:** 10,015 skin lesion images (HAM10000, with external validation on BCN20000) for intersectional age/gender.
    *   **Ophthalmology:** 10,000 fundus images (Harvard-FairVLMed) for glaucoma detection, considering intersectional age/gender/race.
*   **Comparisons:** CMAC-MMD was compared against standard training (ERM) and seven established fairness interventions, including data-level pre-processing (Resampling, Reweighting), algorithmic in-processing (GroupDRO, Mean Accuracy, DANN, CDANN), and a VLM-specific method (FairCLIP).
*   **Metrics:** Primary endpoints were overall diagnostic performance (Area Under the Curve, AUC) and intersectional fairness (Difference in True Positive Rate, ∆TPR, representing the maximum disparity in sensitivity between any two subgroups).

## 📊 Impact

CMAC-MMD demonstrates a significant leap forward in achieving both accuracy and equity in medical AI systems, particularly VLMs:

*   **Reduced Intersectional Missed Diagnosis Gap:**
    *   In the **dermatology cohort**, the method reduced the overall intersectional missed diagnosis gap (∆TPR) from **0.50 to 0.26** compared to standard training.
    *   For **glaucoma screening**, it reduced ∆TPR from **0.41 to 0.31**.
*   **Improved Overall Diagnostic Performance:**
    *   In **dermatology**, the method improved the overall AUC from **0.94 to 0.97**.
    *   For **glaucoma screening**, it achieved a better AUC of **0.72** (compared to 0.71 baseline).
*   **Enhanced Reliability and Trust:** By standardizing diagnostic certainty across subgroups, CMAC-MMD ensures that marginalized populations receive predictions with equally reliable confidence, addressing the critical "certainty gap" overlooked by previous methods.
*   **Scalability and Privacy:** It establishes a scalable framework for high-stakes clinical decision support systems that can perform equitably across diverse patient subgroups **without requiring sensitive demographic data during clinical inference**, thus preserving patient privacy and easing deployment constraints.
*   **Addresses Limitations of Prior Work:** Unlike many existing fairness interventions, CMAC-MMD avoids "levelling down" effects and directly tackles intersectional biases by ensuring consistent certainty distributions, rather than just balancing average outcomes.

This work paves the way for the development of more trustworthy, accurate, and equitable medical AI tools that can genuinely reduce health disparities in diverse patient populations.
