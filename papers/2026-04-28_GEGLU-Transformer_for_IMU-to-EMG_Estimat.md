# GEGLU-Transformer for IMU-to-EMG Estimation with Few-Shot Adaptation

- **Category:** Robotics
- **Date:** 2026-04-28
- **Link:** http://arxiv.org/abs/2604.25670v1

---
Here's a summary of the research paper in Markdown format:

---

### GEGLU-Transformer for IMU-to-EMG Estimation with Few-Shot Adaptation

**Problem:**
Reliable estimation of neuromuscular activation is crucial for adaptive and personalized control in wearable robotics (e.g., exoskeletons, prostheses). However, direct surface electromyography (EMG) is challenging to deploy outside laboratories due to its sensitivity to electrode placement, signal non-stationarity, motion artifacts, and strong subject dependence, limiting its scalability and long-term usability. While Inertial Measurement Units (IMUs) offer a robust alternative for biomechanical estimation, existing IMU-to-EMG learning methods often rely on static models that degrade significantly on unseen users and fail to account for the highly individualized nature of neuromuscular strategies and varied real-world movement conditions. There is a critical need for an adaptive, data-efficient learning framework that can accurately reconstruct continuous muscle activation from IMU data with rapid, subject-specific personalization, without extensive calibration.

**Method:**
This work proposes an adaptive IMU-to-EMG learning framework combining a novel **GEGLU-Transformer** architecture with a **few-shot adaptation** mechanism.

1.  **Signal Processing:** Raw IMU and EMG signals undergo standard pre-processing (filtering, rectification for EMG), temporal alignment, segmentation into time-normalized gait cycles (0-100%), and min-max normalization.
2.  **GEGLU-Transformer Architecture:**
    *   **Convolutional Front-End:** A 1D convolutional layer processes high-resolution, multi-channel IMU signals to extract local motion patterns and enhance stability before attention-based modeling.
    *   **Positional Encoding:** Added to preserve temporal order in the permutation-invariant Transformer.
    *   **Transformer Encoder:** Composed of multiple layers of multi-head self-attention, designed to capture global temporal dependencies across multimodal sensor inputs.
    *   **GEGLU Feed-Forward Network:** Replaces the standard position-wise feed-forward network. It employs a Gaussian Error Gated Linear Unit (GEGLU) formulation (`FFGEGLU(x) = Wo [GELU(W1x) ⊙ (W2x)]`). This gating mechanism improves feature selection, provides smoother activation dynamics, and enhances gradient propagation, which is particularly beneficial for neuromuscular signal regression.
    *   **Output Projection:** A final linear layer maps the latent representation to the target multi-muscle EMG envelopes.
3.  **Few-Shot Adaptation:** After multi-subject offline training, the model is rapidly personalized for an unseen subject.
    *   **Mechanism:** A small fraction of subject-specific movement cycles (e.g., as low as 0.5% of the test data) is used to fine-tune *all* network parameters via gradient-based updates, minimizing MSE loss.
    *   **Constraints:** Adaptation is performed under strict data and computational constraints to prevent catastrophic forgetting and ensure practicality.
4.  **Evaluation:** The method was validated using a Leave-One-Subject-Out (LOSO) cross-validation protocol on a multi-condition lower-limb biomechanics dataset (including treadmill, level-ground, stair, and ramp locomotion) from 22 healthy adults, comparing against LSTM and CNN-LSTM baselines. Performance was measured using Pearson correlation (r), coefficient of determination (R²), normalized RMSE (nRMSE), peak timing error (∆Tp), and peak amplitude error (∆Ep).

**Impact:**
The proposed GEGLU-Transformer demonstrates significant advancements in IMU-to-EMG estimation:

1.  **Superior Cross-Subject Generalization:** Without any subject-specific adaptation, the GEGLU-Transformer achieved significantly higher performance (`r = 0.706 ± 0.139`, `R² = 0.474 ± 0.208`) compared to state-of-the-art LSTM and CNN-LSTM baselines, both for overall multi-locomotion data and level-ground conditions, indicating improved transferability to unseen users and robustness across diverse tasks.
2.  **Rapid and Data-Efficient Personalization:** With only **0.5%** of subject-specific calibration data (approximately 10-20 gait cycles), performance substantially increased to `r = 0.761 ± 0.030` and `R² = 0.559 ± 0.047`. This demonstrates remarkably fast adaptation and early performance saturation, making the system highly practical for real-world deployment.
3.  **Enhanced Robustness Across Locomotion Modes:** The benefits of few-shot adaptation were consistently observed across all evaluated locomotion modes (stair ascent/descent, level-ground walking, ramp ascent/descent, and treadmill walking), proving the system's robustness to environmental variability.
4.  **Practical Alternative for Wearable Robotics:** These results support attention-based architectures combined with lightweight adaptation as a practical and scalable alternative to direct EMG sensing. It enables reliable and personalized neuromuscular activation estimation from ubiquitous IMU sensors, facilitating adaptive and safe control in real-world wearable robotic applications without the typical challenges of EMG.

---