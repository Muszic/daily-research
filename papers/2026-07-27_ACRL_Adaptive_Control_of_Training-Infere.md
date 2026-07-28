# ACRL: Adaptive Control of Training-Inference Discrepancy for Stable Reinforcement Learning

- **Category:** NLP
- **Date:** 2026-07-27
- **Link:** http://arxiv.org/abs/2607.24062v1

---
```markdown
### Problem

Reinforcement Learning (RL) training for Large Language Models (LLMs) suffers from **instability and potential training collapse** due to a significant **training-inference discrepancy**. This discrepancy arises from two main factors:
1.  **Architectural Separation:** Dedicated high-performance inference engines (e.g., vLLM, SGLang) are used, separate from training engines (e.g., FSDP, Megatron).
2.  **Low-Precision Quantization:** Inference engines employ aggressive low-precision quantization (e.g., FP8, INT8) to accelerate computation and save memory, while training typically uses higher precision (e.g., BF16).

This mismatch leads to different probability distributions between the training policy ($\pi$) and the inference policy ($\mu$), effectively turning on-policy learning into off-policy, which amplifies instability. Existing solutions are inadequate:
*   **Importance Sampling (IS) fixes** (token-level TIS, sequence-level MIS) often yield biased gradient estimators, suffer from vanishingly small ratios, or fail to converge with low-precision data.
*   **Precision alignment** (using the same precision for both) sacrifices the computational efficiency benefits of low-precision inference or results in a loss of accuracy.

### Method

The paper proposes **Adaptive Control Reinforcement Learning (ACRL)**, an algorithm that adaptively controls the training-inference discrepancy within a reasonable range rather than attempting to eliminate it completely. The core idea is that:
*   **Excessively large discrepancy** causes instability and collapse.
*   **Excessively small discrepancy** restricts the parameter space, leads to overfitting to the inference policy, and hinders exploration, ultimately causing accuracy loss.

ACRL implements this control by modifying the importance sampling ratio $\rho_{i,t}$ in the policy gradient update:
*   $\rho_{i,t} = \left( \frac{\pi(a_{i,t}|q,a_{i,<t},\theta_{old})}{\mu(a_{i,t}|q,a_{i,<t},\theta_{old})} \right)^{\alpha}$
*   The exponent $\alpha$ is adaptively calculated as: $\alpha = \gamma \cdot \text{sign}(A_{i,t}) \cdot (1 - Y/X)$
    *   **$X$**: A **reference value** for the sequence-level training-inference discrepancy, computed once at the beginning of training (average absolute distance between $\pi$ and $\mu$ over initial data).
    *   **$Y$**: The **current sequence-level** training-inference discrepancy (average absolute distance for the current batch).
    *   **$\text{sign}(A_{i,t})$**: Preserves the direction of the policy update (reward or punishment) based on the advantage signal.
    *   **$\gamma > 0$**: A hyper-parameter controlling the strength of the adaptation.

**How ACRL controls discrepancy:**
1.  **If $Y > X$ (discrepancy too large):** $(1 - Y/X)$ becomes negative, leading to an $\alpha$ that **reduces** the discrepancy (brings $\pi$ closer to $\mu$). This is the primary mechanism for preventing training collapse.
2.  **If $Y < X$ (discrepancy too small):** $(1 - Y/X)$ becomes positive, leading to an $\alpha$ that **increases** the discrepancy (moves $\pi$ away from $\mu$). This prevents overfitting and enhances exploration.
3.  The adjustment is applied **token-level** via $\rho_{i,t}$, but its magnitude is dynamically set based on the **sequence-level** comparison of $Y$ and $X$.
4.  ACRL acknowledges that this adaptive exponent makes it a biased estimator, but argues this is a pragmatic trade-off necessary for empirical stability and performance in low-precision RL environments, similar to PPO's clipping mechanism.

### Impact

ACRL demonstrates significant improvements in RL training for LLMs, especially when utilizing aggressive low-precision inference:
*   **Enhanced Stability:** Consistently maintains the training-inference discrepancy within a reasonable range, ensuring **stable RL training** and preventing collapse, even with aggressive FP8 quantization.
*   **Improved Accuracy:** Achieves accuracy that **matches BF16 baselines**, despite leveraging the efficiency of FP8 inference.
*   **Superior Performance:** **Outperforms previous Importance Sampling (IS) fixes** (TIS and MIS) on mathematical reasoning benchmarks (GSM8K, AIME, HMMT, AMC, MATH500).
*   **Enhanced Exploration:** Inherently increases policy entropy, leading to **better exploration** and improved overall accuracy.
*   **Practical Efficiency:** Enables the full utilization of highly efficient, low-precision inference engines without compromising training stability or final model quality, making large-scale LLM RL post-training more feasible.
```