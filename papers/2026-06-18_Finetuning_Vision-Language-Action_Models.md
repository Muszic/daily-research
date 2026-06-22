# Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think

- **Category:** Artificial Intelligence
- **Date:** 2026-06-18
- **Link:** http://arxiv.org/abs/2606.20246v1

---
This paper addresses the computational challenges associated with large Vision-Language-Action (VLA) models in robotic manipulation.

### Problem

State-of-the-art continuous control VLA models (e.g., $\pi$0, GR00T-N1.5) are multi-billion parameter architectures that, despite their capabilities, impose **prohibitive computational burdens** during both downstream fine-tuning and real-time inference. This leads to staggering hardware costs, high operational latency, and significant memory overhead. Existing optimization strategies often suffer from narrow scope (focusing on older models), fail to accelerate the expensive fine-tuning phase, or introduce immense architectural complexity through auxiliary routing modules or distillation pipelines. The core underlying issue identified is that these deep VLA models exhibit **severe layer-wise representational redundancy**.

### Method

The authors propose **CKA-guided Layer Pruning (CLP)**, a structural compression pipeline designed to exploit this redundancy. The method is entirely **training-free** and is performed *before* fine-tuning begins.

1.  **Diagnosis of Redundancy**: CLP performs a single forward pass on a small calibration dataset.
2.  **Redundant Layer Identification**: It uses **Centered Kernel Alignment (CKA)** to quantify the representational similarity between consecutive transformer layers in both the VLM backbone and the continuous control policy head. High CKA scores indicate minimal representational change between layers, signaling redundancy.
3.  **Permanent Layer Removal**: Identified "twin" or highly redundant layers are permanently removed from the model, effectively compressing its depth by up to 50%.
4.  **Streamlined Architecture**: This process results in a statically smaller model, eliminating the need for complex auxiliary modules, additional training objectives, or task-dependent runtime decisions required by dynamic methods. The compressed model is then fine-tuned directly using the native training objective.

### Impact

CLP yields substantial benefits in computational efficiency and performance:

*   **Acceleration**: Achieves a **40-50% reduction in training time** and up to **30% faster real-time inference** compared to full-scale models. It also eliminates approximately 30% of trainable parameters.
*   **Performance**: The streamlined architecture consistently **matches or even exceeds** the performance of full-scale base models across various tasks.
*   **Regularization**: The structural compression acts as an effective regularizer in data-scarce regimes. For instance, it boosts success rates from 77.7% to 84.6% when training on only 10% of LIBERO data, and delivers a 15-20% performance boost on real-world tasks with limited datasets (e.g., 100 demonstrations).
*   **Robust Validation**: The method is comprehensively validated across:
    *   Three simulation benchmarks (LIBERO, RoboCasa, SimplerEnv).
    *   Ten diverse real-world manipulation tasks.
    *   Four unique robotic embodiments (Aloha Single/Bimanual, UR10, UR5).

This research demonstrates that advanced VLA models require significantly fewer layers than previously assumed, offering a highly compute-efficient paradigm for scalable robot learning without sacrificing performance or introducing architectural complexity.