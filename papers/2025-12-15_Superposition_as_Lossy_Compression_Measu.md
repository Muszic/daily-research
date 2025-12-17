# Superposition as Lossy Compression: Measure with Sparse Autoencoders and Connect to Adversarial Vulnerability

- **Category:** Machine Learning
- **Published:** 2025-12-15
- **Source:** [Original ArXiv Link](http://arxiv.org/abs/2512.13568v1)

---

## 🧐 Problem

Neural networks achieve remarkable performance through **superposition**, where multiple features are encoded as overlapping directions in activation space rather than dedicating individual neurons to each feature. This phenomenon poses significant challenges for **interpretability**, as neurons become "polysemantic," responding to multiple unrelated concepts.

Despite its importance, there is a fundamental lack of **principled, practical methods to measure superposition** in real neural networks. Existing approaches are limited to toy models requiring knowledge of ground truth features, making them inapplicable to complex, real-world scenarios.

A key hypothesis suggests that superposition might be a mechanistic cause of **adversarial vulnerability**, implying that adversarial training should reduce superposition. However, testing this prediction has been impossible due to the absence of a reliable measurement framework.

## 🛠️ Method

The authors propose an **information-theoretic framework to measure superposition** by defining it as "lossy compression."

1.  **Feature Extraction via Sparse Autoencoders (SAEs):** For any given neural network layer's activations, a Sparse Autoencoder is trained to decompose these activations into a higher-dimensional set of "sparse codes" (features). The `L1` regularization in SAEs ensures that these features compete for representational budget, reflecting their computational importance.
2.  **Quantifying Feature Allocation:** The "probability" ($p_i$) of each extracted SAE feature is computed based on its total activation magnitude across a dataset. This reflects the feature's share of the network's total representational budget.
3.  **Calculating Effective Features:** The **Shannon entropy** ($H(p)$) of this feature probability distribution is calculated. Its exponential, $F = e^{H(p)}$, represents the "effective degrees of freedom" or "virtual neurons." This is interpreted as the minimum number of interference-free channels (or neurons) required to losslessly encode the observed feature distribution.
4.  **Defining Superposition Metric ($\psi$):** Superposition is then quantified as the ratio of effective features ($F$) to the actual number of physical neurons ($N$) in the layer: $\psi = F/N$.
    *   $\psi = 1$ indicates that the network operates at its interference-free limit (lossless compression, no superposition).
    *   $\psi > 1$ indicates lossy compression, meaning the network simulates more effective features than it has physical neurons, necessitating interference.

The framework is validated in toy models, demonstrating strong correlation with observable ground truth interference patterns and robustness to hyperparameter choices.

## 📊 Impact

This work makes a significant impact by:

*   **Enabling Principled Measurement:** For the first time, it provides a principled and practical method to quantitatively measure superposition (as lossy compression) in real-world neural networks without requiring ground truth features. This opens up new avenues for mechanistic interpretability research.
*   **Challenging a Core Hypothesis:** The findings contradict the simple hypothesis that superposition universally causes adversarial vulnerability. Instead, adversarial training's effect on superposition is nuanced:
    *   For simple tasks with ample network capacity, adversarial training can **increase effective features** ("abundance regime"), improving robustness.
    *   For complex tasks or limited capacity, it forces **feature reduction** ("scarcity regime").
*   **Revealing Neural Organization Dynamics:** The metric provides novel insights into how neural networks organize information under computational constraints:
    *   **Dropout** systematically reduces superposition, suggesting it acts as a capacity constraint.
    *   Networks trained on **algorithmic tasks** show minimal superposition ($\psi \le 1$).
    *   Detects sharp **feature consolidation** (drop in superposition) during the "grokking" phase transition, marking algorithmic discovery.
    *   **Layer-wise patterns** in models like Pythia-70M reveal that compression peaks in early MLP layers before declining, mirroring findings from intrinsic dimensionality studies.

Ultimately, this framework allows for quantitative study of how networks encode information, potentially facilitating the **systematic engineering of interpretable and robust architectures**.
