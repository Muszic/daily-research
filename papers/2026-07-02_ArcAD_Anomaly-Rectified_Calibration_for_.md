# ArcAD: Anomaly-Rectified Calibration for Cold-Start Supervised Anomaly Detection

- **Category:** Computer Vision
- **Date:** 2026-07-02
- **Link:** http://arxiv.org/abs/2607.02252v1

---
## ArcAD: Anomaly-Rectified Calibration for Cold-Start Supervised Anomaly Detection

### Problem

Industrial Anomaly Detection (IAD) faces a critical **cold-start bottleneck** during real-world manufacturing deployment. This scenario is characterized by:
*   **Limited Normal Samples:** The available normal data is insufficient to represent the full normal distribution.
*   **Scarce Anomalies:** Only a few anomaly samples are collected during early system deployment.

Under these conditions, existing methods struggle:
*   **Unsupervised methods:** Form loose and imprecise normal boundaries, leading to poor detection performance and underutilization of valuable anomaly signals.
*   **Supervised methods:** Prone to overfitting to the few available anomalies, resulting in poor generalization to unseen defect patterns.

The core challenge is: **How to leverage limited normal samples and rare anomalies to construct a compact and discriminative normal boundary?**

### Method

ArcAD proposes an **Anomaly-Rectified Cold-start AD (ArcAD)**, a **plug-and-play calibration framework** designed to enhance reconstruction-based IAD baselines without modifying their core architecture. It operates in the latent space following a **push-pull learning paradigm** to build a compact and discriminative normal boundary.

The framework consists of two core components:

1.  **Sinkhorn-based Prototype Modeling (SPM):**
    *   **Goal:** To organize limited normal samples into multiple compact and uniformly distributed clusters on a hypersphere, thereby maximizing coverage of the normal manifold.
    *   **Mechanism:**
        *   **Hypersphere Projection:** Latent patch features are projected onto a **unit hypersphere** via L2 normalization, allowing them to be modeled by the **von Mises-Fisher (vMF) distribution**. This provides a compact, bounded geometric representation.
        *   **Sinkhorn-based Clustering:** Formulates feature-to-prototype assignment as a **balanced optimal transport problem**. This uses the iterative Sinkhorn-Knopp algorithm to learn **multiple normal prototypes** while ensuring uniform mass assignment, preventing prototypes from collapsing into dense regions and guaranteeing comprehensive manifold coverage.
    *   **Loss:** `L_spm` (cross-entropy).

2.  **Defect-Guided Calibration (DGC):**
    *   **Goal:** To explicitly rectify the normal boundary using anomaly signals, pushing it inward and sharpening anomaly discrimination.
    *   **Mechanism:**
        *   **Prototype-Restricted Anomaly Synthesis:** Generates synthetic anomalies directly on the hypersphere by filtering candidate samples against the learned normal prototypes, addressing the scarcity of real anomalies.
        *   **Contrastive Calibration:** Leverages both real and synthesized anomalies with a **contrastive objective**. This objective pulls anomalies together while simultaneously pushing them away from their nearest normal prototypes, reinforcing the compactness and discriminative power of the normal manifold.
    *   **Loss:** `L_dgc` (contrastive, inferred from description).

### Impact

ArcAD significantly improves the performance of Industrial Anomaly Detection in cold-start scenarios:
*   **Superior Performance:** Consistently and significantly **outperforms state-of-the-art supervised and unsupervised methods** in both single-class and multi-class settings under cold-start conditions.
*   **Broad Applicability:** Serves as a **generic, plug-and-play calibration framework** that enhances various reconstruction-based baselines (e.g., ReContrast, RD4AD, Dinomaly).
*   **Quantitative Gains:** Achieves notable performance improvements on challenging datasets:
    *   On the **Real-IAD dataset** (multi-class setting), ArcAD achieved **Image-level AUROC gains of +2.2%, +8.9%, and +3.7%** for ReContrast, RD4AD, and Dinomaly models, respectively.
*   **Robustness & Generalization:** Forms compact and unified boundaries, mitigating overfitting to known anomalies and improving generalization to unseen defect patterns.
*   **Empirical Validation:** Extensively validated through experiments on four standard datasets: MVTec-AD, VisA, Real-IAD, and MANTA.
*   **Reproducibility:** Code is publicly available on GitHub.