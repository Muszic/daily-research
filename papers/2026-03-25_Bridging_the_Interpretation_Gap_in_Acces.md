# Bridging the Interpretation Gap in Accessibility Testing: Empathetic and Legal-Aware Bug Report Generation via Large Language Models

- **Category:** Software Engineering
- **Date:** 2026-03-25
- **Link:** http://arxiv.org/abs/2603.23828v1

---
This paper introduces HEAR (Human-cEntered Accessibility Reporting), a framework designed to bridge the gap between technical accessibility bug detections and stakeholder understanding, leveraging Large Language Models (LLMs).

## Problem

Automated accessibility testing tools for mobile applications have significantly improved the *detection* of UI violations, but their impact on *remediation* (fixing) remains limited. The core issue is an "interpretation gap":
*   **Technical Outputs:** Existing tools produce low-level, technical outputs (e.g., JSON logs with coordinates, cryptic error codes) that are difficult for non-specialist stakeholders (product managers, designers) to understand.
*   **Lack of Context:** These technical logs lack semantic context regarding real user harm, functional blockage, or legal compliance risks.
*   **Deprioritization:** Consequently, accessibility issues are often perceived as trivial "polish" problems and are frequently deprioritized in favor of new features, despite their significant impact on users with disabilities and potential legal implications.

## Method

HEAR transforms raw, technical accessibility bug reports into empathetic, stakeholder-oriented narratives through a three-phase process:

1.  **Context Retrieval & Visual Grounding:**
    *   **Input:** Raw bug reports (e.g., from Google Accessibility Scanner), UI states (View Hierarchy XML), and high-resolution screenshots.
    *   **Action:** Reconstructs the semantic UI scene. It aligns the technical report with UI artifacts, uses "semantic slicing" to extract a localized textual context from the View Hierarchy, and crops the screenshot around the bug's coordinates with padding.
    *   **Output:** A dual-modal input (textual context and visual crop) for the LLM.

2.  **Dynamic Persona Injection:**
    *   **Action:** Dynamically selects a specific, detailed user persona based on the nature of the detected accessibility violation.
    *   **Persona Definition:** Each persona (`P = <Name, Loc, Cond, Cons, Psy, Log>`) includes a name, geographic jurisdiction, medical condition, physical constraints (e.g., `±40px` touch deviation for Cerebral Palsy), psychological traits, and anticipated logical difficulties. Personas are aligned with WCAG Success Criteria.
    *   **Goal:** To evoke empathy by linking technical errors directly to the lived experience and struggles of a specific user with disabilities.

3.  **Multi-Layer Causal Reasoning (Chain-of-Thought - CoT):**
    *   **Tool:** Utilizes an LLM (GPT-4o) with CoT prompting to bridge low-level geometry with high-level legal risk.
    *   **Layer 1: Physical Barrier:** The LLM simulates the direct interaction between the injected persona's physical constraints and the identified UI element (e.g., a small touch target combined with a user's motor tremors).
    *   **Layer 2: Functional Blockage:** The LLM analyzes the semantic role of the UI element to deduce how the physical barrier disrupts the user's intended workflow (e.g., failing to tap a "Submit" button leads to workflow abandonment).
    *   **Layer 3: Legal and Compliance Concerns:** The framework evaluates the functional blockage against specific regional accessibility mandates (e.g., JIS X 8341-3 for Japan, ADA/EAA for other regions). It dynamically retrieves and injects relevant legal clauses, enabling the LLM to perform a comparative analysis and transform usability concerns into documented "legal vulnerabilities."

## Impact

The evaluation of HEAR on 103 real-world bug instances from four popular Android applications (Instagram, Wish, Teams, Booking) and a user study (N=12 developers/students) demonstrated significant improvements:

*   **Accuracy & Reliability (RQ1):** HEAR generates *factually accurate narratives* without hallucinating UI elements or functional consequences, consistently passing checks for visual grounding, textual fidelity, and functional logic.
*   **Utility & Persuasiveness (RQ2):**
    *   **Increased Empathy & Urgency:** Substantially improves perceived *empathy, urgency, persuasiveness*, and *awareness of legal risk* compared to raw technical logs. Participants found HEAR reports easier to understand and more impactful.
    *   **Low Cognitive Burden:** Achieves these improvements while imposing little additional cognitive burden on stakeholders.
    *   **Task-Specific Preferences:**
        *   **Strongly Preferred For:** Learning accessibility concepts (92% "much better"), explaining issues to non-technical stakeholders (100% preferred, 67% "much better"), and deciding bug-fix priority (84% preferred).
        *   **Mixed Preference For:** Locating relevant code and implementing fixes (59% still favored HEAR, but 41% preferred the baseline). This indicates HEAR serves as a *complementary reporting layer* for communication and prioritization, rather than a direct replacement for low-level technical details during hands-on debugging.

*   **Limitations:**
    *   **Upstream Dependency:** HEAR's effectiveness depends on the accuracy of underlying detection tools; it can "amplify error" by generating persuasive narratives for false positives.
    *   **Persona Simplification:** Dynamic personas simplify complex human conditions, potentially leading to "stereotype bias" if developers only optimize for specific persona traits rather than the full spectrum of user needs.