# Memory Centric Power Allocation for Multi-Agent Embodied Question Answering

- **Category:** Robotics
- **Date:** 2026-04-20
- **Link:** http://arxiv.org/abs/2604.17810v1

---
```markdown
### Problem

Multi-Agent Embodied Question Answering (MA-EQA) aims to query robot teams on what they have seen over a long horizon, by aggregating their distributed memories into a global knowledge base. A key challenge is resource allocation (specifically, transmit power) for these robots. Traditional approaches for edge resource management prioritize sensing coverage, communication throughput, or computation efficiency. However, for MA-EQA, the critical metric is *memory quality*. Existing methods overlook the non-uniform memory contributions of different agents, leading to degraded EQA accuracy. Furthermore, MA-EQA is an open-set task, meaning the specific questions users might ask are unknown in advance, making it difficult to formulate an explicit, memory-oriented objective function for power allocation at the memory collection stage. Semantic communication and task-oriented communication typically fall short due to this open-set nature and the need for end-to-end optimization specific to EQA accuracy.

### Method

The paper proposes **Memory Centric Power Allocation (MCPA)**, an end-to-end optimization framework that unifies memorization and communication by introducing a novel **Quality of Memory (QoM)** model and an allocation algorithm.

1.  **Quality of Memory (QoM) Model:**
    *   **Generative Adversarial Exam (GAE):** This is the core mechanism to assess memory quality for open-set EQA. It leverages the insight that while specific questions are unpredictable, their patterns and templates are not.
        *   **Process:** Each robot uploads a small "pilot" subset of its data. An LLM on the edge server then acts as a "questioner," generating "in-context" question-answer pairs (`eQk`, `eA*k`) from *each robot's own pilot memory* (ensuring generated questions are valid and answerable by that robot). These generated questions are then used to "practice test" the *current pre-existing global memory* (`M0`).
        *   **GAE Score:** The `GAE_k` score represents how well `M0` can answer questions derived from robot `k`'s data. A lower `GAE_k` (higher error probability for `M0`) indicates that robot `k`'s memory contains more novel and valuable information that would significantly improve the system's EQA capabilities.
    *   **QoM Function:** The QoM for each robot (`Θk(p)`) is then explicitly defined as a function of `(1 - GAE_k)` (representing the memory's novelty/value) and the robot's achievable communication rate (`Fk(p)`), which depends on its transmit power `p`. This provides a quantifiable objective for resource allocation.
    *   **Iterative Memory Retrieval (IMR):** To make the GAE process computationally feasible with large language models (LLMs) and extensive memory, the paper employs an IMR scheme, where LLMs iteratively retrieve small, relevant memory chunks rather than processing the entire memory at once.

2.  **Memory Centric Power Allocation (MCPA) Algorithm:**
    *   **Objective:** Maximize the sum of QoM across all robots under a total transmit power budget constraint.
    *   **Optimization:** The resulting optimization problem is non-convex. The paper tackles this using **Successive Convex Approximation (SCA)**, which involves constructing a sequence of convex surrogate functions that iteratively converge to a stationary point of the original problem. This allows for efficient solution using standard convex programming tools.
    *   **Asymptotic Analysis:** An analytical solution for the asymptotic case (infinite antennas, orthogonal channels) shows that the optimal transmit power `pk` for each robot is directly proportional to `(1 - GAE_k)`. This provides a fundamental insight: MCPA naturally prioritizes robots that contribute more novel information (higher EQA error probability for the existing memory).

### Impact

*   **Significant EQA Accuracy Improvement:** MCPA achieves superior EQA accuracy (e.g., 95.35%) and QoM values compared to various benchmarks, including methods maximizing communication sum-rate (MaxRate: 61.69%), sensing coverage (MaxCov: 86.09%), fairness (Fairness: 61.88%), and a standalone memory baseline (Remember: 41.0%). It also outperforms a Greedy approach and Semantic Communication (SemCom) in identifying memory value.
*   **Validation of Memory-Centric Paradigm:** The results demonstrate that simply maximizing communication throughput or sensing coverage does not necessarily translate to better memorization or EQA performance. MCPA proves that prioritizing *memory quality* (as measured by GAE/QoM) is crucial for effective MA-EQA systems. For instance, MaxRate achieves 3x higher data rates but significantly lower EQA accuracy.
*   **Effective Open-Set Problem Solution:** The GAE model is validated to effectively identify semantic richness and novelty, outperforming simple semantic similarity metrics (e.g., SemCom) in distinguishing the true value of new memory.
*   **Robustness and Adaptability:** MCPA consistently maintains superior EQA accuracy and memory quality across various total power budgets, showcasing its robustness to different resource constraints.
*   **Practical Framework:** The proposed model and algorithm are implemented and tested in a high-fidelity Carla simulation environment, utilizing state-of-the-art Vision-Language Models (VLMs) and Large Language Models (LLMs), confirming its practical applicability.
```