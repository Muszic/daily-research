# From Imagined Futures to Executable Actions: Mixture of Latent Actions for Robot Manipulation

- **Category:** Robotics
- **Date:** 2026-05-12
- **Link:** http://arxiv.org/abs/2605.12167v1

---
Here's a summary of the research paper "From Imagined Futures to Executable Actions: Mixture of Latent Actions for Robot Manipulation" in Markdown format:

```markdown
### Problem

Existing robot manipulation approaches that leverage video generation models for "imagined futures" face a significant challenge: effectively translating these predicted future observations into executable actions. Current methods either use predicted frames as policy input or directly decode them into actions, but both suffer from a fundamental mismatch. Video generation models prioritize perceptual realism over action-centric control relevance, meaning their predictions emphasize visual fidelity rather than the underlying physical causes of state transitions. This leads to indirect, unstable, and perceptually-driven rather than action-oriented control.

### Method

The authors propose **MoLA (Mixture of Latent Actions)**, a control-oriented interface that transforms imagined future videos into executable representations. Instead of directly using predicted frames, MoLA infers a structured, physically grounded "mixture of latent actions" implied by these visual transitions.

1.  **Video Generation Model:** MoLA uses a frozen Stable Video Diffusion (SVD) model to synthesize long-horizon future visual rollouts (imagined futures) conditioned on the current observation and task instruction.
2.  **Mixture of Inverse Dynamics Models (MoIDM):** This is the core latent-action interface.
    *   **Pretraining:** Individual modality-aware inverse dynamics models are pretrained on large-scale robot datasets. Each model is specialized to capture distinct cues: semantic (using SAM2), depth (using Depth Anything v2), and motion flow (using CoTracker3). They infer discrete latent actions by modeling the causal transition between a current and future RGB frame, using modality-specific spatiotemporal transformers and VQ codebooks.
    *   **Integration:** In the MoLA framework, the pretrained MoIDM takes the *predicted* future RGB frames from the video generation model and infers a "mixture of latent actions" (semantic, depth, flow) that explain the imagined visual transitions.
3.  **Action Head:** A Diffusion Transformer architecture is trained to decode this mixture of latent actions, combined with visual features of the predicted future frames, into executable robot control commands using a flow matching objective.

The training process involves three stages: fine-tuning the video generation model, pretraining the MoIDM (independently), and then jointly fine-tuning the MoIDM and action head end-to-end, while keeping the video generation model frozen.

### Impact

MoLA achieves significant improvements in robot manipulation performance, demonstrating its effectiveness across various benchmarks and real-world scenarios:

*   **Superior Performance:** Achieves the highest average success rates across challenging simulated benchmarks including CALVIN (ABC-D split), LIBERO (all four task suites), and LIBERO-Plus (10,030 tasks), consistently outperforming existing approaches. On LIBERO-Plus, MoLA surpasses the strongest baseline (OpenVLA-OFT+) by an average of 13.2% in success rate.
*   **Enhanced Generalization and Consistency:** The results indicate stronger multi-task learning capabilities, improved temporal consistency, and superior generalization performance in simulated environments.
*   **Data Efficiency:** Demonstrates better data efficiency, especially in low-data regimes, outperforming baselines even with limited training data (e.g., 10% of the dataset), showcasing its ability to leverage pretrained representations effectively.
*   **Real-world Validation:** Proven effective on real-world robot manipulation tasks using a UR5e robotic arm, validating its practical applicability beyond simulation.
*   **Key Contributions:** The paper introduces a novel latent-action interface for imagination-based robot manipulation, proposes MoLA as a model that effectively couples video generation and action through modality-aware inverse dynamics, and provides extensive experimental validation.
```