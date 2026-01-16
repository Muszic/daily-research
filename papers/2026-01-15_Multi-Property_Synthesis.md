# Multi-Property Synthesis

- **Category:** Artificial Intelligence
- **Date:** 2026-01-15
- **Link:** http://arxiv.org/abs/2601.10651v1

---
```markdown
### Problem

Existing LTLf (Linear Temporal Logic over finite traces) synthesis methods operate on an "all-or-nothing" paradigm: they either synthesize a strategy to satisfy a single, monolithic specification or declare the problem unsolvable. This approach is restrictive in many real-world "over-subscribed" scenarios (e.g., robotics, multi-service orchestration, planning under resource constraints) where an agent faces multiple properties (goals), but satisfying all of them simultaneously may be impossible due to conflicts or environmental factors.

The challenge is to determine not just if all goals are achievable, but **which subsets of goals are realizable** and to synthesize strategies that achieve the most desirable (typically maximal) subsets, without resorting to computationally infeasible enumeration of all possible goal subsets.

### Method

The authors propose a novel multi-property LTLf synthesis technique that addresses this by computing realizability for all goal combinations simultaneously within a single fixed-point computation.

1.  **Multi-Property Game Arena:** They construct a single "multi-property game arena" by taking the product of individual DFA (Deterministic Finite Automaton) games for each LTLf property. This product state `s = (q1, ..., qn)` tracks progress towards all `n` goals.
2.  **Fixed-Point Computation for Realizable Sets:**
    *   They define a "multi-property winning relation" `WinM` as the least fixed point of controllable predecessors over pairs `(s, C)`, where `s` is a product state and `C` is a set of properties.
    *   The base case `WinM0` includes pairs `(s, C)` where all goals in `C` are already satisfied at `s`.
    *   The `PreMC` operator identifies states `s` from which an agent can guarantee, with one move, reaching a successor state `s'` that also enables realizing all goals in `C`, regardless of environment choices.
3.  **Maximal Multi-Property Synthesis:** To avoid tracking redundant subsets (due to monotonicity – if `C` is realizable, any `D ⊆ C` is also realizable), they refine the fixed-point computation to maintain only *maximal* realizable sets for each state. This uses a `Max` operator to prune non-maximal sets and a `PreMMC` operator that allows a successor state `s'` to guarantee satisfaction of *any* superset `D` of the currently considered `C` (`D ⊇ C`).
4.  **Symbolic Synthesis (Key Innovation):**
    *   They develop a fully symbolic algorithm that significantly improves efficiency.
    *   **Boolean Goal Variables:** They introduce `n` Boolean variables `K = {k1, ..., kn}` to represent subsets of properties (where `ki` is true if `φi` is in the subset).
    *   **Compact Representation:** The initial winning formula `w0(Z, K)` (where `Z` are state variables) is defined using implications: `w0(Z, K) := AND_i (ki => fi(Zi))`. This crucial formulation inherently captures the monotonicity property: if a state `Z` satisfies a set of goals `K`, it also satisfies any subset of `K`. This allows the algorithm to compactly represent exponentially many goal combinations without explicit enumeration.
    *   **Unified Fixed-Point:** The *same symbolic fixed-point computation* (using efficient Boolean operations, e.g., BDDs) as for single-property synthesis is then applied over the combined `Z` (state) and `K` (goal) variables. The resulting formula `w(Z, K)` compactly encodes the full maximal multi-property winning relation.
    *   **Strategy Extraction:** A winning strategy (finite transducer) can be extracted from the final symbolic move formula `t(Z, Y, K)` for any realizable maximal goal set `C`.

### Impact

*   **Significant Performance Improvement:** The symbolic approach substantially outperforms enumeration-based baselines, achieving speedups of up to **two orders of magnitude**.
*   **Comprehensive Realizability Analysis:** The method provides a complete characterization of which subsets of goals are simultaneously realizable from any given state, enabling a deep understanding of system capabilities.
*   **Enabling Principled Decision-Making:** By identifying maximal realizable goal sets, the approach allows agents in over-subscribed domains to make informed trade-offs and pursue the most desirable, yet achievable, outcomes.
*   **Algorithmic Efficiency:** The innovative use of Boolean goal variables and a unified symbolic fixed-point computation effectively exploits monotonicity to compactly represent and compute exponential numbers of goal combinations, making the problem tractable in practice despite its 2EXPTIME-completeness.
*   **Foundation for Complex AI Tasks:** This work provides a robust foundation for building more sophisticated AI systems that can handle partial satisfaction and dynamic goal prioritization in finite-horizon tasks.
```