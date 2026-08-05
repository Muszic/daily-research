# CPrefix: A Combinatorial Tensor Framework for Structured Discrete Color Mappings

- **Category:** Computer Vision
- **Date:** 2026-08-04
- **Link:** http://arxiv.org/abs/2608.03863v1

---
## CPrefix: A Combinatorial Tensor Framework for Structured Discrete Color Mappings

### Problem

Traditional representations of discrete multi-channel mappings (e.g., color transformations in imaging, look-up tables) primarily rely on sampled values. While these provide accurate evaluations, they offer **limited insight into the underlying observable structure or combinatorial organization** of the mappings. This lack of structural understanding hinders deeper analysis, such as identifying intrinsic properties or developing more principled transformation methods beyond direct sampling and interpolation.

### Method

The paper introduces **CPrefix**, a novel combinatorial observable representation realized within a unified tensor framework.

1.  **Combinatorial Observable Representation:** CPrefix represents the observable organization of a mapping rather than just its sampled values. This shifts focus from evaluation to understanding structure.
2.  **Counting Tensor:** The core is a structured **counting tensor**, denoted as `T(R,G,B,r,g,b)`. This tensor quantifies the multiplicity of underlying "ternary configurations" (sequences of length `N` from `{0,1,2}`) that are compatible with a given observable state `(R,G,B)` (e.g., an RGB color) and a latent simplex configuration `(r,g,b)`.
3.  **Discrete Pascal Simplex as Latent Space:** The support of this counting tensor forms a discrete Pascal simplex. This simplex is *not* a constraint on the observable space, but rather a **latent combinatorial coordinate system** that organizes observable configurations according to their underlying counting structure (`r+g+b <= N`). This formulation effectively separates the intrinsic combinatorial organization of a mapping from its measured values.
4.  **Representation and Reconstruction:**
    *   Observable representations (`X_obs`) are derived by linearly projecting latent simplex coefficients (`C_inner`) using the tensor: `X_obs = T C_inner`.
    *   Conversely, latent coefficients can be **reconstructed** from observed measurements (`X_obs`) by solving a regularized inverse problem: `C_inner = (T^T T + λI)^-1 T^T X_obs`.
5.  **Generalizability:** The framework is designed to be independent of the physical interpretation of the observables, extending beyond color to other structured multi-channel discrete systems.

### Impact

1.  **Enhanced Structural Insight:** CPrefix provides a quantitative framework to expose and analyze the intrinsic combinatorial structure underlying discrete mappings, moving beyond mere value-based evaluations.
2.  **Faithful Reconstruction:** The framework demonstrates **highly accurate reconstruction** of complex real-world color transformations, specifically ICC display and printer profiles. Perceptual errors (ΔE00) were consistently low, often below the visibility threshold, validating that these measured mappings admit faithful combinatorial observable representations within the CPrefix framework. Reconstruction residuals also provide insights into the compatibility of mappings with this representation.
3.  **Structured Perceptual Gamut Mapping:** The tensor framework naturally induces a principled method for **perceptual gamut mapping** directly within the latent Pascal simplex domain. Preliminary results show smooth, shell-local compression, indicating a promising approach for handling color space transformations.
4.  **Broad Applicability:** While validated on color imaging, the method's independence from physical observable interpretation suggests its applicability to a wide range of structured multi-channel discrete systems, including spectral reconstruction, multi-ink printer separation, metameric analysis, and general structured inverse problems in science and engineering. This positions CPrefix as a fundamental mathematical language for understanding and manipulating such systems.