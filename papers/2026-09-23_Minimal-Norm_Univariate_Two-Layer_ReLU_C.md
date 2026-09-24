# Minimal-Norm Univariate Two-Layer ReLU Classification: Exact Solutions and Global Optimality with Skip Connections

- **Category:** Machine Learning
- **Date:** 2026-09-23
- **Link:** http://arxiv.org/abs/2609.28438v1

---
This research paper investigates minimal-norm interpolation and ℓ2-regularized logistic-loss minimization for binary classification using univariate two-layer ReLU networks.

## Problem

The paper addresses existing gaps in the theoretical understanding of optimal solutions in neural networks, specifically concerning:
1.  **Geometric Characterization:** Providing a complete geometric description of minimal-norm classifier functions for finite datasets.
2.  **Architectural and Penalization Dependencies:** Analyzing how these solutions depend on two critical distinctions:
    *   Whether hidden-layer biases are included in the parameter norm (penalized vs. unpenalized).
    *   Whether the network incorporates a free affine skip connection (present vs. absent).
3.  **Optimization Landscape:** Understanding how adding a skip connection impacts the optimization landscape, particularly regarding the global optimality of Karush-Kuhn-Tucker (KKT) points.
4.  **Regularization vs. Interpolation:** Characterizing minimizers of the ℓ2-regularized logistic loss and their relationship to minimal-norm interpolators, especially how they behave as regularization strength approaches zero.

These questions are crucial for explaining the generalization properties and implicit biases of gradient-based algorithms in overparameterized neural networks.

## Method

The authors employ a rigorous theoretical and analytical approach, complemented by numerical experiments:
*   **Exact Function Space Characterizations:** They provide complete geometric characterizations of optimal classifiers in function space for all four combinations of bias penalization and skip connection presence.
*   **First-Order Optimality Analysis:** The core of their proofs involves analyzing KKT points and constructing "descent directions" using infinitesimal perturbations. Violations of geometric conditions are shown to lead to a decrease in parameter norm without violating constraints, contradicting first-order optimality.
*   **Role of Skip Connections:** The skip connection is demonstrated to be crucial for this analysis, as it can absorb affine changes when a neuron is reversed, facilitating the construction of descent directions and ensuring global optimality for KKT points.
*   **Parameter Norm Mechanisms:** They detail how different penalization schemes influence the optimal solutions:
    *   **Unpenalized Biases:** The total variation of the function "telescopes" for specific "switch-hugging" and "convexity-correct" functions, resulting in minimal norm.
    *   **Penalized Biases:** First-order rescaling enforces "balancedness," and a strict triangle inequality rules out multiple kinks in a same-label segment, leading to a unique, sparse solution.
*   **Regularized Loss Analysis:** Analogous global-optimality and geometric results are established for sufficiently weak ℓ2-regularization of the logistic loss, connecting it to the interpolation problem.
*   **Numerical Validation:** The theoretical predictions regarding optimization landscape changes (due to skip connections) and sparsity phenomena (due to regularization) are validated through numerical experiments on various synthetic datasets and network widths.

## Impact

The research delivers several key contributions and implications for the understanding and application of ReLU networks:
*   **Unified Geometric Understanding:** Provides a complete geometric characterization of minimal-norm interpolators and regularized-loss minimizers, clarifying how these optimal functions differ based on bias penalization and whether they exhibit properties like "switch hugging," "convexity correct," "single turning," or "interval turning."
*   **Skip Connections for Global Optimality:** Demonstrates that adding a free affine skip connection fundamentally transforms the optimization landscape, guaranteeing that every KKT point (or positive-margin stationary point for regularized loss) is a global minimizer. This is a significant finding for training stability and convergence in non-convex settings.
*   **Sparsity Driven by Regularization:** Reveals that when biases are unpenalized, ℓ2-regularized logistic loss induces a unique "interval turning" sparsity property that minimal-norm interpolators do not necessarily possess. This implies that most minimal-norm interpolators cannot be achieved as limits of margin-normalized regularized-loss minimizers as regularization strength approaches zero, highlighting a distinct mechanism for sparsity beyond bias penalization.
*   **Improvements to Prior Work:**
    *   **Reduced Complexity Bounds:** Lowers the bound on the number of linear regions for KKT points in prior work (Safran et al., 2022) from `32r + 67` to `r` (where `r` is the number of label switches), either with skip connections or by focusing on global minimizers.
    *   **Conjecture Proof:** Confirms the conjecture by Boursier and Flammarion (2023) regarding the uniqueness of minimal-norm interpolators with penalized biases and skip connections, extending uniqueness and optimal sparsity results even without skip connections.
    *   **Enhanced Privacy Attacks:** Improves a privacy attack by Smorodinsky et al. (2026), ensuring higher accuracy and representation of dataset segments when skip connections are present or global minimizers are considered.