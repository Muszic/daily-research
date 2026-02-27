# RhythmBERT: A Self-Supervised Language Model Based on Latent Representations of ECG Waveforms for Heart Disease Detection

- **Category:** Machine Learning
- **Date:** 2026-02-26
- **Link:** http://arxiv.org/abs/2602.23060v1

---
Here's a summary of the RHYTHMBERT research paper in Markdown:

### RHYTHMBERT: A SELF-SUPERVISED LANGUAGE MODEL BASED ON LATENT REPRESENTATIONS OF ECG WAVEFORMS FOR HEART DISEASE DETECTION

#### Problem

Traditional self-supervised learning (SSL) methods for Electrocardiogram (ECG) analysis often treat ECGs as generic time series, overlooking crucial physiological semantics and rhythm-level structures. Existing approaches suffer from several limitations:
1.  **Distortion by Augmentations:** Contrastive SSL methods rely on data augmentations that can inadvertently distort vital morphological features and inter-beat intervals, leading to "bad positive pairs."
2.  **Misaligned Segmentation:** Generative SSL models frequently employ fixed-window segmentation, which misaligns with natural cardiac cycle boundaries, obscuring form-level (wave morphology) and rhythm-level semantics.
3.  **Limited Scope in "ECG-as-Language" Models:** Prior models that attempt to view ECG as a language, such as HeartLang, primarily focus on QRS waves, neglecting the diagnostic importance of P- and T-wave morphology, thereby limiting clinical generalization (e.g., for atrial or repolarization cues).
4.  **Computational Bottleneck:** Models like ECGBERT, while generative, use raw, high-dimensional ECG segments for vocabulary, leading to computational inefficiency and scalability issues.

#### Method

The authors propose **RhythmBERT**, a novel generative self-supervised ECG language model designed to overcome these limitations by viewing ECGs as a structured language.

1.  **ECG Waveform Tokenizer:**
    *   Raw ECG (Lead II only) is preprocessed (filtering) and delineated to identify individual P, QRS, and T wave segments.
    *   **Autoencoder-based Latent Representations:** For each wave type (P, QRS, T), a dedicated 1D Convolutional Autoencoder (1D-CAE) maps variable-length raw segments into fixed-size, low-dimensional continuous latent vectors. This process compresses morphological information.
    *   **Discrete Tokenization:** The latent vectors for each wave type are then clustered (using k-means with optimal `k` determined by the elbow method) to form a discrete "wave vocabulary." Each segment is assigned a cluster ID, serving as a symbolic token.
    *   **Heartbeat Sentences:** These discrete P, QRS, and T tokens are concatenated in physiological order (P-QRS-T) to form "heartbeat sentences," creating a structured symbolic sequence.

2.  **BERT Backbone Network:**
    *   A Transformer encoder learns contextual representations from these heartbeat sentences.
    *   **Hybrid Input Embeddings:** To mitigate fidelity loss from discretization, the model fuses three types of embeddings:
        *   **Token Embeddings:** Dense vectors for the discrete cluster IDs.
        *   **Positional Embeddings:** Learned embeddings to capture sequence order.
        *   **Morphological Embeddings:** Continuous feature vectors extracted from the *raw* P, QRS, and T segments using a pre-trained XResNet1d-101 model. These continuous embeddings preserve fine-grained morphological details and are projected and summed with the other embeddings.
    *   **Self-supervised Pre-training:** RhythmBERT is pre-trained on approximately 800,000 unlabeled single-lead ECG recordings (from MIMIC-IV-ECG) using a **Masked Language Modeling (MLM)** objective, where 20% of the input tokens are randomly masked, and the model learns to predict them.

#### Impact

RhythmBERT demonstrates significant advancements in ECG analysis, particularly its ability to learn robust, transferable, and physiologically meaningful representations:

1.  **Strong Generalization and Performance:** Despite being trained exclusively on a single ECG lead (Lead II), RhythmBERT achieves competitive and, in some cases, superior performance compared to state-of-the-art models that utilize full 12-lead ECGs on various downstream heart disease classification tasks (PTB-XL, CPSC2018, Chapman-Shaoxing datasets).
2.  **Broad Clinical Applicability:** The model shows robust generalization across a wide spectrum of conditions, from highly prevalent arrhythmias like atrial fibrillation to diagnostically challenging and subtle abnormalities such as myocardial infarction (MI) and ST-T deviations.
3.  **Scalability and Efficiency:** The discrete tokenization strategy and self-supervised pre-training on a large unlabeled dataset enable a scalable approach to learning ECG representations. Its single-lead capability also makes it highly relevant for wearable devices and remote monitoring.
4.  **Physiologically Aligned Approach:** By explicitly modeling P, QRS, and T waves as fundamental "words" and heartbeats as "sentences," and by fusing discrete rhythm semantics with continuous morphological embeddings, RhythmBERT offers a novel and physiologically aligned pathway for advancing cardiac analysis.