# A Flow Matching Framework for Soft-Robot Inverse Dynamics

- **Category:** Robotics
- **Date:** 2026-04-03
- **Link:** http://arxiv.org/abs/2604.03006v1

---
## Flow Matching Framework for Soft-Robot Inverse Dynamics

### Problem

Learning the inverse dynamics for soft continuum robots presents significant challenges due to their high-dimensional nonlinearities, complex actuation coupling, hysteresis, and inertial effects. Existing control strategies often suffer from limitations:
*   **Feedback-based controllers:** Prone to control chattering and oscillations, making them less suitable when feedback is unavailable, delayed, or undesirable.
*   **Deterministic regression-based learners (e.g., MLP, LSTM, Transformer):** Struggle to capture the intricate nonlinear mappings and often produce inconsistent, oscillatory, or delayed control inputs, and their local linearization can be inaccurate under strong nonlinearity.
*   **Model-based methods:** Rely heavily on parameter identification, state estimation, and demanding online computation.
*   **Generative action models (e.g., diffusion policies):** While expressive, their iterative denoising process is computationally heavy, hindering real-time deployment.

There is a critical need for a lightweight, robust, and general inverse-dynamics mapping that enables direct open-loop feedforward control for accurate trajectory tracking in soft robotic systems, especially for differential state transitions over control intervals.

### Method

The proposed framework reformulates the inverse dynamics problem for open-loop feedforward control as a **conditional generative transport problem** using **Flow Matching**. It aims to learn the actuation `u_t` required to achieve a local state transition from `x_t` to `x_t+1`.

1.  **Core Framework (Rectified Flow - RF):**
    *   Inverse dynamics is framed as learning a conditional velocity field that transports a Gaussian noise sample `z` to the target control input `u_t`, conditioned on the desired state transition `(x_t, x_t+1)`.
    *   Rectified Flow (RF) is chosen as a lightweight instance to generate physically consistent control inputs rather than conditional averages, by integrating the learned velocity field. This effectively learns a discrete inverse map `u_t = g(x_t, x_t+1)`.

2.  **Physics-Consistent Variants:**
    *   **RF-Physical:** Enhances physical consistency by utilizing a physics-based quasi-static prior (`u_phys_t`) from a geometrically exact model. The model then learns only the *residual actuation* (`η_t = u_t - u_phys_t`), making the learning task easier and incorporating domain knowledge.
    *   **RF-FWD:** Further integrates a **forward-dynamics consistency loss** during flow matching. A lightweight learned forward-dynamics surrogate (`f_phi`) is used to predict the next state given the current state and the generated control input. This loss (`L_cons`) regularizes the inverse predictions by ensuring that the generated `u_t` would, if applied to `x_t` by the forward model, lead to `x_t+1`.

3.  **Inference:** During deployment, the trained flow model is queried for each local state transition, and the control input `u_t` is obtained by numerically integrating the learned flow (or residual flow for RF-Physical) from a Gaussian sample. The full open-loop actuation sequence for a trajectory is then constructed iteratively.

### Impact

The proposed flow matching framework, particularly the RF-FWD variant, demonstrates significant improvements in learning soft robot inverse dynamics:

*   **Superior Tracking Accuracy:** Reduced trajectory tracking RMSE by over 50% compared to standard regression baselines (MLP, LSTM, Transformer) in simulation. Achieved 5.0 mm RMSE on structured trajectories and 3.5 mm on random trajectories in simulation.
*   **High-Speed Performance:** Sustained stable open-loop execution at a peak end-effector velocity of 1.14 m/s in physical experiments (2.03 m/s in simulation), maintaining tracking RMSE of 20.65 mm (4.59% of robot length) at high speeds.
*   **Real-time Capabilities:** Achieved sub-millisecond inference latency (0.995 ms), making it suitable for real-time control applications.
*   **Improved Actuation Quality:** Generated smoother and dynamically consistent control inputs with minimum phase lag (45.0 ms for RF-FWD) and lower input energy, addressing the issue of high-frequency oscillations and response delays observed in deterministic baselines.
*   **Robustness and Generalization:** Demonstrated robustness to high-speed motions and generalization to complex, out-of-distribution trajectories that differed from training data, indicating the model learns underlying dynamics rather than memorizing patterns.
*   **Physical Validation:** Successfully transferred to a physical cable-driven soft continuum robot, maintaining millimeter-level tracking accuracy in both vertical (mean RMSE 4.3 mm) and more challenging horizontal (mean RMSE 6.4 mm) gravity configurations.

This work establishes flow matching as a robust, high-performance paradigm for learning differential inverse dynamics, offering a lightweight and effective solution for open-loop feedforward control in complex soft robotic systems.