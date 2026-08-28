# Investigating Software Aging in LLM-Generated Software Systems across Generation-and-Execution Environments

- **Category:** Software Engineering
- **Date:** 2026-08-26
- **Link:** http://arxiv.org/abs/2608.26391v1

---
Here's a summary of the research paper in Markdown format:

### Problem

Large Language Models (LLMs) are increasingly used to generate executable software systems, accelerating development. While existing research has focused on the functional correctness, security, maintainability, robustness, and performance of LLM-generated code, there is **little to no understanding of its long-term operational reliability under sustained execution**. Specifically, it's unknown whether LLM-generated applications exhibit **software aging symptoms** (e.g., progressive degradation of performance or dependability due to resource leaks, memory bloat, or accumulated errors) when deployed as continuously running backend services. Functional correctness alone is insufficient to assess their suitability for real-world, long-running environments.

### Method

1.  **Application Generation:** Four backend application scenarios (image converter, credit card password manager, process monitoring tool, service availability checker) derived from BaxBench prompts were used. Implementations were generated in three distinct generation-and-execution environments:
    *   JavaScript (Node.js/Express) via Bolt
    *   Python (FastAPI) via ChatGPT
    *   Rust (Actix Web) via Gemini
    *   Each generated application was functionally validated using BaxBench-derived tests; failed generations were discarded and regenerated.
2.  **Long-Duration Workload Execution:** Functionally validated applications were subjected to **48-hour continuous workload executions** using Apache JMeter, simulating sustained usage.
3.  **Monitoring:** During execution, key operational metrics were monitored: **memory usage, response time, and throughput**.
4.  **Statistical Analysis:** The collected data were analyzed for degradation trends using the **Mann–Kendall test** and **Sen’s slope estimator** to identify statistically significant changes.
5.  **Complementary Analyses:**
    *   **Static Analysis & LLM-Assisted Code Review:** The source code of LLM-generated applications was statically analyzed to identify plausible code-level mechanisms (e.g., unbounded persistent state, missing cleanup paths, conditional resource retention) that could explain observed aging symptoms.
    *   **Comparison with Human-Written Systems:** An exploratory comparison was made with functionally related human-written open-source implementations using the same workload and monitoring procedures to contextualize the findings.

### Impact

*   **Evidence of Software Aging:** LLM-generated applications *do* exhibit software aging symptoms. **Memory usage was identified as the most consistent indicator**, showing statistically significant upward trends across most application-language combinations. Response time and throughput behavior were more heterogeneous.
*   **Identified Aging Mechanisms:** Static analysis successfully identified plausible code-level aging mechanisms (such as unbounded persistent state, missing cleanup paths, and conditional resource retention) in the LLM-generated code, providing insights into the root causes of degradation.
*   **Comparison to Human-Written Code:** The study found that software aging trends are not unique to LLM-generated code; **human-written implementations of similar backend scenarios can also exhibit comparable or even stronger aging symptoms**, contextualizing the findings within the broader software engineering landscape.
*   **Crucial Implication for Deployment:** The findings highlight that **functional correctness alone is insufficient** to assess the operational reliability of LLM-generated software intended for continuous, long-running deployment. Developers and organizations must consider long-term reliability and potential aging effects before deploying such systems in production.
*   **Extension of Research:** This work extends software aging research into the critical and rapidly growing domain of LLM-generated applications, opening new avenues for future investigation into the long-term dependability of AI-generated software.