# Clusters are All You Need: Pre-Training the Tsetlin Machine with Semantic Clusters from Language Models for Interpretability

- **Category:** NLP
- **Date:** 2026-06-18
- **Link:** http://arxiv.org/abs/2606.19815v1

---
### Problem

Modern pre-trained language models (e.g., BERT) achieve strong text classification performance but lack transparency, limiting their application in high-stakes domains where interpretability is crucial. Tsetlin Machines (TMs), while inherently interpretable through clause-based reasoning, struggle to incorporate rich, contextual semantic information from these language models. Prior attempts to bridge this gap using static word embeddings (e.g., Word2Vec, GloVe) failed to capture contextual meaning effectively.

### Method

The authors propose a two-stage semantic pre-training framework to transfer knowledge from pre-trained language models (LMs) into a TM while preserving interpretability:

1.  **Semantic Cluster Extraction and Non-Negated TM (NTM) Pre-training:**
    *   Unlabeled text samples are first embedded using a pre-trained language model (BERT-variants or Top2Vec).
    *   These embeddings are then grouped into semantically coherent clusters using K-means (for BERT embeddings) or Top2Vec (for joint document/word vectors).
    *   The resulting cluster-sample pairs are used to pre-train a **Non-Negated Tsetlin Machine (NTM)**. The NTM employs an enhanced Type I feedback mechanism (boosting positive reinforcement) and crucially *disables negated literals* in its clauses, forcing it to learn monotone, interpretable representations for each cluster.
    *   From the pre-trained NTM, high-confidence words or phrases (semantic keywords) are extracted as descriptors for each cluster based on the states of their Tsetlin Automata (TA).

2.  **Fine-tuning with Semantic Keywords:**
    *   For the downstream task, labeled text samples are augmented by enriching their Bag-of-Words (BOW) representation with the pre-trained semantic keywords of their assigned clusters.
    *   This "semantically enriched BOW" is then used to fine-tune a standard Tsetlin Machine (TM), which can reintroduce negated literals for task-specific learning.

### Impact

The proposed method demonstrates significant advancements:

*   **Performance:** It substantially outperforms vanilla TMs and TMs augmented with static embeddings (e.g., GloVe-TM). It achieves performance competitive with state-of-the-art BERT-based models, often within 1-2% accuracy of BERT-large, and in some cases, even surpasses them on specific datasets (e.g., R52).
*   **Interpretability:** The framework successfully transfers semantic knowledge without sacrificing the Tsetlin Machine's inherent interpretability. The learned cluster keywords are explicit and human-understandable, and the fine-tuned TM's decision-making process becomes more transparent and robust due to the semantically enriched input, which can reduce reliance on complex negated features.
*   **Bridging the Gap:** This research offers a promising direction for creating effective and explainable AI models by combining the high performance of modern language models with the transparency of logical reasoning machines, particularly valuable for high-stakes applications.