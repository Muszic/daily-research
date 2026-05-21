# A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents

- **Category:** Software Engineering
- **Date:** 2026-05-19
- **Link:** http://arxiv.org/abs/2605.20173v1

---
```markdown
### Problem

Production Large Language Model (LLM) agents combine a stochastic LLM core with surrounding deterministic systems. Failures often arise not from the LLM itself, but from the un-named and implicitly designed "load-bearing engineering surface" where LLM outputs become system actions. As LLM core capabilities improve and per-call variance ($\sigma$) diminishes, architectural choices become the dominant factor ($\mu$, "architectural momentum") in an agent's long-term reliability ($y(t) = \mu t + \sigma\xi(t)$). Practitioners lack an explicit framework to design this critical interface, leading to costly rediscoveries and inconsistent reliability.

### Method

The paper introduces:

1.  **The Stochastic-Deterministic Boundary (SDB):** A named primitive defining the interface where an LLM proposal becomes a system action. It's a four-part contract:
    *   **Proposer:** The LLM's output.
    *   **Verifier:** A deterministic check (e.g., schema, policy rule, state-machine transition predicate).
    *   **Commit Step:** The durable write or external side-effect.
    *   **Reject Signal:** A typed response to the LLM if verification fails.
    (Empirical audit found explicit verifier/commit logic at 19/21 LLM-to-action call sites in open-source frameworks, and 71% of agent failures localized to SDB weaknesses).

2.  **Organizing Framework:** Three orthogonal concerns for production agent runtimes:
    *   **Coordination:** How work splits and combines (inspired by Actor model).
    *   **State:** How the system remembers (influenced by CAP theorem, event-time vs. processing-time).
    *   **Control:** Who decides what runs and when to stop (from control theory, e.g., supervision).

3.  **Pattern Catalog:** Six architectural patterns, derived from established distributed-systems results (e.g., actors, sagas, state machines, supervision), adapted for stochastic workers, and organized by the three concerns. Each pattern specifies how the SDB is assembled to provide resilience (e.g., Hierarchical Delegation for Coordination, Event-Driven Sequencing for State, Supervisor plus Gate for Control).

4.  **Methodology for Selection and Diagnosis:**
    *   A **five-step selection methodology** with decision predicates based on systems trade-offs to choose appropriate patterns for a given workload.
    *   A **diagnostic procedure** that maps observed production failures to specific patterns through a failure-signature catalog, identifying common issues like "replay divergence" (where LLM consumers of an event log produce different outputs under model-version change).

### Impact

The proposed methodology and SDB primitive significantly impact the design and reliability of production LLM agents by:

*   **Providing a Formal Design Surface:** Offering a common language and explicit design primitive (SDB) for architecting the critical interface between LLMs and deterministic systems, moving beyond ad-hoc solutions.
*   **Improving Long-Run Reliability:** Enabling practitioners to strategically design for "architectural momentum" ($\mu$) by strengthening SDBs and selecting appropriate patterns, which becomes the dominant lever on reliability as base models improve.
*   **Enhancing Failure Analysis and Resolution:** Equipping teams with a diagnostic framework to localize production failures to specific SDB weaknesses or pattern misapplications, leading to more targeted and effective fixes.
*   **Catalyzing Pattern Discovery:** Establishing an open framework that can accommodate and predict the emergence of new architectural patterns as the field matures.
*   **Validated Practicality:** Demonstrated applicability through end-to-end application on five diverse workloads, including a runnable reference implementation, showcasing its real-world utility.
```