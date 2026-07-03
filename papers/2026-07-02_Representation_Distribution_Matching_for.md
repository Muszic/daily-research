# Representation Distribution Matching for One-Step Visual Generation

- **Category:** Computer Vision
- **Date:** 2026-07-02
- **Link:** http://arxiv.org/abs/2607.02375v1

---
Here's a summary of the research paper in Markdown format:

## Problem

Traditional generative models like diffusion and flow models are inherently multi-step, leading to high inference costs and latency. While one-step generators exist, the design choices underlying their effectiveness (how distributions are compared and which representations are used) are often fixed jointly, obscuring what truly drives quality. Specific challenges include:
1.  **Ineffective Distribution Matching:** Classical Maximum Mean Discrepancy (MMD) was previously dismissed as too weak for training competitive generators.
2.  **Suboptimal Batch Sizes:** Current practices use batch sizes far too small for accurate distribution estimation, leading to noisy gradients.
3.  **Gaming Single Representations:** Generators can "game" individual pretrained encoders, achieving low scores (better than real data) while producing visibly fake images, indicating a lack of true realism.
4.  **Lack of Prompt Fidelity:** For conditional generation (e.g., text-to-image), models might achieve realism but drift from the given prompts if only the image marginal is matched.

## Method

The authors propose **Representation Distribution Matching (RDM)**, a paradigm for training one-step image generators by explicitly matching generated and reference feature distributions under frozen pretrained encoders, without an online teacher or adversary. They explore two key design axes:

1.  **The Comparison Axis (How distributions are compared):**
    *   **MMD Reassessment:** They revive the Maximum Mean Discrepancy (MMD) as a strong objective, arguing it was previously "badly estimated."
    *   **Improved MMD Estimation:**
        *   **Exact Within-Batch Repulsion:** The generator term (repulsion) is estimated exactly within each generated batch to prevent mode collapse.
        *   **Frozen Nyström Attraction:** The attraction term compares generated samples against a *precomputed, frozen Nyström kernel mean embedding* of the *entire 1.28M-image training set* (using 4096 landmarks). This provides a stable, low-variance reference, unlike noisy per-batch references.
    *   **Large, Fresh Generation Batches:** They identify that optimal batch sizes are above 2048 (e.g., 5120 for ImageNet, 10240 for FLUX post-training) for sharper estimates, enabled by gradient caching.
    *   **Joint Image-Text Objective:** For conditional tasks, they match the *joint law* of image and text features (using a concatenated representation $\Phi(x, c) = \phi(x) \oplus \tau(c)$), ensuring prompt fidelity alongside image realism.

2.  **The Representation Axis (Which encoders define the feature spaces):**
    *   **Diverse Encoder Battery:** To prevent gaming, they match distributions against a diverse battery of pretrained encoders (e.g., 10 for training). They demonstrate that a single encoder (even a strong one like DINOv2) can be overfit, leading to fake images achieving "real" scores.
    *   **Adaptive Weighting:** Instead of uniform weighting, a *proportional Lagrangian controller* adaptively upweights encoders that are hardest to satisfy and downweights those the generator is starting to overfit, following a "weakest-stave rule."
    *   **Evaluation Metric (SW_r14):** They introduce and evaluate with SW_r14, a Sliced-Wasserstein distance averaged over 14 diverse pretrained encoders, which is independent of the training loss and resists gaming.

Combining these preferred choices yields **improved RDM (iRDM)**, a simple yet effective recipe for one-step generation.

## Impact

The proposed iRDM framework delivers significant advancements:

1.  **State-of-the-Art One-Step Generation:**
    *   Achieves a new one-step state of the art on ImageNet at **SW_r14 1.30** (where real data scores 1.00).
    *   Corroborated by a human-preference proxy, achieving a **71.2% PickScore win rate** over the prior best one-step generator (pMF-H FD-SIM).

2.  **Efficient Post-training of Multi-step Models:**
    *   Successfully post-trains the four-step FLUX.2 [klein] into a *one-step generator* in only **90 H200 GPU-hours**.
    *   The resulting one-step model *surpasses* the original four-step version on both GenEval (**0.826 to 0.794**) and PickScore (**22.76 to 22.58**), demonstrating superior quality and efficiency.

3.  **Unified Framework & Fundamental Insights:**
    *   Formalizes RDM, providing a unifying framework that clarifies the design space of one-step generators and allows attributing quality ceilings to specific design choices.
    *   Overturns prior assumptions about MMD's weakness and optimal batch sizes, highlighting the effectiveness of explicit distribution matching with careful estimation.

4.  **Robust Evaluation Metric:**
    *   Introduces SW_r14, a robust evaluation metric that is harder to game than single-encoder scores (like FID) and independent of the training loss, providing more reliable quality assessment.