# AI-NativeBench: An Open-Source White-Box Agentic Benchmark Suite for AI-Native Systems

- **Category:** Software Engineering
- **Date:** 2026-01-14
- **Link:** http://arxiv.org/abs/2601.09393v1

---
This research paper introduces **AI-NativeBench**, a novel benchmark suite designed to address the challenges of evaluating AI-Native systems.

## Problem

The software engineering paradigm is shifting from **Cloud-Native** (deterministic microservices) to **AI-Native** (probabilistic agentic services driven by LLMs). This shift renders traditional **black-box evaluation paradigms** (which measure raw model capabilities based on final outcomes or coarse-grained trajectories) insufficient. Existing benchmarks lack visibility into internal execution dynamics, system-level bottlenecks, and the "dual-failure nature" of AI-Native systems (combining deterministic infrastructure issues with stochastic AI decision failures like hallucinations or incorrect tool use). Engineers are left unable to diagnose *why* a system fails or performs poorly, hindering the development of reliable and performant AI-Native applications that increasingly rely on standardized protocols like Model Context Protocol (MCP) and Agent-to-Agent (A2A).

## Method

The authors introduce **AI-NativeBench**, the first open-source, application-centric, and **white-box benchmark suite** explicitly designed for AI-Native systems.
1.  **Application-Centric Suite:** It comprises eight realistic applications across three domains, supporting various architectural configurations from monolithic agents to heterogeneous multi-agent systems (up to five agents).
2.  **Protocol Implementation:** It fully implements and evaluates systems built with emerging industry standards: the **Model Context Protocol (MCP)** for tool abstraction and the **Agent-to-Agent (A2A) protocol** for inter-service orchestration, enabling controlled architectural comparisons.
3.  **Trace-First Evaluation:** AI-NativeBench employs a novel **trace-first methodology** by natively integrating **distributed tracing via OpenTelemetry**. This treats "agentic spans" as first-class citizens, fusing technical trace data with deep semantic context. This enables granular analysis and precise attribution of latency, errors, and behavioral anomalies (e.g., identifying skipped tool calls or fabricated outputs), connecting high-level behavioral issues to low-level system bottlenecks.

## Impact

Through an extensive empirical study across seven LLMs and 21 system variants using AI-NativeBench, the research uncovers critical engineering realities:

1.  **Parameter Paradox:** Lightweight models (e.g., GPT-4o-mini) often demonstrate greater protocol adherence and act as more compliant executors than flagship models. Reasoning models, while generating deeper insights, show a "content-process divergence" by internalizing execution and bypassing necessary tools, thereby breaking application structural integrity.
2.  **Inference Dominance:** LLM computation (inference time) accounts for a pervasive 86.9% to 99.9% of total execution time. This "inference dominance" renders protocol overheads (MCP/A2A) statistically secondary in most high-capability workflows, meaning system latency is primarily dictated by straggler agents on the critical path rather than communication transport.
3.  **Expensive Failure Pattern:** Current AI-Native systems fail to adhere to the "fail-fast" principle. Failed workflows consume significantly more resources than successful ones because agents exhaust their retry budgets on doomed tasks. Furthermore, while distributed architectures (A2A) can mask latency, they incur a "reliability tax" due to context redundancy required for synchronization.

This work provides the first systematic evidence to guide the transition from measuring model capability to engineering reliable and cost-effective AI-Native systems. The benchmark and dataset are open-sourced to facilitate reproducibility and further research.