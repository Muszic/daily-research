# Biconvex Optimization for Smooth Minimum-Time Trajectories around Convex Obstacles

- **Category:** Robotics
- **Date:** 2026-08-03
- **Link:** http://arxiv.org/abs/2608.02834v1

---
This research paper proposes a novel biconvex optimization approach for generating minimum-time, smooth trajectories around convex obstacles.

### Problem

The paper addresses the fundamental challenge of **minimum-time motion planning** for robots operating in environments with convex obstacles. Existing methods suffer from several limitations:
1.  **Lack of Smoothness and Higher-Order Derivative Support:** Sampling-based planners produce jagged paths and do not natively encode smoothness or higher-order derivative constraints (e.g., jerk, snap), which are critical for real-world robot operation. Post-processing steps are often heuristic and can be suboptimal or brittle.
2.  **Local Minima and Robustness Issues:** Traditional trajectory optimization methods struggle with the non-convexity of collision-avoidance constraints, leading to local minima, inconsistent runtimes, and a strong dependency on good warm-starting.
3.  **Computational Cost of Environment Decomposition:** State-of-the-art decomposition-based motion planners (DBMPs) require computationally expensive pre-decomposition of the free space into convex sets, which needs to be redone every time the environment changes. They also face difficulties in jointly optimizing trajectory duration and enforcing higher-order derivative constraints in a convex manner.

The goal is to develop a planner that is guaranteed to converge, is anytime, produces high-quality smooth trajectories, supports derivative constraints to arbitrary order, and avoids the need for costly environment pre-decomposition.

### Method

The proposed **Biconvex Minimum-Time Planner (BMTP)** tackles these challenges using a novel biconvex optimization framework:

1.  **Joint Convexification of Objective and Derivative Constraints:** The minimum-time objective and all derivative constraints (up to an arbitrary order $I$) are convexified through a change of variables. The trajectory $q:[0,T] \to \mathbb{R}^n$ is reparameterized as $r:[0,1] \to \mathbb{R}^n$, and the objective is changed from minimizing $T$ to minimizing $T^I$. This allows derivative constraints like $r^{(i)}(s) \in T^{i/I} C_i$ to be expressed as convex sets using a specialized lemma.
2.  **Collision Avoidance via Time-Varying Separating Planes:** Collision avoidance constraints with convex obstacles are reformulated using time-varying separating planes. For each obstacle $O_k$, a time-varying plane $(a_k(s), b_k(s))$ is introduced such that $a_k(s)^\top r(s) + b_k(s) < 0$ for all $s \in [0,1]$, where $(a_k(s), b_k(s))$ belongs to the polar of the obstacle $O_k^\circ$. This reformulation introduces bilinearities ($a_k(s)^\top r(s)$), making the overall problem biconvex.
3.  **Alternating Optimization for Biconvex Program:** The biconvex problem is solved iteratively by alternating between two convex subproblems:
    *   **Plane Update:** Given a fixed, collision-free trajectory, optimal time-varying separating planes are computed that maximize the margin (distance) between the trajectory and the obstacles.
    *   **Trajectory Update:** Given fixed separating planes, the trajectory and its duration are optimized in a now-convex problem.
4.  **Local Minima Escape and Anytime Guarantees:** The BMTP incorporates a mechanism to escape local minima by dynamically adding and updating separating planes only for obstacles that the *current iterate* collides with. This allows the trajectory to "jump around" obstacles. The method is initialized with a simple collision-free polygonal curve and is guaranteed to converge to a feasible solution, with the trajectory duration never increasing across outer iterations. It is also "anytime," meaning it can be interrupted at any point and return the best feasible (collision-free, constraint-satisfying) trajectory found so far.
5.  **Finite-Dimensional Formulation with Bézier Curves:** For practical implementation, continuous trajectory and plane functions are represented using composite Bézier curves. This leverages Bézier curve properties for enforcing derivative, continuity, and collision avoidance constraints efficiently in a finite-dimensional optimization problem.

### Impact

The Biconvex Minimum-Time Planner (BMTP) offers substantial improvements over existing motion planning methods:

*   **Reliable and Guaranteed Performance:** It is guaranteed to converge to a feasible solution and is an "anytime" algorithm, providing robust performance even with poor initializations. This addresses a critical drawback of many local trajectory optimizers.
*   **High-Quality, Smooth Trajectories:** The method reliably produces high-quality, minimum-time trajectories that are smooth and satisfy derivative constraints to arbitrary order (e.g., velocity, acceleration, jerk, snap, etc.) and continuity constraints.
*   **Broad Applicability without Pre-computation:** Unlike decomposition-based methods, BMTP does not require a costly, up-front convex decomposition of the free space, making it more adaptable to dynamic environments and general problem settings.
*   **Competitive Computation Times:** Despite its advanced capabilities, the proposed method achieves computation times comparable to state-of-the-art decomposition-based planners.
*   **Enhanced Throughput for Robotics:** The ability to generate efficient, high-quality, and predictable motion plans can significantly improve throughput in high-demand robotic applications such as industrial manufacturing, warehouse logistics, and advanced manipulation tasks (e.g., drone navigation, dual-arm bin unloading as demonstrated).