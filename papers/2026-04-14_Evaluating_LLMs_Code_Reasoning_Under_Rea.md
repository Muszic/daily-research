# Evaluating LLMs Code Reasoning Under Real-World Context

- **Category:** Software Engineering
- **Date:** 2026-04-14
- **Link:** http://arxiv.org/abs/2604.12881v1

---
### Problem

*   Existing benchmarks for evaluating Large Language Models (LLMs) on code reasoning tasks are often simplistic. They rely on LLM-generated snippets or human-written solutions to code challenges, restricting inputs and outputs to primitive data types.
*   This simplification fails to capture the structural complexity, inter/intra-procedural dependencies, and diverse data types (compound, custom) found in real-world software projects.
*   Consequently, current evaluations may overestimate LLMs' practical generalizability and code reasoning abilities in realistic contexts.

### Method

*   The paper introduces **R2Eval**, a new benchmark designed for realistic code reasoning evaluation.
*   **Data Source:** R2Eval comprises 135 code reasoning problems meticulously extracted from ten widely used, real-world Python projects (e.g., scikit-learn, django, requests).
*   **Handling Complex Data:** A core innovation is the ability to handle compound and custom data types, which are prevalent in real-world code but often discarded by prior benchmarks. R2Eval leverages static and dynamic program analysis to:
    *   Iteratively decompose complex data types (inputs/outputs) into primitives or core compound types.
    *   Serialize these complex values into a JSON format that LLMs can process, preserving the original data's complexity.
*   **Robust Evaluation:** To accurately assess LLM predictions and avoid false negatives from textual comparisons, R2Eval deserializes LLM outputs and generates runtime tests to verify correctness against ground truth objects.
*   **Problem Structure:** Each problem is provided as a triplet `{P, I, O}`, where `P` is the code (including dependencies and context), and `I`/`O` are the serialized inputs/outputs.

### Impact

*   **Significant Performance Drop:** Experiments using R2Eval show a substantial performance drop for assessed LLMs compared to their performance on the simpler CRUXEval benchmark (e.g., 64.32% for input prediction and 52.22% for output prediction).
*   **Questioning LLM Claims:** This drastic reduction in performance challenges "bold claims" about LLMs' code reasoning capabilities, indicating that high scores on simplified benchmarks do not translate to real-world robustness.
*   **Promoting Realistic Evaluation:** R2Eval promotes a more meaningful and rigorous evaluation of LLMs' code reasoning by incorporating real-world project complexities like inter/intra-procedural dependencies, third-party API usage, and non-primitive data types.
*   **Advancing LLM Development:** The findings highlight critical areas for improvement in LLMs, aiming to motivate the development of models that exhibit genuinely robust code reasoning under practical, real-world software engineering settings.