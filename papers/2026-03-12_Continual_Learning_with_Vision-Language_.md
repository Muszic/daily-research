# Continual Learning with Vision-Language Models via Semantic-Geometry Preservation

- **Category:** Computer Vision
- **Date:** 2026-03-12
- **Link:** http://arxiv.org/abs/2603.12055v1

---
Here's a summary of the research paper "Continual Learning with Vision-Language Models via Semantic-Geometry Preservation" in Markdown:

---

### Problem

Continual learning (CL) with pretrained Vision-Language Models (VLMs) like CLIP suffers from catastrophic forgetting. Existing approaches adapt to new tasks without explicitly preserving the intricate cross-modal semantic geometry inherited from pretraining and previous tasks. This oversight allows new-task supervision to induce significant geometric distortion, leading to forgetting. The most pronounced drift occurs in "vulnerable neighborhoods" near the old-new semantic interface, where shared visual patterns can be easily re-explained by new textual semantics, especially challenging under exemplar-free constraints (no old data available).

### Method

The proposed **Semantic Geometry Preservation for Continual Learning (SeGP-CL)** addresses these challenges through a three-pronged approach:

1.  **Anchor Construction (Probing Drift-Prone Regions):**
    *   **Dual-targeted Projected Gradient Descent (DPGD):** Generates a compact set of adversarial anchors. It perturbs new-task seed samples to push their visual features towards old-class semantics in the VLM's embedding space (text-targeted) while simultaneously constraining them to remain close to the corresponding old raw-space visual prototypes (visual anchoring). This ensures anchors effectively probe the vulnerable old-new semantic interface and remain visually faithful despite the modality gap.

2.  **Semantic Geometry Preservation (During Training):**
    *   **Anchor-guided Cross-modal Geometry Distillation (ACGD):** Applies knowledge distillation on the generated adversarial anchors. It minimizes the KL divergence between the teacher VLM's (frozen from the previous task) old-class similarity distribution and the student VLM's distribution, effectively preserving the established cross-modal structure in the drift-prone regions.
    *   **Text Semantic-Geometry Regularization (TSGR):** Stabilizes the textual semantic "reference frame" across tasks. It uses a fixed reference textual encoder (e.g., by resetting LoRA parameters) to define a consistent relational subgraph (k-nearest neighbors) for new classes. TSGR then regularizes the student text encoder to match this stable relational structure, preventing distortion of the relative geometry among textual concepts.

3.  **Post-Training Enhancement (After Training):**
    *   **Anchor-induced Prototype Transfer:** Estimates the raw-space drift of old visual prototypes. After training, it measures the discrepancy in raw visual features of the adversarial anchors between the teacher and the updated student model. These anchor-induced variations are used to update (transfer) the old-class prototypes, keeping the raw-space decision reference consistent with the adapted visual encoder, all in an exemplar-free manner.
    *   **Dual-path Prediction:** Combines complementary decision signals during inference. It fuses the cross-modal matching scores from the VLM's CLIP branch with the raw-space prototype scores from the visual branch. This leverages both high-level semantic alignment and discriminative raw visual patterns, improving robust inference, especially in the presence of the modality gap.

### Impact

SeGP-CL consistently achieves state-of-the-art performance across five continual learning benchmarks. It demonstrates significant improvements in both stability (mitigating catastrophic forgetting) and forward transfer (effectively learning new tasks). Crucially, the method is shown to better preserve the cross-modal semantic geometry of VLMs, validating the core hypothesis that explicit geometric preservation is key to effective VLM-based continual learning.

---