# Fourier Preconditioning for Neural Feature Learning

- **Category:** Machine Learning
- **Date:** 2026-07-02
- **Link:** http://arxiv.org/abs/2607.02199v1

---
```markdown
## Summary of "Fourier Preconditioning for Neural Feature Learning"

### Problem
Mutual Information (MI)-inspired neural feature learning, while effective for capturing nonlinear dependencies in low-dimensional embeddings, suffers from significant "truncation error" when implemented with practical, finite-width neural networks. Theoretically, the underlying H-Score objective is invariant to invertible input transformations. However, under the constrained approximation classes of finite-width networks and limited training data, the learned representation becomes highly sensitive to the input basis. This sensitivity prevents the networks from efficiently capturing dependence structures, leading to suboptimal feature extraction, particularly in resource-constrained (low-data) regimes where existing methods like PCA/CCA are also unreliable due to noisy covariance estimates.

### Method
The authors propose a novel **input preconditioning step** for H-Score networks to minimize finite-width truncation error. Their core method involves:
1.  **Unitary Preconditioning:** Recognizing that the projection error of the H-Score network (which truncates to a fixed number of modes) depends on how well the input basis aligns dominant singular values with the network's approximation capacity, they seek a unitary transformation that concentrates predictive dependence.
2.  **Fast Fourier Transform (FFT) as Preconditioner:** For processes that are approximately stationary, the Fast Fourier Transform (FFT) is identified as an effective, data-independent, and low-cost preconditioner. The FFT approximately diagonalizes the cross-covariance matrix in the frequency domain, thereby concentrating the cross-covariance singular value spectrum into fewer dominant modes.
3.  **Training-Free Spectral Metrics:** To quantitatively predict the suitability of FFT preconditioning for a given dataset, the authors introduce two training-free metrics derived from the singular value spectrum of the empirical cross-covariance operators:
    *   **Normalized Spectral Entropy (H):** Measures the concentration of predictive information.
    *   **Entropy Ratio (ER):** The ratio of spectral entropy in the frequency domain ($H_f$) to the temporal domain ($H_t$). An $ER < 1$ indicates better concentration in the frequency domain, predicting reduced truncation error.
    *   **Cumulative Energy Rank (CER):** Estimates the minimum latent dimension required to retain a certain percentage of total dependence energy.
4.  **Experimental Validation:** H-Score feature extraction networks (Echo State Network for `f`, MLP for `g`) were trained on eight multivariate datasets, comparing performance (NMSE of a downstream MLP predictor) with no preconditioning, random rotation, and FFT preconditioning. Metrics were computed *prior* to training to assess their predictive power.

### Impact
The research demonstrates significant improvements in neural feature learning and provides a principled way to select input bases:
*   **Performance Enhancement:** FFT preconditioning substantially reduces prediction error, achieving up to **50% normalized mean squared error (NMSE) reduction** in downstream inference tasks, especially impactful in resource-constrained (low-data) regimes.
*   **Predictive Metrics:** The proposed training-free spectral metrics (Entropy Ratio) accurately predict when FFT preconditioning will be beneficial or detrimental. They showed a statistically significant correlation with observed performance gains, correctly identifying cases (like aperiodic "wine" datasets) where spectral preconditioning would degrade performance.
*   **Efficiency and Robustness:** FFT offers a low-cost, data-independent preconditioning step that enhances the robustness and efficiency of H-Score networks. This makes them more effective in real-world scenarios where data scarcity or computational limits are common.
*   **New Design Paradigm:** The work shifts focus from solely optimizing neural network architecture to also considering and optimizing the structure of the input data, offering a complementary approach to improve feature learning.
```