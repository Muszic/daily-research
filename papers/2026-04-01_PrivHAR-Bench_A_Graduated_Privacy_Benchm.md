# PrivHAR-Bench: A Graduated Privacy Benchmark Dataset for Video-Based Action Recognition

- **Category:** Cryptography
- **Date:** 2026-04-01
- **Link:** http://arxiv.org/abs/2604.00761v1

---
## PRIVHAR-BENCH: A GRADUATED PRIVACY BENCHMARK DATASET FOR VIDEO-BASED ACTION RECOGNITION

### Problem

Existing research on privacy-preserving Human Activity Recognition (HAR) suffers from three key limitations:
1.  **Binary Evaluation:** Methods are typically evaluated against a single baseline (clear vs. one transformation), failing to capture the nuanced trade-off between privacy strength and recognition utility across a continuum. This prevents cross-method comparability.
2.  **Context Bias Contamination:** HAR models often exploit static background context for classification rather than human motion. When privacy transformations are applied only to the human region of interest (ROI), background context remains visible, allowing models to bypass privacy measures.
3.  **Non-Comparable Evaluation Protocols:** A lack of standardized data splits, resolutions, temporal windows, and evaluation metrics across studies makes direct comparison of proposed methods unreliable.

### Method

The authors introduce **PrivHAR-Bench**, a multi-tier benchmark dataset designed to standardize the evaluation of the Privacy-Utility Trade-off in video-based action recognition.
Key components and design principles include:

*   **Graduated Privacy Spectrum:** 1,932 source videos (from a curated subset of 15 UCF101 activity classes) are distributed across **9 parallel tiers of increasing privacy strength**. These tiers progressively destroy different categories of visual information:
    *   **Tier 1 (Spatial Obfuscation):** Gaussian Blur (σ=15) applied to ROI, destroying fine-grained features.
    *   **Tier 2 (Structural Abstraction):** Canny Edge Detection applied to ROI, retaining only structural contours.
    *   **Tier 3 (Cryptographic Block Permutation):** AES-based block scrambling of the ROI at three granularities (block sizes B=16, B=8, B=4), destroying spatial structure and texture.
*   **Context Bias Control:** For every Tier 3 encrypted video, a **background-removed (NoBG)** variant is provided where all non-ROI pixels are set to black, forcing models to rely exclusively on the transformed human region.
*   **Standardized Evaluation Protocol:**
    *   **Data Selection:** 15 activity classes from UCF101, chosen for articulation diversity, minimal object/context dependency, and high person detection feasibility.
    *   **Temporal Window:** All videos are clipped to a standardized 32-frame window from the temporal center.
    *   **Lossless Storage:** All frames are stored as lossless PNG sequences to preserve the mathematical properties of privacy transformations.
    *   **Ancillary Data:** Per-frame bounding boxes, estimated pose keypoints with joint-level confidence scores.
    *   **Evaluation Toolkit:** Provides standardized group-based train/test splits and computes metrics like Top-1 accuracy, SSIM, PSNR, and a composite Privacy-Utility score.
*   **Reproducibility:** The complete generation pipeline, pinned dependencies, and deterministic seeds are publicly released alongside the dataset.

### Impact

PrivHAR-Bench has the following significant impacts:

*   **Standardized Benchmarking:** It establishes a much-needed controlled benchmark for comparing privacy-preserving HAR methods under standardized conditions, enabling direct and reliable cross-method comparisons.
*   **Quantifiable Privacy-Utility Trade-off:** By providing a graduated spectrum of privacy transformations, it allows researchers to plot and analyze their model's accuracy as a continuous function of privacy strength, revealing the true privacy-utility trade-off rather than just binary performance.
*   **Robust Evaluation:** The inclusion of background-removed (NoBG) variants directly addresses and controls for context bias, ensuring that models are evaluated on their ability to recognize actions from transformed human motion, not environmental cues.
*   **Empirical Validation:** Baseline experiments using R3D-18 demonstrated a measurable and interpretable degradation curve across tiers (from 88.8% accuracy on clear videos to 53.5% on encrypted, background-removed videos, and 4.8% on cross-domain evaluation), confirming its effectiveness in highlighting varying levels of recognition utility.
*   **Facilitates Future Research:** The public availability of the dataset, generation pipeline, and evaluation code fosters further research and development in privacy-preserving HAR.