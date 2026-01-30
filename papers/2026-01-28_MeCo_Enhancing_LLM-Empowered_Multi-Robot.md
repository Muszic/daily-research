# MeCo: Enhancing LLM-Empowered Multi-Robot Collaboration via Similar Task Memoization

- **Category:** Robotics
- **Date:** 2026-01-28
- **Link:** http://arxiv.org/abs/2601.20577v1

---
Here's a summary of the MeCo research paper:

## Problem

Existing LLM-empowered multi-robot collaboration methods, while offering flexibility without extensive task-specific training, are inefficient. They treat tasks as isolated entities and lack the ability to recognize or leverage similarities between tasks. Consequently, when confronted with identical or *similar* tasks, these systems must replan from scratch by repeatedly invoking large language models (LLMs). This leads to:
*   **Redundant computation:** Unnecessary replanning for similar problems.
*   **High operational costs:** Excessive LLM token consumption.
*   **Increased planning time:** Slower response and execution for recurring scenarios.
*   **Limited adaptability:** Inability to efficiently scale in real-world applications where similar tasks frequently appear (e.g., variations of parcel sorting, grocery packing, floor sweeping).

The core challenge lies in accurately identifying and effectively reusing solutions for tasks that are *similar but not identical*, especially in complex multi-robot environments where coordination and collision avoidance are critical.

## Method

MeCo proposes a **similarity-aware multi-robot collaboration framework** that applies the principle of "cache and reuse" (memoization) to enhance efficiency. Its key components and workflow are:

1.  **Task Cache and Selective Caching:** Successfully planned tasks and their associated plans are selectively stored in a task cache. A deduplication mechanism (inspired by LFU) and quality checks (e.g., effective step count) manage cache size and ensure diversity and utility of cached plans.
2.  **Similarity Testing:** When a new task arrives, MeCo first searches the task cache for a similar, previously solved task using a novel similarity testing method. This method differentiates based on workspace overlap:
    *   **Low-workspace-overlap tasks:** Similarity is determined if target objects undergo only restricted geometric transformations *within the same pre-defined work areas*, without altering cross-region interaction structures.
    *   **High-workspace-overlap tasks:** Due to higher collision risk, similarity is based on a "reuse ratio" ($\alpha$) – the proportion of the historical trajectory that is reusable in the current environment. This metric is correlated with planning success probability. Predefined thresholds (e.g., 0.85 for "Pack Grocery," 0.7 for "Move Rope") determine similarity.
3.  **Similar Motion Planner (S-Planner):** If a similar task is found, S-Planner is invoked to generate a plan for the current task by referencing the cached plan *without re-invoking LLMs*.
    *   **Low-workspace-overlap mode:** Inherits the action sequence. If target poses are within a tolerance threshold, the trajectory is reused; otherwise, an RRT-based motion planner generates a new trajectory.
    *   **High-workspace-overlap mode:** Inherits the action sequence. It performs "back checking" (truncating paths to prevent backtracking) and "collision checking" (truncating paths before collision points) to identify valid reference trajectory segments. Key sampling points from these segments guide an RRT-based motion planner.
4.  **Continuous Planning:** If S-Planner fails (e.g., due to unexpected environmental changes), the system does not restart. Instead, the failure reason and current environment state are fed back to the LLMs, allowing them to *continue planning from the failed step* rather than from scratch.
5.  **MeCoBench:** A new benchmark is introduced, extending RoCoBench, specifically designed to evaluate multi-robot collaboration performance in scenarios involving similar tasks. It can generate tasks that are similar, different, or random relative to cached tasks.

## Impact

MeCo significantly enhances the efficiency and effectiveness of LLM-empowered multi-robot collaboration:

*   **Substantial Cost Reduction:**
    *   Achieves approximately **55% saving in planning time**.
    *   Reduces LLM token consumption by **up to 70%**.
*   **Improved Task Success Rates:**
    *   Demonstrates an overall improvement of around **30% in success rate** compared to state-of-the-art LLM-based approaches.
*   **Enhanced Adaptability:** By memoizing and reusing solutions for similar tasks, MeCo allows multi-robot systems to handle diverse and recurring scenarios more efficiently, reducing reliance on expensive and time-consuming LLM invocations.
*   **Novel Evaluation Standard:** The introduction of **MeCoBench** provides the first dedicated benchmark for assessing similar-task collaboration scenarios, offering a valuable tool for future research and development in this area.
*   **Open-Source Contribution:** The framework's code is open-sourced, facilitating reproducibility and further advancements in the field.