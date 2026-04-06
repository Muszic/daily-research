# SkillRT: Compiling Skills for Efficient Execution Everywhere

- **Category:** Software Engineering
- **Date:** 2026-04-03
- **Link:** http://arxiv.org/abs/2604.03088v1

---
Here's a summary of the research paper "SkillRT: Compiling Skills for Efficient Execution Everywhere" in Markdown format:

---

### Problem

LLM agents increasingly rely on "skills" (natural language descriptions and scripts) as reusable units for composition and task execution. However, current systems treat these skills as raw context fed directly to the LLM, leading to significant challenges:

*   **Inconsistent Behavior & Fragility:** The same skill can behave inconsistently across different LLMs or agent platforms because skills make implicit assumptions about model capabilities and execution environments.
*   **Poor Portability:** The fragility undermines the promise of portable skills, as they often fail when moved between models, harnesses, or environments.
*   **Execution Inefficiency:** Treating skills as raw text leads to substantial token overhead and increased latency, as LLMs must parse and interpret the skill repeatedly.
*   **Three Key Mismatches:**
    1.  **Model Mismatch:** Different LLMs vary dramatically in their ability to understand and follow skill instructions, often ignoring guidance or misinterpreting requirements.
    2.  **Harness Mismatch:** Agent harnesses provide different sets of tools, APIs, and concurrency capabilities, which skills are not adapted to.
    3.  **Environment Mismatch:** Skills often have unfulfilled dependencies (e.g., missing packages, CLI tools) in the user's local execution environment.
*   **Challenges in Adaptation:** Adapting skills is complex due to the combinatorial nature of target variations (model, harness, environment) and the unstructured natural language format of skills, which makes automated analysis difficult.

### Method

The authors propose **SkillRT**, a novel compilation and runtime system for skills, drawing inspiration from traditional compiler design. SkillRT treats skills as "code" and LLMs as "heterogeneous processors" to enable efficient and portable cross-model execution.

**1. AOT (Ahead-Of-Time) Compiler (at skill installation time):**
The compiler analyzes the raw skill against the target environment (model, harness, host) and produces optimized "skill variants" through three passes:

*   **Capability-Based Compilation:**
    *   **Primitive Capabilities:** Decomposes skill requirements into a set of **26 primitive capabilities** (e.g., `gen.code.shell`, `reason.arithmetic`, `tool.exec`, `follow.procedure`), each with multiple proficiency levels.
    *   **Gap Measurement:** Profiles the target LLM and harness against these capabilities using microbenchmarks to determine its proficiency level for each.
    *   **Skill Transforms:** Based on the gap between skill requirements and target capabilities, it applies:
        *   **Compensation:** Adapts the skill (e.g., adding explicit instructions, examples, stronger constraints) to reduce its capability requirement to a level the target supports.
        *   **Substitution:** If compensation is not viable, it switches to an alternative implementation path that achieves the same goal using capabilities the target model possesses.
*   **Environment Binding:** Extracts implicit dependencies (packages, CLI tools, services) from skill descriptions and generates platform-specific setup scripts to ensure all prerequisites are met.
*   **Concurrency Extraction:** Identifies latent parallelism opportunities within the skill's workflow (e.g., data-level, instruction-level, thread-level parallelism) and explicitly exposes them to the agent harness for optimized execution.

**2. Runtime System & JIT (Just-In-Time) Optimizer (at execution time):**
The runtime manages skill loading and execution, optimizing performance and correctness dynamically.

*   **Task Variant Selection:** Selects the pre-compiled skill variant best suited for the current (model, harness) pair.
*   **Code Solidification:** Identifies high-frequency, parameterized script templates within skills and JIT-compiles them into instantiated, executable code, bypassing repeated LLM parsing and inference.
*   **Adaptive Recompilation:** Monitors skill execution outcomes; if systematic failures or new capability gaps emerge, it triggers adaptive recompilation to further optimize the skill.
*   **Resource-Aware Scheduler:** Coordinates with system resources and tool capabilities to schedule concurrent sub-agents efficiently.

### Impact

SkillRT significantly enhances the reliability, efficiency, and portability of LLM skills:

*   **Improved Task Completion:** Increases task completion rates by an average of **15.3%** across diverse LLMs and agent harnesses.
*   **Reduced Token Consumption:** Decreases token consumption by up to **40%** for completed tasks, leading to cost savings and faster inference.
*   **Enhanced Performance:**
    *   Achieves up to **3.2x speedup** through fine-grained parallelization enabled by concurrency extraction.
    *   Provides **19-50x latency reduction** by bypassing LLM inference for frequently executed code patterns through JIT code solidification.
*   **Robust Portability:** Enables skills to execute reliably and consistently across a wide range of heterogeneous LLMs, agent harnesses, and user environments, addressing the fundamental mismatch problem.

---