# DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA

- **Category:** NLP
- **Date:** 2026-05-21
- **Link:** http://arxiv.org/abs/2605.22411v1

---
## DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA

### Problem

Large language model (LLM) agents struggle with long-term memory question answering (QA) because answer-supporting evidence is often scattered across extensive conversational histories and buried under significant irrelevant content. Existing memory systems typically:
1.  Organize memory *before* future queries are known (query-agnostic), potentially discarding or blurring crucial details.
2.  Retrieve information based on indirect relevance cues like embedding similarity, often yielding a high-recall but highly noisy set of candidates.
3.  Leave the task of denoising and reconstructing query-specific evidence to the downstream answerer, which is inefficient and a critical bottleneck. LLMs also face "lost in the middle" problems with very long contexts.

### Method

DeferMem is a long-term memory framework that addresses this by decoupling the problem into two stages: high-recall candidate retrieval and query-conditioned evidence distillation.

1.  **High-Recall Candidate Retrieval (Segment-Link Structure):**
    *   Instead of compressing memory pre-query, DeferMem organizes raw conversation history using a lightweight **segment-link structure**.
    *   **Segment Construction:** Divides each session into contiguous segments based on discourse transitions and semantic similarity, preserving raw messages.
    *   **Segment-Link Construction:** Connects semantically related segments across the entire history, capturing topic continuity.
    *   **Query-Time Retrieval:** Given a query, it retrieves top-k relevant messages, then expands to their containing segments and linked segments. This generates a broad, high-recall, but noisy candidate set (`C_hat`).

2.  **Query-Conditioned Evidence Distillation (DistillPO):**
    *   A **memory distiller** (a trainable LLM policy `πθ`) is used to transform the noisy candidate set (`C_hat`) into a compact set of faithful, self-contained, and query-conditioned evidence (`E_hat`).
    *   The distiller is trained with **DistillPO**, a novel reinforcement learning algorithm, which formulates post-retrieval evidence distillation as a **structured action**:
        *   **Message Selection:** Identifies useful messages from `C_hat`.
        *   **Evidence Rewriting:** Generates distilled evidence statements, aligned with selected messages, faithful to sources, self-contained, and conditioned on the query.
    *   **Decomposed-and-Gated Reward Pipeline:** DistillPO uses eight verifiable reward components covering output schema validity, message selection quality (coverage, conciseness), evidence quality (alignment, faithfulness, self-contained), and downstream answerability. It employs a *leaky hierarchical gating strategy* to expose task-level correctness feedback early while still enforcing dependencies for validity-related rewards.
    *   **Structure-Aligned Advantage Assignment:** Rewards are specifically assigned to the responsible output spans (selection-related rewards to message identifiers, rewriting/answerability rewards to evidence statements) to improve learning efficiency.
    *   A full-reward anchor completion strategy is also used to stabilize training.

### Impact

DeferMem demonstrates significant improvements over strong baselines:

*   **Higher QA Accuracy:** Achieves the highest QA accuracy on long-term memory QA benchmarks (LoCoMo and LongMemEval-S).
*   **Improved Efficiency:**
    *   Fastest runtime for memory operations.
    *   Zero commercial-API token cost for memory operations (pre-LLM answerer).
*   **Effective Evidence Distillation:** Successfully distills highly noisy candidates into precise, query-conditioned evidence, offloading this crucial task from the downstream LLM answerer.
*   **Enhanced LLM Agent Capabilities:** Enables LLM agents to efficiently and accurately utilize long-term memory for flexible and sustained interactions.