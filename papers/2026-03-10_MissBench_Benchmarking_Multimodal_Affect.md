# MissBench: Benchmarking Multimodal Affective Analysis under Imbalanced Missing Modalities

- **Category:** Computer Vision
- **Date:** 2026-03-10
- **Link:** http://arxiv.org/abs/2603.09874v1

---
## MissBench: Benchmarking Multimodal Affective Analysis under Imbalanced Missing Modalities

### Problem

Standard evaluations in multimodal affective computing (e.g., sentiment analysis, emotion recognition) often assume that all modalities (textual, acoustic, visual) are equally available or missing randomly. However, in real-world applications, some modalities are systematically more fragile or expensive, leading to **imbalanced missing rates (IMR)**. This creates training biases and unequal modality contributions that task-level metrics (e.g., accuracy, F1-score) alone fail to reveal. Existing benchmarks lack systematic protocols to simulate IMR and provide diagnostics beyond overall performance, thus hindering the development of truly robust models for incomplete-modality settings.

### Method

The authors introduce **MissBench**, a benchmark and framework designed to standardize the evaluation of multimodal affective models under both shared and imbalanced missing modalities.

1.  **Missingness Protocols:** MissBench standardizes two protocols on four widely used sentiment and emotion datasets (CMU-MOSI, CMU-MOSEI, IEMOCAP, CH-SIMS):
    *   **Shared Missing Rate (SMR):** All modalities share the same missing probability.
    *   **Imbalanced Missing Rate (IMR):** Each modality is assigned a heterogeneous missing probability, reflecting real-world scenarios.
2.  **Diagnostic Metrics:** Beyond conventional task metrics, MissBench introduces two novel diagnostic measures:
    *   **Modality Equity Index (MEI):** Quantifies how evenly different modalities contribute to predictive performance across various missing-modality configurations. A higher MEI indicates more balanced modality contribution.
    *   **Modality Learning Index (MLI):** Measures optimization imbalance by comparing modality-specific gradient magnitudes during training, aggregated across modality-related modules. A lower MLI indicates more consistent and balanced temporal updates across modalities.
3.  **Unified Pipeline:** MissBench provides a standardized evaluation pipeline, including fixed data splits, masking seeds, training parameters (optimizer, batch size, epochs), and a simple model plugin interface. This ensures fair and reproducible comparisons, logging necessary statistics for MEI and MLI computation.

### Impact

MissBench, combined with MEI and MLI, provides critical insights into model behavior under realistic incomplete-modality conditions:

*   **Revealing Hidden Biases:** Experiments on representative model families demonstrate that models appearing robust under SMR can still exhibit marked modality inequity (low MEI) and optimization imbalance (high MLI) when evaluated under IMR.
*   **Performance Degradation under IMR:** Even when the *average missing rate* is matched between SMR and IMR conditions, models consistently show degraded task performance under IMR, highlighting its challenging nature.
*   **Enhanced Model Analysis:** MEI and MLI successfully diagnose which modalities are disadvantaged or dominate the learning process, providing a deeper understanding of model strengths and weaknesses beyond aggregate performance scores.
*   **Practical Tool for Development:** MissBench positions itself as a practical tool for stress-testing and analyzing multimodal affective models, guiding the development of more equitable and robust architectures for real-world applications where imbalanced missing data are prevalent.
*   **Reproducibility:** The code release ensures the reproducibility of the benchmark and its findings.