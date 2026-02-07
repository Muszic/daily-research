# Scalable and General Whole-Body Control for Cross-Humanoid Locomotion

- **Category:** Robotics
- **Date:** 2026-02-05
- **Link:** http://arxiv.org/abs/2602.05791v1

---
```markdown
### Problem

Most existing learning-based whole-body controllers for humanoid robots are **robot-specific**, requiring extensive and costly retraining for each new platform with unique morphology, kinematics, and dynamics. Traditional cross-embodiment methods often fail for humanoids due to their highly diverse and complex kinematic structures, varying degrees of freedom, and intricate whole-body dynamics, which break assumptions of shared morphological priors or unified state-action representations. The central open question is whether a **single learned controller can generalize robustly across diverse humanoid embodiments** without robot-specific fine-tuning.

### Method

The authors introduce **XHugWBC**, a novel cross-embodiment training framework designed to learn a generalist whole-body controller for humanoids. It achieves this through three key innovations:

1.  **Physics-Consistent Morphological Randomization:**
    *   Instead of arbitrary perturbations, XHugWBC reparameterizes the robot's **link space** and **joint space** to ensure physical consistency during randomization.
    *   The link space randomization uses a **Cholesky-level parameterization** and **affine transformations** of the pseudo-inertia matrix, allowing unconstrained perturbations in a 10-dimensional space while guaranteeing physically valid rigid body properties.
    *   Joint space randomization perturbs **joint rotational axes** (especially hips), **joint positions** relative to parent links, and **actuation types** (sampling joints as revolute or fixed). This generates a broad distribution of embodiments with varying degrees of freedom (12 to 32 active joints), maintaining consistent actuation behavior.

2.  **Universal Cross-Embodiment Representation:**
    *   **Joint Space Semantic Alignment:** Robot-specific joint states are mapped into a global, canonical joint space of Nmax=32 dimensions. Joints not present on a specific robot are zero-padded, creating a fixed-dimensional, semantically aligned input/output for the control policy regardless of the robot's specific morphology or number of actuated joints.
    *   **Graph-based Morphology Description:** Each robot's kinematic structure is represented as a directed kinematic graph where vertices are joints and edges capture rigid-body connections. An adjacency matrix encodes the overall connectivity, even collapsing parallel linkages (e.g., ankles to knees) to form an acyclic kinematic tree. This provides explicit structural information to the policy.

3.  **Cross-Humanoid Learning:**
    *   The problem is formulated as a reinforcement learning task, optimizing a single policy across a family of randomized robot morphologies.
    *   **Observations** include a five-step history of proprioception (base angular velocity, gravity, joint positions/velocities, previous action), a joint controllability indicator, and a whole-body command vector (target velocities, base height, pelvis angle, waist rotations, gait parameters).
    *   **Policy Architectures:** Two encoder architectures are explored to process the structural information:
        *   **Graph Convolutional Networks (GCNs):** Stacked GCN layers aggregate information from kinematic neighborhoods.
        *   **Transformers:** Uses node embeddings augmented with positional encodings and a "topology-aware hybrid-mask strategy" (masked attention in the first layer, unmasked self-attention subsequently) to integrate local kinematic structure and global coordination.
    *   **State Estimator:** Trained concurrently via supervised regression to reconstruct privileged information (e.g., base linear velocity, height) unavailable on real robots, improving sim-to-real transfer.
    *   **Action Prediction:** Encoder features, global observations, and estimator outputs are fed into linear layers to generate per-node joint actions, which are then mapped back to the robot's physical joints.

### Impact

XHugWBC demonstrates a significant breakthrough in scalable and general whole-body control for humanoids:

*   **Zero-Shot Generalization:** It is the **first generalist controller to achieve robust zero-shot whole-body control across seven diverse real-world humanoid robots** (with substantial variations in kinematics, dynamics, and morphology) and twelve simulated humanoids **not seen during training**.
*   **High Performance:** All evaluated robots achieve a **100% survival rate** and maintain consistently high command-tracking accuracy, exhibiting no bias towards specific systems. The generalist policy reaches approximately **85% of specialist (robot-specific) performance** in simulation.
*   **Enhanced Fine-tuning:** When used as a pre-trained initialization, the generalist policy significantly improves subsequent fine-tuning, **surpassing specialist controllers by up to 10%** on individual robots.
*   **Scalability and Efficiency:** By learning strong embodiment-agnostic motion priors, XHugWBC drastically reduces the need for robot-specific training, enabling **rapid deployment and control of new humanoid platforms** with minimal effort and cost.
```