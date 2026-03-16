# Why Neural Structural Obfuscation Can't Kill White-Box Watermarks for Good!

- **Category:** Cryptography
- **Date:** 2026-03-13
- **Link:** http://arxiv.org/abs/2603.12679v1

---
## Summary of "Why Neural Structural Obfuscation Can’t Kill White-Box Watermarks for Good!"

### Problem

Neural Structural Obfuscation (NSO) is a family of "zero-cost" structure-editing transforms (e.g., nso_zero, nso_clique, nso_split) that inject dummy neurons into deep learning models. By combining neuron permutation and parameter scaling, NSO radically modifies network structure and parameters while strictly preserving functional equivalence. This disrupts white-box watermark verification, which often relies on index-ordered parameters, posing a fundamental challenge to the reliability of existing white-box watermarking schemes and claiming "zero-cost" removal of watermarks.

The challenge is exacerbated in modern graph-structured networks (e.g., ResNet, Inception) where NSO edits are not merely layer-local but propagate graph-consistently through fan-out, residual merges (add), and channel concatenations (cat). This makes attack-induced dummy neurons appear structurally plausible and functionally equivalent, rendering local or layer-wise defenses ineffective. The core problem is how to reliably distinguish these attack-induced dummy neurons from benign structural components and recover a compact, compatible model parameterization for watermark verification without prior knowledge of the attack.

### Method

The authors rethink NSO, recognizing that to preserve functional equivalence in graph-structured networks, any obfuscation of a producer node *must* necessitate a compatible layout update in *all downstream consumers* to maintain structural integrity. This means NSO induces structured, globally constrained redundancy, despite appearing indistinguishable locally.

Building on this "producer–consumer consistency" insight, the paper proposes **CANON**, a graph-consistent recovery framework:

1.  **Redundancy Inference via Activation Probes:** CANON probes the attacked model with a small set of inputs (synthetic or public) to collect activation signatures. It leverages these signatures to identify redundancy and dummy channels by inferring consistent signatures and proportionality relations that NSO edits must satisfy. This step identifies the channel-basis transformations introduced by NSO.
2.  **Global Canonicalization via Downstream Rewriting:** Once a ChannelTransform (representing an NSO edit) is inferred at a producer edge, CANON propagates this correction throughout the computation graph. It globally canonicalizes the network by rewriting *all downstream linear consumers* (e.g., Conv/Linear layer weights) by construction. This involves synchronizing channel layouts across structural operations like fan-out, residual add, and channel cat, ensuring a globally consistent and compact representation. This process reverses the structural obfuscation and restores a parameterization compatible with existing white-box watermark extractors, effectively eliminating NSO-induced index scrambling.

CANON operates graph-consistently, propagating layout corrections and ensuring global synchronization of channel representations while strictly preserving end-to-end functionality, without requiring the original clean model or knowledge of the attacker's specific construction details.

### Impact

CANON effectively defeats NSO attacks, demonstrating that white-box watermarks cannot be "killed for good" at zero cost.

*   **100% Recovery Success:** Extensive experiments show that CANON achieves 100% recovery success for watermark verifiability, even under strong, composed, and graph-consistent NSO attacks on modern CNN architectures.
*   **Preserves Task Utility:** The recovery process preserves the model's task utility with no accuracy loss, ensuring the usability of the restored model.
*   **Invalidates NSO's Claim:** The research empirically invalidates the "zero-cost removal" claim of NSO, making embedding watermarks practical and robust against structural obfuscation.
*   **Novel Framework:** CANON is the first end-to-end canonicalization framework that systematically defeats NSO by construction, offering a robust defense for white-box watermarking schemes.
*   **Generalizes Threat Model:** It reformulates NSO into a more realistic graph-consistent producer–consumer model, exposing signal-consistency constraints that prior layer-local NSO formulations missed.