# CAN We Trust Your Results? A Cross-Dataset Study of Automotive IDS Evaluation

- **Category:** Cryptography
- **Date:** 2026-06-29
- **Link:** http://arxiv.org/abs/2606.30430v1

---
Here's a summary of the research paper using the Markdown format (Problem, Method, Impact):

---

## Problem

The evaluation of Intrusion Detection Systems (IDS) for Controller Area Network (CAN) buses in modern vehicles is critically challenged by several factors:
*   **Inconsistent Experimental Setups:** A lack of standardized benchmarking frameworks and methodologies makes it difficult to reliably assess and compare the effectiveness of proposed CAN IDS approaches.
*   **Dataset-Specific Performance:** Reported IDS performance often depends heavily on proprietary or uniquely collected datasets, leading to results that are not reproducible, comparable across studies, or indicative of real-world generalization capabilities. This is exacerbated by dataset bias and data drift where models rely on environment-specific artifacts rather than underlying malicious behavior.
*   **Limited Generalization Studies:** Most existing benchmark studies focus on testing multiple IDS approaches on a single dataset, failing to reveal whether detection methods generalize across different vehicle environments, attack scenarios, or data collection setups.
*   **Reproducibility Issues:** Difficulty in reproducing prior work due to limited availability of implementation details, source code, and even instances of incorrect reported evaluation metrics (as identified by the authors with a widely cited paper).

These issues mean that current evaluations may not accurately reflect how IDS methods behave in diverse operational environments, hindering the adoption of state-of-the-art solutions and fair comparison.

## Method

The authors address these problems by introducing a **unified benchmarking framework** for consistent and reproducible evaluation of CAN IDS methods across multiple datasets.
The framework's core components are:
1.  **Unified Dataset Representation:** Normalizes heterogeneous CAN datasets (raw logs, structured tabular, signal-level, synthetic) into a common format.
2.  **Common IDS Interface:** Enables the integration of different detection approaches, regardless of their internal mechanisms.
3.  **Uniform Evaluation Protocol:** Ensures fair comparison between diverse detection outputs (binary classification vs. continuous anomaly scores, message-level vs. time-window aggregation) using threshold-independent metrics like ROC-AUC, and imbalance-robust metrics such as Balanced Accuracy (bACC), F1-score (F1), and Matthews Correlation Coefficient (MCC).

Using this framework, the study performs a comprehensive cross-dataset evaluation:
*   **Datasets:** Seven publicly available CAN IDS datasets, collected under different experimental conditions, from various vehicle platforms (e.g., Kia Soul, Volvo V40, Opel Astra, Renault Clio, ROAD, In-Vehicle CAN Dataset, Ventus, SYN-CAN) and including diverse attack scenarios (fabrication, suspension, masquerade attacks), were integrated.
*   **IDS Approaches:** Five conceptually different IDS methods, representing various detection principles (message ordering, statistical properties, signal relationships, temporal behavior), were implemented and evaluated:
    *   **FlowN-Gram:** A sequence-based flow analysis method.
    *   **MBA-OCSVM:** A machine learning-based anomaly detector using One-Class SVM.
    *   **AssocRules:** An association-rule-based method modeling vehicle state through message correlations.
    *   **CANShield-CNN-AE:** A deep learning-based signal-level convolutional autoencoder.
    *   **CANet-LSTM-AE:** An LSTM-based signal reconstruction method.

The evaluation specifically investigates how detection performance varies across datasets, whether relative IDS rankings remain stable, and if single-dataset results can reliably predict performance on other datasets.

## Impact

The research provides significant impact in advancing the evaluation of automotive IDSs:
*   **Highlights Performance Variability:** The cross-dataset evaluation clearly demonstrates that **IDS detection performance can vary significantly across different CAN intrusion datasets**. This confirms that results obtained on a single dataset may not reliably predict IDS performance in other environments.
*   **Establishes a Robust Benchmarking Standard:** The proposed framework offers a **reproducible and consistent methodology** for evaluating CAN IDS methods, addressing a critical gap in standardization and facilitating fair comparison of future work.
*   **Enables Generalization Assessment:** By performing cross-dataset evaluation, the work establishes a crucial precedent for **assessing the robustness and generalization capabilities** of CAN IDS methods, moving beyond dataset-specific performance claims.
*   **Enhances Trust in Results:** The framework helps overcome challenges related to reproducibility and clarifies the interpretation of evaluation results, as exemplified by the authors' identification and public reporting of inconsistencies in a previously published work's metrics.
*   **Informs IDS Development:** The findings provide valuable insights for IDS developers, emphasizing the need to consider diverse data sources and testing environments during design and validation to ensure real-world applicability and resilience against various attack types and vehicle configurations.

In essence, the study argues that trusting IDS evaluation results requires moving beyond single-dataset experiments and adopting a robust, cross-dataset benchmarking approach, which their framework enables.

---