# Models Recall What They Violate: Constraint Adherence in Multi-Turn LLM Ideation

- **Category:** NLP
- **Date:** 2026-04-30
- **Link:** http://arxiv.org/abs/2604.28031v1

---
Here's a summary of the research paper in Markdown format:

---

### Problem

Multi-turn Large Language Model (LLM) interaction is prevalent, but existing benchmarks do not adequately evaluate **constraint adherence** under **iterative pressure** across sustained dialogue. Crucially, they fail to assess whether LLMs can **recall** their initial constraints while simultaneously **violating** them in their outputs. This gap challenges prevailing theories of multi-turn degradation, which often attribute performance drops primarily to forgetting or context loss, suggesting a more complex underlying mechanism.

### Method

To address this, the authors introduce **DRIFTBENCH**, a novel benchmark designed for evaluating constraint adherence in multi-turn LLM-assisted scientific ideation.

1.  **Task:** LLMs were tasked with iteratively refining research proposals based on 38 structured research briefs from 24 scientific domains. Each brief included clear objectives, **hard constraints** (binary-checkable), and banned moves to enable objective scoring.
2.  **Models:** Seven diverse LLMs (including frontier commercial models like GPT-5.4 and Gemini 3.1 Pro, and open-weight models like Qwen3-235B and Llama-3.3-70B-Instruct) were tested.
3.  **Interaction Conditions:** Four conditions simulated different multi-turn scenarios:
    *   **Single-shot (SS):** Baseline, one turn.
    *   **Multi-turn neutral (MT-N):** Six turns with generic "Continue" prompts.
    *   **Multi-turn pressure (MT-P):** Six turns with escalating refinement pressure (e.g., "Make it more novel").
    *   **Checkpointed (CK-P):** Multi-turn pressure with structured reflection/restatement after turns 2 and 4.
4.  **Restatement Probe:** A critical, separate API call at each multi-turn step asked the model to verbatim reproduce the original objective, hard constraints, and banned moves. This probe was *not* fed back to the model, isolating declarative recall.
5.  **Scoring:** Outputs were scored by cross-family LLM judges on a 0-4 rubric for objective fidelity, **constraint adherence**, alternative coverage, and **complexity inflation**. The primary metric derived was the **"knows-but-violates" (KBV) rate**, which measures the proportion of runs where a model correctly restates constraints (≥80% recall) yet scores below 4 on adherence (any non-compliance).
6.  **Validation:** Human validation with blind raters confirmed that the LLM judge consistently *under-detected* constraint violations, meaning reported adherence scores are conservative. Sensitivity analyses confirmed robustness to temperature and pressure type.

### Impact

The research reveals a robust and widespread **"knows-but-violates" (KBV) phenomenon**, which is the paper's central empirical finding:

1.  **Recall-Adherence Dissociation:** Models can achieve near-perfect declarative recall of original constraints (up to 100% across six of seven models) while simultaneously exhibiting high rates of non-compliance in their generated ideas. KBV rates varied drastically from **8% (GPT-5.4)** to **99% (Sonnet 4.6)** across the tested models, with five of seven models exceeding 50%. This directly challenges the assumption that multi-turn degradation is primarily driven by forgetting or context loss.
2.  **Universal Complexity Inflation:** Iterative pressure reliably increased structural complexity across *all seven* benchmarked models, even when not explicitly prompted for it. This effect was structural rather than merely an increase in output length.
3.  **Widespread Constraint Drift:** Multi-turn pressure consistently reduced adherence to original constraints across models, with degradation varying significantly across providers and model types.
4.  **Limited Mitigation:** While structured checkpointing partially reduced KBV rates, it did not fully close the dissociation between recall and adherence, and complexity inflation persisted.
5.  **Conservative Estimates:** Human validation confirmed that the automated LLM judge *under-detected* constraint violations compared to human raters, implying that the reported adherence issues are conservative estimates of the true problem.
6.  **Open Benchmark:** The **DRIFTBENCH** dataset, including all briefs, prompts, rubrics, transcripts, and scores, is openly released to facilitate further research into this critical aspect of LLM behavior.

---