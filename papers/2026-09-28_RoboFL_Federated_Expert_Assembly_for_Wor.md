# RoboFL: Federated Expert Assembly for World Action Models

- **Category:** Robotics
- **Date:** 2026-09-28
- **Link:** http://arxiv.org/abs/2609.34968v1

---
Here's a summary of the research paper "ROBOFL: FEDERATED EXPERT ASSEMBLY FOR WORLD ACTION MODELS" in Markdown format:

---

## ROBOFL: FEDERATED EXPERT ASSEMBLY FOR WORLD ACTION MODELS

### Problem

Vision-language-action (VLA) and World-Action Models (WAMs) are critical for general-purpose embodied intelligence but are severely bottlenecked by the scarcity, institutional siloed nature, and task-heterogeneity of physical interaction data. Existing solutions face several challenges:

1.  **Data Scarcity & Privacy:** Robot interaction data is expensive to collect, private, and institutional assets, making centralized training infeasible and raw data sharing undesirable.
2.  **Federated Learning Limitations:** While federated learning (FL) is a natural fit, existing approaches struggle with the non-IID (non-independently and identically distributed) nature of task-siloed robotic data.
    *   **Naive Aggregation:** Simple averaging of parameter-efficient fine-tuning (PEFT) adapters (like LoRA) can entangle incompatible updates, leading to a dilution of local specialization.
    *   **MoE Integration:** Directly federating Mixture-of-Experts (MoE) models, where each client trains its own MoE and router on a narrow task distribution, can result in inconsistent expert assignments, further diluting task-specific knowledge and destabilizing expert selection.
    *   **Communication Overhead:** MoE-based FL methods can incur significant communication costs.

The core problem is to combine complementary, task-specific robot capabilities into a broadly competent policy in a federated setting, without exposing raw data, erasing local specialization, or introducing high communication overhead.

### Method

ROBOFL introduces a federated framework that combines a **task-silo protocol with server-side expert assembly** for World-Action Models (WAMs), addressing the challenges through:

1.  **MoSAIC (Mixture of Slotted Adapters):**
    *   **Client-Side Specialization:** Each client (institution) trains a *single LoRA adapter* on its private, focused family of tasks. Only these compact LoRA parameters (not raw data or full models) are uploaded to the server. This simplifies client-side training and minimizes communication.
    *   **Server-Side Expert Assembly:** The server maintains an MoE architecture. It directly installs the uploaded client-trained LoRA adapters into *fixed expert slots* within its layer-wise MoE.
    *   **Routed Expert Integration:** A *server-side router* is then trained on mixed-task server data to learn token assignments over these prior-informed, task-specialized LoRA experts. Both the router and the expert parameters are jointly refined on the server.
    *   **Global Adapter Conversion & Personalized Redistribution:** After server-side refinement, the resulting expert updates are converted into a compact, rank-constrained global adapter, which is then blended with each client's associated expert and redistributed for the next communication round.

2.  **FARD (Foresight-to-Action Routing Distillation):**
    *   Leveraging the three-path structure of WAMs (Understanding, Generation, Action), FARD uses the agreement between the Understanding (U) and Generation (G) paths to guide the Action (A) path's routing.
    *   A geometric-mean teacher, derived from U/G routing probabilities, distills reliable consensus into the action router, using a detached teacher to guide expert selection for action generation. This aligns routing decisions across the model's different pathways.

3.  **PCEA (Path-Consensus Expert Aggregation):**
    *   PCEA aggregates the *complete server-refined LoRA expert updates* (rather than just their factors) into a compact global adapter.
    *   It uses detached Hellinger-barycenter evidence, calculated across all three paths (Understanding, Generation, Action), to weight the individual expert updates.
    *   This agreement-weighted aggregation then reconstructs a rank-constrained global adapter (via QR reduction and SVD) for personalized redistribution to clients.

This approach separates local specialization (client-side LoRA training) from global router learning (server-side MoE), ensuring stable routing without requiring clients to train multi-expert models or incur high communication costs.

### Impact

ROBOFL demonstrates significant improvements in performance and communication efficiency across various settings:

1.  **Superior Performance:**
    *   Outperforms centralized PEFT InternVLA-A1 by **12.23%** on a real-world Franka robot arm.
    *   Achieves an **83.12%** overall success rate on RoboTwin 2.0, which is **4.2%** above federated averaging and **1.52%** above centralized InternVLA-A1.
    *   Attains a **59.17%** success rate on six real-world Franka tasks, significantly higher than the **46.94%** of centralized InternVLA.

2.  **Reduced Communication:**
    *   Reduces per-round client communication by up to **86.81%** compared to MoE-based federated VLA baselines, making it highly suitable for communication-constrained FL settings.

3.  **Addresses Core Challenges:**
    *   Successfully enables federated learning for WAMs in highly heterogeneous, task-siloed, and communication-constrained environments.
    *   Combines complementary task-specific capabilities into a broadly competent policy without centralizing raw trajectories, thus preserving data privacy and local specialization.
    *   Provides a structured expert assembly mechanism that avoids the pitfalls of naive aggregation and inconsistent MoE routing in federated settings.

---