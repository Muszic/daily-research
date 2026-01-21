# APEX-Agents

- **Category:** NLP
- **Date:** 2026-01-20
- **Link:** http://arxiv.org/abs/2601.14242v1

---
**Problem:**
Existing AI agent evaluations suffer from a significant "sim-to-real gap," being too narrow and simplistic to accurately assess agents' ability to perform complex, long-horizon, and cross-application tasks common in professional services (e.g., investment banking, management consulting, corporate law). There is a need for a robust benchmark that reflects the intricate demands of real-world knowledge work environments, requiring advanced reasoning, multi-application use, and long-term planning.

**Method:**
The authors introduce **APEX–Agents**, a new benchmark designed to evaluate AI agents on realistic professional services tasks.
1.  **Task Creation:** Over 250 domain experts (former consultants, bankers, lawyers) were surveyed to understand their daily work. They then created 33 "data-rich worlds" based on real-world project scenarios. Each world contains an average of 166 files and up to 63 tools across 9 applications (web search disabled for reproducibility). Within these worlds, experts crafted 480 challenging, long-horizon tasks, requiring agents to use the provided files and tools.
2.  **Evaluation Protocol:** Eight frontier AI agents (e.g., Gemini 3 Flash, GPT-5.2, Claude Opus 4.5) were tested. Each agent attempted every task 8 times. Agent outputs were graded by a judge model (Gemini 3 Flash, 98.5% accuracy) against expert-designed rubrics and gold outputs. The primary metric is Pass@1, the proportion of tasks where an agent successfully meets all criteria on its first attempt.
3.  **Open-Sourcing:** The APEX–Agents benchmark (including prompts, rubrics, gold outputs, files, and metadata) and the "Archipelago" agent execution/evaluation infrastructure are open-sourced to facilitate further research.

**Impact:**
1.  **Benchmark Contribution:** APEX–Agents provides a crucial, realistic, and complex benchmark that addresses the limitations of prior agent evaluations, offering a more accurate measure of AI agents' capabilities in professional settings.
2.  **Agent Performance Insights:**
    *   Current frontier AI agents demonstrate low reliability, with the best-performing model (Gemini 3 Flash) achieving only 24.0% Pass@1, highlighting significant room for improvement in completing complex professional tasks autonomously.
    *   Closed-source models substantially outperform open-source models.
    *   Agents show potential capability (e.g., GPT-5.2 achieved 40.0% Pass@8), but suffer from inconsistency (much lower Pass^8 scores), indicating a need for enhanced robustness.
    *   Even when failing to complete tasks fully, agents often produce partially useful outputs (higher mean scores).
3.  **Future Research & Development:** By open-sourcing the benchmark and infrastructure, the research provides valuable resources to accelerate the development of more capable, reliable, and consistent AI agents, which could profoundly reshape knowledge work and productivity.