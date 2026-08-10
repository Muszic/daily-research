# H2AL: Hyperbolic Hierarchy-aware Aggregative Learning for Registration-based Few-shot Medical Image Segmentation

- **Category:** Artificial Intelligence
- **Date:** 2026-08-07
- **Link:** http://arxiv.org/abs/2608.07340v1

---
This paper introduces H2AL, a novel framework for Registration-based Few-shot medical image segmentation (RFMIS) that leverages hyperbolic geometry to model anatomical hierarchies and improve segmentation accuracy, particularly for small or ambiguous structures.

---

### Problem

Existing Registration-based Few-shot Medical Image Segmentation (RFMIS) methods primarily operate in Euclidean space, performing pixel-level optimization and treating anatomical structures as flat and disjoint entities. This approach neglects the inherent coarse-to-fine hierarchical organization of anatomical categories (as defined by radiologists), leading to:
1.  **Degraded pseudo-label quality:** Registration fields may fit local intensities but violate global hierarchical anatomical consistency, resulting in inaccurate pseudo-labels for unlabeled images.
2.  **Weakened discrimination:** Ambiguous or small anatomical structures (e.g., those less than 1% volume) are prone to confusion, limiting the segmentation performance.
3.  **Incomplete representation:** While some advanced methods utilize hyperbolic space for hierarchy modeling, they often overlook the rich semantic information available in Euclidean space. Furthermore, none have addressed its potential in the complex dual-task setting of RFMIS, which requires joint optimization of registration and segmentation.

### Method

The proposed **H2AL (Hyperbolic Hierarchy-aware Aggregative Learning)** framework addresses these challenges by enhancing both deformation plausibility and anatomical discrimination through a novel dual-task learning approach. Key components include:

1.  **Hyperbolic Hierarchy-aware Infusion (H2I) Module:** This module integrates hierarchical information from hyperbolic space into Euclidean feature maps while preserving semantic richness.
    *   **Transformation-guided Supervised Hyperbolic Contrastive Learning (TSHCL):** Maps Euclidean embeddings into the Poincaré ball model of hyperbolic space. It employs multi-label supervision (using pseudo-labels from registration) to explicitly guide the formation of a structured embedding space. An adaptive "push-and-pull" mechanism with distance-aware contrastive weights ensures stronger attraction for dissimilar true positive samples and softer repulsion for already distant negatives, yielding more discriminative and hierarchy-aware representations.
    *   **Gated Infusion Block (GIB):** Projects the hierarchy-aware hyperbolic embeddings back to Euclidean space. A gated attention mechanism then modulates the Euclidean features with this hierarchical knowledge, creating task-specific features that are simultaneously semantically discriminative and hierarchically structured.

2.  **End-to-end Joint Optimization with Gradient Aggregation (GA):** Unlike complex, time-consuming two-stage training strategies used in previous RFMIS methods, H2AL utilizes an efficient one-stage, end-to-end training approach.
    *   After task-specific decoder updates, the gradients from both the registration and segmentation decoders (which now embed semantic and hierarchical cues) are aggregated to update a shared encoder. This strategy promotes collaborative learning, enables the encoder to learn features beneficial to both tasks, and ensures stable optimization.

### Impact

H2AL demonstrates significant improvements in RFMIS, particularly for challenging anatomical structures:

1.  **Superior Segmentation Performance:** H2AL achieves state-of-the-art segmentation results across various settings (atlas-based, 1-shot, 5-shot) on both Brain (T1 MRI) and Cardiac (CT) datasets. It consistently outperforms leading few-shot methods like BRBS and Bi-JROS.
2.  **Enhanced Registration Quality:** The framework also improves registration performance, yielding more anatomically plausible deformations.
3.  **Improved Discrimination for Small Structures:** Critically, H2AL addresses the ambiguity of small anatomical structures. For these challenging regions, it improves Dice scores by **1.47%** for registration and **1.84%** for segmentation over the second-best methods.
4.  **Efficient and Robust Training:** The proposed Gradient Aggregation strategy enables efficient one-stage, end-to-end training, promoting synergistic representation learning across registration and segmentation tasks.
5.  **Unified Framework:** H2AL offers a unified solution that effectively leverages both rich Euclidean semantic information and intrinsic hyperbolic anatomical hierarchies, leading to more robust and accurate medical image segmentation. The code is publicly available.