# Adaptive Inference Batching using Policy Gradients

- **Category:** Artificial Intelligence
- **Date:** 2026-07-06
- **Link:** http://arxiv.org/abs/2607.05272v1

---
# Adaptive Inference Batching using Policy Gradients

## Problem
*   Machine learning inference serving systems face the challenge of balancing high throughput and low latency, especially under dynamic, bursty, and heterogeneous workloads.
*   **Static batching policies** are rigid and fail to adapt to varying traffic patterns, leading to suboptimal performance (e.g., unnecessary latency during low traffic, underutilization during high traffic).
*   In **multi-GPU or multi-model environments**, heterogeneous requests (e.g., short ResNet inferences mixed with long GPT generations) lead to **Head-of-Line (HoL) blocking**, where fast requests get stuck behind slow ones, severely impacting latency.
*   The core problem is to find adaptive batching and routing policies that can outperform these static heuristics and mitigate HoL blocking in complex, dynamic multi-GPU scenarios.

## Method
*   **Formulation:** The adaptive batching and request routing problem is formulated as a **Markov Decision Process (MDP)**.
    *   **State Space:** Captures real-time system state including normalized queue length, time since last batch, type of request at the head of the queue (Memory-bound vs Compute-bound), and GPU availability (busy/free status).
    *   **Action Space:**
        *   **Single-GPU:** Discrete batch size selection (including an option to "wait").
        *   **Multi-GPU:** Joint decision of which GPU to route to and the batch size for that GPU, optimizing both simultaneously.
    *   **Reward Function:** A composite reward balancing throughput and latency, with weighted penalties for different request types (e.g., significantly higher penalty for delaying "Fast" requests, `w_fast=200.0` vs `w_slow=20.0`, to encourage SLA compliance and segregation).
*   **Algorithms:** Policy Gradient methods, specifically **REINFORCE** and **Proximal Policy Optimization (PPO)**, are used to learn the optimal policy.
*   **Environment:** A **custom discrete-event simulator** was developed and validated against standard queuing models and real-world traces (Azure Functions, BurstGPT). This simulator models request arrivals, execution latency (including fixed overheads and per-sample processing time), queuing, and multi-GPU support for heterogeneous workloads.
*   **Policy Network:** A neural network architecture (MLP with a **Multi-Head Attention layer**) approximates the stochastic policy `π_θ(a|s)`. The attention mechanism helps the agent correlate state features like queue depth and GPU availability.
*   **Workloads:** Evaluated on Standard (Poisson), Extreme Burst, Real-World Trace, and critically, a **Multi-GPU Routing scenario** with a 50/50 mix of "Fast" (ResNet-50) and "Slow" (GPT-2) requests to specifically test HoL blocking.

## Impact
*   **Significant Performance Improvement in Multi-GPU Environments:** While RL agents matched static heuristics in simple single-GPU scenarios, they demonstrated a **3.5x (348%) performance improvement** over Round-Robin scheduling and a 48% improvement over the Shortest-Queue heuristic in the **multi-GPU heterogeneous routing scenario**.
*   **Dynamic Workload Segregation:** The RL agent successfully learned to dynamically **segregate heterogeneous workloads** (e.g., routing fast requests to one GPU and slow requests to another) to effectively eliminate Head-of-Line (HoL) blocking, a critical challenge in distributed inference.
*   **Optimized Latency-Throughput Trade-off:** The RL agent found a "sweet spot," achieving **60% higher throughput** than Shortest-Queue (17.98 vs 11.18 req/s) while maintaining **25% lower latency** than Round-Robin (2.59s vs 3.46s), all within defined SLA constraints (e.g., 3.0s latency threshold).
*   **Generalization:** The learned policies generalized well to unseen "Extreme Burst" and "Real-World Trace" workloads, indicating that the agent learned robust, state-dependent policies rather than just memorizing traffic patterns.
*   **Importance of Reward Shaping:** The research highlights the critical role of domain-specific reward shaping (e.g., weighted latency penalties) in enabling RL agents to discover non-trivial and SLA-compliant policies for complex system optimization problems.
*   **Future Potential:** Demonstrates the strong potential of RL not just for temporal batching, but for the *joint optimization of request routing and batch composition* in sophisticated, distributed inference systems, paving the way for more efficient and adaptive ML serving.