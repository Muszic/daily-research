# Can Broad Biomedical Knowledge be Contextualized into Scenario-Grounded Propositions?

- **Category:** Artificial Intelligence
- **Date:** 2026-05-26
- **Link:** http://arxiv.org/abs/2605.27082v1

---
Here's a summary of the research paper in Markdown format:

```markdown
### Problem

Biomedical discovery faces a critical challenge: reconciling broad, abstract biomedical knowledge (e.g., "metabolic dysregulation") with specific, concrete experimental or clinical data (e.g., patient BMI, glucose levels). Broad knowledge is often too general to map directly onto concrete dataset variables, while data-driven patterns are typically dataset-specific and lack mechanistic insight. This mismatch creates a "missing link" or "gap," making it difficult to prioritize data patterns for follow-up or test plausible biomedical ideas in available data. The paper formulates this as **knowledge contextualization**: the need to transform broad biomedical knowledge into evidence-supported, scenario-grounded propositions that experts can efficiently inspect, replay, and validate. Challenges include:
1.  Broad biomedical concepts don't directly match concrete variables.
2.  The same principle requires different grounding across distinct settings.
3.  The search space for valid candidate propositions is immense.

### Method

The authors propose **SCENE (Scenario-Contextualized Evidence and Knowledge Engine)**, a bi-level multi-agent framework that implements knowledge contextualization as an iterative closed-loop search process.

1.  **Inputs:** SCENE takes biomedical prior knowledge, scenario-specific evidence (observables, outcomes, context), and a machine-readable data schema.
2.  **Bi-level Multi-Agent System:**
    *   **Upper Level (Direction Planning):** This level translates broad biomedical knowledge and task context into testable search directions. It formulates a **schema-grounding plan** by mapping these directions onto the dataset's variables and constraints (e.g., instantiating "metabolic dysregulation" with BMI, glucose, triglycerides). It also provides **search guidance** (operator mixtures, budgets, support floors, target preferences) to constrain the lower-level search space.
    *   **Lower Level (Knowledge Discovery Searching):** This level executes the grounded directions. It searches for concrete, executable propositions (e.g., subgroup rules in clinical trials, context-specific findings in L1000 studies) using **multi-objective optimization**. It balances two objectives:
        *   **Evidential Strength/Effect:** Measures the configured scenario contrast (e.g., treatment benefit contrast, target-response contrast).
        *   **Data Support:** Ensures the proposition is sufficiently supported by the data, preventing highly specific but poorly supported fragments.
        It uses evolutionary operators (mutation, crossover, tuning, injection) and retains a Pareto frontier of optimal candidates.
3.  **Closed-Loop Interaction:** A crucial bidirectional feedback loop exists. The upper level guides the lower level by constraining its search. In return, the lower level provides scenario-specific feedback (retained frontiers, execution logs, failure modes, trade-offs) to the upper level, allowing it to refine or pivot subsequent search directions.
4.  **Output:** SCENE produces a set of **scenario-grounded propositions**, each consisting of a search direction, an executable grounded rule or finding, and an evidence record with diagnostics and provenance for inspectability and replayability.

### Impact

SCENE effectively bridges the gap between broad biomedical knowledge and scenario-specific evidence, providing traceable and inspectable hypotheses.

1.  **Clinical Trial Subgroup Discovery:** In settings discovering patient subgroups with heterogeneous treatment benefits, SCENE consistently **outperforms existing baselines** (e.g., Virtual Twins, SIDES, Causal Forest). It discovers highly specific, strongly supported subgroups, demonstrating significantly higher risk reduction and stronger data support.
2.  **LINCS L1000 Studies:** In identifying context-specific biological responses, SCENE **uniquely enables the discovery of perturbational contexts** (cell-perturbagen-dose-time combinations) with strong target-response matching and high positive rates, which existing methods do not address.
3.  **Downstream Utility:** The scenario-grounded propositions discovered by SCENE can improve downstream tasks, such as **few-shot classification**.
4.  **Generality and Interpretability:** The framework's design demonstrates generality across distinct biomedical settings and yields interpretable, evidence-grounded findings crucial for follow-up validation.
```