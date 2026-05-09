# From Token Lists to Graph Motifs: Weisfeiler-Lehman Analysis of Sparse Autoencoder Features

- **Category:** Artificial Intelligence
- **Date:** 2026-05-07
- **Link:** http://arxiv.org/abs/2605.06494v1

---
Here's a summary of the research paper in Markdown:

### Problem

Existing analyses of Sparse Autoencoder (SAE) features in large language models (LLMs) primarily rely on examining top-activating token lists or decoder weight vectors. This approach fails to capture the "higher-order co-occurrence structure" and shared structural motifs among features, making it challenging to systematically organize and compare large dictionaries of features beyond individual descriptions.

### Method

1.  **Graph Representation:** Each SAE feature is represented as a "token co-occurrence graph."
    *   **Nodes:** The tokens most frequently appearing near strong activations of a given feature.
    *   **Edges:** Connect pairs of tokens that co-occur within local context windows when the feature is active. Edge weights are based on co-occurrence counts.
    *   **Node Labels:** Derived from log-scaled, binned co-occurrence frequencies to reflect activation strength rather than raw token identity.
2.  **Similarity Measure:** A "custom WL-style, frequency-binned graph kernel" is introduced to compute similarity between these feature graphs. This kernel iteratively refines node labels by aggregating weighted neighbor information and binning, differing from the canonical Weisfeiler-Lehman (WL) subtree kernel in label initialization, refinement, and final kernel computation.
3.  **Clustering & Analysis:** The graph kernel is used to build a similarity matrix, which is then embedded into a low-dimensional space via Kernel PCA. K-means clustering is applied in this space to group features.
4.  **Evaluation:** Clusters are benchmarked against baselines (decoder cosine similarity and token-histogram cosine similarity) using a heuristic "token-type purity" metric (categorizing tokens as symbolic, alphabetic, numeric, or mixed) to assess if they align with interpretable structural families.
5.  **Data:** The method is applied as a proof of concept to features from an SAE (6-RES-JB) trained on GPT-2 Small, probed with a synthetic mixed-domain corpus designed to elicit varied surface motifs.

### Impact

*   **Discovery of Structural Motifs:** The graph-based clustering successfully recovers "heuristic motif families" such as punctuation-heavy patterns, language and script clusters, and code-like templates, which are *not* identified by clustering on decoder cosine similarity.
*   **Complementary View:** The graph view provides a valuable *complementary* perspective. While a token-histogram baseline achieved higher overall purity (0.854 vs. 0.760 for WL-style), the WL-style kernel significantly outperformed decoder cosine similarity in capturing specific structural patterns, notably achieving an alphabetic purity of 0.516 compared to 0.000 for decoder cosine. This indicates its unique ability to surface structural relationships beyond marginal token frequencies and decoder weights.
*   **Robustness:** The cluster assignments demonstrate stability across various graph-construction hyperparameters and random seeds, suggesting the reliability of the method.
*   **Advancement in Interpretability:** This work introduces a novel and systematic method for organizing and comparing SAE features by their higher-order co-occurrence structure, enriching the tools available for mechanistic interpretability by moving beyond isolated token lists.