# Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under Distribution Shift

- **Category:** NLP
- **Date:** 2026-07-10
- **Link:** http://arxiv.org/abs/2607.09175v1

---
```markdown
### Problem

Deployed LLM agents rely on "agentic context," specifically a mutable, persistent system-level instruction, to guide their behavior. Over long evolution horizons, maintaining this instruction as flat text makes verification increasingly difficult due to the accumulation and interaction of instructions. This leads to issues like "context collapse," unbounded memory growth, and guideline conflict accumulation. The core problem is that flat-text maintenance leaves structural relationships implicit, making effective verification over growing context challenging, especially under distribution shift.

### Method

The authors propose **Graph-Regularized Agentic Context Evolution (GRACE)**, a system that maintains the persistent instruction component as a typed semantic graph.

1.  **Graph-Regularized Substrate:** Atomic instruction units are represented as nodes, and structural relationships (e.g., `supports`, `refines`, `sequence`) are encoded as typed directed edges. A network schema defines admissible object types (e.g., `identity`, `norm`, `knowledge`) and relation types, ensuring schema-conformant updates.
2.  **Evolution Pipeline:**
    *   **Operation Planning:** Based on diagnostic observations, GRACE plans proposed graph edits.
    *   **Structural Validation:** Proposed updates are validated within the local typed neighborhoods of modified nodes, combining deterministic schema checks with iterative structural analysis. This "scoped verification" is central to addressing the flat-text limitations.
    *   **Delta Reconstruction:** Accepted graph updates are then reconstructed as incremental text edits to generate the textual instruction checkpoint used for deployment.

GRACE isolates the representation substrate and verification mechanism, keeping the LLM, tools, harness, diagnosis, and evaluation fixed.

### Impact

GRACE significantly improves the reliability of LLM agents under long-horizon context evolution and distribution shift:

*   **Improved Reliability:** Evaluated within a fixed telecom agent harness under a controlled distribution-shift protocol, GRACE improved strict reliability (measured by `pass^3`) from a Gemini 2.5 Flash zero-shot baseline of 0.091 to **0.673 ± 0.136** at the final checkpoint.
*   **Outperformance:** This result substantially exceeds a Gemini 3.1 Pro zero-shot reference (0.242) and a flat-text Human Context Evolution (HCE) baseline (0.191 ± 0.051).
*   **Key Requirements for Reliability:** The research identifies two critical requirements for reliable long-horizon context evolution:
    1.  A structural substrate that enables local verification.
    2.  A consolidation mechanism to maintain the usability of accumulated instruction content.
*   **Contributions:** GRACE introduces a graph-regularized substrate with scoped structural validation, an evaluation protocol with alternating distribution shift to test both within-phase improvement and cross-phase retention, and demonstrated its superior performance through replicated experiments. An ablation study highlighted that both contradiction avoidance and instruction consolidation are essential for sustained improvement.
```