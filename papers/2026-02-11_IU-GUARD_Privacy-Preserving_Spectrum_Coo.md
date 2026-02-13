# IU-GUARD: Privacy-Preserving Spectrum Coordination for Incumbent Users under Dynamic Spectrum Sharing

- **Category:** Cryptography
- **Date:** 2026-02-11
- **Link:** http://arxiv.org/abs/2602.11023v1

---
# IU-GUARD: Privacy-Preserving Spectrum Coordination for Incumbent Users under Dynamic Spectrum Sharing

### Problem
Dynamic Spectrum Sharing (DSS) frameworks (e.g., CBRS) aim to improve spectrum utilization while strictly protecting Incumbent Users (IUs) like military radars. However, current IU protection mechanisms have significant drawbacks:
1.  **Environmental Sensing Capability (ESC):** Relies on costly sensor deployments, is vulnerable to interference and security risks (spoofing, jamming, physical tampering), and prone to interference from neighboring bands.
2.  **Incumbent Informing Capability (IIC):** Requires IUs to disclose their identities and operational parameters (e.g., device type, location, frequency range) to the Spectrum Coordination System (SCS). This creates linkable records, compromising IU operational privacy and mission secrecy. Since SCS operators are often commercial entities, they cannot be fully trusted with sensitive federal data. A privacy-preserving IIC variant exists but relies on strong centralized trust assumptions and has not been widely adopted.
The fundamental problem is enabling IUs to securely and efficiently access shared spectrum in DSS environments without exposing sensitive identity and operational data, and without relying on expensive, vulnerable sensors or untrustworthy intermediaries.

### Method
**IU-GUARD** is a novel privacy-preserving spectrum coordination framework that leverages **Verifiable Credentials (VCs)** and **Zero-Knowledge Proofs (ZKPs)** to address these challenges. It enables IUs to prove their authorization to the SCS without revealing their identities or creating linkable records.

The system operates in three phases:
1.  **Credential Issuance (One-time):** A trusted **Credential Authority (CA)** (e.g., FCC or DoD) verifies an IU's identity and operational profile against registered records. The CA then issues a VC to the IU, containing a pseudonymous identifier and its authorized frequency range (e.g., `[f_low, f_high]`). This VC is securely stored by the IU, and this phase is offline from the SCS.
2.  **Anonymous Spectrum Access Request:** When an IU needs to access spectrum, it generates a **Verifiable Presentation (VP)** from its VC. This VP incorporates a ZKP that cryptographically proves:
    *   The IU possesses a valid VC issued by the CA.
    *   The requested operational frequency range (`[freq_low, freq_high]`) lies within its authorized band (`[f_low, f_high]`).
    The VP uses cryptographic randomization, ensuring that each access request is **unlinkable** to previous ones and to the IU's true identity. The IU also sends minimal plaintext operational metadata (e.g., requested frequency, location, time) to the SCS for coordination.
3.  **Authorization and Enforcement:** The SCS receives the VP and operational metadata. It verifies the embedded ZKP using the CA's public key. During this process, the SCS learns **only** the essential operational parameters disclosed in plaintext; **no identity information** is revealed, and multiple requests from the same IU cannot be correlated. If verification succeeds, the SCS grants temporary spectrum access and reallocates lower-tier commercial users as necessary.

### Impact
IU-GUARD provides robust privacy and security guarantees while maintaining practical performance for real-time DSS operations:
*   **Strong Privacy and Anonymity:** IUs can access shared spectrum without revealing their real-world identities or sensitive operational details to the SCS, mitigating risks of data leakage and de-anonymization.
*   **Unlinkability:** Each spectrum access request is cryptographically independent due to VP randomization, preventing correlation and behavioral inference attacks even if the same IU makes multiple requests.
*   **Authentication and Authorization:** Only legitimate IUs possessing valid, CA-issued VCs can generate verifiable presentations, and they are restricted to operating within their authorized frequency ranges, preventing unauthorized access.
*   **Resistance to Impersonation and Inference Attacks:** Cryptographic binding of VCs prevents forgery, and ZKPs ensure the SCS only obtains the minimum necessary information, defending against data inference.
*   **Practical Performance:** Prototype evaluation demonstrates that IU-GUARD achieves strong privacy with practical computation (VP generation and verification within 175 ms at 95th percentile) and communication overheads (end-to-end authorization latency of 278.4 ms). These latencies are well within typical DSS real-time requirements.
*   **Scalability:** The framework exhibits stable latency and good scalability under increasing numbers of concurrent user access requests.
*   **Compatibility:** IU-GUARD is designed to be fully compatible with existing SCS workflows, offering a deployable and secure alternative to current mechanisms without requiring extensive infrastructure changes or strong centralized trust assumptions.