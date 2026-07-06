# LIB-TRAP: Standard Cell Library Hardware Trojan Risk Assessment and Prevention

- **Category:** Cryptography
- **Date:** 2026-07-01
- **Link:** http://arxiv.org/abs/2607.01526v1

---
This research paper, "LIB-TRAP: Standard Cell Library Hardware Trojan Risk Assessment and Prevention," investigates a novel and stealthy hardware Trojan (HT) insertion method.

## Problem

The fabless semiconductor manufacturing model introduces significant security vulnerabilities, particularly the risk of malicious Hardware Trojan (HT) insertion by untrusted foundries. While existing research has explored HTs inserted in the space between standard cells, there is a critical lack of investigation into vulnerabilities *within* the standard cells themselves, which are the fundamental building blocks of digital designs. This gap means current HT detection methods, often relying on "golden ICs" or assumptions of trusted libraries, may be ineffective against HTs deeply embedded within the standard cell library. The core problem is how to detect HTs when the very definition of basic cells provided by the foundry cannot be trusted.

## Method

1.  **Threat Model:** The authors propose a novel threat model where a malicious foundry leverages its control over standard cell descriptions. The foundry provides a *tampered standard cell library* containing "deactivated" HT cells to the design house. The IC is synthesized using this library. During fabrication, the foundry replaces the deactivated HT cells with *activated* counterparts and connects their triggers to internal design signals, ensuring the HT payload is both stealthy and functional.
2.  **HT Design and Integration:**
    *   A stealthy HT payload was embedded into a standard buffer cell using two technology nodes: Synopsys 32nm and open-source Sky130nm.
    *   The HT was carefully designed to match the original cell's drive strength and area, with additional logic folded into unused diffusion regions to avoid geometric detection.
    *   A "deactivated" HT-infected variant was created where the HT trigger input was hardwired to ground. This makes it functionally identical to the original cell, concealing its presence in library characterization files (LIB, LEF, GDSII) and preventing external pin metadata leakage.
    *   The trigger mechanism was engineered to be dormant under normal operation, without external pins, dynamic power draw, or impact on critical path delay that would exceed normal manufacturing variations.
3.  **Experimental Validation:**
    *   Three benchmark circuits (AES-128 encryption core, Ethernet controller, WISHBONE DMA engine) were synthesized using both clean and Trojan-infected standard cell libraries (deactivated and activated variants).
    *   Design-level features like total cell count, area, dynamic power, static power (leakage), and timing slack were extracted from these synthesized circuits.
    *   Machine Learning (ML) models (Logistic Regression, Random Forest, SVM, Deep Neural Network) were trained to classify designs as "Trojan-infected" or "Trojan-free" based on these features. This was done to rigorously test the stealthiness of the proposed HT attack vector.

## Impact

1.  **Demonstrated Stealth:** The research successfully demonstrated a highly stealthy Hardware Trojan threat model by embedding HTs directly into standard cells. Infected cells exhibited minimal and statistically indistinguishable deviations from genuine cells in terms of power, area, and timing, even under extensive parametric variations.
2.  **Evasion of Conventional Detection:** The benchmark evaluations showed that the proposed HT attack evades detection by traditional IC design flow metrics. The design overheads (area, dynamic power, static power) were extremely small, falling within typical process variation bounds, making them indistinguishable from normal manufacturing variations.
3.  **Failure of ML-based Detection:** Crucially, all tested Machine Learning models, relying on conventional design-level features, yielded near-random detection performance (accuracies between 24% and 40%, F1 scores consistently below 0.40). This highlights a significant blind spot in current hardware security practices and ML-based detection methods.
4.  **Necessity for Upstream Validation:** The findings emphasize that traditional simulation and ML-based detection approaches are insufficient to counter this threat. The paper underscores the need for a paradigm shift, recommending mitigation strategies that start at the root of standard cell library validation, including:
    *   Side-channel analysis (SCA) via power tracing.
    *   Equivalence checking between cell schematics and GDSII layouts.
    *   Independent re-characterization of library cells using trusted tools or golden SPICE models.
    *   Preferring trusted or open-source libraries verified for compactness and minimal layout slack to reduce opportunities for HT embedding.

This research highlights a severe vulnerability in the IC supply chain and calls for robust, proactive validation protocols to guarantee the security and integrity of IC designs.