# AI-Assisted Unit Test Writing and Test-Driven Code Refactoring: A Case Study

- **Category:** Artificial Intelligence
- **Date:** 2026-04-03
- **Link:** http://arxiv.org/abs/2604.03135v1

---
This paper presents a case study on using AI-assisted tools for a two-stage software development workflow: generating comprehensive unit tests and then using those tests to safely guide large-scale code refactoring in a commercial frontend codebase.

### Problem

Many software systems, especially those originating as prototypes or Minimum Viable Products (MVPs), prioritize rapid delivery over long-term maintainability. This leads to codebases burdened with technical debt, making them difficult to modify, costly to refactor, and suboptimal for the emerging era of AI-assisted programming (where models perform best in predictable, well-organized environments). Traditional human-led refactoring of such undertested systems is risky and expensive due to the lack of comprehensive test suites to act as safety mechanisms against regressions.

### Method

The authors employed an integrated, two-stage, human-in-the-loop workflow using Large Language Models (LLMs) on a production React/Next.js frontend codebase (approximately 19,000 Lines of Code, previously lacking consistent testing).

1.  **AI-Assisted Test Suite Construction:**
    *   **Setup:** A hierarchical multi-agent approach was used: Gemini 2.5 Pro as a "planner" (for high-level strategy and cross-module dependencies) and Cursor's integrated models as "executors" (for repetitive test implementation and localized changes).
    *   **Workflow:** Followed a "Plan-Act-Verify" loop. Persistent rule files (`GEMINI.md`, `.cursorrules`) and planning documents guided the LLMs on naming conventions, architectural constraints, and test generation principles (e.g., no modifying source code, no mocking internal hooks).
    *   **Validation:** Tests were run on existing source code. Failing tests were given limited retries, then eliminated. Critically, **mutation testing** was applied to identify and prune ineffective tests (addressing "value misalignment" where LLMs might generate performant but low-quality tests). A human reviewer approved entire iterations after generation and mutation testing. The model was allowed to iteratively refactor its own test code.

2.  **AI-Assisted Test-Guarded Refactor:**
    *   **Setup:** The same planner-executor model setup was used. Rule files contained coding guidelines and imposed strict limitations, most importantly that **test files could not be modified** (except for variable renames, etc.).
    *   **Workflow:** The planner model devised refactoring strategies to improve modularity, reduce file sizes, and alleviate complexity hotspots. The executor models performed the code changes.
    *   **Validation:** The comprehensive, AI-generated test suite from Stage 1 acted as the primary guardrail. All refactoring changes were validated by ensuring that the entire test suite continued to pass, preserving existing behavior. Human developers provided supervision and final approval.

### Impact

The study demonstrated significant positive impacts across efficiency, code quality, and risk reduction:

1.  **Efficiency:** Generated nearly **16,000 lines of reliable unit tests** (including mocks, fixtures, and setup utilities) in **hours rather than weeks**, transforming an undertested codebase into one with extensive coverage.
2.  **Test Coverage & Quality:** Achieved up to **78% branch coverage and 67.85% line coverage** in critical, logic-heavy modules (from a negligible baseline). The AI also developed substantial shared test infrastructure (e.g., a centralized mock data catalog, API-mocking layer, global test harness), improving reuse and stability. The test suite evolved to be modular, systematic, and aligned with architectural boundaries.
3.  **Refactoring Outcomes:**
    *   **Structural Transformation:** The refactoring transformed a poorly-organized MVP into a well-defined layered architecture with improved modularity and clear boundaries.
    *   **Reduced Coupling:** The routing layer's internal imports were reduced by **57.5%**, redistributing logic into new `features` and `shared` layers.
    *   **Lower Complexity:** The average cyclomatic complexity per function decreased from 2.24 to 2.13 (and to 1.97 within the routing layer).
    *   **Manageable Code Growth:** While total Lines of Code (LOC) increased by 16.1% and file count by 26, this was attributed to architectural redistribution (120 file deletions vs. 146 additions) rather than bloat, resulting in higher functional cohesion.
    *   **Regression Risk Reduction:** The extensive, AI-generated test suite significantly reduced regression risk during large-scale refactoring by acting as robust guardrails, ensuring externally observable behavior was preserved.

In conclusion, the research shows that AI-assisted workflows can effectively be applied to mature, production systems for significant architectural improvements, provided initial guidance (rule files), robust validation mechanisms (model harnesses, mutation testing), and human supervision are in place.