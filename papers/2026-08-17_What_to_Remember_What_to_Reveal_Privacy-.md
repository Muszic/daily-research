# What to Remember, What to Reveal: Privacy-Aware Memory for Conversational Agents

- **Category:** Cryptography
- **Date:** 2026-08-17
- **Link:** http://arxiv.org/abs/2608.16551v1

---
## What to Remember, What to Reveal: Privacy-Aware Memory for Conversational Agents

### Problem

Personalized conversational agents benefit from long-term memory to retain user information across sessions, enabling continuous, user-adaptive personalization. However, existing memory architectures primarily optimize for utility and neglect the significant privacy risks associated with storing and reusing Personally Identifiable Information (PII) unnecessarily. This creates a privacy-utility tension:
1.  **Unnecessary Exposure:** Direct storage of sensitive information in searchable memory risks exposure in unauthorized contexts or when only non-sensitive preferences are required (e.g., leaking an exact home address for a food preference query).
2.  **Loss of Utility:** Simply removing or permanently masking sensitive values would undermine the agent's ability to complete many personal-assistance tasks that genuinely require exact private information (e.g., form filling, financial assistance).
Existing approaches lack a comprehensive framework for governing the full life-cycle of sensitive values, moving beyond just sanitizing individual records to controlling what is remembered, how it is stored, and what is retrieved.

### Method

The authors propose **Sanitized Privacy-Mapped Memory (SP-Mem)**, a privacy-aware memory architecture that decouples memory utility from exact private-value exposure through three integrated components:

1.  **Privacy-Aware Memory Writing:**
    *   **Information Extraction:** Converts raw user utterances into complementary representations (natural-language facts for vector memory, relation triplets for graph memory). During this, privacy-sensitive values (PII) are detected and annotated using a rule-based extraction strategy based on a predefined taxonomy.
    *   **Privacy Sanitization:** Detected private values are transformed into sanitized representations (e.g., name/alias substitution, suffix-preserving masking, numerical bucketing, LLM-based generalization). Non-private information and *sanitized* private values are written into searchable memory.

2.  **Partitioned Storage with Privacy Mapping:**
    *   **Layered Storage:** The storage layer is partitioned into:
        *   **Searchable Memory (Vector & Graph Stores):** Contains non-private entries and the *sanitized* representations of private values.
        *   **Protected Private Store:** Stores the *exact* private values, isolated from general retrieval.
        *   **Privacy Mapping Layer:** Records mapping keys that link the sanitized representations in searchable memory to their corresponding exact values in the protected store.

3.  **Privacy-Aware Query-Time Reasoning and Authorized Retrieval:**
    *   **Query Analysis:** A query analyzer determines the information required for the task and identifies whether any required entity is private.
    *   **Consent-Gated Retrieval:**
        *   If no private information is needed, retrieval occurs solely from the sanitized searchable memory.
        *   If private information is needed, the system **requests user consent**.
        *   **With consent:** Relevant sanitized memories are retrieved, and *only the task-required exact private values* are restored from the protected private store via the privacy mapping layer.
        *   **Without consent:** The system falls back to using only sanitized memory.

Additionally, the paper introduces a **privacy-aware memory benchmark** to evaluate SP-Mem. This benchmark, constructed through user profile generation, subtask definition, and history/test query generation, assesses response quality, personalization, *and* privacy-appropriate behavior. It includes 1,000 synthesized user profiles (with PII and preferences), 2,100 history dialogues for memory construction, and 5,400 evaluation queries annotated with required information scope and user consent settings across four domains.

### Impact

*   **Enhanced Personalization with Controlled Privacy:** SP-Mem achieves stronger personalization in conversational agents while significantly reducing the unnecessary exposure of private user information, demonstrating a practical solution to the privacy-utility tension.
*   **Full-Lifecycle Privacy Management:** The research formulates privacy-aware long-term memory as a core challenge, shifting the focus from simply remembering user information to comprehensively controlling how sensitive data is written, stored, retrieved, and used throughout its lifecycle.
*   **Novel Evaluation Standard:** The introduction of the first privacy-aware memory benchmark and evaluation pipeline provides a crucial tool for jointly assessing response quality, personalization quality, and privacy-appropriate behavior, addressing a significant gap in existing evaluation frameworks for memory-augmented LLM agents.