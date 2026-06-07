# Policy-Compliant Cloud Storage Systems

- **Category:** Cryptography
- **Date:** 2026-06-03
- **Link:** http://arxiv.org/abs/2606.05423v1

---
This research paper presents **GDPRuler**, a trusted middleware system designed to enable verifiable GDPR compliance for Key-Value Stores (KVS) in untrusted cloud environments.

### Problem

The rapid adoption of Key-Value Stores (KVS) in latency-sensitive applications on untrusted cloud infrastructures creates significant challenges for complying with modern privacy regulations like GDPR:

*   **KVS Limitations:** KVS, with their simple data model, inherently lack support for compliance metadata, secondary indexes for GDPR-specific queries (e.g., "right to be forgotten"), or expressive query semantics needed to enforce complex legal requirements like purpose or storage limitation.
*   **Untrusted Cloud Environment:** Cloud deployments imply that privileged software stacks (hypervisors, cloud operators) can observe or tamper with sensitive data, policy enforcement logic, compliance metadata, and audit trails, undermining confidentiality and the verifiability of compliance evidence.
*   **Existing Approach Deficiencies:** Current methods for GDPR compliance are often invasive (requiring extensive code modifications), incur high performance overheads, or critically, fail to protect the integrity of the compliance mechanisms themselves (like metadata and audit logs) against a malicious cloud provider.
*   **Performance Degradation:** Implementing GDPR mandates (metadata management, complex queries beyond simple key lookups, tamper-evident audit logging) directly in the data path of high-throughput KVS severely degrades performance.

### Method

GDPRuler addresses these challenges by acting as a trusted middleware system, transparently interposed between applications and unmodified KVS backends (e.g., Redis, RocksDB).

1.  **Trusted Execution Environment:** GDPRuler deploys a **Trusted GDPR Monitor** inside a **Confidential Virtual Machine (CVM)**. This leverages hardware-backed isolation, integrity protection, and remote attestation to ensure the confidentiality and integrity of the compliance logic, metadata, and audit logs, even against privileged cloud software.
2.  **Declarative Policy Language:** It introduces a **declarative policy language** and compiler that translates core GDPR obligations (e.g., purpose limitation, storage limitation, right of access/erasure) into enforceable runtime rules. Data owners and processors specify their data handling policies, which are then compiled into compact metadata.
3.  **Efficient Metadata Management:**
    *   **Compact Encoding:** Compliance metadata (e.g., owner, purpose, expiration time, sharing permissions, objections) is compactly encoded (e.g., using bitmaps) and prepended to KV records to minimize storage overhead.
    *   **Dedicated Indexes:** GDPRuler maintains specialized in-memory **metadata indexes** (e.g., hashmaps, B+ trees) within the CVM. These indexes enable efficient, metadata-driven GDPR queries (e.g., finding all data related to a user or purpose) without requiring full KVS scans.
    *   **Background Expiration Scanner:** An asynchronous scanner in the CVM continuously identifies and queues deletion requests for expired data, enforcing storage limitation principles.
4.  **Verifiable and Tamper-Evident Auditing:** A **tamper-evident logging system** securely records all policy-relevant operations and violations in a space-efficient format. These logs, along with remote attestation, allow regulatory authorities to independently verify compliance and the integrity of the system.
5.  **Transparent Proxy Architecture:** GDPRuler operates as a transparent proxy, intercepting all KVS operations. It provides a standard `put/get/delete` API alongside compliance-aware operations (`getm/putm/deletem/getLogs`) to manage metadata and retrieve audit logs, maintaining compatibility with existing KVS deployments without requiring their modification.

### Impact

GDPRuler provides a practical, secure, and performant solution for achieving GDPR compliance in KVS deployed on untrusted clouds.

*   **Verifiable Compliance:** It ensures hardware-backed confidentiality, integrity, and verifiability of GDPR policy enforcement and auditing, protecting against a powerful adversary controlling the cloud infrastructure. It successfully enforces core GDPR obligations such as purpose limitation, storage limitation, and user rights (access, erasure, objection).
*   **High Performance and Efficiency:** Despite introducing a trusted middleware layer, GDPRuler demonstrates low overheads:
    *   Achieves approximately **61% of native KVS throughput** on average, with the CVM environment contributing 28-32% of this overhead.
    *   Metadata storage overhead remains **below 20%**.
    *   GDPR-specific queries (leveraging metadata indexing) benefit from a **13-182x speedup** compared to naive approaches.
    *   The tamper-evident logging system introduces a minimal **2% throughput reduction**.
*   **Non-Invasive Integration:** By acting as a transparent proxy for unmodified KVS, GDPRuler allows organizations to easily retrofit GDPR compliance onto existing deployments (e.g., Redis, RocksDB), reducing development effort and preserving compatibility.
*   **Enhanced Accountability:** The system generates secure, tamper-evident audit logs, enabling regulatory authorities to effectively inspect processing activities and hold data controllers accountable.