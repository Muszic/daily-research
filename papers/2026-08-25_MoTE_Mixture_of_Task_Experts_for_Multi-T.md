# MoTE: Mixture of Task Experts for Multi-Task Video Understanding

- **Category:** Machine Learning
- **Date:** 2026-08-25
- **Link:** http://arxiv.org/abs/2608.24763v1

---
```markdown
## Problem

Procedural video-language models need to process the same visual evidence to solve a diverse range of tasks (e.g., action recognition, forecasting, procedure prediction). Existing approaches face significant challenges:

1.  **Task Entanglement in Dense Decoders:** Standard dense transformer decoders share the same feed-forward networks (FFNs) across all tasks. This leads to entanglement of task behaviors, potential negative transfer between dissimilar tasks, and makes controlled expansion of capabilities difficult, especially when tasks differ in temporal horizon and output structure.
2.  **Misaligned Routing in Sparse MoE:** While sparse Mixture-of-Experts (MoE) decoders offer conditional computation, their token-level or patch-level learned routing is not naturally aligned with high-level, sample-wise task objectives. This lacks interpretability and a stable task-level computation path.
3.  **Lack of Task-Specific Specialization:** Current streaming video-language methods primarily focus on improving memory, token selection, or visual encoding, leaving decoder-side task specialization largely implicit.

The core tension is balancing shared visual-language grounding with the need for task-specific transformations in the decoder.

## Method

The paper proposes **Mixture of Task Experts (MoTE)**, a decoder architecture that explicitly makes task identity an architectural routing variable for multi-task video-language understanding.

1.  **Decoder Architecture:** MoTE modifies the Feed-Forward Network (FFN) sublayers within the Large Language Model (LLM) decoder.
    *   **Shared Components:** The vision encoder, MLP projector, LLM token embedding layer, and **all attention layers** remain shared across all tasks.
    *   **FFN Specialization:** Each FFN layer in the decoder is replaced by:
        *   A **shared FFN expert** that is always active for every input.
        *   A set of **task-specific FFN experts**, where each expert is dedicated to a particular task.
    *   **Conditional Computation:** For any given video-prompt example, only the shared FFN expert and **one** designated task-specific FFN expert are activated. Their outputs are summed and added to the residual stream. This ensures active computation does not grow with the number of stored task experts.
    *   **Initialization:** Both shared and task-specific experts are initialized by copying the weights of the pretrained dense FFN, allowing them to specialize during training.

2.  **Task Routing:**
    *   **Training:** During training, the explicit task identity `t` associated with each example `(v, x, t, y)` directly dictates which task expert is activated. Only the selected task expert and the shared expert receive gradients.
    *   **Inference:** When the task identity is unknown, a prompt-conditioned expert selection mechanism is used. The input prompt is embedded (using a frozen text encoder) and compared (cosine similarity) against natural language descriptions registered for each task expert. The top-1 matching expert is then selected to route the sample.

3.  **Instantiation:** The architecture is instantiated as **VideoLLM-MoTE** for procedural video understanding and also demonstrated on document analysis as **GLM-OCR-MoTE**.

## Impact

MoTE demonstrates significant improvements and offers several architectural advantages:

1.  **Improved Performance:** VideoLLM-MoTE achieves higher average top-1 accuracy on five COIN benchmarks compared to recent VideoLLM baselines, while activating a smaller parameter budget per sample. It also outperforms dense all-expert activation and learned sparse-routing controls under the same expert topology.
2.  **Compute Efficiency:** By activating only one task expert and a shared expert per sample, the active computation remains independent of the total number of stored task experts, making it highly efficient.
3.  **Enhanced Modularity and Interpretability:** MoTE provides an interpretable and compute-efficient decoder alternative. Task experts serve as modular units that can be explicitly added or removed. Analysis shows that new task experts can be introduced without disrupting existing learned knowledge, facilitating controlled capability expansion.
4.  **Generalizability:** The MoTE architectural principle successfully transfers to other domains, evidenced by its application to document analysis tasks (Key Information Extraction and Optical Character Recognition) within GLM-OCR-MoTE.
5.  **Task-Structured Routing:** MoTE's sample-level, task-structured routing directly addresses the "task entanglement" problem by providing dedicated computational paths for distinct tasks, preventing negative transfer while retaining shared components for common visual-language grounding.
```