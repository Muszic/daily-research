# MRG-R1: Reinforcement Learning for Clinically Aligned Medical Report Generation

- **Category:** NLP
- **Published:** 2025-12-18
- **Source:** [Original ArXiv Link](http://arxiv.org/abs/2512.16145v1)

---

## 🧐 Problem

Existing Medical Report Generation (MRG) methods, primarily trained on **token-level objectives** (e.g., cross-entropy loss), often produce text that mimics a radiologist's linguistic style but **fails to guarantee clinical correctness**. This focus on word choice and sentence structure, rather than actual medical accuracy, leads to:
*   **Semantic inconsistencies**: Reports may *look* fluent but contain factual errors (e.g., confusing "no pneumothorax" with "small pneumothorax").
*   **Hallucinations and incomplete coverage**: Models generate plausible but unsupported statements or miss critical findings.
*   **Underconstrained clinical correctness**: The training paradigm does not enforce report-level clinical accuracy directly.

While some prior work incorporates semantic supervision (e.g., contrastive learning, multi-task learning), these methods often provide **indirect signals** (global alignment, coarse/noisy labels, proxy curricula) that do not directly address polarity-sensitive, report-level clinical correctness. There's a clear need for objectives that directly optimize medical accuracy during report generation.

## 🛠️ Method

The authors propose **MRG-R1**, a **semantic-driven reinforcement learning (SRL)** method for medical report generation, implemented on a **medical Large Vision-Language Model (Med-LVLM)**. The core idea is to shift supervision from token-level likelihood to a clinically grounded, report-level reward.

Key components of MRG-R1:

1.  **Med-LVLM as a Policy**: The pre-trained Med-LVLM (specifically, fine-tuning HuatuoGPT-Vision-7B-Qwen2.5VL using LoRA) is treated as a policy that generates full radiology reports.
2.  **Group Relative Policy Optimization (GRPO)**: SRL adopts GRPO for stable and compute-efficient policy updates. For each medical image (study):
    *   The current policy samples a group of **multiple candidate reports**.
    *   **Group-relative advantages** are computed by normalizing rewards *within* this sampled group, sharpening the learning signal without needing a learned value function or critic.
    *   The policy is updated based on these advantages and a Kullback–Leibler (KL) divergence constraint to a reference policy, preventing policy drift.
3.  **Clinically Grounded Report-Level Rewards**:
    *   **Margin CheXbert Cosine Similarity (MCCS) Reward**: This is the primary clinical reward.
        *   It leverages **CheXbert** (a BERT-based automatic labeler) to extract 14 standard chest X-ray observations (e.g., Atelectasis, Pneumothorax) from both generated and reference reports.
        *   These observations are mapped into **signed vectors** (e.g., positive finding = 1, negative = -1, uncertain = 1, blank = 0) for 13 disease-specific categories (excluding "No Finding" to reduce noise).
        *   A **cosine similarity** is computed between these signed vectors.
        *   The similarity is then converted to a **margin-shaped reward** (`max((CCS - m)/(1 - m), 0)`), which:
            *   **Filters weak alignments** (scores below margin `m` yield zero reward).
            *   **Normalizes the dynamic range** to [0, 1].
            *   Provides **stable, interpretable gradients**, strongly rewarding accurate coverage and correct polarity, while penalizing unsupported or contradictory statements.
    *   **Lightweight Format Reward**: Encourages the model to generate structured "thinking → report" outputs (e.g., `<think>...</think> → <report>...</report>`). A rule-based scorer assigns a reward based on structural compliance, improving interpretability and auditability.
4.  **Combined Reward**: The total reward for GRPO is a weighted sum of the MCCS (0.75) and format (0.25) terms, ensuring clinical correctness remains the primary driver.

## 📊 Impact

MRG-R1 demonstrates **state-of-the-art performance** and significantly improves the clinical correctness of generated medical reports, addressing a critical limitation of previous token-level supervision methods.

*   **Quantitative Superiority**:
    *   Achieved **CE-F1 51.88 on IU X-Ray** and **40.39 on MIMIC-CXR**, setting new state-of-the-art benchmarks on IU X-Ray and being highly competitive on MIMIC-CXR.
    *   Outperformed classical token-level MLE generators (e.g., R2GenCMN) and significantly surpassed many instruction-tuned or generalist LVLMs (e.g., LLaVA-Med, BioMedGPT) in **Clinical Efficacy (CE)** metrics.
    *   Showed balanced improvements in both precision and recall, indicating enhanced sensitivity to clinically salient findings and a low rate of false positives.
*   **Qualitative Improvements**:
    *   Generated reports exhibit superior **polarity handling** (accurately stating presence/absence of abnormalities), **uncertainty handling**, and a better balance between **omissions and hallucinations**.
    *   Produced structurally coherent reports following the `think → report` format, aiding readability and auditability.
    *   Qualitative examples show MRG-R1 correcting errors made by baselines, such as hallucinating conditions (e.g., MedGemma-4B hallucinating cardiomegaly) or omitting critical findings.
*   **Validation of Semantic Reinforcement**:
    *   Ablation studies confirmed that the **label-semantic reinforcement is superior to conventional token-level supervision**, with purely lexical NLG rewards yielding limited clinical efficacy.
    *   The **MCCS reward proved to be the most effective shaping** mechanism, significantly outperforming a simple CE-F1 reward by providing polarity-sensitive, margin-calibrated, and continuous clinical signals.

This work marks a significant advancement in MRG by explicitly optimizing for clinical correctness at the report level, paving the way for more reliable and clinically aligned medical report generation using Med-LVLMs. It pioneers the exploration of semantic reinforcement in supervising medical correctness in Med-LVLM training.
