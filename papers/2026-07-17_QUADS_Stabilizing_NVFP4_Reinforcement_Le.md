# QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides

- **Category:** Machine Learning
- **Date:** 2026-07-17
- **Link:** http://arxiv.org/abs/2607.15810v1

---
Here's a summary of the research paper:

### QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides

**Problem:**
Rollout generation is a significant bottleneck in Reinforcement Learning (RL) for Mixture-of-Experts (MoE) Large Language Models (LLMs). While low-precision formats like NVFP4 offer substantial acceleration (up to ~2x over FP8, ~4x over BF16) by enabling native W4A4 (4-bit weights, 4-bit activations) GEMMs, directly applying it to MoE RL rollout causes severe instability. Naive NVFP4 rollout with BF16 training collapses within roughly 150 steps, exhibiting rapidly growing log-probability gaps between the rollout and trainer policies. This instability arises because NVFP4's coarse E2M1 (2-bit exponent, 1-bit mantissa) core amplifies quantization errors beyond what standard importance sampling can correct. Through training–inference error analysis, the authors identified activation quantization error (amplified by online recomputation and engine mismatch `η`), rather than weight quantization error, as the dominant source of this critical instability.

**Method:**
To stabilize NVFP4 RL for MoE, the authors propose **QUantization-error Alignment across Dual Sides (QUADS)**, a two-pronged strategy:

1.  **Trainer-side: Asymmetric Quantization-Aware Training (QAT):**
    *   On the trainer side, a novel asymmetric QAT scheme is introduced. It fake-quantizes model weights to NVFP4 (W4) during training while keeping activations unquantized (A16).
    *   This design leverages the fact that weights are synchronized across engines, allowing a matched quantization-dequantization (QDQ) path to eliminate weight error. Conversely, activations are recomputed online with inherent numerical differences (`η`), meaning symmetric W4A4 fake quantization would amplify, rather than reduce, the activation-related training–inference mismatch.

2.  **Rollout-side: Residual Activation Compensation:**
    *   On the rollout side (inference engine), residual activation compensation is implemented. This technique corrects high-error activation channels by applying a second-pass quantization specific to these channels.
    *   This compensation step is carefully designed and implemented with fused kernels to preserve the high throughput advantage of native W4A4 GEMMs, while effectively reducing the remaining activation error and closing the log-probability gap that asymmetric QAT alone cannot fully resolve.

**Impact:**
QUADS successfully stabilizes NVFP4 RL for MoE, achieving BF16-level accuracy while significantly improving rollout performance:

*   **Accuracy:** It matches the BF16 baseline accuracy, reaching 72.86% average pass@1 across four held-out benchmarks, compared to the 73.15% BF16 baseline and the severe degradation of naive NVFP4 training (51.37%).
*   **Performance:** It improves average pass@1 by **21.49 points** over naive NVFP4 RL.
*   **Throughput:** It delivers approximately **16% higher rollout throughput** than FP8-based RL systems, making NVFP4 a viable and efficient low-precision option for accelerating the critical rollout phase of MoE RL.