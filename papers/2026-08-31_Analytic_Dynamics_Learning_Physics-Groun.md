# Analytic Dynamics: Learning Physics-Grounded Representation for Fast Intrinsic Dynamics Inference from Monocular Videos

- **Category:** Computer Vision
- **Date:** 2026-08-31
- **Link:** http://arxiv.org/abs/2608.31025v1

---
Here's a summary of the research paper "Analytic Dynamics" in Markdown format:

### Problem

Inferring intrinsic object dynamics (material models and parameters) from monocular visual observations is crucial for intelligent agents but remains challenging. The core difficulty lies in the fundamental gap between indirect 2D visual evidence and underlying 3D physical dynamics, which are often entangled with appearance, geometry, and viewpoint.

Existing approaches have significant limitations:
*   **Per-scene optimization methods:** Achieve accuracy but are computationally expensive, require extensive simulation-optimization iterations, and lack scalability to unseen objects.
*   **Vision-Language Model (VLM) based methods:** Offer efficiency but rely on commonsense knowledge, leading to noisy and coarse-grained predictions and susceptibility to appearance/geometry shortcuts.
*   **Feed-forward methods from static 3D assets:** Provide appearance and geometry, which are inherently ambiguous for dynamics inference, as visually identical objects can have different intrinsic dynamics.
*   **Monocular videos:** While capturing behavioral evidence, they only provide 2D projections, making it difficult for models to distinguish dynamics-relevant patterns from spurious correlations.

### Method

The paper proposes **Analytic Dynamics**, a two-stage feed-forward dynamics inference framework that bridges the gap between visual observations and intrinsic dynamics by introducing an intermediate **physics-grounded dynamics representation**.

1.  **Dynamics Data Generation and Benchmark:**
    *   A simulator-based pipeline using the Material Point Method (MPM) is developed to generate a benchmark of 9,000 dynamics instances.
    *   Each instance includes:
        *   Paired **privileged physical-state trajectories** (position, normalized displacement, and deformation gradient fields). These are accessible only in simulation.
        *   Synchronized **monocular mask videos** (to focus on motion/deformation, not texture/color).
        *   Ground-truth material models and parameters.

2.  **Stage I: Physics-Grounded Dynamics Representation Learning (Teacher Model)**
    *   A **trajectory teacher** (P4Transformer) is trained using the privileged physical-state trajectories.
    *   It learns a structured dynamics representation space (`z_T`) by performing:
        *   Material family classification.
        *   Material parameter regression (using a normalized L1 loss, RegL1).
    *   This stage explicitly learns dynamics-relevant patterns directly from 3D physical responses, creating a "physics-grounded" representation. The teacher model is then frozen.

3.  **Stage II: Visual Dynamics Representation Distillation (Student Model)**
    *   A **video student** (UniFormer encoder) processes monocular mask videos.
    *   It is trained with two main objectives:
        *   **Representation Alignment:** Align its visual representation (`z_V`) with the *frozen* physics-grounded representation (`z_T`) from Stage I, using a combination of cosine and L1 distances. This introduces a physics-grounded inductive bias.
        *   **Task Supervision:** Directly predict material family (classification) and parameters (regression), similar to the teacher.
    *   This distillation guides the visual model to capture dynamics-relevant information from videos, rather than appearance/geometry shortcuts, promoting generalization. At inference time, only the video student is used.

### Impact

*   **Efficient and Accurate Inference:** Analytic Dynamics achieves fast inference (3.83 milliseconds per object) while maintaining high accuracy in material model classification and parameter regression.
*   **Strong Generalization:** The framework demonstrates superior out-of-distribution (OOD) generalization to unseen object shapes (e.g., 34% improvement in regression accuracy on OOD shapes), significantly outperforming VLM/Video-LLM baselines and often matching or exceeding per-scene optimization in visual reconstruction quality without test-time optimization.
*   **Physics-Grounded Representations:** The two-stage distillation effectively transfers a physics-grounded inductive bias to the visual model. This results in learned representations that are less dependent on object geometry, continuously organized by intrinsic dynamics (e.g., stiffness), and robust to dynamics-irrelevant factors.
*   **Novel Benchmark:** The development of a scalable dynamics data generation pipeline and benchmark provides a valuable resource for future research in intrinsic dynamics inference from videos.
*   **Key Insights:** The research highlights the critical importance of incorporating **deformation gradients** and **normalized displacements** in privileged physical states for learning transferable dynamics representations, improving both Stage I performance and Stage II distillation efficacy.