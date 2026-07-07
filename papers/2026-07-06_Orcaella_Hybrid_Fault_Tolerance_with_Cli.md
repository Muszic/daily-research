# Orcaella: Hybrid Fault Tolerance with Client-Selectable Finality Latency

- **Category:** Cryptography
- **Date:** 2026-07-06
- **Link:** http://arxiv.org/abs/2607.04789v1

---
This research paper, "Orcaella: Hybrid Fault Tolerance with Client-Selectable Finality Latency," presents a novel approach to state machine replication (SMR) that optimizes for low-latency commits while offering client-selectable trade-offs between latency and stronger fault tolerance guarantees.

### Problem

*   **High Latency in Classical BFT:** Classical partially synchronous SMR protocols like PBFT achieve fault tolerance (`n >= 3f + 1`) but require three communication steps, leading to higher latency.
*   **High Committee Size for Fast-Path:** Recent 2-message-delay protocols (e.g., Minimmit) offer lower latency but demand significantly larger committees (`n >= 5f + 1`), often by conservatively treating all silent replicas as potential Byzantine equivocators.
*   **Limited Fast-Path Fault Tolerance in Hybrid Models:** While hybrid fault models (distinguishing Byzantine `f` from crash `c` faults) exist (e.g., Hydrangea, Kudzu), they primarily focus on optimistic fast-paths and eagerly fall back to slower, 3-round paths when faults increase. This leaves two open challenges:
    1.  How to **maximize the fault tolerance of the optimal 2-message-delay commit itself** under a relaxed mixed fault model (`f` Byzantine, `c` crash)?
    2.  How to provide **even stronger, FlexibleBFT-style safety guarantees** (beyond `f` Byzantine and `c` crash) if a client is willing to accept higher latency?

### Method

*   **Novel Fault Tolerance Bound:** Orcaella formally defines and proves a tight bound for vote-counting protocols providing 2-message-delay commits under a mixed fault model (up to `f` Byzantine and `c` crash faults): `n >= 5f + 3c + 1`. This bound provides a more nuanced approach than the `5f + 1` regime by separating fault types.
*   **Orcaella Protocol with Dual Finality Paths:** The core solution is "Orcaella," a hybrid protocol that exposes two explicit finality paths for clients, allowing them to choose their desired latency-safety trade-off:
    1.  **Optimal Fast-Path (2-message-delay):** Clients can finalize quickly upon collecting a `VoteQC` (a quorum of `q = n - f - c` matching votes). This path guarantees safety against `f` Byzantine faults under normal operating conditions.
    2.  **Resilient Path (4-message-delay):** Clients willing to wait for two additional rounds (chaining a `CheckpointQC` and `FinalityQC`) gain enhanced safety. This path provides resilience against an additional `f_abc` "alive-but-corrupt" (AbC) replicas, which are treated as equivocating faults in this specific client-side threat model.
*   **Robust View Change and Fork Recovery:**
    *   The protocol includes a view-change mechanism (`k = 2f + c + 1` threshold) to ensure that Fast-Path commits are preserved across view changes.
    *   If the core `f` Byzantine fault limit is exceeded (e.g., due to AbC-induced forks breaking Fast-Path safety), the protocol temporarily loses liveness and enters a synchronous *Fork Recovery* mode. During recovery, replicas reliably exchange `CheckpointQCs` and `VoteQCs` using a Byzantine Broadcast protocol (e.g., Dolev-Strong). Crucially, the protocol ensures that at most one `CheckpointQC` can form per height, thus preserving Resilient Path safety throughout the recovery.

### Impact

*   **Maximizes 2-Delay Fault Tolerance:** Orcaella provides the tightest known quorum inequalities (`n >= 5f + 3c + 1`) for 2-message-delay BFT consensus under a mixed Byzantine/crash fault model. This allows for more efficient and resilient deployments by accurately differentiating between fault types and improving liveness guarantees compared to protocols that conflate all non-responsive replicas.
*   **Client-Selectable Latency-Safety Trade-off:** The dual-path architecture empowers clients to explicitly navigate the latency-safety trade-off. They can choose optimal 2-message-delay finality for high-speed transactions or opt for higher 4-message-delay latency to gain stronger safety guarantees against a broader range of equivocating faults.
*   **Enhanced Resilience to Sophisticated Adversaries:** The Resilient Path offers FlexibleBFT-style safety, maintaining the integrity of committed operations even in scenarios where the fast-path's assumptions are violated by a greater number of equivocating faults (`f + f_abc`), without sacrificing core protocol liveness under normal operating conditions.
*   **Practical Deployment Flexibility:** The protocol's configurable nature allows operators to tune `f` and `c` based on their specific threat models (e.g., optimizing for Byzantine-heavy or crash-heavy environments at `n ≈ 100` replicas), providing practical adaptability for real-world decentralized systems.
*   **Theoretical Foundations:** Orcaella contributes a rigorous characterization of vote-counting protocols and their precise quorum requirements, establishing a strong theoretical basis for future low-latency BFT designs.