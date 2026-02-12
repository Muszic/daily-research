# OSIL: Learning Offline Safe Imitation Policies with Safety Inferred from Non-preferred Trajectories

- **Category:** Artificial Intelligence
- **Date:** 2026-02-11
- **Link:** http://arxiv.org/abs/2602.11018v1

---
Here's a summary of the research paper in Markdown format:

---

**Problem:**
*   **Offline Safe Imitation Learning (IL) without Explicit Feedback:** The core challenge is to learn safe and reward-maximizing policies from pre-collected demonstrations (trajectories) when there is no per-timestep safety cost or reward information available.
*   **Real-world Constraints:** Online learning in environments can be risky and costly, and accurately specifying reward functions or per-timestep safety costs (e.g., for autonomous driving or surgical robotics) is extremely difficult.
*   **Leveraging Implicit Safety Information:** The paper focuses on a scenario where it's feasible to collect:
    *   A large dataset of "union trajectories" (`D_U`): high-return, but with *varying degrees of safety cost*.
    *   A limited dataset of "non-preferred trajectories" (`D_N`): high-return, but *explicitly high-cost* (e.g., illegal driving instances), which implicitly convey what to avoid.
*   **Limitations of Prior Work:** Existing methods like SafeDICE make limiting assumptions (e.g., `D_U` contains only low-cost or high-cost behavior), and preference-based methods often assume `D_U` trajectories are entirely safe, which is unrealistic.

**Method:**
The authors propose **OSIL (Offline Safe Imitation Policies with Safety Inferred from Non-preferred Trajectories)**, a novel algorithm that formulates safe policy learning as a Constrained Markov Decision Process (CMDP) problem.

1.  **Learning a Safety Cost Model (`˜c`):**
    *   A parameterized cost model `˜c := g ◦ f` is learned, where `f` is an encoder mapping state-action pairs to a latent representation, and `g` is a linear model predicting the likelihood of a state-action pair being non-preferred.
    *   The encoder `f` is trained using a **contrastive loss (`Lcont_cost`)** that encourages temporally adjacent state-action pairs within the same (partial) trajectory to have similar representations, capturing temporal dependencies.
    *   The full cost model `˜c` is further refined with a **preference-based loss (`Lpref_cost`)** (based on the Bradley-Terry model). This loss forces the model to assign a higher total discounted cost to "non-preferred" trajectories (`τ_N`) compared to "union" trajectories (`τ_U`).
    *   Finally, a **cost action-value function (`Q^π_c`)** for a given policy `π` is learned using a squared Temporal-Difference (TD) loss over the union dataset, leveraging the learned `˜c`.

2.  **Learning a Safe Policy (`π`):**
    *   Since explicit reward functions are unavailable, OSIL reformulates the CMDP objective. It derives and maximizes a **lower bound on the policy's reward performance (`J_r(π)`)**.
    *   This reformulation simplifies the problem to minimizing the **KL divergence (`D_KL(π_U, π)`)** between the current policy `π` and the policy `π_U` that generated the union dataset (which represents high-return behavior).
    *   The KL divergence is approximated as a **Behavior Cloning (BC) term (`-E_(s,a)~DU [log π(a|s)]`)**, encouraging imitation of high-return actions.
    *   The final optimization problem combines this BC objective with the safety constraint (expected cost must be below a threshold `b`) using a **Lagrangian relaxation**: `Lpolicy = -E_(s,a)~DU [log π(a|s)] + α E_(s~ρ0) [Q^π_c(s, π(s))]`. This effectively balances imitation with cost minimization.
    *   An **adaptive penalty coefficient `α`** is introduced to dynamically adjust the trade-off between performance and safety. `α` increases when the policy takes actions that are costlier than those in the dataset and decreases when it chooses safer actions.

**Impact:**
*   **Superior Safety Performance:** OSIL consistently learns significantly safer policies that satisfy cost constraints across a suite of DSRL benchmark tasks (MuJoCo velocity-constrained and navigation tasks). It "outperforms the best baseline by nearly 2.8x" in overall safety, achieving normalized costs close to "0" (matching an oracle Constrained-RL policy).
*   **Maintained Reward Performance:** Crucially, OSIL achieves these safety improvements without degrading the reward performance. It learns policies that maintain competitive or even superior task success, with normalized returns close to "1" (again, matching the oracle).
*   **Effective Safety Inference:** The method successfully infers safety requirements entirely from offline "non-preferred" and "union" trajectories, even without explicit reward or cost annotations, demonstrating robustness in real-world, data-scarce settings.
*   **Addresses Limitations of Baselines:** OSIL avoids the restrictive assumptions about dataset cost distributions made by prior offline safe IL methods like SafeDICE and provides a more realistic framework for learning from demonstrations with varying safety levels.
*   **Comprehensive Evaluation:** Empirical results across six diverse tasks, using metrics like Normalized Return, Normalized Cost, and Normalized Conditional Value at Risk (CVaR) Cost, strongly validate OSIL's effectiveness and its ability to learn high-return, low-cost policies.

---