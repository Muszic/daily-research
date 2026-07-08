# A Function-Space Dichotomy for Compositional Learning: Exponential Sub-Optimality of the Neural Tangent Kernel

- **Category:** Machine Learning
- **Date:** 2026-07-07
- **Link:** http://arxiv.org/abs/2607.06382v1

---
## Research Paper Summary: A Function-Space Dichotomy for Compositional Learning: Exponential Sub-Optimality of the Neural Tangent Kernel

### Problem

A long-standing empirical observation in deep learning is that trained neural networks consistently and substantially outperform their Neural Tangent Kernel (NTK) limit, particularly on tasks involving *compositional structure*. While the NTK provides an analytically convenient "lazy" training regime (infinite width, minimal weight movement), it often fails to capture the true learning capabilities of "rich" regime networks (finite width, genuine feature learning). A quantitative account of *when* and *by how much* the NTK is sub-optimal, especially with respect to *depth* (at fixed input dimension), has been lacking. This gap highlights a fundamental mismatch between the NTK's implicit assumptions and the nature of real-world compositional tasks.

### Method

The authors propose a "function-space dichotomy" to quantitatively explain the NTK's sub-optimality. They compare two measures of a target function's complexity:

1.  **Fourier Complexity:** This governs NTK kernel regression and is tied to the target's smoothness (Sobolev norm on the unit circle, penalizing high-frequency oscillations). On S¹, the NTK's RKHS norm is shown to be proportional to the Sobolev H¹ norm, with eigenvalues decaying as k⁻².
2.  **Architectural Complexity:** This governs learning over depth-L, width-w ReLU networks (quantified by the deep variation norm of weights). Functions with compact compositional descriptions have low architectural complexity, even if they are highly oscillatory.

The research proceeds with the following steps:

1.  **Minimax Characterization of Architecture Class:**
    *   Defined `C_L,w,R` as the class of functions realizable by depth-L, width-w ReLU networks with a bounded deep variation norm.
    *   Established the minimax L2 error rate for this class on the unit circle. The rate is pinned between `Ω(Lw²R²/n)` and `Õ(L²w²R²/n)`, which is polynomial in depth `L`, width `w`, and norm bound `R`. This provides the statistical "floor" of what any estimator can achieve.

2.  **Quantifying the NTK Gap:**
    *   Showed that the NTK's sample complexity for a target `f⋆` with dominant frequency `k⋆` is lower-bounded by `Ω((k⋆)²/D²)`.
    *   Proved an *exponential sample-complexity gap* by comparing this NTK lower bound to the minimax upper bound. The gap is exponential whenever the target's Fourier complexity (high `k⋆`) decouples from its architectural complexity (low `L, w, R`).
    *   **Witness Function:** Used the depth-L iterated sawtooth function (`g_L`) as a theoretical example. `g_L` has `O(L)` architectural complexity but a dominant frequency of `2^(L-1)` (exponential Fourier complexity). For this function, NTK regression needs `Ω(4^L)` samples, while the minimax floor is polynomial in `L`.

3.  **Empirical Validation:**
    *   **NTK Spectrum:** Confirmed the predicted `k⁻²` eigenvalue decay of the NTK on the unit circle (E1).
    *   **No Gap on Smooth Targets:** Demonstrated that for bandlimited (smooth) targets, NTK-KRR is competitive with or better than trained networks, showing *no exponential gap*. This serves as a crucial control, validating the dichotomy (E2).
    *   **Exponential Gap on Compositional Targets:** On the hypercube sparse-parity model (a different compositional task), a standard two-layer network (trained via SGD) achieved 4-6 orders of magnitude lower test error than NTK-KRR for comparable sample sizes, realizing the predicted exponential separation (E3b). (The sawtooth was noted to be difficult for SGD to optimize, making sparse parity a better empirical witness).

### Impact

*   **Quantitative Explanation of NTK Sub-Optimality:** This work provides the first quantitative account of *when* and *by how much* the NTK is sub-optimal for compositional learning, moving beyond qualitative observations.
*   **Depth-Explicit Exponential Gap:** It establishes an exponential sample-complexity gap between NTK and deep ReLU networks that explicitly depends on the *depth* of the target's composition, at a *fixed input dimension*. This distinguishes it from prior work that focused on input-dimension-dependent gaps.
*   **Root Cause: Function-Space Mismatch:** The research identifies the fundamental reason for the gap: a mismatch between the NTK's inherent smoothness bias (penalizing high frequencies) and the target's compositional structure (which can generate high frequencies with low architectural cost).
*   **Dichotomy Confirmed:** The results validate the proposed "function-space dichotomy," demonstrating that the NTK performs near-optimally for smooth targets but is exponentially miscalibrated for compositionally sparse, oscillatory ones. The absence of a gap for bandlimited functions reinforces that the NTK is not *generically* worse than networks, but rather poorly suited for specific function classes.
*   **Minimax Baseline:** By comparing against the minimax floor (the best possible performance of any estimator), the study provides a robust and information-theoretic bound on the NTK's sub-optimality.
*   **Advancing Deep Learning Theory:** The minimax characterization of the deep architecture class `C_L,w,R` and the precise quantification of the "lazy" vs. "rich" regime capabilities contribute significantly to the theoretical understanding of deep learning generalization and representation power.