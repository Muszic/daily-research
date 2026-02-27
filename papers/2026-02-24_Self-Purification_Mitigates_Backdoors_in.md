# Self-Purification Mitigates Backdoors in Multimodal Diffusion Language Models

- **Category:** Cryptography
- **Date:** 2026-02-24
- **Link:** http://arxiv.org/abs/2602.22246v1

---
This research paper investigates and addresses backdoor vulnerabilities in Multimodal Diffusion Language Models (MDLMs).

### Problem

*   **Vulnerability of MDLMs:** Multimodal Diffusion Language Models (MDLMs) are an emerging alternative to autoregressive MLLMs, offering benefits like faster inference. However, their vulnerability to backdoor attacks is largely unexplored.
*   **Successful Attack Implantation:** The paper demonstrates that standard data-poisoning pipelines (originally for AR models) can successfully implant backdoors into MDLMs. Attackers can manipulate model behavior via specific triggers (e.g., content insertion, targeted refusal, semantic misclassification) while maintaining normal performance on clean inputs (ASR >90% on triggered inputs, ASR ~0% on untriggered inputs).
*   **Lack of Defense Strategies:** Existing backdoor defense strategies are not directly transferable or effective for MDLMs, as they are often designed for unimodal or autoregressive models, or require auxiliary models or clean reference data. This leaves MDLMs exposed to significant trustworthiness concerns.

### Method

The paper proposes **DiSP (Diffusion Self-Purification)**, a backdoor defense framework specifically designed for MDLMs, leveraging their unique generative capabilities.

1.  **Key Observation:** DiSP is based on the insight that selectively masking a small subset of high-saliency visual tokens at inference time can neutralize a backdoored model's trigger-induced behaviors and restore normal functionality, with minimal impact on clean performance.
2.  **Saliency Score Calculation:** For a given compromised MDLM and training instance, the method calculates a "saliency score" for each visual token. This is done by approximating the local directional curvature of the output KL-divergence at the first generation step, using a Fisher–Jacobian quadratic form efficiently estimated via a Hutchinson estimator. Tokens with high saliency are deemed more sensitive to trigger patterns.
3.  **Dataset Purification (via Self-Inference):**
    *   A proportion (ρ) of the highest-saliency visual tokens in the input images are identified and *masked*.
    *   The *compromised model itself* is then run on these partially masked inputs. Because the masking neutralizes the trigger, the model generates "purified" (untriggered) responses.
    *   A "purified dataset" is constructed, where original image-text prompts are paired with these newly generated, untriggered responses.
4.  **Model Purification (via Fine-tuning):** The compromised MDLM is then fine-tuned on this newly created purified dataset. This process "rewrites" the trigger-response mappings into untriggered responses, effectively removing the embedded backdoor.
5.  **Self-Contained Defense:** DiSP is notable for performing backdoor removal *without* requiring any auxiliary models or external clean reference data, relying solely on the compromised model and its original training data.

### Impact

*   **First Analysis for MDLMs:** This work presents the first comprehensive analysis of backdoor threats in Multimodal Diffusion Language Models, highlighting their vulnerability and the urgent need for tailored defenses.
*   **Effective Backdoor Mitigation:** DiSP effectively mitigates backdoor effects in MDLMs. Extensive experiments show a dramatic reduction in the Attack Success Rate (ASR) from over 90% (for compromised models) to typically under 5% across various attack targets (content insertion, targeted refusal, semantic misclassification) and trigger patterns.
*   **Maintained Model Utility:** The defense successfully preserves the model's performance on benign, clean tasks, with negligible degradation (typically over 89-91% of original clean performance).
*   **Practical & Resource-Efficient:** DiSP's unique design, which does not require auxiliary models or clean reference data, makes it a practical, efficient, and broadly applicable defense framework for real-world deployment of MDLMs, especially when the trustworthiness of training data is uncertain.