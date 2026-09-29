# Learning Native Reflection in Unified Models with Interleaved Reinforcement Learning

- **Category:** Computer Vision
- **Date:** 2026-09-28
- **Link:** http://arxiv.org/abs/2609.35767v1

---
```markdown
### Problem

Unified multimodal models, capable of both visual understanding and image generation, inherently possess the potential for self-correction: diagnosing flaws in their own generations, revising them, and re-evaluating the outcome in a loop. However, effectively training this "native reflection" loop within a single unified model presents several challenges:

1.  **Ineffective Supervised Fine-tuning (SFT)**: While SFT on reflection trajectories can teach the model *how* to produce reflections and revisions (a "cold start"), it fails to reliably identify and follow high-success repair paths, often leading to sub-optimal or circling corrections.
2.  **Untapped Potential of Naive RL**: Applying reinforcement learning naively by optimizing only the renderer or only one part of the multi-round loop leaves significant performance gains unrealized.
3.  **Limitations of Existing RL Approaches**: Current RL methods for visual generators are typically single-pass (never revising their own renders) or rely on external critics and separate pipelines, preventing end-to-end optimization of the internal reflection-and-revision process.
4.  **Credit Assignment Complexity**: Learning jointly over the entire reflection loop (where the value of a revision is known only after rendering, and potentially multiple rounds later) makes per-round credit assignment combinatorially complex.

### Method

The paper introduces **UMM-Reflection**, a reinforcement learning approach designed to enable multi-round native reflection within a single unified multimodal model (BAGEL backbone).

1.  **Reflection Protocol**: The model follows an interleaved inspect–diagnose–revise loop for up to three rounds. In each round, it observes the request, history, and current image, then emits a structured reflection text (e.g., with `[THINKING]`, `[ACTION]`, `[EDIT]` tags) and either generates a revised image or stops.
2.  **Supervised Initialization (SFT)**: The model is first fine-tuned on multi-round trajectories distilled from external models (GPT-5.5 as critic, Qwen-Image for rendering/editing). This SFT stage teaches the basic interleaved protocol and enables the model to produce meaningful (though not always effective) revisions.
3.  **Whole-Trajectory Reinforcement Learning**:
    *   **Shared-Root Sampling**: For each prompt, `K=16` "sibling" trajectories are generated, all starting from the *same initial image* (which is detached from the computation graph and not optimized by RL). This allows for direct comparison of reflection strategies.
    *   **Trajectory-Level Reward Function**: A frozen verifier assigns a graded alignment score `q_t` to each image. The reward `R(τ)` for a full trajectory `τ` aggregates the final image quality (`q_T`), rewards positive progress (`[Δt]+`), penalizes regressions (`[−Δt]+`), and specifically credits trajectories that show sustained improvement over multiple rounds (`S_multi(τ)`), while also penalizing premature stopping.
    *   **Group-Relative Advantage**: Instead of complex per-round credit assignment, a single advantage `A_i` is computed *per trajectory* based on its reward relative to other siblings in the shared-root group. This avoids the combinatorial explosion of per-round branching.
    *   **Text-Flow Coordination**: Crucially, both the textual reflection policy and the flow-based image renderer *share the same trajectory-level advantage*. This design ensures that reflections leading to better visual outcomes jointly update both the diagnostic text tokens and the subsequent image generation transitions, fostering effective coordination between understanding and generation roles within the same model.
    *   The external verifier and reference policy are used *only during training* to compute rewards; at inference, only the unified UMM-Reflection model is used.

### Impact

UMM-Reflection demonstrates significant improvements in multi-round image generation and self-correction:

1.  **Substantial Performance Gains on GenEval**: It improves GenEval composite accuracy by **+12.05 points** over its SFT counterpart (reaching 0.84 vs. 0.72) and +13 points over the BAGEL-Base model (0.71). These gains are particularly pronounced in complex compositional aspects, with scores for `Position` rising by +42 points, `Color Binding` by +14, and `Counting` by +10 over SFT.
2.  **Increased Repair Reliability**: While SFT can produce meaningful revisions, it repairs only 20.59% of initially incorrect images. UMM-Reflection significantly boosts this conditional repair rate to **64.94%**.
3.  **Strong Transferability to Unseen Benchmarks**: The improvements generalize well to benchmarks not used during RL training:
    *   **WISE**: +10.97 points over SFT.
    *   **T2I-CompBench++**: +4.63 points over SFT.
    *   **OneIG-Bench**: +3.48 points over SFT.
4.  **Mechanism Insight**: The research reveals that SFT already teaches the model to produce *useful revisions*, but RL's role is to make these revisions *reliable* by selecting better repair paths. RL achieves this by guiding failing images into the "correct" region as perceived by the model, without fundamentally altering its core perception or correctness readout.
5.  **Efficient Training Paradigm**: By using whole-trajectory, group-relative advantages, UMM-Reflection avoids the impractical computational cost of per-round credit assignment for image-generating policies and eliminates the need for a learned value model or an external critic at inference.
```