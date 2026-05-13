# Reconnecting Fragmented Citation Networks with Semantic Augmentation

- **Category:** Artificial Intelligence
- **Date:** 2026-05-12
- **Link:** http://arxiv.org/abs/2605.12263v1

---
This research paper addresses the issue of fragmentation in scientific citation networks and proposes a novel method to enhance their structure and interpretability.

---

### Problem

Citation networks, though fundamental for science mapping, are often fragmented due to missing citation links. This fragmentation arises from factors such as database coverage limitations, unmatched references, time-window truncation, and extraction artifacts. Consequently, these networks exhibit numerous small, disconnected components that may not represent distinct intellectual domains but rather artificial structural isolations. This poses a significant methodological concern as it distorts academic indicators like field delineation, impact normalization, and measures of interdisciplinarity, leading to inaccurate representations of scientific structure. The core question is whether semantic similarity can effectively compensate for these missing citation edges while preserving the inherent interpretability and disciplinary structure of the networks.

### Method

The paper proposes a computationally efficient **hybrid framework** that integrates citation topology with Large Language Model (LLM)-based text similarity.

1.  **Semantic Embedding:** Titles and abstracts of publications are concatenated and encoded using the `mxbai-embed-large` LLM, generating 1024-dimensional vectors. Cosine similarity is used as the measure of semantic proximity.

2.  **Targeted Semantic Augmentation (Two-Step Process):**
    *   **S1: Repair of Small Components:** For nodes identified within small, disconnected clusters from an initial Leiden clustering (baseline), semantic *k*-nearest-neighbor (kNN) edges are added. This focuses on structurally vulnerable regions by connecting publications that are semantically similar but lack citation links. Experiments were conducted with k=10, 100, and 1000.
    *   **S2: Semantic Weighting of Citation Edges:** For *existing* citation edges, the cosine similarity between the textual representations of the citing and cited publications is computed. Each citation edge is then weighted by this semantic similarity, giving more influence to citations between topically related papers and less to semantically weak ones.

3.  **Graph Construction:** The textual edges from S1 are merged with the semantically weighted citation edges from S2, using an optional weighting parameter $\alpha$ (set to 0.5 for primary experiments) to balance their contributions. This results in augmented graphs ($G_{10nn}, G_{100nn}, G_{1000nn}$).

4.  **Community Detection and Comparison:** The Leiden algorithm is re-applied to these augmented graphs. The results are compared against a baseline (Leiden on the original citation graph) and an embedding-only clustering approach (K-means with 2 clusters on the semantic embeddings) based on metrics like cluster count, size distribution, disciplinary homogeneity, and stability.

The method was applied to a dataset of 662,369 Web of Science (WoS) publications in Mathematics and Operations Research & Management Science.

### Impact

The proposed hybrid framework demonstrates several significant impacts:

1.  **Reduced Fragmentation:** Targeted semantic augmentation substantially reduces the number of small, disconnected components in the citation network, effectively "reconnecting" fragmented areas.
2.  **Preserved Disciplinary Homogeneity:** The method successfully maintains high subject homogeneity within clusters (e.g., Mathematics clusters remain nearly 98% Mathematics), indicating that the added semantic links strengthen connections within existing disciplinary boundaries rather than collapsing them.
3.  **Enhanced Interpretability:** Compared to embedding-only clustering (e.g., K-means), the hybrid approach preserves the structural interpretability of the clusters, allowing for a clearer understanding of scientific organization and multi-scale structure.
4.  **Computational Efficiency:** The method is computationally feasible and scales efficiently to large datasets, making it a practical solution for real-world bibliometric analysis.
5.  **Improved Academic Indicators:** By repairing incomplete linkage without distorting disciplinary boundaries, the framework offers a robust strategy for strengthening citation-based indicators, leading to more accurate field delineation, impact normalization, and interdisciplinarity measures in science mapping.