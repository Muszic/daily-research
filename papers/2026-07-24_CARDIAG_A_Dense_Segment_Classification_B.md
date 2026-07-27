# CARDIAG: A Dense Segment Classification Benchmark of Deep Learning Architectures for Coronary Angiography

- **Category:** Artificial Intelligence
- **Date:** 2026-07-24
- **Link:** http://arxiv.org/abs/2607.22139v1

---
This research paper introduces a new benchmark and dataset for pixel-level SYNTAX classification of coronary angiograms using deep learning.

### Problem

The field of AI-based coronary angiogram analysis, crucial for cardiovascular disease assessment, suffers from a lack of standardized evaluation protocols and high-quality, publicly available multi-center datasets for dense SYNTAX classification. Existing datasets like ARCADE have concerns regarding label quality, lack of essential metadata, and potential data leakage, hindering robust generalization testing and reproducible research. Furthermore, prior studies often relied on in-house datasets or focused on single, simpler architectures, leaving a gap for a comprehensive, multi-family architectural benchmark to identify best practices.

### Method

1.  **CARDIAG Dataset Creation:**
    *   A multi-center, multi-label dataset ("CARDIAG") was created from 114 anonymized patient examinations across five medical centers in Northern Poland.
    *   Annotations (SYNTAX classes, binary vessel, catheter, uncertainty masks) were performed by three expert interventional cardiologists (3+ years experience) using AngioTagger software, adhering to SYNTAX score definitions. Inter-observer agreement was high (Dice score 0.9072 with uncertainty masks, Fleiss' kappa 0.7611 for stenosis).
    *   The dataset includes comprehensive metadata (acquisition parameters like SID, SOD, primary/secondary angles, center ID, sample ID) and supplementary frames to prevent data leakage and enable advanced tasks like 3D reconstruction and frame interpolation.
    *   It addresses label imbalance (more left-side vessels, fewer distal segments) and patient demographic biases (more males, 50-80 age group) for responsible model development.

2.  **Comprehensive Architectural Benchmark:**
    *   A rigorous evaluation was conducted on 24 state-of-the-art deep learning vision models, categorized into:
        *   Standard CNNs (e.g., U-Net, DeepLabV3+).
        *   Vision Transformers (e.g., SegFormer, SwinUNETR).
        *   Modern and Large-Kernel CNNs (e.g., ConvNeXtV2, MedNeXt).
        *   State Space Models (SSMs) (e.g., Mamba-UNet, SegMamba).
        *   Domain-Pretrained Baselines (using XRayVision and RadImageNet encoders).
    *   All models were trained using a consistent setup: a combined Cross-Entropy and Dice loss, AdamW optimizer, and scheduler.
    *   An ensemble model combining ConvNeXt V2, FPN, and Mamba U-Net was also developed and evaluated using hard, soft, and entropy-weighted voting.

3.  **Robustness and Performance Evaluation:**
    *   Models were assessed for real-world robustness through leave-one-center-out generalization validation.
    *   Data efficiency analysis was performed.
    *   The influence of patient demographics (age, sex) and X-ray acquisition parameters (projection angles) on model performance was systematically investigated.
    *   Model calibration and uncertainty were evaluated using inference-time dropout to ensure reliability for clinical decision support.

### Impact

*   **New Benchmark and Dataset:** The release of CARDIAG provides a comprehensive, multi-center, multi-label dataset with detailed metadata and annotation for SYNTAX classification, establishing a robust and reproducible benchmark for future research. It addresses critical limitations of previous datasets, enabling true generalization testing.
*   **Best Performing Baseline:** The study nominated ConvNeXt V2 encoder with DeepLab V3 Plus decoder as the best performing single architecture (macroF1 = 0.456). An ensemble of ConvNeXt V2, FPN, and Mamba U-Net further improved performance (macroF1 = 0.479), establishing strong baselines for the community.
*   **Architectural Insights:** The extensive benchmark provides a deep understanding of diverse deep learning architectures (CNNs, ViTs, SSMs) for this task, demonstrating their generalization capabilities, data efficiency, and calibration. It highlights the importance of both high-resolution and low-resolution features for effective encoding.
*   **Clinical Relevance and Robustness:** The meta-analysis on patient demographics and acquisition parameters provides crucial insights into algorithmic robustness across varying, real-world clinical conditions. The evaluation of model calibration and uncertainty quantification addresses a key prerequisite for safe and reliable clinical decision support.
*   **Facilitates Future Research:** The CARDIAG dataset's rich set of labels (including uncertainty, catheter masks, supplementary frames, and detailed metadata) opens avenues for broader research beyond SYNTAX segmentation, such as stenosis detection, 3D reconstruction, and frame interpolation, accelerating advancements in cardiovascular AI.