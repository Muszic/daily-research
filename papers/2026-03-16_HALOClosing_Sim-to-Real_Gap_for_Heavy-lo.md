# HALO:Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation

- **Category:** Robotics
- **Date:** 2026-03-16
- **Link:** http://arxiv.org/abs/2603.15084v1

---
**Problem:**
*   Humanoid robots in real-world scenarios often carry unknown payloads, which drastically alter their dynamics (mass, Center of Mass, inertia).
*   This introduces a significant "sim-to-real gap," causing reinforcement learning (RL) policies trained with nominal dynamics to degrade, leading to conservative or unstable motions.
*   Existing solutions have limitations:
    *   **Domain Randomization (DR):** Improves robustness but often yields conservative behaviors, failing to exploit the robot's full physical capabilities for large, structured payload variations.
    *   **Traditional System Identification (SysID):** Requires specialized sensing equipment (e.g., torque sensors, motion capture) or partial robot disassembly, making it impractical for complex, floating-base humanoid robots.
*   A key challenge is the *entanglement* between intrinsic nominal model mismatch (e.g., wear, calibration drift) and load-induced dynamic changes, which can lead to biased parameter identification.

**Method:**
The authors propose **HALO (HeAvy-LOaded humanoid motion control)**, a unified framework that uses differentiable simulation for a two-stage gradient-based system identification, enabling zero-shot sim-to-real transfer for heavy-loaded humanoids.

1.  **Sensor-Minimal Data Collection:**
    *   To overcome the need for external sensors, trajectory data is collected by mechanically constraining one foot of the robot (e.g., using vises).
    *   Full-body trajectories are then reconstructed from onboard joint encoder measurements using forward kinematics.
    *   A constrained quadratic program is applied at each timestep to correct for foot-height discrepancies caused by sensor noise and accumulated drift, ensuring physically consistent ground contact.
    *   Only a small amount of data is required due to the sensitivity of dynamics to mass/CoM changes.

2.  **Two-Stage Gradient-Based System Identification:**
    *   Built upon the differentiable simulator MuJoCo XLA, parameter identification is formulated as a trajectory-level optimization problem, minimizing the discrepancy between simulated and real-world trajectories.
    *   **Stage 1 (Base Model Calibration):** Using trajectories collected *without payload*, the full set of nominal robot model parameters (link mass, CoM position, inertia, joint damping, friction coefficients) is optimized. This reduces the inherent sim-to-real gap unrelated to the payload.
    *   **Stage 2 (Payload Parameter Identification):** With the calibrated base model as initialization, *only payload-related parameters* (specifically, mass and CoM positions of the links directly affected by the payload, such as torso and hands) are optimized using trajectories collected *under loaded conditions*. This structured decomposition effectively separates base-model errors from payload effects, improving identification stability and accuracy.
    *   The optimization uses gradient descent, leveraging the analytical gradients provided by the differentiable simulator, complemented by regularization terms to maintain physical plausibility of identified parameters.

3.  **Heavy-Load Skill Acquisition:**
    *   Once the robot's dynamics are accurately identified, RL policies (e.g., motion imitation using PPO) are trained in simulation.
    *   The precise identified model parameters reduce the need for extensive domain randomization during training, allowing for *zero-shot sim-to-real transfer* of agile locomotion skills to the physical heavy-loaded humanoid.

**Impact:**
*   **Superior Parameter Identification:** HALO demonstrates more precise and stable parameter identification, especially under extreme heavy-load conditions, significantly outperforming sampling-based methods like CMA-ES which can converge to physically unreasonable values.
*   **Improved Motion Tracking Accuracy:** Policies trained with HALO's identified parameters achieve substantially lower global mean per-joint position error (E g-mpjpe), mean per-joint position error (E mpjpe), and velocity error (E vel) across both steady-state and high-agility tasks, compared to Wide Range Domain Randomization (WDR) and Calibrated Mass (CM) baselines.
*   **Enhanced Real-World Agility and Robustness (Zero-Shot Transfer):**
    *   Enables successful zero-shot transfer of complex, agile RL policies to physical humanoids carrying heavy, unknown payloads.
    *   Improves performance in real-world gait precision tasks by 45.45% to 73.33%.
    *   Enhances performance in challenging tasks like in-place 90-degree yaw jumping by 72.97%.
    *   Achieves a 100% success rate in challenging motion tracking tasks on the physical robot, confirming its ability to effectively narrow the sim-to-real gap while preserving agility.