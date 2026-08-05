# What the Detector Can See: Evaluating CPS Anomaly Detectors Independently of the Decision Rule

- **Category:** Cryptography
- **Date:** 2026-08-03
- **Link:** http://arxiv.org/abs/2608.02821v1

---
### Problem

Traditional evaluation metrics for Cyber-Physical System (CPS) anomaly detectors (e.g., precision, recall, F1 score) conflate two distinct aspects:
1.  **Detector Representation Quality (Stage 1):** How well the detector's internal representation (residuals) captures evidence of an anomaly.
2.  **Decision Rule Calibration (Stage 2):** How effectively the alarm threshold is set to convert these residuals into binary alarms.

This conflation makes it difficult to diagnose the root cause of detection failures (e.g., weak evidence vs. poor thresholding) and hinders fair comparison across heterogeneous detectors that use different internal representations and decision rules. Moreover, threshold-tied evaluations can reorder detector rankings, suggesting the operating point can dominate the comparison over the representation itself. This masks whether an attack was inherently *visible* to the detector or merely missed due to a poorly set alarm threshold.

### Method

The paper proposes a novel, decision-rule-independent evaluation framework that treats a CPS anomaly detector as a two-stage pipeline:
1.  **Stage 1 ($\phi$):** Maps observations to an intermediate residual representation ($r_t$). This is the core "evidence signal."
2.  **Stage 2 ($\pi$):** Maps one or more residuals to binary alarms ($a_t$). This involves thresholding, smoothing, or sequential testing.

Instead of evaluating only the final alarms (Stage 2 output), the framework focuses on evaluating **Stage 1 directly** using **normalized residual energy ($e_t$)**.

*   **Normalized Residual Energy:** Defined as $e_t = \frac{1}{2} (r_t - \mu_0)^\top S_0^{-1} (r_t - \mu_0)$, where $\mu_0$ and $S_0$ are the mean and covariance of the trained-normal residual reference. This is essentially half the squared Mahalanobis distance.
*   **Energy-KL Identity:** Crucially, the expectation of this normalized residual energy has an *exact theoretical connection to the Kullback–Leibler (KL) divergence* from the trained-normal reference distribution (specifically, a moment-matched Gaussian version). This provides a common "information-energy scale" to measure:
    *   **Attack Separation:** How well attack residuals deviate from normal.
    *   **Train-Test Stability:** How much the normal residual distribution shifts between training and testing.
    *   **Residual Space Compactness:** How compactly the detector encodes the plant's normal behavior.
*   **Decision-Rule-Free Diagnostics:** Using this energy stream, the framework derives several diagnostics:
    *   **Point-level metrics:** ROC-AUC, pAUC@1% (for overall attack visibility).
    *   **Drift-corrected evidence:** To account for train-test shifts (e.g., using Statistical Detection Rate - SDR).
    *   **Compactness measures:** To understand the residual space structure.
    *   **Controlled Stage 2 Probe (F1@p99, p99 coverage):** A fixed, simple threshold (the 99th percentile of train-normal energy) is applied as a *probe* to see if existing Stage 1 evidence can be extracted, rather than for primary detector ranking.
*   **Application:** The framework was uniformly applied to five diverse CPS anomaly detectors (GDN, FuSAGNet, TranAD, NSIBF, GeCo) across three benchmarks (SWaT, WADI, HAI) without per-detector tuning.

### Impact

The application of this framework yielded several significant insights into CPS anomaly detection failures:

*   **Disparity between ROC-AUC and Practical Performance:** Detectors with broadly similar ROC-AUC values (indicating overall separability) can exhibit performance differences of *more than an order of magnitude* in F1 scores when evaluated at a common, controlled false-alarm rate (e.g., p99 calibration). This highlights that ROC-AUC alone can be misleading about real-world deployability and Stage 2 extraction efficiency.
*   **Inconsistent Detector Rankings Across Testbeds:** Detector performance rankings do not reliably transfer across different CPS testbeds. For example, TranAD ranked first on HAI but last on SWaT, while NSIBF ranked first on WADI but last on HAI. This underscores the need for context-specific evaluation and questions the generality of "best" detectors.
*   **Vulnerability to Localized Attacks:** On testbeds like WADI, localized attacks can effectively evade detectors that pool evidence across all channels, demonstrating how the structure of the residual space (e.g., localized vs. global aggregation) influences detectability. This helps explain why detectors like NSIBF (which can focus evidence) outperform methods that perform well on other benchmarks with more distributed attacks.
*   **Improved Failure Attribution:** The decision-rule-free analysis successfully separates detection failure causes, allowing for more precise diagnosis:
    *   **Weak Residual Evidence:** The detector simply doesn't "see" the attack in its internal representation.
    *   **Train-Test Drift:** The normal reference distribution shifts between training and testing, causing false alarms or masking attacks.
    *   **Dimensional Dilution:** Attack evidence is present but diluted by aggregation across too many channels.
    *   **Stage 2 Calibration Failure:** Strong evidence exists, but the chosen alarm rule fails to extract it effectively.
    *   **Limited Physical Effect:** The attack itself has minimal measurable impact on the observed telemetry.
*   **Actionable Insights for Improvement:** By diagnosing the specific cause of failure, the framework guides targeted interventions: representation redesign (for weak evidence), reference stabilization (for train-test drift), or Stage 2 recalibration (for extraction failures). This provides a more granular and diagnostic approach to evaluating CPS anomaly detectors, moving beyond single-point alarm metrics to understand *what* a detector can truly "see" and *why* it might fail.