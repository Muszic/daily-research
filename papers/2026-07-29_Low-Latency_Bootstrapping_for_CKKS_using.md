# Low-Latency Bootstrapping for CKKS using Roots of Unity

- **Category:** Cryptography
- **Date:** 2026-07-29
- **Link:** http://arxiv.org/abs/2607.27401v1

---
Here's a summary of the research paper "Low-Latency Bootstrapping for CKKS using Roots of Unity":

## Low-Latency Bootstrapping for CKKS using Roots of Unity

### Problem

The original CKKS (Cheon-Kim-Kim-Song) homomorphic encryption scheme for approximate arithmetic suffers from high latency and runtime during its bootstrapping procedure. This is primarily due to the **substantial multiplicative depth** required to homomorphically evaluate a high-degree polynomial that approximates modular reduction. This high multiplicative depth necessitates:
*   A large modulus, which consumes more levels of computation after bootstrapping.
*   A larger ring dimension, leading to increased latency.
The goal is to reduce this multiplicative depth to enable faster bootstrapping, free up more computation levels, and allow for smaller ring dimensions.

### Method

The paper introduces **Sparse Roots of Unity (SPRU) bootstrapping**, a novel approach that avoids the expensive polynomial approximation of modular reduction.
1.  **Core Idea**: Instead of polynomial approximation, SPRU bootstrapping directly embeds the additive group $\mathbb{Z}_q$ into the complex roots of unity via the homomorphism $f: \mathbb{Z}_q \rightarrow \mathbb{C}, x \mapsto \exp(2i\pi \cdot x/q)$. This allows modular reduction to be evaluated natively within the CKKS scheme.
2.  **Decryption Evaluation**: The method homomorphically evaluates a product expression $1 + m \cdot \frac{2i\pi}{q} \approx \prod_{k=0}^{N-1} (1 + (\exp(2i\pi \cdot c_k/q) - 1) \cdot s_k)$, where $m = \langle s, c \rangle \pmod q$ is the decrypted message, $c_k$ are ciphertext coefficients, and $s_k$ are secret key bits.
3.  **Key Optimizations**:
    *   **Packing Secret-Key Bits**: The $N$ secret-key bits $s_i$ are packed into $N/2$ CKKS slots. This reduces the bootstrapping key size and decreases ciphertext-ciphertext multiplications from $O(N)$ to $O(\log N)$ using a product operator.
    *   **Sparse Block Secret-Key**: By structuring the secret key into $h$ blocks (each of size $B=N/h$) with exactly one non-zero bit per block, most homomorphic multiplications are replaced by additions using the trace operator. This significantly reduces the multiplicative depth from $O(\log N)$ to $O(\log h)$.
4.  **Multiple Slots**: The method is extended to handle multiple slots by treating each polynomial message coefficient as an independent LWE ciphertext. The process involves summing across distinct ciphertexts, applying the trace operator, and then the product operator. It reuses the existing `SlotToCoeff` operation from original CKKS but eliminates the need for `CoeffToSlot`.

### Impact

The SPRU bootstrapping method provides significant practical improvements for CKKS:
*   **Reduced Latency**: Achieves up to a **5x reduction in latency** for ciphertexts with a *small number of slots* compared to the original CKKS bootstrapping.
*   **Lower Multiplicative Depth**: Drastically reduces the multiplicative depth required for bootstrapping (from $O(\log N)$ to $O(\log h)$), which is the primary driver for improved efficiency.
*   **Efficiency for Small Slot Counts**: While the original CKKS bootstrapping scales better asymptotically for a large number of slots ($O(\log n + \log N)$ vs. SPRU's $O(n + \log N)$), SPRU is *significantly faster in practice for a small number of slots* due to its lower multiplicative depth.
*   **Parallelizability**: The method is highly parallelizable, achieving $O(\log N)$ complexity with $n$ processors.
*   **Practical Implementation**: An open-source implementation is provided based on the OpenFHE C++ library, enabling direct comparison with existing state-of-the-art CKKS bootstrapping implementations.
*   **Compatibility**: The new algorithm is compatible with other existing CKKS optimizations, such as RNS (Residue Number System), GPU acceleration, and modulus-reducing ciphertext multiplication techniques.