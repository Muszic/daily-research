# Can LLMs Solve Science or Just Write Code? Evaluating Quantum Solver Generation

- **Category:** Software Engineering
- **Date:** 2026-05-08
- **Link:** http://arxiv.org/abs/2605.07525v1

---
This paper introduces Q-SAGE, a novel iterative methodology for evaluating the capability of Large Language Models (LLMs) in generating numerically accurate quantum solvers for scientific problems.

## Problem

LLMs demonstrate strong capabilities in general code generation, which motivates their application to automated quantum solver development. However, for scientific computing problems in quantum mechanics, simple code execution or syntactic correctness is insufficient. The actual correctness of quantum solver code depends on:

1.  **Numerical accuracy:** Results must match classical solutions within a precise tolerance.
2.  **Complexity of quantum systems:** This involves non-trivial mappings (e.g., fermion-to-qubit), hybrid quantum-classical workflows, and algorithm-specific approximations, all of which are sensitive to errors.
3.  **Lack of sufficient evaluation:** Existing benchmarks for LLM-generated quantum code primarily focus on circuit validity, compilation success, or syntax, rather than end-to-end numerical correctness against trusted scientific references for complex problems.
4.  **Error-prone manual development:** Adapting textbook quantum algorithms to specific instances (e.g., different physical parameters, languages, APIs) is a complex and error-prone engineering task.

## Method

The paper introduces **Q-SAGE (Quantum-Solver Automated GEneration)**, an iterative, execution-based methodology designed to evaluate LLM-generated quantum solver code for numerical correctness.

1.  **Iterative Loop:** Q-SAGE operates on a `generate-execute-verify-refine` loop.
    *   **Generate:** An LLM is prompted (using a detailed "coder prompt" specifying the problem, software stack, parameters, computational steps, and output requirements) to generate quantum solver code.
    *   **Execute:** The generated code is executed in a controlled environment. Concurrently, a "classical solver" (a trusted numerical implementation) runs to compute a reference solution for the given problem instance.
    *   **Verify:** A "verifier" component compares the quantum solver's output with the classical solver's reference value. Correctness is determined by numerical agreement within a predefined tolerance.
    *   **Refine:** If the code fails to execute or produce numerically accurate results, execution feedback (e.g., error messages, incorrect output) is provided to the LLM, prompting it to refine the script in a new iteration. This loop continues for a set number of turns or until a correct solution is found.
2.  **Problem Agnosticism:** The methodology is designed to be problem-agnostic; adapting it to different scientific problems only requires defining new prompts and a corresponding classical solver for verification.
3.  **Empirical Evaluation:** The methodology was empirically evaluated using:
    *   **Five problem families (PFs):** Ranging in complexity and domain (e.g., Fermi-Hubbard model, Transverse Field Ising Model, MaxCut, Schwinger model, Molecular Electronic Structure).
    *   **Five LLMs:** Including both open-source and proprietary models.
    *   **Two feedback configurations:** One providing only the previous output, and another providing the previous output *plus* the expected reference result from the classical solver.
    *   **Metrics:** Success rate (success@t, i.e., success by turn `t`) and computational time overhead.

## Impact

The research reveals significant insights into LLMs' capabilities and limitations in generating scientific quantum solvers:

1.  **Improved Success Rates via Iterative Refinement:** Iterative refinement with feedback (Q-SAGE) substantially improves the success rates of LLMs in generating correct quantum solvers compared to single-turn generation.
2.  **Significant Computational Overhead:** This improvement comes at the cost of a significant computational overhead due to the multiple execution and refinement steps.
3.  **Shift in Failure Modes:** As LLM capabilities improve, the primary failure modes shift from basic execution errors (e.g., syntax, runtime) to more subtle and harder-to-diagnose **numerical inaccuracies**. This highlights a critical limitation of current LLMs in handling the precise numerical demands of scientific quantum problems.
4.  **Complexity Matters:** LLMs perform better for problems with lower algorithmic complexity (e.g., PF2 and PF3 showed much higher success rates) but struggle significantly with more complex transformations and physics (e.g., PF1, PF4, PF5 had very low success rates).
5.  **Novel Benchmark:** Q-SAGE provides a robust methodology and benchmark for evaluating LLM-generated scientific quantum code for **end-to-end numerical correctness**, a crucial aspect previously underexplored.
6.  **Practical Implications:** The findings offer actionable insights for software engineers and physicists on the current limitations of LLMs for quantum software development and the trade-offs involved in using iterative refinement.