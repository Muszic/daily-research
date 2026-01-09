# Why Commodity WiFi Sensors Fail at Multi-Person Gait Identification: A Systematic Analysis Using ESP32

- **Category:** Cryptography
- **Date:** 2026-01-05
- **Link:** http://arxiv.org/abs/2601.02177v1

---
```markdown
### Problem

Multi-person gait identification using WiFi Channel State Information (CSI) remains a significant challenge, despite high accuracy (85-95%) achieved in single-person scenarios. The core difficulty lies in separating the mixed gait signatures of multiple individuals (blind source separation problem) when using WiFi signals. Existing research on multi-person systems either relies on complex, expensive hardware setups with modified firmware or yields only modest performance with commodity hardware. This raises a critical unanswered question: is the poor performance an algorithmic limitation that can be overcome with better signal processing, or a fundamental hardware constraint of readily available, low-cost WiFi devices? Understanding this distinction is crucial for guiding future research efforts.

### Method

This paper systematically evaluates the performance of multi-person gait identification using **commodity ESP32 WiFi sensors** (low-cost, off-the-shelf devices with standard 3 antennas and 52 subcarriers). The methodology involves:

1.  **Data Collection:** CSI data from 1-10 people across seven scenarios in controlled lab and realistic classroom environments.
2.  **Preprocessing:** Subcarrier filtering, z-score normalization, and temporal alignment.
3.  **Person Count Estimation:** Using eigenvalue-based source enumeration.
4.  **Signal Separation:** Evaluation of six diverse blind source separation methods:
    *   FastICA (Independent Component Analysis)
    *   SOBI (Second-Order Blind Identification)
    *   PCA (Principal Component Analysis)
    *   NMF (Non-negative Matrix Factorization)
    *   Wavelet Transform
    *   Tensor Decomposition (Tucker decomposition)
5.  **Feature Extraction:** 24 temporal, frequency, and spatial features from each separated source.
6.  **Classification:** Support Vector Machine (SVM) with RBF kernel for person identification.
7.  **Novel Diagnostic Metrics:** Introduction of Intra-Subject Variability (ISV), Inter-Subject Distinguishability (ISD), and Performance Degradation Rate (PDR) to analyze failure modes beyond standard accuracy.

### Impact

The study reveals that commodity ESP32 WiFi sensors are fundamentally limited for reliable multi-person gait identification, indicating that algorithmic improvements alone cannot overcome these hardware constraints.

*   **Low Accuracy & Insignificant Differences:** All six diverse signal separation methods achieved similarly low identification accuracies (ranging from 45-56%, with NMF being the best at 56%), and statistical analysis showed no significant performance differences between them (p > 0.05).
*   **High Variability & Low Distinguishability:** Novel diagnostic metrics revealed extremely high Intra-Subject Variability (ISV) and low Inter-Subject Distinguishability (ISD). Within-class variance (ISV) exceeded between-class separation (ISD) by factors of 73 to 1,266,000, leading to severe feature overlap (>97%).
*   **Performance Degradation & Unpredictability:** Performance degraded significantly as the number of people increased. Environmental conditions also had an unpredictable effect, with some methods performing better in the realistic classroom than in the controlled lab.
*   **Hardware Limitations as the Root Cause:** The analysis attributes the failures to fundamental limitations of commodity ESP32 sensors:
    *   **Insufficient Spatial Resolution:** Only 3 antennas and 52 subcarriers provide inadequate angular resolution and effective rank for distinguishing multiple individuals.
    *   **Gait Similarity vs. Noise:** Human gait differences are easily masked by environmental variations and sensor noise, as ISV far outweighs ISD.
    *   **Environmental Unpredictability:** Multipath effects unpredictably enhance or degrade signal separation, preventing reliable generalization across environments.

The paper provides strong evidence-based guidance, suggesting that continued efforts on algorithmic refinements using commodity WiFi sensors will yield diminishing returns. Instead, future research should focus on next-generation sensing technologies with enhanced hardware capabilities, such as massive MIMO (8+ antennas), mmWave systems, sensor fusion, and deep learning, adhering to the proposed diagnostic metric thresholds (ISV/ISD < 10 and |PDR| < 20%) for viable systems.
```