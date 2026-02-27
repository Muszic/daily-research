# Test-Time Scaling with Diffusion Language Models via Reward-Guided Stitching

- **Category:** NLP
- **Date:** 2026-02-26
- **Link:** http://arxiv.org/abs/2602.22871v1

---
This paper introduces **Stitching Noisy Diffusion Thoughts**, a self-consistency framework that improves reasoning with large language models by aggregating high-quality intermediate steps from diverse, cheaply generated reasoning trajectories.

### Problem

Existing methods for leveraging multiple chains-of-thought (CoTs) in large language models (LLMs) often aggregate at the *trajectory level* (e.g., selecting the best full trace or voting on final answers). This approach discards useful intermediate work from partial or "nearly correct" attempts, leading to wasted computation and reduced accuracy, especially on complex problems. While diffusion language models offer broad exploration, and hybrid models exist, they often couple exploration, scoring, and generation, limiting flexibility and leading to accuracy drops compared to strong autoregressive (AR) models. Reliable reasoning on hard problems remains expensive.

### Method

The proposed framework, Stitching Noisy Diffusion Thoughts, is a modular, training-free pipeline that decouples exploration, evaluation, and solution synthesis:

1.  **Explore (Diffusion-based Sampling):** Given a problem, a masked diffusion language model (dLLM) samples many diverse, low-cost reasoning trajectories (chains-of-thought) in parallel. These trajectories are then segmented into human-readable intermediate steps.
2.  **Evaluate (Step-level Scoring):** An off-the-shelf Process Reward Model (PRM) scores *every intermediate step* within each sampled trajectory. This step-level confidence score allows the system to identify and retain useful sub-results even if the overall trajectory later derails. Scoring is done efficiently in a single pass using marker tokens.
3.  **Stitch (Reward-Guided Aggregation):** The system constructs a "stitched evidence list" by collecting the highest-quality steps (those with PRM scores above a certain confidence threshold) from *across all* sampled trajectories. To maintain coherence and provide an anchor, all steps from the best overall trajectory (ranked by geometric mean of step scores) are also included. Steps are concatenated chronologically and annotated with their confidence scores.
4.  **Recompute (AR Solver Synthesis):** A lightweight autoregressive (AR) model (solver) then conditions on the original problem and the confidence-annotated stitched rationale to recompute the final answer. This AR solver acts as a reconciliation step, selecting consistent evidence, filling gaps, and producing a coherent final solution.

This pipeline also extends to coding tasks by adapting the step definitions and PRMs (e.g., treating code lines as steps for MBPP or natural-language rationales for HumanEval).

### Impact

*   **Significant Accuracy Gains:** The framework achieves substantial accuracy improvements, up to **23.9% average absolute points** over vanilla diffusion decoding across six math and coding tasks (e.g., +30.1% on HumanEval, +9.7% on GSM8K). It outperforms recent hybrid diffusion-AR systems (e.g., +7.1% over TiDAR) and is competitive with or superior to strong AR baselines (e.g., +4.3% over Qwen3-8B).
*   **Improved Efficiency and Latency:** It significantly improves the accuracy–latency Pareto frontier. The method achieves up to **1.8× latency reduction** and **9.85× fewer sequential forward passes** compared to traditional diffusion models and unified architectures at matched accuracy. This is due to efficient, parallel diffusion-based exploration and a single invocation of the AR solver.
*   **Modularity and Robustness:** The decoupled pipeline separates exploration from evaluation and synthesis, allowing for flexible improvements. The step-level recombination is particularly beneficial on harder problems, and ablations show the crucial role of the AR solver in converting stitched but imperfect rationales into accurate answers.
*   **Training-Free:** The framework is training-free, leveraging existing diffusion models, PRMs, and AR solvers.