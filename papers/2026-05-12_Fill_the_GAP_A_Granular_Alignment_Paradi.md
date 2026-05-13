# Fill the GAP: A Granular Alignment Paradigm for Visual Reasoning in Multimodal Large Language Models

- **Category:** Machine Learning
- **Date:** 2026-05-12
- **Link:** http://arxiv.org/abs/2605.12374v1

---
Here's a summary of the research paper "Fill the GAP: A Granular Alignment Paradigm for Visual Reasoning in Multimodal Large Language Models" in Markdown format:

### Problem

Multimodal Large Language Models (MLLMs) struggle with complex visual reasoning tasks (e.g., charts, high-resolution perception, visual math) due to missing or poorly localized visual evidence. While "visual latent reasoning" (MLLMs generating continuous latent tokens as intermediate visual evidence) offers a lightweight, internal solution compared to external tools, existing methods yield **unstable empirical gains**. The paper identifies a core reason for this instability: a **feature-space mismatch** in pre-norm MLLMs. Specifically, decoder hidden states, which are often reused as latent inputs, exist in a substantially different (much higher) norm regime than the input embeddings the model was trained to consume, making direct latent feedback unreliable.

### Method

The authors propose **GAP (Granular Alignment Paradigm)**, which aligns visual latent reasoning at three levels to overcome the identified instability:

1.  **Feature-Level Alignment (PCA-aligned latent head):** To address the norm and subspace mismatch, a lightweight PCA-aligned latent head maps the MLLM's decoder outputs into the principal subspace of auxiliary-image vision embeddings. This reconstructs generated latents in an input-compatible vision-embedding coordinate system before re-injection, ensuring they are aligned with the model's expected input distribution.
2.  **Data-Level Alignment (Context-grounded latent supervision):** A curated dataset of 49,309 multimodal QA examples is constructed. Each example includes an auxiliary image (whose frozen-ViT embeddings serve as latent targets) and a structured teacher response. This response format intersperses text reasoning with `<latent>` tokens and a `<parser>` description that explicitly records the intended auxiliary visual signal, making continuous latent targets inspectable and controllable.
3.  **Model-Level Alignment (Difficulty-aware latent assignment):** Latent supervision is applied selectively. For each training query, the base MLLM's empirical accuracy is estimated, and latent targets are assigned only to examples where the base model struggles. This prevents imposing unnecessary latent supervision on easy examples, reducing noise and focusing training on where latent reasoning is most beneficial.

### Impact

*   **State-of-the-Art Performance:** On Qwen2.5-VL 7B, GAP achieves the best mean aggregate perception (HRBench4K, MMStar, MME-RealWorld-Lite) and reasoning (MathVista, WeMath) performance among the supervised variants compared, significantly outperforming prior visual-latent baselines.
*   **Validation of Mechanisms:** Controlled ablations demonstrate that each component of GAP – PCA alignment, curated latent supervision, and difficulty-aware assignment – contributes significantly to the observed gains.
*   **Task-Relevant Visual Signal:** Inference-time intervention probing suggests that the generated latents provide genuine, task-relevant visual signals beyond merely adding token slots.
*   **Open Data Release:** The authors commit to releasing the 49K high-quality multimodal latent-supervision dataset to support future research in visual latent reasoning.