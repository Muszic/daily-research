# Long-Range Indirect Control-Flow Prediction in Stripped Binaries via Dual Virtual Hubs and Multi-Task Graph Learning

- **Category:** Cryptography
- **Date:** 2026-09-03
- **Link:** http://arxiv.org/abs/2609.03280v1

---
```markdown
### Problem

Recovering Indirect Control-Flow (ICF) edges in stripped binaries is fundamental for security analysis but presents several challenges for existing methods:
1.  **Long-Range Dependencies:** Current graph-based models struggle to propagate information across many hops, degrading performance when evidence for an ICF transfer is distant or fragmented across the graph.
2.  **Task Fragmentation:** Existing solutions compartmentalize different ICF types (indirect calls, indirect tail calls, jump tables, returns), missing useful cross-type structural relationships and underutilizing supervision.
3.  **Ground-Truth Quality:** Prior datasets often rely on single-source labels prone to over/under-approximation and lack clean, standardized test protocols, leading to unreliable benchmarks.
4.  **Data Leakage:** Inadequate dataset partitioning (e.g., without package-level isolation or function-level deduplication) allows models to memorize artifacts, inflating reported performance and limiting generalization.

### Method

The authors propose **ICFlowNet**, a unified framework addressing these challenges:

1.  **Augmented CFG with Dual Virtual Hubs:**
    *   **Base Graph:** Recovers a heterogeneous augmented Control-Flow Graph (ACFG) from stripped binaries using `angr` and symbolization, preserving direct control-flow and code-data cross-references (xRefs).
    *   **Global Code Hub (GCH):** A virtual node that provides short routing paths among task-relevant code candidates (sources and destinations of potential ICFs), addressing long-range code dependencies.
    *   **Global Data Hub (GDH):** A virtual node that aggregates data-side evidence by connecting only to a sparsified neighborhood of data nodes (within 2-hops of code candidates), avoiding indiscriminate global aggregation.
    *   **Purpose:** These candidate-aware hubs create constant-depth communication paths between distant code and data evidence, mitigating long-range bottlenecks while preserving graph sparsity.

2.  **Multi-Task Graph Learning:**
    *   **Shared Encoder:** Uses a Heterogeneous Graph Attention Network (HGAT) to encode the augmented graph into relation-aware node representations, preserving distinct semantics for control-flow and data-flow edges.
    *   **Task-Specific Heads:** Adds separate prediction heads and classifiers for each ICF type (indirect calls, indirect tail calls, jump tables, and returns) on top of the shared encoder.
    *   **Purpose:** This allows the model to capture reusable structural patterns across ICF types, enabling inductive transfer (e.g., from abundant tasks like returns to rarer ones like indirect tail calls) while maintaining task-specific decision boundaries.

3.  **Rigorous Evaluation Protocol:**
    *   **Dataset:** Constructed a large-scale dataset of 15,901 unique stripped x86_64 binaries, including 1,351 with dynamic ground truth.
    *   **Leakage-Aware Splits:** Employs package-level splits and function-level mnemonic-hash deduplication to prevent data leakage between training and test sets.
    *   **Noise-Controlled Test Protocol:** Utilizes verified dynamic positives (observed targets) and absolute negatives (sampled only from regions outside static candidate sets) for credible and fair evaluation, avoiding penalizing plausible but unseen edges.
    *   **Supervision Source Separation:** Trains architecturally identical models under separate static (compiler-derived) and dynamic (Intel Pin traces) supervision regimes to isolate the impact of supervision quality.

### Impact

ICFlowNet significantly advances long-range ICF prediction in stripped binaries, demonstrating:
*   **Superior Performance:** The model outperforms prior baselines by more than **13 F1** on long-range indirect calls.
*   **Effectiveness of Architectural Designs:**
    *   Dual Virtual Hubs improve long-range F1 by up to **9.13 points**.
    *   Multi-task learning adds up to **5.81 points**.
*   **Efficiency:** These performance gains are achieved with only **11.44% topological overhead** from the virtual hubs.
*   **Empirical Insights:** The research reveals that merely scaling static supervision yields only marginal gains, underscoring the critical importance of structural repair (Dual Virtual Hubs) and cross-type transfer (multi-task learning) for robust ICF prediction.
*   **Credible Evaluation:** The developed leakage-aware, noise-controlled pipeline and dataset enable more reliable and transferable evaluation for learning-based binary analysis methods.
*   **Generalization:** ICFlowNet achieves robust, cross-dataset generalization across both static and dynamic settings, with notable gains on structurally complex inter-procedural ICF edges.
```