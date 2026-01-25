# HyperAlign: Hypernetwork for Efficient Test-Time Alignment of Diffusion Models

- **Category:** Computer Vision
- **Date:** 2026-01-22
- **Link:** http://arxiv.org/abs/2601.15968v1

---
Here's a summary of the research paper "HyperAlign: Hypernetwork for Efficient Test-Time Alignment of Diffusion Models" in Markdown:

### HyperAlign: Hypernetwork for Efficient Test-Time Alignment of Diffusion Models

**Problem:**
Diffusion models, despite their state-of-the-art generative capabilities, frequently produce outputs that poorly align with human preferences and intentions, leading to images with low aesthetic quality and semantic inconsistencies. Existing alignment approaches face significant trade-offs:
1.  **Fine-tuning methods** (e.g., RL-based) can suffer from reward over-optimization, which leads to a severe loss of diversity and creativity in generated outputs.
2.  **Test-time scaling methods** (e.g., gradient-based guidance) introduce substantial computational overhead during inference due to gradient calculations and repeated sampling, and often under-optimize the target rewards because their injected priors are isolated from the model's training dynamics.
The core challenge is to achieve efficient *and* effective test-time alignment that adapts to specific inputs without sacrificing diversity or incurring prohibitive computational costs.

**Method:**
The authors propose **HyperAlign**, a novel framework that trains a hypernetwork for efficient and effective test-time alignment of diffusion models.
1.  **Dynamic LoRA Prediction:** Instead of directly modifying latent states or fine-tuning the base model, HyperAlign trains a hypernetwork to dynamically generate **low-rank adaptation (LoRA) weights**. These weights modulate the diffusion model's generation operators at each denoising step.
2.  **Input-Adaptive Adjustments:** The hypernetwork takes the current latent state (`xt`), timestep (`t`), and user prompt (`c`) as input. It uses a perception encoder (derived from the U-Net) and a transformer decoder to process these inputs and output the step-specific `∆θt` LoRA weights. This allows the denoising trajectory to be adaptively adjusted based on input conditions for reward-conditioned alignment.
3.  **Efficiency Variants:** To balance performance and efficiency, HyperAlign introduces three strategies for weight generation:
    *   **HyperAlign-S (Step-wise):** Generates new LoRA weights at every denoising step for fine-grained alignment.
    *   **HyperAlign-I (Initial):** Generates LoRA weights only once at the starting point (`T`) and applies them throughout all steps for minimal computation.
    *   **HyperAlign-P (Piece-wise):** Generates new LoRA weights only at a few *key timesteps* (identified by analyzing temporal dynamics), sharing weights within segments to balance efficiency and performance.
4.  **Training Objective:** HyperAlign optimizes the hypernetwork using a combined loss:
    *   A primary **reward score objective (`LR`)** to maximize reward signals and align the latent trajectory with the true conditional distribution.
    *   A **preference regularization term (`LG`)**, which encourages the learned denoising conditional score to match the score in preferred data, thereby mitigating reward hacking and preserving generation quality and fidelity.

**Impact:**
HyperAlign demonstrates significant improvements in aligning diffusion models with human preferences and intentions:
1.  **Superior Performance:** It significantly outperforms existing state-of-the-art fine-tuning (e.g., DanceGRPO, MixGRPO, SRPO) and test-time scaling (e.g., Best-of-N, ε-greedy, FreeDoM, DyMO) baselines across various metrics.
2.  **Enhanced Quality:** The method effectively enhances semantic consistency with text prompts and improves the visual appeal and aesthetic quality of generated images.
3.  **Efficiency and Flexibility:** HyperAlign offers an efficient and flexible approach to test-time alignment, amortizing costly optimization into a learnable process. The different generation strategies provide a trade-off between computational cost and alignment granularity.
4.  **Broad Applicability:** The proposed framework is compatible with different generative paradigms, validated on popular diffusion models like Stable Diffusion V1.5 and rectified flow models like FLUX.