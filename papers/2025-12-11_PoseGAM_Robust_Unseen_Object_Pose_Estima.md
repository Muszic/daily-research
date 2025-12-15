# PoseGAM: Robust Unseen Object Pose Estimation via Geometry-Aware Multi-View Reasoning

- **Category:** Computer Vision
- **Published:** 2025-12-11
- **Source:** [Original ArXiv Link](http://arxiv.org/abs/2512.10840v1)

---

## 🧐 Problem Statement
The paper addresses the challenge of **robust 6D object pose estimation for unseen objects**. Traditional methods for 6D pose estimation typically focus on instance-specific or category-specific objects, failing to generalize to novel objects encountered after training. Existing approaches that attempt to generalize often rely on explicit feature matching between a query image and a 3D object model or template images. This reliance makes their performance susceptible to inaccuracies when feature matching is unreliable or when there are significant appearance inconsistencies between rendered CAD models and real-world observations. Furthermore, current multi-view foundation models, while capable of inferring 3D geometry, lack explicit 3D object model information and are sensitive to these appearance variations, limiting their effectiveness for object pose estimation.

## 🛠️ Methodology
The authors propose **PoseGAM**, a geometry-aware multi-view framework that directly predicts 6D object pose in an end-to-end manner, eliminating the need for explicit feature matching.

1.  **Multi-View Network Architecture**:
    *   Inspired by recent multi-view foundation models (e.g., VGGT), PoseGAM uses a multi-view network that jointly processes a query image and multiple template images rendered from known camera poses of the target object.
    *   It extracts visual feature tokens from RGB images (using DINOv2) and encodes camera poses into dedicated camera tokens.
    *   The network employs an alternating attention transformer with inter- and intra-frame self-attention layers to process these multi-view tokens.
    *   A lightweight head decodes the camera tokens to predict the object-to-camera transformation.

2.  **Geometry Integration Mechanisms**:
    *   To overcome the limitations of purely visual inputs, PoseGAM incorporates object geometry information through two complementary mechanisms, injected via **cross-attention** operations before each self-attention layer:
        *   **Explicit Point-Based Geometry**: Depth maps are rendered from the 3D object mesh and known camera poses, then reconstructed into point maps. These point maps are processed by a lightweight CNN to generate point map tokens.
        *   **Learned Geometry Features**: An off-the-shelf point cloud network (e.g., PointTransformer v3) extracts per-point feature embeddings from the object's 3D point cloud (augmented with color and normals). Crucially, these per-point features are spatially reorganized into a **view-map format** (Feature Maps) and then encoded into feature tokens using a lightweight CNN.
    *   These point map tokens and feature tokens are combined to form the Key/Value inputs for the cross-attention, allowing the network to effectively reason about object poses by integrating geometric structure.

3.  **Large-Scale Synthetic Dataset Construction**:
    *   To enhance robustness and generalization to unseen objects and diverse conditions, a synthetic dataset was created with over 190,000 high-quality 3D object assets collected from various public sources.
    *   Objects were standardized through **texture re-baking** to ensure consistent material representation across different rendering platforms.
    *   For each object, 50 multi-view images and corresponding geometry-related maps (depth, normal, mask) were rendered.
    *   Query images were generated under four distinct, challenging scenarios: centric, uncentric, uncentric with varying HDR lighting (using Blender Cycles for physical accuracy), and centric/uncentric with **appearance-edited textures** (using DDIM inversion and a text-conditioned diffusion model FLUX to introduce inconsistencies while preserving geometry).

## 📊 Results & Impact
PoseGAM demonstrates **state-of-the-art performance** in unseen object 6D pose estimation, significantly improving upon prior methods:

*   **Superior Performance on Benchmarks**: Achieved the highest average Average Recall (AR) of **41.1%** across five widely used BOP benchmark datasets (LM-O, T-LESS, YCB-V, TUD-L, IC-BIN), outperforming the previous best approach (FoundPose) by 3.3% absolute AR (37.8%) and yielding an average AR improvement of **5.1%** over prior methods.
*   **Significant Gains on Individual Datasets**: Demonstrated remarkable gains on specific datasets, achieving up to a **17.6% improvement** on the TUD-L dataset, which has simpler scenes well-aligned with the synthetic training data conditions.
*   **Enhanced Generalization**: The extensive evaluations confirm PoseGAM's strong generalization capabilities to unseen objects across diverse real-world scenarios, attributed to its geometry-aware design and comprehensive synthetic training data.
*   **Validation of Geometry Integration**: Ablation studies confirmed the critical role of geometry information. Incorporating point maps alone notably improved AUC metrics, and further adding learned geometry features in a view-map format yielded additional performance gains. Baseline multi-view foundation models (VGGT) without explicit geometry integration showed significantly poorer performance (AR 16.3%), validating the necessity of PoseGAM's approach.
*   **Impact of Dataset Diversity**: The constructed large-scale synthetic dataset, featuring varied lighting, appearance, and camera conditions, proved crucial for the model's robustness and ability to generalize effectively to complex real-world challenges.

