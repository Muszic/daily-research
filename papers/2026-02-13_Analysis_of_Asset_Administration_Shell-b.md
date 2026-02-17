# Analysis of Asset Administration Shell-based Negotiation Processes for Scaling Applications

- **Category:** Software Engineering
- **Date:** 2026-02-13
- **Link:** http://arxiv.org/abs/2602.13029v1

---
Here's a summary of the research paper using the Problem, Method, and Impact structure:

---

### Problem

Proactive Asset Administration Shells (AAS) enable decentralized, bidirectional communication and negotiation processes (e.g., allocating products to production resources) using the I4.0 Language (VDI/VDE 2193). While AAS standardization focuses on data models and security, the proactive behavior enabling complex interactions like negotiations remains conceptual and under-researched. Existing studies on proactive AAS architectures typically involve only a limited number of assets, making their scalability and efficiency for large-scale industrial environments with a growing number of assets uncertain. The core research question is: How can current approaches of proactive AAS be scaled, and what performance do they exhibit regarding interaction metrics such as negotiation time or message load?

### Method

The authors analyzed the scalability of proactive AAS negotiation by developing a scenario with a logarithmically scaling number of assets. The scenario involved Service Requesters (SRs) seeking services from Service Providers (SPs), where the number of SRs was twice that of SPs.

1.  **System Modeling:** Defined SRs and SPs with attributes (capabilities, costs, duration, quality, budget) and introduced criteria for capability, feasibility, and actionability of negotiations.
2.  **Implementation:** Developed a scalable architecture where each proactive AAS (comprising negotiation logic, an MQTT client for communication, and passive AAS data) was encapsulated in a Docker container. An orchestration service using Docker Swarm managed the scaling and conducted experiments on a single powerful virtual machine.
3.  **Negotiation Protocol:** Utilized a multicast request mechanism for SRs to find suitable SPs based on semantic service descriptions. SPs processed requests using a "first-in-first-out" principle, responding with offers only if they were capable, feasible, and actionable (i.e., not already processing another agreement within the expected response time). SRs selected the cost-best offer.
4.  **Evaluation Criteria:** Measured system scalability (Ψ), average message load (τ_mes), average successful requests (τ_s), average calls for proposals per requester (τ_cfp), and average costs per successful request (τ_c) across varying scales.

### Impact

The study revealed significant performance limitations and communication overhead in proactive AAS-based negotiation processes when scaled:

*   **Unscalable Performance:** The system demonstrated inherently *unscalable* behavior, indicating that its performance does not improve proportionally with increased resources or assets.
*   **Exponential Communication Overhead:** The average message load (τ_mes) exhibited an *exponential increase* with the scaling factor, highlighting a substantial communication overhead that would be prohibitive in large-scale deployments.
*   **Negotiation Dynamics:** For smaller scales, the success rate (τ_s) was low due to mismatches between SR and SP capabilities. As the scale increased, the average number of calls for proposals (τ_cfp) per SR also increased, suggesting that SRs required more attempts to find actionable providers. The average costs (τ_c) decreased with scaling, possibly indicating a queuing effect where SRs with higher budgets secured services, leaving others to wait or make multiple attempts.

These findings provide critical insights into the practical challenges and limitations of current proactive AAS implementations for industrial-scale applications, directly informing the further development and standardization efforts of the Asset Administration Shell to address scalability and efficiency concerns.