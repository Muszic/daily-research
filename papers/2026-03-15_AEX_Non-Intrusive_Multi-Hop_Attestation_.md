# AEX: Non-Intrusive Multi-Hop Attestation and Provenance for LLM APIs

- **Category:** Cryptography
- **Date:** 2026-03-15
- **Link:** http://arxiv.org/abs/2603.14283v1

---
## AEX: Non-Intrusive Multi-Hop Attestation and Provenance for LLM APIs

### Problem

Hosted Large Language Models (LLMs) are primarily accessed via remote APIs, which shifts the trust boundary and creates a critical gap: clients lack direct, verifiable evidence that a returned output genuinely corresponds to their original request. Existing issues include:
1.  **Shadow API Divergence:** Unofficial or intermediary endpoints can deviate significantly from claimed LLM behavior (e.g., utility divergence, fingerprint failures), as shown by recent audits.
2.  **Incomplete Existing Solutions:** Methods like LLM fingerprinting, model equality testing, verifiable inference, and TEE attestation are useful but either inferential or address different trust questions, not the direct request-output binding at the API level.
3.  **Middleware Complexity:** LLM APIs frequently pass through intermediaries (gateways, proxies, middleware) that may benignly or maliciously modify requests (e.g., adding defaults, rewriting prompts) or responses (e.g., redacting, buffering, re-packaging streams), making it hard to trust the final output's origin.
4.  **Streaming Integrity:** Ensuring the integrity, order, completeness, and non-truncation of streamed LLM outputs is particularly challenging, especially when intermediaries transform the stream.

The core problem is how to provide direct, online, verifiable evidence at the API protocol boundary that a specific client-visible request is bound to a specific response or streaming output sequence, while preserving existing API semantics and accounting for trusted intermediary transformations.

### Method

AEX (Attestation EXtension) is a non-intrusive protocol extension for existing JSON-based LLM APIs that addresses the request-output binding problem by composing well-understood cryptographic mechanisms:
1.  **Non-Invasive Design:** AEX adds a signed top-level `attestation` object to JSON responses, without altering the core request, response, tool-calling, streaming, or error semantics of the API. It uses JSON Canonicalization Scheme (JCS) and Ed25519 signatures for consistent and secure representations.
2.  **Core Commitments:**
    *   **Request Commitment:** A cryptographic digest of a client-visible request projection.
    *   **Effective Request Commitment:** An optional digest of the final request actually executed after trusted rewriting or normalization.
    *   **Output Commitment:** A digest over a complete non-streaming response object or a complete authenticated streaming chain.
3.  **Explicit Request Binding Modes:** Clients can choose the strictness of request binding (`full`, `top_level_exclude`, `top_level_include`) to accommodate benign middleware changes while protecting against unauthorized field injection.
4.  **Streaming Integrity via Hash Chains:** For streaming outputs, AEX uses a dual-anchor chunk hash chain to detect tampering, deletion, insertion, reordering, and truncation of individual chunks.
5.  **Sound Streaming Proof Boundaries:** It explicitly distinguishes between:
    *   **Checkpoint Proofs:** For verified prefixes of an untransformed source stream.
    *   **Complete-Output Lineage:** For outputs that have been rewritten, buffered, aggregated, or re-packaged by trusted intermediaries, linking them back to an attested source output via a signed chain of output transforms.
6.  **Trusted Transformation Receipts:**
    *   **Request Transform Chain:** Signed `request_transforms` receipts explicitly attest when a request commitment is transformed into an effective request commitment by named, trusted intermediaries.
    *   **Output Transform Chain:** Signed `output_transforms` receipts document how a source output was modified by trusted intermediaries, preserving a verifiable lineage.
7.  **Protocol Profile:** AEX provides an OpenAI-compatible chat-completions profile and a reference TypeScript prototype with conformance tests and microbenchmarks to demonstrate practical deployment.

### Impact

AEX's primary impact is providing **direct, online, and verifiable evidence** for the request-output relationship at the API boundary, addressing a critical trust gap in hosted LLM services.
1.  **Enhanced Trust and Transparency:** It offers a robust mechanism for clients and auditors to confirm the integrity and provenance of LLM API interactions, mitigating risks from shadow APIs and untrusted intermediaries.
2.  **Deployment Realism:** Its non-invasive protocol extension approach and compatibility with existing JSON-based APIs (e.g., OpenAI) make it highly practical and easily deployable in current LLM infrastructure.
3.  **Auditable Intermediary Actions:** By formalizing and signing trusted request and output transformations, AEX transforms otherwise opaque middleware actions into verifiable, auditable provenance chains, enhancing accountability.
4.  **Robust Streaming Guarantees:** It provides strong integrity guarantees for streaming outputs, explicitly differentiating between untransformed source streams and modified outputs, preventing misinterpretation of partial evidence.
5.  **Complements Existing Security:** AEX doesn't replace TEE attestation, model fingerprinting, or model-equality testing but complements them by focusing on the integrity and binding of transaction data at the API boundary.
6.  **Practical Validation:** The provision of a reference TypeScript prototype, conformance tests, and microbenchmarks demonstrates its feasibility and readiness for real-world application, making it a concrete step towards more secure LLM API consumption.