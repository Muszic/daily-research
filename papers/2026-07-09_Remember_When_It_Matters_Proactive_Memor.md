# Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents

- **Category:** NLP
- **Date:** 2026-07-09
- **Link:** http://arxiv.org/abs/2607.08716v1

---
Here's a summary of the research paper in Markdown format:

### Problem

Long-horizon tasks for LLM agents are prone to **behavioral state decay**, where decision-relevant information (e.g., task requirements, environment facts, prior failed attempts, diagnoses, open subgoals) becomes buried, is pushed out of the context window, or ceases to influence the agent's decisions. This leads to common failures such as repeating mistakes, violating established requirements, or re-diagnosing known issues, even when the information is technically present in the trajectory. Existing memory systems primarily focus on passive storage and retrieval, but active task execution requires an additional crucial component: deciding *when* to intervene with remembered information without overwhelming the agent or introducing unnecessary latency.

### Method

The authors propose a **proactive memory agent architecture** that runs alongside an unmodified action agent. This memory agent operates in two phases at fixed intervals:

1.  **Memory Management (Phase 1):** The memory agent observes a recent trajectory window and updates a **structured memory bank**. This bank contains three components:
    *   **Status:** Private tracking of the memory agent's progress and issues.
    *   **Knowledge:** Stable facts like task requirements, environment properties, and user-verified information.
    *   **Procedural:** Records of attempts, outcomes, failed commands, successful fixes, and diagnoses.
    The memory agent uses specific tool calls (e.g., `memory_save_knowledge`, `memory_delete`) to explicitly manage and update these entries, ensuring a compact and organized representation of execution state.

2.  **Intervention Selection (Phase 2):** Based on the updated memory bank and recent trajectory, the memory agent decides whether to inject a concise, **memory-grounded reminder** into the action agent's context for its next decision, or to remain silent. The core principle is *selective intervention*: only intervene when a remembered item is highly likely to affect and improve the next action, avoiding broad advice or redundant information.

The architecture is plug-and-play, allowing integration with existing action agents. The memory agent itself can be implemented as a prompted LLM, and the authors also explore training an open-weight memory agent using Supervised Fine-Tuning (SFT) and Group Policy Optimization (GRPO) to learn optimal intervention policies.

### Impact

The proactive memory agent demonstrates significant improvements in long-horizon task performance:

*   **Improved Task Completion:** Across Terminal-Bench 2.0 (autonomous command-line execution) and τ2-Bench (interactive tool-use), the system boosts `pass@1` for both weaker (Claude Sonnet 4.5) and stronger (Claude Opus 4.6) action agents.
    *   For Sonnet 4.5: **+8.3 pp** on Terminal-Bench and **+6.8 pp** on τ2-Bench.
    *   For Opus 4.6: **+2.4 pp** on Terminal-Bench and **+2.5 pp** on τ2-Bench.
*   **Validation of Selective Intervention:** Ablation studies confirm that the proposed selective intervention policy significantly outperforms alternative memory approaches, including passive bank exposure, always-on injection, advisor-only guidance, and general retrieval, highlighting the importance of *when* and *how* to intervene.
*   **Feasibility of Open-Weight Memory Policies:** Preliminary training of Qwen3.5-27B as the memory agent using SFT and GRPO showed improved validation reward and partial transfer to Terminal-Bench, suggesting the potential for learnable, open-weight memory policies to reduce inference costs and calibrate interventions more effectively.
*   **Addresses a Core LLM Agent Failure:** The work identifies behavioral state decay as a critical failure mode and provides an effective, plug-and-play solution that enhances the robustness and efficiency of long-horizon language agents.