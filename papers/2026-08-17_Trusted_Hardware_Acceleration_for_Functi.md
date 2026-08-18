# Trusted Hardware Acceleration for Function Secret Sharing

- **Category:** Cryptography
- **Date:** 2026-08-17
- **Link:** http://arxiv.org/abs/2608.16223v1

---
## Summary of "Trusted Hardware Acceleration for Function Secret Sharing"

This research paper introduces a novel hardware accelerator, the Distributed Function Accelerator (DFA), to address the significant overheads of Function Secret Sharing (FSS) in privacy-preserving systems.

### Problem

Function Secret Sharing (FSS) is a fundamental building block for critical privacy-preserving applications like secure inference and Private Information Retrieval (PIR). However, its practical deployment is hindered by substantial system-level overheads:

*   **High Offline Costs:** FSS-based protocols, especially for secure inference, incur massive offline overheads for key generation (e.g., 16.84GB for BERT-Base, 200GB for LLaMA2-7B), communication (distributing these large keys), storage, and data movement. These costs often cannot be entirely hidden and dominate performance and energy consumption.
*   **Computational Bottleneck:** The core primitive in FSS, Distributed Point Function (DPF) generation and evaluation, relies heavily on repeated AES-based Pseudorandom Number Generation (PRG) operations. This makes DPF the dominant computational bottleneck for both secure inference (offline key generation) and PIR (online full-path evaluation, requiring O(N) PRG evaluations).
*   **Memory Pressure:** Full-path DPF evaluation for PIR also places significant pressure on memory resources due to large intermediate states.

### Method

The authors propose the **Distributed Function Accelerator (DFA)**, a hardware accelerator co-designed with algorithms and system integration to target the DPF primitive:

1.  **Hardware Architecture:**
    *   **Hybrid Design:** DFA combines a high-throughput **fixed-function DPF engine** (centered around a deeply pipelined AES-based PRG) for the dominant DPF computations, with a **lightweight programmable Vector Processing Unit (VPU)** for protocol-specific logic, transformations, and masking. This ensures both high performance for the bottleneck and flexibility for evolving FSS protocols.
    *   **GPU Integration:** DFA is designed as a small, on-die acceleration unit within the GPU architecture. DPF units are distributed and co-located with L2 cache banks, while a centralized control unit and VPU handle coordination. This tight integration minimizes data movement overheads between the accelerator and the GPU for co-located linear algebra operations.
    *   **Control Unit:** Manages system initialization, secure key provisioning, and attestation.

2.  **Protocol Co-Design:**
    *   **Decoupled DPF:** FSS protocols are refactored to decouple DPF generation and evaluation from higher-level logic, enabling independent and efficient parallel execution.
    *   **"Generate-and-Consume":** The system introduces an end-to-end execution model that minimizes unnecessary key storage and data movement by generating and consuming keys on-the-fly.

3.  **System Integration and Operating Modes:**
    *   **Untrusted Mode:** DFA acts as a pure accelerator for DPF evaluation. It improves throughput and energy efficiency over a GPU-only solution without changing the existing FSS protocol's security model.
    *   **Trusted Mode:** DFA leverages secure hardware capabilities (e.g., remote attestation, key exchange via the control unit) to enable **local, on-the-fly FSS key generation**. This *eliminates key distribution* from an external trusted third party, dramatically reducing communication, storage, and data movement overheads by effectively removing the offline phase.

### Impact

The DFA provides substantial improvements across representative FSS workloads with modest hardware cost:

*   **Secure Inference:**
    *   **10x reduction** in end-to-end latency.
    *   **Up to 20x reduction** in communication volume (offline key distribution).
    *   **Significant reduction** in storage and data movement overheads.
    *   **More than 5x energy savings.**
*   **Private Information Retrieval (PIR):**
    *   **5x improvement** in throughput.
    *   **10x energy reduction.**
*   **Practicality:** Transforms FSS from a theoretically appealing but system-heavy primitive into a practical and efficient building block for real-world privacy-preserving systems.
*   **Flexibility:** The hybrid architecture ensures adaptability to other DPF/DCF-heavy FSS functions and evolving protocols.