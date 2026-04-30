# AGEL-Comp: A Neuro-Symbolic Framework for Compositional Generalization in Interactive Agents

- **Category:** Artificial Intelligence
- **Date:** 2026-04-29
- **Link:** http://arxiv.org/abs/2604.26522v1

---
```markdown
### Problem

Large Language Model (LLM)-based agents struggle with **compositional generalization**, which is the ability to understand and produce novel combinations from known, primitive components. This leads to systemic failures and brittleness in interactive environments because their knowledge is primarily statistical, disembodied, and lacks empirical grounding in a structured, causal world. They rely on pattern matching rather than a systematic, interpretable understanding.

### Method

The paper introduces **AGEL-Comp (Action-Grounded Experiential Learning for Compositionality)**, a novel neuro-symbolic AI agent architecture designed to foster compositional reasoning by grounding agent actions. It integrates three core innovations:

1.  **Dynamic Causal Program Graph (CPG) as a World Model (W):** Represents the agent's procedural and causal knowledge as a structured, executable directed hypergraph. Nodes are grounded predicates or concepts, and hyperedges are Horn clauses modeling logical/causal dependencies. This modular structure facilitates hierarchical planning.
2.  **Inductive Logic Programming (ILP) Engine (G):** Synthesizes new, generalizable Horn clauses from sparse experiential feedback, formally grounding symbolic knowledge through interaction. This engine is part of the "Grounding Function."
3.  **Hybrid Reasoning Core:**
    *   An **LLM acts as a high-level Planner** to generate a set of candidate sub-goals given a goal and percept.
    *   A **Neural Theorem Prover (NTP) acts as a Verifier**, checking the logical consistency and soundness of these candidate sub-goals against the agent's CPG world model. It performs differentiable backward chaining to produce proof scores and paths, which are translated into executable action sequences.

These components operationalize a **deduction–abduction learning cycle**: the agent deduces plans (LLM + NTP) and abductively expands its symbolic world model (via ILP from experience), with neural adaptation aligning the reasoning engine.

The **Grounding Function (G)** is a two-stage mechanism:
*   **Stage 1: Experience-Driven Causal Attribution (using Minimal Contrastive Search - MCS):** Addresses the credit assignment problem when a prediction error occurs (actual feedback differs from expected). It identifies the minimal set of environmental literals in the trigger state responsible for the unexpected outcome.
*   **Stage 2: Abstractive Induction (using ILP):** Generalizes these specific causal attributions into reusable symbolic Horn clauses, which are then integrated into the CPG world model.

The framework is evaluated in the **Retro Quest simulation environment** using a new protocol specifically designed for compositional generalization.

### Impact

AGEL-Comp provides a principled path toward agents that build an **explicit, interpretable, and compositionally structured understanding of their world**.

Key impacts and contributions include:
*   **Significantly better performance** over pure LLM-based models in compositional generalization scenarios.
*   The **AGEL-Comp architecture**, a hybrid cognitive framework that enforces compositional reasoning in LLM-based agents.
*   A **hybrid deductive-abductive learning cycle** that enables agents to learn from interaction by dynamically expanding their symbolic world model and adapting their neural reasoner.
*   A **two-stage grounding mechanism** that effectively transforms raw experience into symbolic rules via causal attribution and inductive synthesis.
```