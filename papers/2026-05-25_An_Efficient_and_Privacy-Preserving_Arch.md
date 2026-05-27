# An Efficient and Privacy-Preserving Architecture for Cross-Institutional Collaborative RAG

- **Category:** Cryptography
- **Date:** 2026-05-25
- **Link:** http://arxiv.org/abs/2605.25716v1

---
## An Efficient and Privacy-Preserving Architecture for Cross-Institutional Collaborative RAG

### Problem

Cross-institutional collaboration for Retrieval-Augmented Generation (RAG) is highly promising for leveraging diverse domain-specific knowledge with Large Language Models (LLMs). However, this is severely hindered by **strict privacy regulations and "data silos"** that prevent direct sharing of proprietary data.

The core technical challenge lies in the **Transformer's self-attention mechanism**, which fundamentally conflicts with distributed inference by mandating cross-node access to distributed Key-Value (KV) caches. This makes collaborative RAG difficult and privacy-violating.

Existing solutions face critical drawbacks:
*   **Privacy Vulnerabilities:** Transmitting LLM intermediate states is vulnerable to sophisticated inversion attacks (e.g., Vocabulary Mapping Attacks) that can reconstruct plaintext.
*   **Prohibitive Inference Overhead:** Cryptographic methods (e.g., Secure Multi-Party Computation, Homomorphic Encryption) induce immense latency (minutes per token) and communication overhead (tens to hundreds of times ciphertext expansion), making them impractical.
*   **Lack of Universality & Rapid Deployment:** Hardware-based solutions (e.g., TEEs) require specialized infrastructure, while model retraining or operator approximations lead to accuracy degradation or hinder adoption of state-of-the-art LLMs.

### Method

The authors propose **FedRAG**, a high-throughput, privacy-preserving federated RAG framework. Its core innovation is a novel **Scrambled Distributed Attention protocol**.

1.  **Distributed Attention Foundation:** FedRAG builds upon the online-softmax decomposition of attention, which separates computation into per-node local processing and lightweight global aggregation.
2.  **Privacy-Preserving Transformation:**
    *   **Numerically Stable Feature Scrambling:** Instead of cryptography, FedRAG employs a carefully constructed invertible scrambling matrix $\Phi = S_1P_1HP_2S_2$. This matrix, composed of random scaling matrices ($S_1, S_2$), permutation matrices ($P_1, P_2$), and a normalized Hadamard matrix ($H$), achieves:
        *   **Privacy:** Sufficient mixing to obscure plaintext while defending against inversion attacks.
        *   **Numerical Stability:** Base Hadamard matrix operations are robust under low-precision floating-point arithmetic, avoiding severe round-off errors common with dense random matrices.
        *   **Mathematical Guarantees:** Preserves inner products ($⟨x_1\Phi, x_2\Phi^{-⊤}⟩ = ⟨x_1, x_2⟩$) and linearity ($∑w_i(x_i\Phi) = (∑w_ix_i)\Phi$), allowing correct attention computation on scrambled tensors.
    *   **Random Token Permutation:** K and V matrices (and Q) are permuted in the token dimension, further enhancing resilience against known-plaintext and brute-force attacks.
3.  **Decoupled Computation:** The scrambling mechanism allows participating institutions to dynamically delegate scrambled computations to an independent "Compute Node." This decouples attention execution from data localization, meaning no single entity accesses the plaintext context of others.
4.  **Threat Model:** Operates under an "honest-but-curious" (semi-honest) adversary model, assuming "reputation-aware" and "non-collusion" among institutions.

### Impact

FedRAG achieves significant advancements in enabling cross-institutional RAG:

*   **Breaks Data Silos & Enables Collaboration:** Provides a secure and efficient framework for collaborative RAG, allowing institutions to synergize knowledge without exposing sensitive plaintext data.
*   **High Efficiency & Practical Throughput:** Achieves up to a **62× latency reduction** over existing cryptographic secure baselines, sustaining practical, human-reading throughput for LLM inference.
*   **Negligible Utility Degradation:** Preserves model utility with a **negligible degradation (<0.1%)** across various LLMs and six question-answering and summarization benchmarks.
*   **Robust Privacy without Cryptographic Overhead:** Provides strong mathematical and empirical defense against sophisticated intermediate state inversion attacks (like VMA) by replacing prohibitive cryptographic overhead with hardware-friendly linear transformations.
*   **Universal & Rapid Deployment:** Requires **no specialized hardware** (e.g., TEEs), **no model retraining**, and **no approximate operators**, making it seamlessly deployable with state-of-the-art LLMs.