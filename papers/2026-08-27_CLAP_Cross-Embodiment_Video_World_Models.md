# CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators

- **Category:** Artificial Intelligence
- **Date:** 2026-08-27
- **Link:** http://arxiv.org/abs/2608.27406v1

---
## Problem

State-of-the-art action-conditioned video world models are typically restricted to single robot embodiments, preventing them from leveraging the vast and diverse corpus of internet-scale video data (including human and robotic agents). This limitation hinders their ability to learn generalizable physical priors and achieve robust, real-world generalization. The core challenge lies in the inherent heterogeneity of action representations across different robot platforms and the complete absence of action labels in most human videos.

## Method

CLAP (Cross-Embodiment Video World Models) is a framework designed to train action-conditioned video generation models on diverse, internet-scale video data by leveraging the insight that universal physical laws govern spatiotemporal dynamics regardless of the actor. It addresses the cross-embodiment challenge through three core contributions:

1.  **Action Space Harmonization:** Reconciles disparate action spaces across human and robot morphologies using:
    *   **End-effector (EE) Poses (CLAP-EE):** Adopts a 7-DoF operational space (translation, Euler angles, gripper) as a unified, task-relevant representation. It maps joint positions via forward kinematics and normalizes disparate action ranges to `[-1,1]` bounds. This enables fine-grained control but requires labeled data.
    *   **Natural Language Instructions (CLAP-LANG):** Projects numerical end-effector actions into concise, templated text (e.g., "x=, y=..."). It uses relative-action spaces to improve information density. While versatile, it offers lower precision due to tokenizer limitations.
    *   **Learned Latent Actions (CLAP-LAM):** Utilizes a VAE to learn low-dimensional proxy actions from pairs of video frames `(ft, ft+Δt)` through self-supervision on a reconstruction loss. This allows training on massive amounts of unlabeled video data, crucial for scaling. However, it requires downstream alignment for real-world deployment.

2.  **Curriculum-Based Latent-to-EE Actions (CLAP-CURR):** To overcome the individual limitations of each action representation, CLAP introduces a curriculum-based learning strategy:
    *   **Phase 1 (Latent Pretraining):** Learns foundational physical priors from unlabeled video data using latent actions (CLAP-LAM). This harnesses the scale of diverse, unannotated videos.
    *   **Phase 2 (EE Refinement):** Retains the pretrained video model backbone, swaps the action head for one compatible with 7-dimensional end-effector actions, and jointly trains the new head and backbone on action-labeled data. This grounds the learned priors directly in end-effector action spaces, enabling zero-shot deployment without requiring separate alignment layers.

3.  **Data-Efficient Adaptation to Target Morphologies:** CLAP establishes a novel paradigm for training high-fidelity single-embodiment video world models:
    *   **Pretrained Embodiments:** For robots already seen during training, CLAP's models provide strong priors that can be readily adapted via *few-shot finetuning* on the robot's native end-effector action space, without architectural modifications. This is shown to be superior to training from scratch.
    *   **Novel Embodiments:** For markedly different morphologies (e.g., bimanual robots, humanoids), the action head is replaced with a new one compatible with the target embodiment, while retaining the main cross-embodiment video model backbone. This allows sample-efficient transfer of learned spatiotemporal priors.

The core model architecture utilizes a video diffusion paradigm, specifically latent video diffusion models with a VAE for video tokenization and a U-Net for spatiotemporal modeling. It incorporates history conditioning and multi-view video prediction for richer temporal context and geometric consistency.

## Impact

CLAP achieves significant breakthroughs in action-conditioned video world modeling:

*   **Zero-Shot Real-World Generalization:** Demonstrates zero-shot generalization to real-world manipulation tasks through inference-time cross-policy planning and reinforcement-learning-based policy finetuning within video world models. It improves the performance of state-of-the-art robot policies like π0.5 and MolmoAct-2.
*   **Superior Performance:** Approaches or surpasses state-of-the-art *single-embodiment* video models in challenging environments (e.g., DROID). Its performance advantages compound further via sample-efficient, few-shot adaptation to target embodiments.
*   **Most Comprehensive Suite:** Delivers the most comprehensive suite of action-conditioned video world models to date, spanning diverse action-conditioning spaces (end-effector, language, and latent) and a wide range of robot morphologies (e.g., DROID, Bridge, bimanual YAM robots, and G1 humanoids, in addition to general cross-embodiment capabilities).
*   **Novel Training Paradigm:** Establishes a new, sample-efficient method for training high-fidelity single-embodiment video world models by adapting pre-trained cross-embodiment models, outperforming methods that train from scratch.
*   **Open-Source Contribution:** All code and models are open-sourced, facilitating further research and development in the field.