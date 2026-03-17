# Directional Embedding Smoothing for Robust Vision Language Models

- **Category:** NLP
- **Date:** 2026-03-16
- **Link:** http://arxiv.org/abs/2603.15259v1

---
```markdown
### Problem

Vision-Language Models (VLMs), crucial components for trustworthy agentic AI systems, remain highly vulnerable to "jailbreaking attacks." These malicious inputs undermine the models' safety alignment, leading them to generate harmful or undesirable outputs. Securing these foundation models against such attacks is an open and challenging problem that needs robust, practical defenses.

### Method

This paper extends the "Randomized Embedding Smoothing and Token Aggregation (RESTA)" defense, previously developed for Large Language Models (LLMs), to Vision-Language Models (VLMs). RESTA is an inference-time defense that operates as follows:
1.  **Embedding Perturbation:** It injects noise into the input token embeddings, specifically perturbing only user-controlled content tokens.
2.  **Stochastic Generation:** It generates `k` (e.g., 10) noisy perturbations of the unified input embedding sequence (which combines visual and textual embeddings).
3.  **Token Aggregation:** For each next token generation step, it performs greedy decoding for each of the `k` perturbed sequences. The final next token is then selected by a majority vote across the `k` generated candidates.

The core innovation and focus of this work lie in comparing two types of embedding noise:
*   **Isotropic (Normal) Noise:** Adds independent and identically distributed (iid) Gaussian noise to every element of the embedding vectors.
*   **Hard Directional Noise:** Adds Gaussian noise specifically *aligned with the direction of the original token embedding vectors*. This variant is motivated by the hypothesis that semantic meaning is primarily encoded in the direction of embeddings, thus preserving semantics better while introducing noise.

### Impact

The evaluation of RESTA on LLaVA-1.5-7B and Gemma-3-4B VLMs, using the JailBreakV-28K benchmark for security and ScienceQA for utility, demonstrates significant findings:
*   **Enhanced Security with Directional Noise:** RESTA, particularly when employing **hard directional noise**, substantially reduces the Attack Success Rate (ASR) of multi-modal jailbreaking attacks. For instance, on LLaVA-1.5-7B, ASR was reduced from an undefended baseline of 50.13% to 25.93%.
*   **Favorable Safety-Utility Trade-off:** This security improvement is achieved with only a minor degradation in model utility (e.g., ScienceQA accuracy degrading from 64.07% to 61.42% for LLaVA-1.5-7B at the aforementioned ASR reduction). In contrast, isotropic (normal) noise yielded much poorer trade-off curves, often worse than a trivial defense.
*   **Critical Role of Directionality:** The results strongly emphasize that the *directionality* of embedding noise is crucial for RESTA's effectiveness, highlighting its importance in preserving semantic content while conferring robustness.
*   **Practical Defense Layer:** The research demonstrates that RESTA can serve as a lightweight, inference-time defense layer, contributing to the overall security framework for building trustworthy agentic AI systems.
```