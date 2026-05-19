# A Readiness-Driven Runtime for Pipeline-Parallel Training under Runtime Variability

- **Category:** Machine Learning
- **Date:** 2026-05-18
- **Link:** http://arxiv.org/abs/2605.18750v1

---
This paper introduces a novel runtime system for pipeline-parallel training that addresses inefficiencies caused by runtime variability.

---

### Problem

Existing pipeline parallelism systems for large model training suffer from significant inefficiencies like **idle bubbles, stage misalignment, and reduced utilization**. This stems from two main factors:
1.  **Runtime Variability:** Computation and communication latencies exhibit unpredictable jitter and variation, especially at scale and in multimodal workloads.
2.  **Pre-Committed Execution Orders:** Current systems treat statically profiled or adaptively generated schedules as rigid, pre-committed execution sequences. When actual task readiness deviates from this fixed order due to runtime variability, pipeline stages are forced to wait for not-yet-ready tasks, even if other executable work is available, leading to stalls and suboptimal performance.

---

### Method

The paper proposes **Runtime-Readiness-First Pipeline (RRFP)**, a readiness-driven runtime that fundamentally changes how schedules are consumed. Instead of enforcing a fixed order, RRFP treats a schedule as a **non-binding hint order** for ranking currently ready work. If a higher-ranked task isn't ready, the system skips it and dispatches another ready task, preventing blockages.

RRFP achieves this out-of-order, readiness-driven execution through three key mechanisms:

1.  **Message-Driven Asynchronous Communication:** Decouples data transfer from computation using dedicated send/receive threads. Tensors are sent as messages with microbatch identifiers, allowing out-of-order arrivals to update per-microbatch buffers and dynamically inform task readiness, eliminating stalls from fixed send/receive sequences.
2.  **Lightweight Tensor-Parallel Coordination:** Addresses the challenge of maintaining collective consistency across tensor-parallel ranks in an out-of-order environment. Before executing tasks involving tensor-parallel collectives, ranks use a scalar all-gather to agree on the microbatch to process, deferring if a consensus cannot be reached, thereby preserving correctness without imposing global pipeline order.
3.  **Ready-Set Arbitration:** A low-overhead local arbitration layer repeatedly polls ready buffers. It scans the non-binding hint order (e.g., a simple Backward-Forward (BF) strategy) and dispatches the first *available* task from the ready set, effectively guiding execution based on the schedule without waiting for unavailable tasks.

---

### Impact

RRFP significantly improves end-to-end training performance and resource utilization by proactively executing ready work instead of waiting for a pre-committed order.

*   **Speedup:** Achieves up to **1.77× speedup** on language-only workloads and up to **2.77× speedup** on multimodal workloads over fixed-order 1F1B baselines (using the BFW hint variant).
*   **Cross-Framework Performance:** In representative cross-framework comparisons, RRFP (with its default BF hint) outperforms the fastest available external system by up to **1.84×**, while preserving training correctness.
*   **Robustness:** Effectively mitigates the impact of runtime variability by reducing pipeline bubbles and stage misalignment, enabling more efficient large-scale distributed training for modern deep learning models.