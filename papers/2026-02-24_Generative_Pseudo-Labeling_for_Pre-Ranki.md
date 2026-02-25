# Generative Pseudo-Labeling for Pre-Ranking with LLMs

- **Category:** NLP
- **Date:** 2026-02-24
- **Link:** http://arxiv.org/abs/2602.20995v1

---
Here's a summary of the research paper in Markdown format:

---

## Generative Pseudo-Labeling for Pre-Ranking with LLMs

### Problem

Industrial recommendation systems face a critical challenge in the **pre-ranking stage**: a severe **train-serving discrepancy**. Pre-ranking models are trained exclusively on *exposed interactions* (items users actually saw and interacted with), but at serving time, they must score *all recalled candidates*, including a large proportion of *unexposed items* that lack feedback. This mismatch leads to:

1.  **Sample Selection Bias (SSB):** Models learn from a biased subset of data.
2.  **Degraded Generalization:** Poor performance on unexposed, novel, or long-tail items.
3.  **Reduced Diversity:** Over-recommendation of popular content, reinforcing information cocoons.

Existing debiasing approaches fall short: negative sampling mislabels plausible unexposed items, knowledge distillation from biased rankers propagates exposure bias, and randomized content delivery is costly and risks user experience.

### Method

The paper proposes **Generative Pseudo-Labeling (GPL)**, a two-stage framework that leverages Large Language Models (LLMs) to generate unbiased, content-aware pseudo-labels for unexposed items, aligning the training distribution with the online serving space.

1.  **Offline Pseudo-Label Generation:**
    *   **Tokenization of User Behaviors:** Items are tokenized into hierarchical **Semantic Identifiers (SIDs)** using a *frozen pre-trained multimodal encoder* (fusing text/visual features) and a *Residual Quantized VAE (RQ-VAE)*. This ensures SIDs are grounded purely in content, decoupled from biased interaction history.
    *   **Interest-Anchors Generation:** A pre-trained LLM (e.g., Qwen2.5-0.5B) is fine-tuned with Low-Rank Adaptation (LoRA) on sequences of positively interacted SIDs, with frequency-based downsampling for popular items to mitigate popularity bias. The LLM predicts future SIDs (interest anchors) via hierarchical beam search, representing diverse potential user interests.
    *   **Representation Alignment & Matching:** The generated interest-anchors and unexposed candidate items are projected into a shared semantic space using the *frozen multimodal encoder*. Relevance scores are computed as the max-pooled cosine similarity between the candidate item and the set of user's interest anchors.
    *   **Uncertainty Quantification:** Pseudo-labels are calibrated by confidence weights based on three factors: **Semantic Dispersion** (consistency among generated anchors), **Historical Consistency** (alignment with user's past behaviors), and **LLM-Intrinsic Confidence** (generation probability).

2.  **Dual-Label Fusion for Pre-ranker Training:**
    *   A lightweight pre-ranking model is trained with a unified objective combining standard Binary Cross-Entropy (BCE) for observed interactions (actual labels) and a **confidence-weighted BCE** for the LLM-generated pseudo-labels of unexposed items.
    *   Crucially, **all LLM inference and pseudo-label generation are performed entirely offline and cached per user**, ensuring **zero latency overhead** during online serving. This is optimized by generating user-level interest anchors once per user request, rather than per candidate.

### Impact

GPL has been deployed in a large-scale industrial recommendation system (Alibaba Group) and demonstrated significant improvements:

*   **Click-Through Rate (CTR):** Increased by **3.07%** in online A/B testing.
*   **Recommendation Diversity:** Significantly enhanced.
*   **Long-tail Item Discovery:** Significantly enhanced, alleviating long-tail distribution bias.
*   **Generalization:** Enables robust generalization to unexposed and long-tail items.
*   **Practicality:** Provides high-quality, content-aware supervision without adding online latency, seamlessly integrating into existing pre-ranking pipelines.
*   **Offline Efficiency:** Achieves pseudo-label generation for one day's user traffic within six hours on a dedicated GPU cluster (96 NVIDIA H20 GPUs).