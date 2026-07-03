# VT-WAM: Visual-Tactile World Action Model for Contact-Rich Manipulation

- **Category:** Robotics
- **Date:** 2026-07-02
- **Link:** http://arxiv.org/abs/2607.02503v1

---
### Problem

Contact-rich manipulation tasks are challenging for robots because success relies on reacting to local interaction states like deformation, pressure, slip, and friction. These critical tactile cues are often temporally sparse, subtle, or invisible in visual observations. Existing visual-tactile policies typically feed tactile observations directly into action prediction but rarely model the explicit dynamics of tactile deformation during action generation. This leads to an imbalance where neural networks, during joint training, tend to favor dense visual evidence over the sparse, but decisive, tactile signals, resulting in underutilized tactile information and unreliable policies during critical contact phases.

### Method

The authors introduce **VT-W AM (Visual-Tactile World Action Model)**, a novel framework that jointly learns future visual prediction, tactile deformation prediction, and action prediction within a unified flow matching objective. VT-W AM's key methodological contributions are:

1.  **Asymmetric Mixture-of-Transformers (MoT) Attention**: This mechanism is designed to efficiently bridge a first-frame visual anchor (for global scene context) with the full temporal sequence of tactile dynamics (for contact evolution). During inference, action queries attend to the entire tactile sequence for detailed contact information, but only to the first-frame visual tokens for general scene context. This asymmetric design enables a "visual-cache inference mode" that provides crucial contact dynamics for action prediction without incurring the latency of predicting future visual frames.
2.  **Contact-gated Action-Visual-Tactile Attention Guidance (AVTAG)**: To mitigate the visual-dominance bias in joint training, AVTAG introduces a training-only auxiliary hinge ranking loss. During identified contact phases, this loss penalizes instances where action queries exhibit lower relative attention to tactile evidence compared to visual evidence. This explicitly guides action queries to prioritize and rely more on tactile signals when local physical interaction is informative, without altering the model's inference-time architecture.

### Impact

VT-W AM demonstrates substantial improvements in performing real-world contact-rich manipulation tasks:

*   **Superior Performance**: Achieved an average success rate of **71.67%** across six diverse real-world contact-rich tasks, encompassing both surface-interaction and constrained insertion scenarios.
*   **Significant Outperformance**: Outperformed leading baselines, including a **26.67%** absolute improvement over Fast-W AM and a **35.84%** improvement over OmniVTLA.
*   **Validated Design**: Ablation studies confirmed the critical importance of both explicitly modeling tactile deformation dynamics and employing the contact-gated attention guidance (AVTAG) for achieving high success rates in contact-rich tasks.
*   **Predictive Capability**: Analysis of visual-tactile prediction confirmed that VT-W AM can generate temporally coherent visual observations and tactile deformation fields, accurately capturing local contact patterns and pressure changes.