# PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference

- **Category:** Computer Vision
- **Date:** 2026-03-26
- **Link:** http://arxiv.org/abs/2603.25730v1

---
# PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference

## Problem

Autoregressive video diffusion models, while promising for long video generation, are bottlenecked by several critical issues:
1.  **Unbounded Memory Growth:** The Key-Value (KV) cache grows linearly with video length, leading to intractable memory requirements. For a 2-minute, 832x480 video at 16 FPS, the KV cache can swell to ~749K tokens, demanding ~138 GB across 30 transformer layers, far exceeding single GPU capacity. Existing solutions like history truncation or sliding windows severely compromise long-range coherence.
2.  **Error Accumulation:** Small prediction errors compound iteratively during autoregressive denoising, causing progressive quality degradation and semantic drift over extended durations. Models like Self-Forcing show a significant decline in text-video alignment, losing prompt semantics within 60 seconds.
3.  **Fundamental Dilemma:** A core challenge is the trade-off between mitigating error accumulation (which requires extensive contextual history) and bounding KV cache growth (which often forces discarding critical memory). Maintaining a large *effective* context window while strictly limiting memory footprint remains an open problem.

## Method

PackForcing addresses these challenges with a unified framework centered on a novel **three-partition KV-cache strategy** and advanced context management techniques:

1.  **Three-Partition KV Cache:** Generation history is categorized into three distinct types, each with a tailored management policy:
    *   **Sink Tokens:** Preserves early anchor frames at full resolution (e.g., first 8 frames) to maintain global semantics and prevent drift. These are never compressed or evicted, consuming <2% of the total token budget but providing a stable global reference.
    *   **Compressed Mid Tokens:** Represents the vast majority of historical context between sink and recent frames. These undergo massive spatiotemporal compression (~32x token reduction per block) via a **dual-branch network**. Memory is strictly bounded by dynamically selecting only the most informative tokens.
    *   **Recent & Current Tokens:** Keeps the most recently generated frames and the current block at full resolution to ensure fine-grained local temporal coherence and smooth transitions.

2.  **Dual-Branch HR Compression:** For mid tokens, a hybrid compression layer achieves ~32x token reduction while retaining rich information:
    *   **HR Branch:** Uses progressive 4-stage 3D convolutions directly on VAE latents to preserve local, fine-grained structural details.
    *   **LR Branch:** Decodes latents to pixel space, applies 3D average pooling, and re-encodes with a frozen VAE encoder to capture complementary global context and perceptual layout.
    *   Outputs from both branches are fused via element-wise addition.

3.  **Dual-Resolution Shifting & Incremental RoPE Adjustment:**
    *   **Dual-Resolution Shifting:** Concurrently computes full-resolution KV for immediate prediction and a reduced-resolution backup. Aging recent tokens smoothly transition into the compressed mid-partition without incurring sequential latency.
    *   **Incremental RoPE Adjustment:** To resolve positional discontinuities caused by managing and dropping tokens from the mid-buffer (due to selection), a temporal-only RoPE adjustment gracefully corrects position gaps, ensuring continuous positional indices across the historical contexts with negligible overhead.

4.  **Dynamic Context Selection:** An advanced top-K selection strategy is applied to the compressed mid tokens, dynamically evaluating query-key affinities to retrieve only the most informative blocks for the current computation, further bounding the active memory.

This hierarchical design ensures a *constant* token count for the attention computation (`O(1)` complexity) regardless of total video length, effectively bounding the memory footprint while comprehensively retaining historical information.

## Impact

PackForcing significantly advances long-video generation capabilities:

*   **Extended Generation Length:** Enables the generation of coherent 2-minute, 832x480 videos at 16 FPS on a single H200 GPU.
*   **Memory Efficiency:** Achieves a strictly bounded KV cache of just ~4 GB per transformer layer, making minute-scale video generation feasible on commodity hardware.
*   **Temporal Extrapolation:** Demonstrates a remarkable **24x temporal extrapolation** (5s training clips -> 120s generation), proving that short-video supervision is sufficient for high-quality, long-video synthesis, even operating effectively zero-shot.
*   **State-of-the-Art Quality:** Achieves state-of-the-art results on VBench, with superior temporal consistency (26.07) and dynamic degree (56.25) compared to prior methods.
*   **Reduced Semantic Drift:** Maintains the most stable CLIP score trajectory among all compared methods, effectively mitigating error accumulation and semantic drift over long durations.