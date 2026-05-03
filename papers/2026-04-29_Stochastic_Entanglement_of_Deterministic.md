# Stochastic Entanglement of Deterministic Origami Tentacles For Universal Robotic Gripping

- **Category:** Robotics
- **Date:** 2026-04-29
- **Link:** http://arxiv.org/abs/2604.26897v1

---
## Problem

*   Traditional origami-inspired robotic grippers are limited by their **kinematically deterministic** nature, which fixes folding trajectories and grasp modes once designed.
*   This makes them unsuitable for robustly capturing objects with **random shapes** in dynamic environments without requiring **additional actuation channels and control complexity**.
*   Current demonstrations are often on a small set of curated targets, not truly open-ended tasks.

## Method

The research introduces a novel approach for universal gripping by exploiting a synergy between **local, deterministic deformation programming** (at the single-tentacle level) and **global, stochastic emergent behaviors** (at the multiple-tentacle level).

### 1. Single Tentacle Design and Deterministic Deformation Programming

*   **Fabrication:** Each origami tentacle is made by cutting thin Mylar sheets using a plotter cutter.
*   **Key Features:** Tapered shape (defined by tapering ratio $R_T$), carefully placed holes for routing an actuation tendon (defined by spacing ratio $R_S$), and origami creases (defined by angles $\alpha, \beta$) for controlling deformation.
*   **Actuation:** A simple tendon pull.
*   **Deterministic Programming:** By tailoring the design parameters ($R_T, R_S, \alpha, \beta$):
    *   **Tapering ratio ($R_T$):** Primarily determines where folding initiates (e.g., from the tentacle's tip).
    *   **Spacing ratio ($R_S$):** Creates in-plane bending by offsetting the tendon from the neutral axis.
    *   **Crease angles ($\alpha, \beta$):** Adds out-of-plane twisting deformation.
    *   These parameters are combined to prescribe **shrinking, bending, and twisting**, eventually creating **deterministic coiling** with a simple tendon pull.
*   **Modeling (Single Tentacle):** A first-principle mechanics model was derived, treating the tentacle as a kinematic chain of rigid polygonal plates connected by revolute "hinges" along crease lines. This model quantitatively maps origami design to deformation output.

### 2. Stochastic Entanglement of Multiple Tentacles

*   **Arrangement:** Multiple coiling tentacles are placed in proximity (e.g., in a circular array).
*   **Emergent Behavior:** When individually actuated, the deterministic coiling of multiple tentacles leads to **stochastic entanglement**, causing the tentacles to braid, knot, and loop around each other and the target object.
*   **Gripping Mechanism:** This emergent entanglement enables robust gripping of objects with random shapes, with "braiding" identified as a mechanically more robust approach than "looping." The grip is not permanent and can be released by relaxing the tendons.
*   **Modeling (Multiple Tentacles):** A simulation model was developed by integrating the origami mechanics (for single-tentacle deformation) with **Cosserat rods** to capture the dynamic 3D interactions and collective gripping performance, including "link-based quantities" of entanglement.
*   **Experimental Validation:**
    *   Demonstrated that the possibility and success rate of gripping increase with the number of tentacles (e.g., 100% success with 8 pairs).
    *   Tested grasping performance under various working conditions, including under gravity, in water (accounting for buoyancy and drag), and a simulated in-orbit environment (without gravity) using a stow-and-release deployment mechanism.

## Impact

*   **Novel Gripping Strategy:** Presents a new, unique strategy for robust robotic object grasping by combining local, deterministic origami deformation programming with global, stochastic entanglement, marking the first attempt in robotics to achieve such synergy.
*   **Universal & Robust Grasping:** Achieves **universal object gripping** for objects with **random shapes** in diverse and dynamic environments, overcoming a significant limitation of kinematically deterministic grippers.
*   **Simplicity and Efficiency:** Offers a solution that maintains **simple design** (thin Mylar sheets, basic crease patterns) and **minimal actuation complexity** (a single global tendon pull for an array of tentacles), avoiding the need for additional channels or intricate control.
*   **Comprehensive Framework:** Provides a complete framework encompassing origami design, mechanics modeling, dynamic simulation, and fabrication, offering a practical pathway for developing compact and versatile grippers.
*   **Versatile Applications:** Demonstrated effectiveness in various conditions (gravity, underwater, simulated microgravity), suggesting broad applicability in uncertain and complex task environments.