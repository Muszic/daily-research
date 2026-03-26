# A Sensorless, Inherently Compliant Anthropomorphic Musculoskeletal Hand Driven by Electrohydraulic Actuators

- **Category:** Robotics
- **Date:** 2026-03-25
- **Link:** http://arxiv.org/abs/2603.24357v1

---
## Research Paper Summary

### Problem

Traditional rigid robotic hands, driven by electromagnetic motors, lack inherent physical compliance and rely on complex, expensive external sensors (e.g., force/torque sensors, tactile arrays) for safe interaction with fragile objects, unknown shapes, or humans. This increases system complexity, weight, and computational overhead. While soft robotics offers compliance, fluid-driven actuators are often bulky. Electrohydraulic HASEL actuators are promising due to their compliance and self-sensing capabilities, but their integration into dexterous, anthropomorphic hands faces challenges:

*   **Limited Grasp Taxonomy:** Direct HASEL actuation often restricts grasp types and kinematic precision compared to tendon-driven skeletal designs.
*   **Limited Contraction Strain:** HASEL actuators typically have limited linear contraction (<15%), insufficient for the large joint excursions of human-inspired hands.
*   **Safety & Bulkiness:** Placing high-voltage actuators directly at the grasping interface raises safety concerns and adds bulk to the fingers.
*   **Scalability:** Existing HASEL prosthetic solutions, while achieving high forces/motion for single digits, are often too bulky or complex to scale to fully integrated, multi-fingered anthropomorphic hands while maintaining compliance.

### Method

This paper presents a novel, integrated musculoskeletal robotic hand architecture driven by remote Peano-HASEL electrohydraulic actuators, optimized for safe manipulation.

1.  **Remote Actuation & Form Factor:** Peano-HASEL actuators are relocated to a human-sized forearm, functionally isolating the grasping interface from electrical hazards and maintaining a slim, human-like hand profile. Multiple actuators are stacked in parallel to amplify force (2-stack for DIP/PIP, 3-stack for MCP joints) with insulation and friction reduction between layers.
2.  **Stroke Amplification:** To overcome the limited linear contraction of HASEL actuators, a **1:2 pulley routing mechanism** is integrated for the flexor tendons. This mechanically amplifies tendon displacement, halving the required actuator contraction to achieve the necessary finger joint excursion (e.g., 6mm actuator contraction for 12mm tendon excursion).
3.  **Anthropomorphic Hand Design:** The hand utilizes a tendon-driven architecture with active flexion and passive elastic extension. It features circular rolling-contact joints for smooth, space-efficient flexion (index, middle, ring, pinky fingers with coupled PIP/DIP joints; thumb with IP/MCP rolling joints). A soft silicone skin covers the palm and fingers for enhanced grip and safety.
4.  **Sensorless Control:** Leveraging the HASEL actuators' inherent capacitive nature, the system achieves real-time grasp detection and closed-loop contact-aware control by simply monitoring the **operating current**. As the actuator's motion is constrained upon contact, the rate of capacitance change (and thus current) drops, allowing for contact detection without external force transducers or encoders.

### Impact

The proposed HASEL-driven robotic hand achieves significant advancements in compliant robotic manipulation:

*   **Inherent Safety:**
    *   Achieves high inherent compliance and backdrivability, absorbing impacts (e.g., tennis ball collision) and allowing objects to be easily removed during active grasp.
    *   Prioritizes compliant interaction with intrinsic force-limiting characteristics, enabling non-destructive grasping of highly fragile objects (e.g., a paper balloon).
    *   Electrical isolation of high-voltage components in the forearm enhances user safety.
*   **Simplified Design & Control:**
    *   Eliminates the need for external force sensors or encoders, reducing system complexity, wiring, weight, and computational overhead.
    *   Enables robust real-time grasp detection and contact-aware control solely through operating current monitoring.
*   **Dexterity & Versatility:**
    *   Successfully executes various grasp taxonomies (pinching, tripod, power grasp) and adapts to diverse object geometries (mushroom, cube, stuffed toy, PET bottle) while maintaining stable grasps.
    *   Achieves an anthropomorphic, slim form factor while maintaining the kinematic range necessary for dexterous manipulation, bridging the gap between soft actuator compliance and rigid kinematic dexterity.
*   **Advancement in Soft Robotics:** Represents a significant step toward simplified, inherently compliant soft robotic manipulation suitable for unstructured environments and safe human-robot interaction.