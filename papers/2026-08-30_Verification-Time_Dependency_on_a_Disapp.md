# Verification-Time Dependency on a Disappearing Evaluator

- **Category:** Software Engineering
- **Date:** 2026-08-30
- **Link:** http://arxiv.org/abs/2608.29912v1

---
Here's a summary of the research paper in Markdown format:

---

### Problem

The core problem addressed is the temporal mismatch between the need for long-term verifiability and auditability of consequential AI-mediated decisions and the dynamic, often short lifecycles of AI models (evaluators). Regulatory retention periods for documentation (e.g., 10 years under EU AI Act Article 18) and logs (e.g., 6 months under Article 19) do not guarantee that the original AI model or its exact execution context will remain accessible or reinstantiable. This "disappearing evaluator" makes it challenging or impossible for later reviewers to:
1.  Verify the basis on which an AI decision was authorized.
2.  Reproduce or reconstruct the original decision.
3.  Statistically defensibly claim what the evaluator would have done under counterfactual inputs, undermining post-hoc testing and auditability.
Evaluator identity is not merely a model-version string but includes the hosting/service surface and time, which also have varying availability states.

### Method

The paper employs a dual approach: theoretical protocol development and empirical re-analysis.

1.  **Theoretical Protocol Development:**
    *   Derives three verification-time constructs from the published Execution Governance (EG) 3.0 architecture: **Decision-State Commitment**, **Independent Verifiability**, and **Counterfactual Auditability**. These are specializations, not new core EG primitives.
    *   Jointly proposes an **operational verification-time protocol** and an optional **Verification-Time Preservation Package (VTPP)**. This protocol specifies:
        *   What a higher-assurance profile binds at authorization time.
        *   What a separately trusted verifier can substantiate later.
        *   Semantic and cross-field conformance checks beyond schema validity.
        *   How stability and paired counterfactual tests should be calibrated.
        *   What evidence must be preserved when later access to the original evaluator cannot be assumed.

2.  **Empirical Re-analysis (using Siddiqui's "The Retiring Witness v1.1" artifacts):**
    *   **Retirement Event Census:** Independently recomputes model retirement lifespans, confirming a median of ~16.4 months for 22 events across three providers, reinforcing the operational reality of disappearing evaluators.
    *   **Within-Family Behavioural Comparisons:** Reproduces original comparisons demonstrating significant decision reversals:
        *   52.0% modal-decision reversal between Llama 3.1 8B and Llama 3.3 70B (26/50 cases).
        *   30.0% modal-decision reversal between GPT-OSS 20B and GPT-OSS 120B (15/50 cases).
    *   **Provider-Designated Replacement-Path Reanalysis (Post-hoc):** Re-pairs released outputs against Groq's published migration maps (e.g., Llama to GPT-OSS models), yielding:
        *   38.0% decision reversal for Llama 3.3 70B -> GPT-OSS 120B (19/50 cases).
        *   64.0% decision reversal for Llama 3.1 8B -> GPT-OSS 20B (32/50 cases), noted as a boundary observation due to high initial approval.
        *   Acknowledges cross-family invocation differences (e.g., `max_tokens`, `reasoning_effort`).
    *   **Within-Version Instability:** Measures decision variation (2% pair-level incidence) and reason-channel instability (exact text varying more often than decisions) across three temperature-zero repetitions.
    *   **Provenance and Verification:** Emphasizes independent reprocessing of raw files and verifiable artifact identity using SHA-256 and MD5 hashes.

### Impact

The paper's primary impact is the provision of a practical, operational framework—the **Verification-Time Preservation Package (VTPP)** and its associated protocol—to address a critical, unaddressed temporal challenge in AI governance and assurance.

*   **Enables Long-Term Verifiability:** It offers concrete mechanisms to enable independent verification, commitment, and counterfactual auditability of AI decisions, even when the original AI system is no longer available. This fills a crucial gap where regulatory retention periods for documentation currently fall short.
*   **Empirical Justification:** The empirical re-analyses powerfully demonstrate the necessity of such a protocol. They show significant behavioral divergence (up to 64% decision reversal) between functionally related models, even within families or on provider-designated migration paths, highlighting that simple model replacement or later reconstruction is often unreliable. They also quantify within-version decision and reasoning instability.
*   **Practical Guidance:** The VTPP provides specific guidance on what evidence to preserve, how to calibrate stability and counterfactual tests, and the scope of verification checks, offering a blueprint for higher-assurance profiles.
*   **Non-Authorizing and Downstream:** By clarifying that the protocol is downstream and non-authorizing, it provides tools for post-decision review and accountability without altering core authorization processes or stating legal admissibility.
*   **Addresses AI Lifecycle Challenges:** It offers a robust approach to maintain accountability and trust in AI systems within dynamic commercial lifecycles, where model evolution and retirement are common.

---