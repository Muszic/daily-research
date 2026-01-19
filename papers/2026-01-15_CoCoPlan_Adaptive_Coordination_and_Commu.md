# CoCoPlan: Adaptive Coordination and Communication for Multi-robot Systems in Dynamic and Unknown Environments

- **Category:** Robotics
- **Date:** 2026-01-15
- **Link:** http://arxiv.org/abs/2601.10116v1

---
**Problem:**
Multi-robot systems greatly benefit from coordination, but real-world deployments are severely limited by intermittent, close-range communication and dynamic, unknown environments with unpredictable task distributions. Existing methods either rely on unrealistic assumptions of constant connectivity, employ rigid fixed schedules that fail under uncertainty, or use inefficient pairwise communication protocols. This leads to suboptimal coordination, degraded information flow, and a critical gap in jointly handling online task discovery, sparse connectivity management, and temporal task constraints for team-wide coordination, especially as robot fleet sizes increase.

**Method:**
CoCoPlan is a unified framework that **co-optimizes collaborative task planning and team-wise intermittent communication** for multi-robot systems. Its core components are:
1.  **Branch-and-Bound (BnB) Architecture:** This central planning engine jointly encodes task assignments and communication events within unified search nodes. It systematically explores collective plans (sequences of agent tasks interleaved with communication events) to find an optimal strategy.
2.  **Adaptive Objective Function:** CoCoPlan employs a novel objective function that balances task completion efficiency against communication latency within each execution horizon. This serves as a local approximation of the long-run global task completion rate, providing robustness to unknown spatio-temporal task distributions.
3.  **Communication Event Optimization Module (`ComOpt`):** This iterative algorithm strategically determines *when, where, and how* global connectivity should be re-established. It minimizes the maximum delay for agents to reach designated communication points, ensuring all robots can synchronize and establish a globally connected communication graph at the scheduled event.
The framework operates online, allowing agents to discover new tasks dynamically. At each team-wise communication event, all detected tasks are aggregated, and CoCoPlan is invoked to compute updated collective plans and the timing/locations for the next communication.

**Impact:**
CoCoPlan demonstrates significant improvements over state-of-the-art methods:
*   **Task Completion:** Achieves a **22.4% higher task completion rate**.
*   **Communication Efficiency:** Reduces communication overhead by **58.6%**.
*   **Scalability:** Greatly improves scalability, effectively supporting up to **100 robots** in dynamic environments.
*   **Real-world Validation:** Extensive validation was conducted through large-scale simulations (e.g., DARPA SubT challenge, subterranean caves) and hardware experiments in complex scenarios, including a 2D office environment and a 3D disaster-response mission.