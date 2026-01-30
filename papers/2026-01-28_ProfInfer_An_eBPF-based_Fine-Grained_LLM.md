# ProfInfer: An eBPF-based Fine-Grained LLM Inference Profiler

- **Category:** Software Engineering
- **Date:** 2026-01-28
- **Link:** http://arxiv.org/abs/2601.20755v2

---
```markdown
# PROFINFER: An eBPF-based Fine-Grained LLM Inference Profiler

## Problem

Modern Large Language Model (LLM) inference engines, especially those targeting on-device and edge scenarios, suffer from a critical lack of fine-grained, operator-level visibility. Unlike general-purpose ML runtimes, they offer little insight into resource consumption and execution flow, leaving developers unable to answer fundamental questions like whether a workload is memory-bound or compute-bound. Existing profiling solutions are often coarse-grained, require source modification or recompilation, introduce significant overhead, or fail to expose critical dimensions like dynamic operator graphs, per-thread scheduling, hardware counter events, and phase-specific behaviors (e.g., prefill vs. decode). While eBPF has been used for deep learning performance tracing, it hasn't been adapted to correlate low-level hardware metrics with high-level LLM operator semantics, particularly under the stringent constraints of mobile/edge environments.

## Method

ProfInfer is a fine-grained, non-intrusive profiling framework for LLM inference engines, exemplified by `llama.cpp` and its underlying GGML library. It is built on **eBPF (extended Berkeley Packet Filter)** technology.

1.  **Non-Intrusive Tracing:** ProfInfer dynamically attaches eBPF probes to runtime functions across multiple layers (user-space `uprobes`/`uretprobes` and kernel `tracepoints`) without modifying or recompiling the LLM inference engine's source code.
2.  **Multi-Granularity Probing:**
    *   **Token-level:** Traces `llama_decode` to measure time-to-first-token (TTFT) and time-per-output-token (TPOT), enabling dynamic adjustment of tracing overheads based on QoS.
    *   **Graph-level:** Hooks into `ggml_backend_graph_compute_async` to measure execution time of computation graphs on different backends (CPU, GPU, NPU) and analyze graph partitioning.
    *   **Operator-level:** Probes `ggml_compute_forward` (and backend-specific equivalents) to capture execution times, tensor dimensions, operator types, and addresses, allowing reconstruction of the computational DAG.
    *   **Scheduler-level:** Uses `sched_switch` and `sched_wakeup` tracepoints to monitor thread scheduling, identify interference, and track CPU utilization.
3.  **Hardware Counter Integration (PMCs):** It collects per-operator Performance Monitoring Counter (PMC) data, such as cache refills, memory accesses, and CPU cycles, to provide low-level insights into hardware behavior and identify bottlenecks.
4.  **MoE Expert Tracing:** Specifically traces expert activations in Mixture-of-Experts (MoE) models to understand dynamic behavior and its impact on memory and I/O.
5.  **Two-Phase Architecture:**
    *   **Tracer (eBPF Kernel/User Space):** Collects raw timestamps, thread IDs, CPU IDs, function arguments, and PMC data. It can dynamically enable/disable probes to control overhead.
    *   **Analyzer:** Processes collected traces into rich visualizations and statistical analyses:
        *   **ProfDAG:** Reconstructs the dynamic computational graph (DAG) with per-operator profiling results (e.g., memory bandwidth).
        *   **ProfTime:** Generates timeline views for token, graph, operator, and thread scheduling activities, visualized using tools like Perfetto.
        *   **ProfStat:** Provides statistical breakdowns across tokens, per-operator type (considering tensor dimensions and PMCs), and activated MoE experts to correlate model characteristics with performance.

## Impact

ProfInfer addresses the critical visibility gap in LLM inference by making it **transparent and diagnosable**.

1.  **Enhanced Visibility:** Provides comprehensive, fine-grained observability across the entire LLM inference pipeline, covering each forward pass, computation graph, operator execution, processor thread, and hardware counter trends.
2.  **Low Overhead:** Achieves less than **4% runtime overhead** and high profiling fidelity, making it practical for real-world deployments, including resource-constrained mobile and edge devices.
3.  **Practical Tool for Optimization:** Transforms performance profiling into a practical tool for:
    *   **Identifying Bottlenecks:** Pinpointing compute-bound vs. memory-bound operations, and memory/disk I/O issues.
    *   **Guiding Optimizations:** Analyzing the effects of quantization, KV-cache reuse, accelerator offloading, and memory bandwidth constraints.
    *   **Scheduling and Deployment:** Informing resource allocation decisions, understanding workload interference, and analyzing backend performance divergence.
4.  **Intuitive Analytics:** Offers intuitive performance analytics through timeline views, dynamic DAG visualizations, and statistical operator-level plots that directly correlate model structure with hardware behavior.
5.  **Applicability:** Its non-intrusive and lightweight design makes it uniquely suitable for diverse Linux-based environments, including Android/OpenHarmony on mobile and edge devices, where traditional profilers often fall short.

```