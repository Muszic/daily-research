# AI with Authority, from Application to Silicon

- **Category:** Software Engineering
- **Date:** 2026-08-21
- **Link:** http://arxiv.org/abs/2608.21356v1

---
Here's a summary of the research paper in Markdown:

### Problem

For sixty years, machine verification has been an extremely costly overhead, making formal assurance practical only for exceptional artifacts and requiring extensive re-verification when requirements change. While generative AI can produce candidate proofs and designs quickly, it has not, by itself, solved the fundamental challenges of *trusting* these artifacts or making verification economically viable for widespread use. The field needs to address the cost, accessibility, and reliability governance of AI-produced verified mathematics.

### Method

The paper introduces the **Salt method**, a framework for highly autonomous AI development grounded in formal methods, demonstrating a paradigm shift where machine verification becomes essential for AI-scale productivity.

1.  **AI Fleet & Human Role:** One researcher, using consumer AI subscriptions, directed a fleet of five long-running AI agents (coordinator, mathematics, compiler, silicon, evidence). The human's role is limited to defining objectives in English, reviewing high-level statements/designs, and making rulings, acting as the "irreducible authority" at the human-language interfaces.
2.  **Kernel-Checked Truth:** Mathematical claims travel between agents only as kernel-checked artifacts (using the Lean 4 kernel against mathlib), ensuring no hallucinated proofs pass. The human never reviews proofs directly.
3.  **Five Artifacts per Task:** For every objective, agents produce five artifacts:
    *   An implementation (P)
    *   A formal specification (S)
    *   A machine-checked proof (`⊢ P ∈ S`) that the implementation meets the specification.
    *   Adversarial tests (`T(P)`) to check the proof's bite.
    *   Formal certificates (`S'`, `⊢ S ⇒ S'`) that restate the specification in simplified vocabulary, allowing human comprehension without full formal development.
4.  **Verification Chain (Application to Silicon):** Verification is established link-by-link:
    *   Application code to emitted design artifacts: Kernel-checked in Lean.
    *   Verilog to synthesized netlist: SAT-based equivalence checks (Yosys).
    *   Hardware verification utilizes a chain of independent checkers, recognizing the non-uniformity at the current verified-hardware boundary.
5.  **Operational Discipline:** The method makes three core commitments:
    *   Truth is machine-checked only.
    *   What the kernel cannot check is checked by structured opposition (e.g., adversarial refuter passes for designs, independent witnessing for landings).
    *   Human attention is the scarcest resource, reserved for statements, designs, and rulings; tasks are budgeted, and agents fail loudly rather than grinding on.
6.  **Complete Accounting:** The project provides full transparency, including theorem provenance, a pre-registered token meter for economics, floor-bounded human time, and an append-only error ledger (logging all design errors and retractions as first-class results) to maintain integrity and provide data on AI-assisted research.

### Impact

The research demonstrates a profound inversion of the cost-benefit relationship for formal verification, making it not just economical but *essential* for productivity at AI speed:

1.  **Unprecedented Efficiency & Scale:** One researcher, in just five weeks (working evenings and weekends on consumer AI subscriptions), directed a fleet of AI agents to develop a complete system stack—from application code, through a verified compiler and executive, to a RISC-V processor successfully taped out on a community silicon shuttle. Crucially, no proofs were reviewed by a human, and no RTL was written by a human.
2.  **Reliability & Trust:** The rigorous methodology, centered on a proof kernel, resulted in zero incorrect proofs reaching the record, despite catching #256 design errors via adversarial layers and cross-checks. This establishes machine verification as an "incorruptible referee" for autonomous machine work.
3.  **Economic Shift:** The central finding is economic: verification, traditionally a cost overhead, becomes a productivity multiplier at AI speed, enabling a single individual to achieve results previously requiring expert teams over years. This makes AI-scale development usable.
4.  **Documented Case Study:** It provides the most completely documented instance of AI-assisted engineering under machine verification, with every mathematical claim kernel-checked and replayable, and metered economics.
5.  **Methodological Advancement:** The Salt method itself, with its six required invariants and six advisory articles, offers a robust framework for governing AI reliability in producing complex, formally verified artifacts.