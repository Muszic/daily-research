# Impact of 5G SA Logical Vulnerabilities on UAV Communications: Threat Models and Testbed Evaluation

- **Category:** Cryptography
- **Date:** 2026-03-04
- **Link:** http://arxiv.org/abs/2603.04662v1

---
This paper investigates the security implications of logical vulnerabilities in 5G Standalone (SA) networks on Unmanned Aerial Vehicle (UAV) command and control (C2) communications.

---

### Problem

Unmanned Aerial Vehicles (UAVs) depend on continuous and secure communication with their Ground Control Stations (GCS) for command execution and telemetry transmission. While 5G Standalone networks offer low latency and high capacity suitable for such critical communications, their complex architecture introduces multiple potential points of failure and attack. This research aims to understand how logical vulnerabilities within the 5G SA architecture, exploited from different attacker positions, can impact the confidentiality, integrity, and availability of UAV C2 communications, potentially disrupting critical flight operations.

### Method

The researchers evaluated the impact of 5G SA logical vulnerabilities through the following approach:

*   **Threat Models:** Three distinct threat models were defined, representing different attacker capabilities and access points:
    1.  **Rogue UE:** A malicious User Equipment (UE) connected to the same logical network (slice/DNN) as the UAV.
    2.  **Insider Threat:** An adversary with access to the 5G core network, specifically targeting the N4 interface (PFCP) between the SMF and UPF.
    3.  **Compromised gNodeB:** An attacker gaining control of a legitimate gNodeB (gNB) already integrated into the 5G network.
*   **Testbed Environment:** A Kubernetes-based testbed was constructed, utilizing:
    *   **Open5GS:** For simulating the 5G core network functions (AMF, SMF, UPF).
    *   **UERANSIM:** For simulating gNodeBs and UE devices (UAV, GCS, Rogue UE).
    *   **MAVLink Simulator:** Running on the UAV UE to replicate real-world telemetry and control communication.
*   **Attack Implementation & Evaluation:** Specific attacks were designed and executed in the testbed for each threat model:
    *   **Rogue UE:** Implemented a C2 injection and GCS spoofing attack, leveraging the lack of MAVLink signing to send fake commands (e.g., `MAV_CMD_NAV_LAND`) directly to the UAV.
    *   **Insider Threat:** Executed a PFCP Session Deletion Flood attack on the N4 interface, sending a high rate of `Session_Deletion_Request` messages to the UPF to disrupt UAV data sessions.
    *   **Compromised gNodeB:** Intercepted and tampered with MAVLink navigation commands (e.g., `SET_POSITION_TARGET_LOCAL_NED`) within the cleartext GTP-U tunnel (N3 interface) to hijack UAV movement.

### Impact

The research demonstrated significant impacts of 5G SA logical vulnerabilities on UAV communications, leading to critical disruptions:

*   **Confirmed Attack Efficacy:** Attacks from all three distinct architectural points (malicious UE, core insider, compromised gNB) successfully disrupted UAV operations, highlighting cross-layer vulnerabilities.
*   **Specific Observed Impacts:**
    *   **Rogue UE (Threat Model 1):** Achieved forced UAV landing by spoofing the GCS and injecting malicious commands due to the lack of application-layer authentication in MAVLink, compromising confidentiality (telemetry exfiltration), integrity (command manipulation), and availability (mission termination).
    *   **Insider Threat (Threat Model 2):** Successfully terminated UAV PDU sessions and their GTP-U tunnels via PFCP session deletion floods on an unprotected N4 interface, forcing the UAV into failsafe mode and impacting its availability.
    *   **Compromised gNodeB (Threat Model 3):** Achieved UAV navigation hijacking by modifying C2 traffic within the cleartext GTP-U tunnel (N3 interface), causing the UAV to fly to unintended locations. This vulnerability stems from the gNB's cleartext access to user plane data and the common absence of integrity protection on the N3 interface and application-layer C2 protocols.
*   **Critical Recommendations:** The findings underscore the urgent need for:
    *   **Multi-layered Protection:** Emphasizing that security must be implemented across all layers of the system, not just one.
    *   **Enhanced 5G Network Isolation:** Implementing robust isolation mechanisms in the 5G user plane to prevent lateral attacks between devices within the same data domain.
    *   **Integrity Protection for C2 Protocols:** Enforcing strong authentication and integrity protection (e.g., MAVLink signing) at the application layer of UAV command protocols.
    *   **Secure Core and User Plane Interfaces:** Protecting internal 5G core interfaces (like N4) with mutual authentication and integrity (e.g., IPsec/TLS) and ensuring integrity protection on user plane interfaces like N3 (GTP-U between gNB and UPF).