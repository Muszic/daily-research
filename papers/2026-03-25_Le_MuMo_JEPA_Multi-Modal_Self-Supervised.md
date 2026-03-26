# Le MuMo JEPA: Multi-Modal Self-Supervised Representation Learning with Learnable Fusion Tokens

- **Category:** Computer Vision
- **Date:** 2026-03-25
- **Link:** http://arxiv.org/abs/2603.24327v1

---
```markdown
### Problem

Most self-supervised learning (SSL) methods operate on a single modality, failing to leverage the complementary information available from heterogeneous sensors like RGB cameras, LiDAR depth, or thermal infrared. Learning unified representations from these diverse signals remains a significant challenge, as existing multi-modal perception models often rely on costly, large-scale supervised annotations. Extending SSL, particularly JEPA-based methods, to multi-modal settings requires addressing issues of differing stream structures, ensuring meaningful alignment, and facilitating efficient cross-modal interaction without incurring the quadratic computational cost of unrestricted all-to-all token mixing.

### Method

Le MuMo JEPA (Learnable Multi-Modal Joint-Embedding Predictive Architecture) is a self-supervised framework that extends LeJEPA to jointly learn unified representations from RGB images and aligned companion modalities (e.g., LiDAR depth or thermal images).

Key components:

*   **Shared 2D Spatial Grid:** Both RGB and companion modalities are processed into 2D patch grids with modality-specific embeddings, enabling them to be handled within a single Vision Transformer (ViT).
*   **Learnable Fusion Tokens:** A set of `N` learnable tokens (equal to the number of spatial patches) acts as a Perceiver-style latent bottleneck. These tokens aggregate information from spatially corresponding RGB and companion-modality patches through attention.
*   **Pruned Fusion Strategy (Default):** In the first transformer layer (Layer 0), each fusion token attends to its spatially corresponding RGB patch, companion-modality patch, and the CLS token. Critically, after Layer 0, the original `2N` RGB and companion-modality tokens are *pruned* from the sequence. This forces the model to compress useful cross-modal information into the shared fusion-token grid early, creating an efficient latent bottleneck and reducing the computational cost of subsequent layers by approximately 9x.
*   **Training Objective:** The model applies LeJEPA's Sketched Isotropic Gaussian Regularization (SIGReg) objective to the *joint multimodal CLS embedding*. SIGReg encourages the combined embedding distribution to match an isotropic Gaussian (N(0,I)), providing a modality-agnostic target that aligns modalities without relying on pairwise contrastive matching or stop-gradients. An invariance loss is also included. The spatial fusion tokens are implicitly updated through the CLS token's attention to them.

### Impact

Le MuMo JEPA achieves a strong performance-efficiency trade-off and consistently outperforms baselines across various multi-modal perception tasks:

*   **Superior Performance:** On Waymo and nuScenes datasets (RGB-LiDAR depth), Le MuMo JEPA provides the strongest results on downstream patch probes. This includes state-of-the-art performance for CenterNet-style 3D object detection (mAP XY and XZ), dense depth estimation (lower MAE), and semantic segmentation (higher mIoU), demonstrating its ability to learn high-quality, object-centric multi-modal representations. It significantly outperforms single-modality baselines (RGB-only LeJEPA, LiDAR-only, DINOv3-style RGB) and other multi-modal SSL approaches (MultiMAE, ImageBind), as well as simpler early/late fusion methods.
*   **Efficient Architecture:** The pruned fusion strategy acts as an efficient latent bottleneck, substantially reducing compute, memory, and estimated training time compared to persistent fusion or full token concatenation, while still maintaining or improving performance.
*   **Robust Transfer Learning:** On the Teledyne FLIR ADAS benchmark (RGB-thermal), the Waymo-pretrained Le MuMo JEPA encoder transfers more effectively than other multimodal baselines without FLIR fine-tuning, and achieves the best 2D detection transfer results after fine-tuning.
*   **Effective Modality-Agnostic Alignment:** By extending SIGReg to a joint multimodal CLS embedding, Le MuMo JEPA successfully learns unified representations across modalities without auxiliary alignment labels, addressing a key challenge in multi-modal SSL.

In summary, Le MuMo JEPA provides an efficient and effective framework for multi-modal self-supervised representation learning, enabling superior performance on critical perception tasks for autonomous driving and other real-world applications.
```