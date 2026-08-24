# QUASAR: A Quantum-Classical Neural Network for SAR Satellite Physical-Layer Authentication

- **Category:** Cryptography
- **Date:** 2026-08-20
- **Link:** http://arxiv.org/abs/2608.20240v1

---
**Problem:**
X-band SAR satellites (8–12 GHz) are critical for disaster response, environmental monitoring, and military intelligence, but they lack robust physical-layer authentication (PLA). Existing classical deep learning methods for radio-frequency fingerprinting are often limited to sub-6 GHz and underfit the subtle, nonlinear IQ phase characteristics unique to satellite hardware. This limitation, coupled with vulnerabilities in cryptographic solutions (e.g., key leakage, legacy hardware, long mission lifetimes), leaves critical SAR services susceptible to impersonation and disruption, especially in the challenging X-band frequency range where commercial SDRs struggle with direct capture.

**Method:**
The authors propose **QUASAR**, a novel quantum-classical hybrid neural network designed for X-band SAR signal authentication.
1.  **Data Collection:** A custom X-band SAR RF fingerprinting testbed (Aaronia Hyperlog Pro 70140 antenna, DSI MX12000 programmable mixer, Ettus USRP X310 SDR) was designed and deployed to collect 3.76 TB of raw IQ data from 37 operational ICEYE satellites over 28 days. Imaging pulses, rather than data downlinks, were targeted due to their passive availability, signal richness, and collection frequency.
2.  **Preprocessing:** Raw IQ data undergoes noise mitigation via adaptive magnitude thresholding, then segmented and transformed into grayscale spectrograms (224x224 pixels). Class balancing is applied using a one-vs-rest (OvR) protocol for each satellite.
3.  **QUASAR Architecture:** The architecture is a quantum-classical hybrid that combines:
    *   A deep **CNN Spectrogram Encoder**: Processes input spectrograms to extract hierarchical spectral and temporal features, outputting a dense latent vector.
    *   A **Variational Quantum Circuit (VQC)**: This four-layer VQC operates over an 8-qubit register. A key innovation is the "IQ-native encoding," which directly maps the amplitude and phase of complex features from the latent vector onto the polar and azimuthal angles of each qubit, leveraging the geometric isomorphism between complex IQ samples and single-qubit pure states.
    *   A **Classical Skip Connection**: A parallel classical path that directly processes the latent vector, bypassing the VQC.
    *   The outputs from the VQC and the classical skip connection are fused via late concatenation before being passed to a final binary classifier for authentication.

**Impact:**
QUASAR demonstrates significant improvements in physical-layer authentication for X-band SAR satellites, establishing the first quantum-enhanced physical-layer classifier for satellite constellations:
*   **Superior Accuracy & Data Efficiency:** Achieves 97.3% validation accuracy and a macro-F1 score of 0.973. It matches the accuracy of classical baselines using only 10% of the training data, significantly reducing the time-consuming data collection and enrollment costs. At an equal data budget, QUASAR outperforms classical-only baselines by 7.5 percentage points.
*   **Robust Adversarial Defense:** Successfully rejects spoofed transmissions in three challenging adversarial scenarios:
    *   Replay attacks: 89.7% detection rate.
    *   Crafted-IQ injection: 94.1% detection rate.
    *   Space-borne spoofing (emulated using other ICEYE satellites as adversaries in an open-set protocol): 81.3% detection rate.
*   **Novelty and Explainability:** QUASAR represents a pioneering quantum-enhanced physical-layer classifier. Explainability analysis (via gradient saliency maps and latent-space clustering) confirms the quantum branch's ability to amplify minute hardware fingerprints and localizes decisions to sub-millisecond windows in the raw IQ domain, providing physical grounding for its superior performance.
*   **New Research Avenue:** The detailed framework and supporting results open a novel and promising research avenue for physical-layer authentication, particularly for high-frequency satellite communications and other critical wireless systems.