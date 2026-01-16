# DInf-Grid: A Neural Differential Equation Solver with Differentiable Feature Grids

- **Category:** Machine Learning
- **Date:** 2026-01-15
- **Link:** http://arxiv.org/abs/2601.10715v1

---
## ∂∞-Grid: A Neural Differential Equation Solver with Differentiable Feature Grids

### Problem

Neural solvers for differential equations (DEs) face two main challenges:
1.  **Computational Inefficiency of MLP-based Solvers:** Coordinate-based Multi-Layer Perceptrons (MLPs), such as Sinusoidal Neural Networks (Siren), are widely used but are computationally intensive and slow to train (often taking hours). They struggle with exploiting the spatial structure of signals and require backpropagating through the entire network for every sample.
2.  **Lack of Differentiability in Existing Grid-based Methods:** While explicit or hybrid grid-based representations (e.g., Instant-NGP, K-Planes) offer significantly faster training by leveraging spatial locality, their reliance on linear (or d-linear) interpolation means they are only C0 or C1 differentiable. This limits their ability to accurately compute higher-order derivatives (Jacobians, Laplacians), which are essential for solving DEs, rendering them unsuitable for physics-informed learning where DEs serve as loss functions.

### Method

The ∂∞-Grid approach addresses these limitations by combining the efficiency of feature grids with an infinitely differentiable interpolation technique and a multi-resolution structure:

1.  **Feature Grid Representation:** The method parametrizes a field `u(x)` as `u(x) = d(f(x;F); Θ)`, where `F` is a learnable feature grid and `d` is a small, shallow decoder MLP. This grid-based encoding leverages spatial locality, meaning only features adjacent to a query point `x` need to be updated during optimization, speeding up training.
2.  **Infinitely Differentiable Radial Basis Function (RBF) Interpolation:** Unlike linear interpolation, ∂∞-Grid uses Gaussian RBFs for interpolating features from the grid. RBFs are smooth and **infinitely differentiable (C∞)**, allowing for the analytical computation of higher-order derivatives (∇u, ∇²u, etc.) via automatic differentiation. This is crucial for accurately incorporating DEs as loss functions. Efficient RBF interpolation is achieved by using stratified sampling and precomputing effective local neighborhoods (e.g., 2-ring) for each sample.
3.  **Multi-resolution Co-located Grids:** To capture both global structure and high-frequency details, and to enable faster global gradient propagation, the method employs a set of feature grids at different resolutions. Features interpolated from each scale are concatenated and fed to the decoder.
4.  **Implicit Training with DE Loss:** The model is trained implicitly by minimizing a loss function derived directly from the DE residual over the spatio-temporal domain, similar to Physics-Informed Neural Networks (PINNs). Boundary or initial conditions can be imposed as hard constraints to improve convergence and ensure uniqueness.

### Impact

∂∞-Grid demonstrates significant advancements for neural DE solvers:

1.  **Dramatic Speed-up:** Achieves a **5–20x speed-up** in training time compared to coordinate-based MLP methods (e.g., Siren), solving complex differential equations in seconds or minutes.
2.  **Comparable Accuracy:** Maintains accuracy comparable to, or even better than, state-of-the-art MLP-based neural solvers.
3.  **Broad Applicability:** Validated on a diverse range of physical problems requiring higher-order derivatives, including:
    *   Poisson equation (for image reconstruction)
    *   Helmholtz equation (for wave fields)
    *   Kirchhoff-Love boundary value problem (for cloth simulation)
    *   Eikonal equation
    *   Advection and Heat equations
4.  **Novel Differentiable Grid:** Provides a novel and practical representation that combines the efficiency of feature grids with the necessary infinite differentiability for solving DEs, overcoming the limitations of prior grid-based methods.