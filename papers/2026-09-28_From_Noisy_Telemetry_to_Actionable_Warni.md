# From Noisy Telemetry to Actionable Warnings: GPU Failure Prediction in Industrial Clusters

- **Category:** Software Engineering
- **Date:** 2026-09-28
- **Link:** http://arxiv.org/abs/2609.34473v1

---
This research paper introduces **Falcon**, a fault-specific warning framework for predicting GPU failures in large-scale industrial clusters.

---

### Problem

Accurate and actionable GPU failure prediction in production settings is hindered by three main obstacles:

*   **Workload-Confounded Telemetry:** GPU health indicators (temperature, power, utilization) are indirect signals and are strongly influenced by varying workloads. Telemetry data is often incomplete (missing values) and misaligned, making it difficult to distinguish normal workload variations from pre-fault health changes.
*   **Heterogeneous Fault Precursors:** Different GPU fault mechanisms (e.g., remapping, uncorrected memory errors, thermal issues, power anomalies) exhibit distinct pre-failure signals (e.g., ECC increments, XID events vs. sustained temperature/power changes). A single model or global threshold is unlikely to effectively predict all fault types.
*   **Gap Between Window-Level Predictions and Actionable Alerts:** Operators require stable, actionable warning events tied to a specific device, fault family, and intervention horizon, rather than fleeting window-level probability scores. This necessitates mechanisms to filter isolated spikes, suppress redundant alerts, and balance precision, recall, and lead time within operational constraints.

### Method

**Falcon** (Fault-specific Alerting for Large-scale GPU Clusters from Operations) is designed to address these challenges through a four-component framework:

1.  **Missingness-Aware Temporal and Peer-Relative Feature Construction:**
    *   **Temporal Features:** Continuous telemetry (temperature, power) is aligned to a 1-minute grid, missing values are linearly interpolated, and imputation is made visible to the model via availability indicators. Features include lagged statistics, changes, slopes, and persistence summaries.
    *   **Hazard Evolution Features:** Sparse event-like signals (XID, ECC, remapping states) are encoded as non-negative increments, event counts, and consecutive hazardous state patterns, which are less prone to dilution by window averages.
    *   **Peer-Relative Features:** For a target GPU, features are computed relative to other GPUs on the same host running the same task (e.g., means, dispersions, z-scores). This helps distinguish single-card degradation from collective workload shifts.

2.  **Fault-Specific Risk Learning:**
    *   **Dedicated Models:** Instead of a single model, Falcon trains a separate risk model for each specific fault type (e.g., GPU Remapping Failure, GPU Temperature High).
    *   **Learner Selection:** Tree-based models (XGBoost, LightGBM, CatBoost, Random Forest) are chosen for their ability to handle heterogeneous tabular features, imputed values, and non-linear interactions common in GPU telemetry. The best learner and its parameters are selected for each fault type based on event-level F1 score during validation, prioritizing precision-recall for imbalanced data.

3.  **Event-Level Warning Policy:**
    *   **Actionable Alert Conversion:** Transforms continuous window-level risk scores ($p_f(g,t)$) into stable warning events.
    *   **Thresholding (τf):** A score must exceed a fault-specific threshold to be considered a warning candidate.
    *   **N-of-K Persistence:** A warning is only emitted if at least `N` out of the latest `K` scores exceed the threshold, filtering out transient spikes.
    *   **Cooldown (Cf):** After an alert is emitted, further warnings for the same GPU and fault type are suppressed for a fault-specific cooldown period, preventing alert fatigue from sustained conditions. This policy is validated alongside the learner to optimize for event-level metrics.

### Impact

*   **Improved Prediction Performance:** On held-out test data for four critical GPU fault types, Falcon achieved the **highest event-level F1 score** across all faults compared to four baselines (Liu et al., LSTM, Transformer, ChatTime).
    *   For example, it reached **0.706 F1** for "GPU Temperature High" (0.632 Precision, 0.800 Recall) and **0.500 F1** for "GPU Remapping Failure" (0.611 Precision, 0.423 Recall).
*   **Actionable Lead Time:** Falcon provides substantial median lead times of **17.34–35.57 hours** for detected cases, well within the 48-hour actionable horizon specified by ByteDance operators for intervention (inspection, migration, maintenance).
*   **Confirmation of Design Choices:** Ablation studies confirmed the critical role of the fault-specific approach, persistence, and cooldown in achieving high F1 scores and managing alert quality.
*   **Successful Production Deployment:**
    *   Falcon was deployed on a **production ByteDance GPU cluster comprising over 10,000 GPUs**.
    *   The deployment was calibrated for **high precision (0.800 converged-alert precision)** to minimize the cost of false positives, which trigger expensive operational work (workload migration, diagnostics, manual inspection).
    *   It generated **50 alerts in one month, of which 40 were confirmed by engineers**, demonstrating its ability to produce a tractable stream of high-confidence, actionable alerts for proactive intervention (migration, diagnosis, RMA decisions).