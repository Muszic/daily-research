# A Schema Bounded Language Model for Refining Robot Policies Without Destabilizing Local Learning

- **Category:** Artificial Intelligence
- **Date:** 2026-09-04
- **Link:** http://arxiv.org/abs/2609.05133v1

---
This paper proposes a decentralized multi-robot system that integrates Large Language Models (LLMs) for high-level policy reasoning with local reinforcement learning (RL) for low-level action control, ensuring temporal decoupling and stable local learning.

---

### Problem

The core problem addressed is enabling heterogeneous multi-robot systems to leverage LLMs for policy generation and refinement in decentralized navigation tasks, while simultaneously allowing local controllers to perform tick-level (high-frequency) action selection. The challenge lies in:
1.  **Temporal Decoupling:** Preventing LLM inference from being called for every single action, which is computationally expensive and introduces latency, thus destabilizing local, high-frequency control loops.
2.  **Decentralized Coordination:** How robot-specific LLM policies can be refined from shared completed-round information without centralizing policy ownership or action selection.
3.  **Policy Interface:** Designing an explicit interface between LLM-generated policies and local learning-based action selection that maintains the LLM's role at the policy level.

### Method

The proposed solution is a **decentralized two-tier architecture** where each robot operates as a composite agent comprising a NetLogo turtle, a dedicated LLM policy agent, an Upper Confidence Bound (UCB1) bandit, and a Double Deep Q-Network (Double DQN) controller.

1.  **One-LLM-per-Robot & Decentralized Ownership:** Each robot has its own LLM (e.g., Llama-3.3, Phi-4, Meta-Llama-3.1), maintaining robot-local policy ownership and learning states. No central LLM generates team actions.
2.  **Temporal Decoupling:**
    *   **Round-Level Policy Generation/Refinement:** LLM inference is confined to round boundaries for generating or refining a robot's policy. Each LLM is called only once per round (after initialization) to update its policy for the next round.
    *   **Tick-Level Action Selection:** A robot-local **policy-conditioned Double DQN** controller performs tick-level action selection based on the currently active LLM-generated policy parameters.
3.  **Cross-LLM Communication via Shared Board:** Robots exchange information through a **shared text board** that aggregates completed-round summaries. These summaries include policies, outcomes, rationales, DQN feedback, and UCB advice from all robots. Each LLM reads this board to inform its *own* next policy refinement, but it only generates its *own* robot's policy.
4.  **UCB-Guided Policy Refinement:** A robot-local UCB1 bandit selects one of five interpretable LLM refinement modes (e.g., `KEEP_CURRENT`, `ADOPT_BEST_SHARED`, `EXPLORE_NEW`) for its dedicated LLM to use in the subsequent round. UCB credits are based on successful completion time, driving exploration-exploitation of refinement strategies.
5.  **Policy-Conditioned Double DQN:**
    *   The DQN's 15-dimensional state input concatenates navigation variables, *active policy parameters* (from the LLM), and the **LLM's action prior** (a soft recommendation).
    *   The LLM's prior acts as a bias (`β`) in the DQN's action selection, guiding exploration without overriding the learned Q-values or forcing tick-level actions, thus preserving local learning.
    *   The DQN learns from local rewards (e.g., penalties for moving away, bonuses for success) and updates its online and target networks.

### Impact

The evaluation of the complete system (including cross-LLM communication, UCB guidance, and policy-conditioned Double DQN) against ablations demonstrated significant performance improvements:

1.  **Reliable Goal Achievement:** The complete configuration successfully reached the goal in all 90 correlated robot-round records across 30 rounds in a fixed simulation.
2.  **Improved Efficiency:** It achieved the lowest median completion time (42 ticks) and P90 (73.2 ticks) among all evaluated configurations.
3.  **Quantified Performance Gain:** The median completion time of the complete configuration was **25.0–39.1% lower** than those of other configurations (e.g., those lacking UCB guidance, cross-LLM communication, or the LLM prior).
4.  **Proof of Concept for Decoupling:** The results provide strong evidence for the effectiveness of the proposed architecture in temporally decoupling LLM policy reasoning from tick-level local control, allowing LLMs to refine high-level policies without destabilizing the rapid feedback loops of reinforcement learning.
5.  **Enabling Heterogeneous Decentralized Systems:** The work demonstrates a viable framework for managing policy ownership and communication in decentralized multi-robot systems with diverse LLM backends.