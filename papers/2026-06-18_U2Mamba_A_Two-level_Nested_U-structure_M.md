# U$^2$Mamba: A Two-level Nested U-structure Mamba for Salient Object Detection

- **Category:** Computer Vision
- **Date:** 2026-06-18
- **Link:** http://arxiv.org/abs/2606.20282v1

---
This research paper introduces **U2Mamba**, a novel network designed for Salient Object Detection (SOD) that leverages the efficiency of Mamba state space models within a nested U-structure.

### Problem

Existing Mamba-based models, while promising for long-range dependency modeling in vision, often fail to adequately explore contextual information and the full depth of the architecture for Salient Object Detection (SOD). They struggle to balance global context modeling with fine-grained boundary preservation, frequently weakening shallow high-resolution features and lacking SOD-specific hierarchical supervision, limiting their effectiveness for precise SOD tasks. Traditional CNNs lose high-resolution details, and Transformer-based models suffer from quadratic computational complexity, making them impractical for high-resolution and real-time SOD applications.

### Method

The paper proposes **U2Mamba**, a novel nested two-level U-structured network specifically designed for single-modal Salient Object Detection, built from scratch without relying on classification-pretrained backbones. Its core components include:

1.  **Nested U-Structure:** U2Mamba adopts a U2Net-style encoder-decoder architecture with six encoder stages and five decoder stages. This nested design integrates various receptive fields from shallow and deep layers, collecting richer contextual information and longer-range data without being constrained by resolution.
2.  **Multiscale Mamba U-Block (MMUB):** Each stage of the U2Mamba is built upon a newly designed MMUB, which embeds the Mamba state space mechanism into a compact U-shaped residual block. MMUB efficiently captures intra-stage multiscale features by performing most computations on downsampled representations and explicitly retaining high-resolution shallow features. This strategy significantly reduces computational redundancy and memory consumption while preserving fine-grained saliency boundaries, leveraging Mamba's linear complexity for long-range dependency modeling.
3.  **Hierarchical Deep Supervision:** Instead of traditional deep supervision, U2Mamba employs a hierarchical training method where the loss is computed at each level during the training process. This combines Binary Cross-Entropy (BCE) loss for pixel-level accuracy with Kullback–Leibler (KL) divergence loss to align probability distributions across different semantic scales, promoting consistent and coherent representation learning among hierarchical outputs.

### Impact

U2Mamba achieves highly competitive performance against state-of-the-art methods across multiple salient object detection benchmarks (ECSSD, PASCAL-S, DUT-OMRON, HKU-IS, DUTS), demonstrating superior or comparable results in terms of Mean Absolute Error (MAE) and maximum F-measure (maxFβ). It exhibits favorable computational efficiency, with significantly fewer parameters (41.97M) and lower FLOPs (127.5G) than conventional CNN-based (U2Net: 176.3M Params, 142.8G FLOPs) and Transformer-based (VST: 94.7M Params, 198.2G FLOPs) models, leading to faster inference speeds (24.7 FPS on an A100 GPU). Ablation studies confirm the critical contributions of both the Multiscale Mamba U-Block and the hierarchical deep supervision strategy to the model's high performance and validate Mamba's effectiveness over other long-range modeling mechanisms (like dilated convolution and self-attention) for SOD.