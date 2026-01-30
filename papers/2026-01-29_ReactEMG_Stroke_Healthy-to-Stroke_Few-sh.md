# ReactEMG Stroke: Healthy-to-Stroke Few-shot Adaptation for sEMG-Based Intent Detection

- **Category:** Robotics
- **Date:** 2026-01-29
- **Link:** http://arxiv.org/abs/2601.22090v1

---
Here's a summary of the research paper "ReactEMG Stroke: Healthy-to-Stroke Few-shot Adaptation for sEMG-Based Intent Detection" in Markdown format:

### Problem
Surface electromyography (sEMG) is a promising control signal for assist-as-needed hand rehabilitation after stroke. However, detecting a stroke survivor's movement intent from paretic muscles faces significant challenges that hinder practical deployment:
*   **Lengthy & Brittle Calibration:** It often requires extensive, subject-specific calibration due to inherent differences in paretic muscle signals (weakness, reduced voluntary drive, spasticity, co-contraction).
*   **Fragility to Variability:** Learned models are fragile and their performance degrades significantly with realistic distribution shifts such as posture changes, imprecise sensor placement (armband repositioning), and within-session signal drift.
*   **Data Scarcity:** Training robust models from scratch using only small, stroke-specific datasets often leads to overfitting and poor generalization, failing to adequately capture the complexities of paretic EMG.

### Method
The authors propose **ReactEMG Stroke**, a healthy-to-stroke few-shot adaptation pipeline designed to improve sEMG-based intent detection for controlling wearable hand orthoses.

1.  **Base Model:** They utilize **ReactEMG**, an encoder-only transformer model, pretrained on a large-scale dataset of sEMG from over 650 able-bodied participants. This model learns a general, reusable EMG representation from the healthy domain.
2.  **Stroke Dataset:** A new dataset was collected from three individuals with chronic stroke, involving 8-channel sEMG recordings using a Myo armband. Participants performed timed hand opening, closing, and relax movements with their paretic limb while wearing the MyHand orthosis. Crucially, the dataset included:
    *   A small amount of subject-specific **training data**.
    *   **Held-out test sets designed to simulate realistic distribution shifts**: within-session drift, unseen posture changes, armband repositioning, and device-driven motion (orthosis actuating during data collection).
3.  **Adaptation Strategies:** The pretrained ReactEMG model was fine-tuned for each stroke participant using only their small, subject-specific training data. Three adaptation strategies were compared:
    *   **Head-only Fine-tuning:** Only the final classification head was updated, with the pretrained backbone frozen.
    *   **LoRA (Low-Rank Adaptation):** All pretrained weights were frozen, and low-rank update matrices were trained for linear layers, offering a parameter-efficient approach.
    *   **Full Fine-tuning:** All model parameters (backbone and classification head) were updated end-to-end.
4.  **Baselines:** Performance was compared against two baselines:
    *   **Healthy Zero-shot Transfer:** The frozen pretrained ReactEMG model was evaluated directly on stroke data without any adaptation.
    *   **Stroke-only Training:** A ReactEMG model was trained from scratch exclusively on the limited stroke data, using random initialization.
5.  **Evaluation Metrics:** Models were evaluated on:
    *   **Raw Accuracy:** Fraction of correctly predicted timesteps.
    *   **Transition Accuracy:** A stringent metric designed for real-time control, measuring correct and stable intent transitions (penalizing delayed switching and "flicker").
    Data efficiency (varying training data budgets) and convergence behavior were also analyzed.

### Impact
The research demonstrates that initializing an sEMG intent detector from a healthy-pretrained model and fine-tuning it with limited stroke-specific data significantly improves performance and robustness for post-stroke hand rehabilitation:

*   **Substantial Performance Gains:** Healthy-pretrained adaptation consistently outperforms both zero-shot transfer and stroke-only training. The best adaptation methods (LoRA and Full Fine-tuning) improved average **transition accuracy from 0.42 to 0.61** and raw accuracy from 0.69 to 0.78 across all three participants and realistic distribution shifts. This indicates improved reliability for real-time control.
*   **Reduced Calibration Burden & Data Efficiency:** The approach achieves measurable improvements even with extremely small amounts of labeled stroke data (e.g., using only 1 training pair), demonstrating its potential to significantly reduce the lengthy and costly subject-specific calibration typically required.
*   **Effective Adaptation Strategies:** While LoRA and Full Fine-tuning generally yield the strongest overall performance by allowing deeper representation changes, the optimal strategy can be participant-dependent, possibly correlating with the severity of hand impairment. LoRA's parameter efficiency is particularly appealing for limited compute environments.
*   **Rapid Convergence:** Healthy-initialized models achieve meaningful gains in transition accuracy very quickly (within the first few fine-tuning epochs), outperforming stroke-only models that struggle to learn robust features from scratch under the same limited data budget.
*   **Scalability for Rehabilitation:** This framework offers a scalable solution by leveraging the abundance of easily collected healthy sEMG data to pretrain robust foundation models, which can then be efficiently adapted to the inherently scarce and heterogeneous stroke data. This paradigm is crucial for translating large model capacity into better, more accessible intent detection for stroke survivors.