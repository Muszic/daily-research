# Improving LLM-based Recommendation with Self-Hard Negatives from Intermediate Layers

- **Category:** Artificial Intelligence
- **Date:** 2026-02-19
- **Link:** http://arxiv.org/abs/2602.17410v1

---
Here's a summary of the research paper "Improving LLM-based Recommendation with Self-Hard Negatives from Intermediate Layers" structured into Problem, Method, and Impact:

---

### Problem

Existing Large Language Model (LLM)-based recommendation systems, which often use supervised fine-tuning (SFT) and preference learning with negative samples, face several challenges:

1.  **Indiscriminative and Coarse-Grained Negatives:** Current methods rely on a small number of *sequence-level* or *offline-generated* negative items. This provides sparse and coarse-grained reward signals, making it difficult for LLMs to capture fine-grained *token-level* patterns and nuanced user preferences, especially given the vast item spaces in recommendation tasks.
2.  **Uninformative and Stale Negatives:** Negative samples are typically collected offline or from outdated policy models. These fail to dynamically reflect the LLM's current learning process, often becoming uninformative or easy to distinguish due to distributional shifts, thus hindering the model's ability to learn from truly "hard" negatives.
3.  **Inefficiency:** Integrating additional preference alignment stages and repeatedly sampling large pools of negative examples introduces significant computational overhead, slowing down the LLM adaptation process.

### Method

The paper proposes **ILRec**, a novel preference fine-tuning framework that addresses these limitations by leveraging self-hard negative signals extracted dynamically from the LLM's intermediate layers. ILRec consists of three main components:

1.  **Self-Hard Negative Extraction from Intermediate Layers:**
    *   The core idea is to treat intermediate LLM layers as "non-expert models" that can dynamically generate appropriately hard negatives during training.
    *   It extracts *token-level* self-hard negative signals from the *ensemble logits* of selected intermediate layers.
    *   High-probability tokens (excluding the ground-truth token) are selected as negatives using a dynamic threshold, enabling fine-grained comparison within the large candidate item space.
2.  **Cross-Layer Preference Fine-tuning:** This component optimizes both the generation and utilization of negative signals.
    *   **Cross-Layer Preference Optimization (CPO):** Integrates the extracted token-level self-hard negative signals as fine-grained penalty coefficients into the cross-entropy loss. This mechanism penalizes more challenging negative tokens (those the final layer still predicts with high probability), guiding the model to better discriminate them.
    *   **Cross-Layer Preference Distillation (CPD):** Employs the final output layer as a "teacher" to supervise the token generation probabilities of intermediate layers ("students") via KL divergence. This ensures that the intermediate layers quickly adapt to the recommendation task and provide more informative and reliable negative signals.
3.  **Collaborative Reward Regularization:**
    *   To mitigate the risk of over-penalizing potential false negatives and to inject collaborative information, a lightweight Collaborative Filtering (CF) model is introduced.
    *   This CF model assigns token-level reward scores to penalized tokens. These rewards are then used as soft labels in an additional cross-entropy loss term, reducing the penalty for tokens that are collaboratively highly relevant.

### Impact

ILRec significantly enhances the performance of LLM-based recommender systems:

*   **Superior Performance:** Extensive experiments on three real-world datasets (Amazon Review Data: Musical Instruments, Arts, Crafts and Sewing, Video Games) consistently demonstrate that ILRec surpasses both traditional sequential recommendation models (e.g., Caser, GRU4Rec, SASRec) and existing LLM-based recommendation methods (e.g., BIGRec, LC-Rec, and DPO-based methods like SDPO, RosePO, SPRec) across various evaluation metrics (Hit@K, NDCG@K).
*   **More Discriminative and Informative Learning:** By dynamically extracting fine-grained, token-level, self-hard negatives from intermediate layers, ILRec enables LLMs to learn more nuanced user preferences and better distinguish between positive and challenging negative items within large candidate spaces.
*   **Efficient Preference Alignment:** The integration of negative signal extraction and utilization within a single fine-tuning process (SFT) eliminates the need for external negative samples or iterative training stages, making the adaptation of LLMs for recommendation tasks more efficient.