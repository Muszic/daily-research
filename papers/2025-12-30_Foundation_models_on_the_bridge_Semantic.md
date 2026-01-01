# Foundation models on the bridge: Semantic hazard detection and safety maneuvers for maritime autonomy with vision-language models

- **Category:** Robotics
- **Published:** 2025-12-30
- **Source:** [Original ArXiv Link](http://arxiv.org/abs/2512.24470v1)

---

## 🧐 Problem

The maritime industry is moving towards autonomous vessels (MASS/ASVs), but current autonomy stacks struggle with "out-of-distribution" (OOD) situations and interpreting **semantic cues** (e.g., a "diver-down" flag, a vessel on fire). These scenarios, where the correct action depends on meaning rather than just geometry, often fall outside predefined taxonomies and require human judgment.

This creates a critical "alert-to-takeover gap" for remote operators. The draft IMO MASS Code mandates that autonomous systems must:
1.  Detect departures from their Operational Design Domain (ODD).
2.  Enter a predefined fallback state.
3.  Notify the operator.
4.  Permit immediate human override.
5.  Avoid changing the voyage plan without approval.

Classical maritime autonomy, focused on obstacle detection and collision avoidance based on kinematics and rules, cannot meet these semantic understanding requirements, leading to a bottleneck in achieving safe and scalable one-to-many remote supervision.

## 🛠️ Method

The authors introduce **Semantic Lookout**, a camera-only, candidate-constrained vision-language model (VLM) fallback maneuver selector, designed to bridge the alert-to-takeover gap for semantic hazards. The system adheres to a strict `alert → fallback maneuver → human override` loop.

1.  **Fast Anomaly Alert:** An external, "fast" embedding-space monitor (adapted from prior work) continuously detects anomalies, triggering the system when a semantic deviation is identified.
2.  **Trajectory Candidate Generation & Gating:**
    *   From a single calibrated forward-facing camera image, an embedded Water Segmentation and Refinement (eWaSR) model computes a binary **water mask** and a **pixel-space clearance map** (distance to nearest non-water pixel).
    *   A set of short, straight motion primitives (candidate trajectories) are sampled from the vessel's bow.
    *   These candidates are **gated**: only those fully projected onto water with a minimum pixel clearance margin (e.g., 40px) are retained.
    *   The surviving candidates are thinned to a fixed set (e.g., K=15) to ensure spatial spread and are numerically labeled (ID 0 is reserved for Station-keeping).
3.  **VLM Fallback Maneuver Selection:**
    *   The VLM receives the camera image with the numbered, overlaid candidate trajectories and a specific instruction prompt.
    *   It outputs a strict JSON object containing a `choice_id` (0 to K) and brief free-text rationales (`see`, `implications`, `action`).
    *   **Safety Defaults:** If the VLM call times out, returns an error, produces invalid JSON, or if no feasible candidates are generated, the system defaults to **Station-keeping** (choice\_id=0).
    *   For robustness evaluation, an ensemble approach (FB-n, with n=3 in experiments) uses a majority vote from multiple VLM calls, defaulting to Station-keeping in case of ties.
    *   **Temporal Anchoring:** Selected candidates are fixed in the world frame at the time of the alert, decoupling perception/decision latency from actuation.
4.  **Execution and Arbitration:**
    *   The chosen fallback maneuver (a world-fixed path or Station-keeping) is executed at a cautious, anomaly-mode speed by the vessel's dynamic positioning system.
    *   **Crucially, immediate human joystick override is always prioritized** and strictly dominates the autonomous action, ensuring continuous human authority in line with IMO MASS Code.

## 📊 Impact

The study demonstrates the feasibility and benefits of using VLMs for semantic hazard detection and safety maneuvers in maritime autonomy:

1.  **IMO MASS Code Compatibility:** The proposed `alert → fallback maneuver → operator handover` architecture is fully aligned with the draft IMO MASS Code, providing short-horizon, pre-approved, immediately overridable actions that do not modify the voyage plan.
2.  **Enhanced Semantic Awareness:** VLMs enable autonomous vessels to interpret and react to "out-of-distribution" semantic hazards (e.g., fire on a vessel) that classical geometry-only systems cannot.
3.  **Practical Latency & Awareness:** Sub-10 second VLM models were shown to retain most of the semantic awareness of slower state-of-the-art models, demonstrating practical runtime performance for safety-critical applications.
4.  **Improved Safety & Human Alignment:**
    *   On 40 harbor scenes, the VLM's scene understanding and selected fallback maneuvers showed strong alignment with human consensus.
    *   The fallback maneuver selector outperformed geometry-only baselines and significantly increased standoff distance on fire hazard scenes, demonstrating effective short-horizon risk relief.
5.  **End-to-End Verification:** A live field run successfully verified the complete `alert → fallback maneuver → operator handover` chain, including immediate joystick override, proving operational readiness.
6.  **Paving the Way for Scalable Supervision:** By allowing vessels to perform safe, context-aware actions during the alert-to-takeover gap, the system helps "buy time" for human operators, which is a critical step towards enabling the safe and scalable one-to-many supervision required for future maritime autonomous shipping.
