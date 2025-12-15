# Back to the Baseline: Examining Baseline Effects on Explainability Metrics

- **Category:** Computer Vision
- **Published:** 2025-12-12
- **Source:** [Original ArXiv Link](http://arxiv.org/abs/2512.11433v1)

---

## 🧐 Problem

The evaluation of XAI attribution methods, particularly through faithfulness metrics like Insertion and Deletion, critically depends on a "baseline function" used to alter input pixels. The paper highlights a fundamental problem:

*   **Baseline Dependence:** The choice of a given baseline significantly and arbitrarily favors certain attribution methods over others, leading to inconsistent and unreliable rankings.
*   **Contradictory Results:** Even for simple linear models, different commonly used baselines yield contradictory results, designating different optimal attribution methods.
*   **Metric Instability:** The Deletion metric is highly sensitive to baseline choice, rendering it unreliable. While Insertion appears more stable, 80% of its score is achieved in an Out-of-Distribution (OOD) regime, raising concerns about its validity. Conversely, Deletion operates mostly in a non-OOD regime.
*   **Inherent Trade-off:** There is an observed trade-off among current baselines: they either effectively remove information OR avoid producing overly OOD images, but none satisfy both criteria simultaneously.

## 🛠️ Method

The authors address these problems by:

*   **Empirical and Theoretical Analysis:** They empirically demonstrate the instability of Deletion and the OOD nature of Insertion across various attribution methods and baselines on deep neural networks (ResNet50, ViT). They theoretically prove this instability for linear models, showing that optimal attribution methods change depending on the baseline (e.g., zero baseline favors Gradient-Input, Rise; uniform noise favors Saliency, SmoothGrad).
*   **Defining Desiderata for Baselines:** They propose two key properties for an effective baseline: (i) it must efficiently remove information, and (ii) it must not produce overly out-of-distribution (OOD) images.
*   **Quantifying the Trade-off:** They use quantitative measures (1-NN OOD score and information removal score via mean logit values) to show that current baselines exhibit an inherent trade-off between information removal and OOD-ness.
*   **Introducing a Novel Baseline:** They propose an optimization-based, model-dependent, and image-independent baseline. This method leverages recent advancements in Feature Visualization to generate images that activate *zero features* in the model's penultimate layer. This design aims to effectively remove information while keeping the generated data within the model's learned distribution, thereby improving on the observed trade-off.

## 📊 Impact

*   **Fundamental Flaw Identified:** The work exposes a critical and previously under-addressed flaw in the evaluation methodologies for XAI attribution methods, revealing that current faithfulness metrics are highly susceptible to baseline choice and can lead to misleading conclusions about method performance.
*   **Improved Understanding:** Provides a deeper theoretical and empirical understanding of the interplay between baselines, attribution methods, and OOD data, explaining *why* current rankings are unstable.
*   **Clearer Evaluation Criteria:** Establishes two crucial desiderata (information removal and OOD-ness) for effective baselines, offering a principled framework for future baseline design and selection.
*   **More Reliable XAI Evaluation:** Introduces a novel baseline that significantly improves the trade-off between information removal and OOD-ness, paving the way for more robust, reliable, and consistent evaluation of attribution methods in XAI. This contributes to building greater trust and confidence in the explanations provided by AI models.
