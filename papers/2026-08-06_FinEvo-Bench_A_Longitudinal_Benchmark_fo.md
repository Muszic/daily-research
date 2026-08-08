# FinEvo-Bench: A Longitudinal Benchmark for Self-Evolving Agents in Professional Financial Workflows

- **Category:** Artificial Intelligence
- **Date:** 2026-08-06
- **Link:** http://arxiv.org/abs/2608.06144v1

---
This paper introduces FinEvo-Bench, a new benchmark designed to evaluate the self-evolution capabilities of AI agents in complex, professional financial workflows.

## Problem

*   **Lack of Longitudinal Evaluation:** Most existing agent benchmarks evaluate tasks independently, failing to measure whether experience from one task helps with subsequent, related tasks. They assess current execution capability but not how knowledge accumulates or transfers over time.
*   **Missing Joint Coverage:** Current self-evolution benchmarks do not jointly cover three crucial aspects necessary for real-world professional settings:
    1.  **Professional Workflows:** Tasks embedded within defined professional procedures and constraints.
    2.  **Open-Ended Deliverables:** Outputs that can vary in form but must meet quality and compliance standards, not just match a reference answer.
    3.  **Multi-Aspect Evaluation:** Assessment that goes beyond simple success/failure to include task quality, financial compliance, and the ability to learn from retained experience.

## Method

*   **FinEvo-Bench Construction:**
    *   **Scope:** Contains 120 real-case-grounded, multi-file tasks across 20 business scenes and six financial domains (e.g., credit review, claim analysis).
    *   **Task Design:** Each scene comprises six related but substantively distinct cases sharing a professional procedure (defined by institution-provided protocols) and a manually reviewed rubric. Tasks are based on eligible institution-provided and publicly documented cases, with sensitive information removed.
    *   **Evaluation Rubrics:** Scene-level 100-point rubrics, constructed by two domain experts, assess output quality (correct use of inputs, complete analysis, supported conclusions) and financial compliance (e.g., fabricated data, definitive claims beyond role). The automated rubric judge demonstrated high agreement with a financial expert (ICC(A,1) = 0.95).
*   **Experimental Protocol:**
    *   **Agents:** Four self-evolving agent scaffolds (Claude Code, Codex, Letta, GenericAgent), all utilizing the Qwen3.7-Max backbone, were evaluated.
    *   **Longitudinal Stream:** Tasks were processed sequentially in three independently shuffled, globally interleaved streams (not contiguous scene blocks) to test experience retention amidst varied tasks.
    *   **Self-Evolution Measurement:** Each evolving run was paired with a "state-reset" (non-evolving) control run. This allowed for the isolation and quantification of self-evolution gains (score increase, compliance issue reduction) attributed to retained experience.
    *   **Feedback Mechanism:** After each task, agents received rubric-based feedback (summarizing problems, not the full rubric or a reference answer) for reflection and experience consolidation.
    *   **Scoring:** An independent Claude Code scoring agent, backed by Claude Opus 4.6, applied the scene rubrics to all outputs.
*   **Analysis:**
    *   **Metrics:** Task quality (mean rubric score), financial compliance (mean issues), self-evolution ability (paired gain in score and compliance reduction), and agent-side token cost.
    *   **Longitudinal Analysis:** Examined gains over "Early" (ranks 1-3) vs. "Late" (ranks 4-6) tasks within a scene to track experience accumulation.
    *   **Experience Carriers:** Diagnosed the performance of different experience retention mechanisms (memory-only, skill-only, combined memory-skill).
    *   **Feedback Forms:** Compared the effectiveness of rubric-based feedback versus complete reference answers.

## Impact

*   **Demonstrated Self-Evolution:** All four self-evolving agent scaffolds significantly outperformed their non-evolving controls, showing positive self-evolution gains (scores increased by 9.33–19.37 points, compliance issues reduced by 0.12–0.44 per task).
*   **Leading Agent Performance:** Letta achieved the highest evolved score (91.65) and fewest compliance issues (0.09 per task) in absolute terms. Codex demonstrated the largest self-evolution gain (+19.37 points).
*   **Evidence of Longitudinal Learning:** Paired score gains were notably higher for later tasks within a scene (ranks 4–6) compared to earlier ones (ranks 1–3), increasing by 6.10–8.70 points, indicating effective accumulation and transfer of experience.
*   **Optimized Experience Carriers:** For Claude Code, skill-only evolution produced the highest task quality (93.71 score) and fewest compliance issues (0.05 per task), outperforming memory-only and combined memory–skill approaches.
*   **Superior Feedback Mechanism:** Rubric-based feedback consistently yielded higher scores (3.95–7.93 points improvement) and fewer compliance issues (0.06–0.14 reduction) across all scaffolds compared to providing complete reference answers.
*   **Novel Benchmark:** FinEvo-Bench provides a critical tool for evaluating self-evolving agents in complex, professional financial domains, being the first benchmark to combine real-case tasks, professional workflows, open-ended deliverables, multi-aspect evaluation, and a robust longitudinal evaluation protocol.