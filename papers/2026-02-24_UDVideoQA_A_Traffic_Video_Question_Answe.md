# UDVideoQA: A Traffic Video Question Answering Dataset for Multi-Object Spatio-Temporal Reasoning in Urban Dynamics

- **Category:** Computer Vision
- **Date:** 2026-02-24
- **Link:** http://arxiv.org/abs/2602.21137v1

---
```markdown
## UDVideoQA: A Traffic Video Question Answering Dataset for Multi-Object Spatio-Temporal Reasoning in Urban Dynamics

### Problem

Understanding the complex, multi-agent dynamics of urban traffic poses a significant challenge for current video-language models (VideoLMs). Existing datasets for this domain are often limited:
*   They typically use curated, short, or simulation-based videos, lacking the unscripted, continuous, and realistic spatio-temporal interactions of real-world urban scenes.
*   They often feature a single, vehicle-mounted perspective, failing to capture the dense multi-agent interactions (vehicles, pedestrians, micro-mobility) at intersections.
*   Many do not adequately test for hallucination robustness by including negative or out-of-context questions.
*   This results in a persistent "perception-reasoning gap" where models struggle with fundamental visual grounding despite exhibiting impressive abstract inference capabilities.

### Method

The authors introduce **UDVideoQA**, a novel benchmark dataset and suite designed to address these limitations:

1.  **Data Collection & Privacy:**
    *   Curated from 16 hours (1.7 million frames) of unscripted traffic footage recorded at multiple city intersections at 30fps under diverse conditions (time of day, weather, lighting).
    *   Employs an **event-driven dynamic blurring technique** (IRB approved) to ensure privacy preservation for identifiable information while maintaining scene fidelity.
    *   Raw footage is segmented into 10-second clips to capture coherent actions efficiently.

2.  **QA Taxonomy & Generation:**
    *   Contains ~28,800 densely annotated question-answer (QA) pairs over 8 hours of video, averaging one question per second.
    *   Follows a hierarchical QA taxonomy with five primary reasoning categories to evaluate visual grounding, causal reasoning, and counterfactual inference:
        *   **Attribution:** Basic perception (objects, attributes, text).
        *   **Basic Understanding:** Global scene comprehension (activities, environment).
        *   **Event Reasoning:** Cause-and-effect over temporal sequences.
        *   **Reverse Reasoning:** Inferring prior states from observed events.
        *   **Counterfactual Inference:** Testing robustness with hypothetical scenarios.
    *   Questions are further labeled by difficulty (easy, medium, hard) and interaction-focus (pedestrian/vehicular-centric) and include out-of-context questions to reduce hallucination.
    *   A semi-automated annotation tool supports scalable generation and validation of free-form QA pairs.

3.  **Benchmarking Frameworks:**
    *   **VideoQA Benchmark:** Evaluates 10 state-of-the-art VideoLMs (e.g., Gemini series, Qwen2.5-VL, GPT-4o/5) on UDVideoQA, assessing both zero-shot and fine-tuned performance.
    *   **VideoQGen Benchmark (First-of-its-Kind):** Introduced to assess a model's ability to generate meaningful, diverse, and contextually grounded questions from untrimmed urban videos. Evaluates 8 models using human-assessed metrics: relevance, answerability, and diversity.

### Impact

UDVideoQA provides a significant advancement for research in multimodal reasoning:

*   **Revealed Perception-Reasoning Gap:** Benchmarking 10 SOTA VideoLMs on UDVideoQA demonstrated a persistent gap, showing models that excel in abstract inference often fail with fundamental visual grounding in real-world traffic scenarios.
*   **Benchmarking Insights:**
    *   Gemini Pro achieved the highest zero-shot accuracy on VideoQA.
    *   Fine-tuning the smaller Qwen2.5-VL 7B model on UDVideoQA successfully bridged the perception-reasoning gap, achieving performance comparable to proprietary systems.
    *   In VideoQGen, Gemini 2.5 Pro and Qwen3 Max generated the most relevant and complex questions, but all models exhibited limited linguistic diversity, highlighting the necessity for human-centric evaluation.
    *   Smaller models sometimes outperformed larger models in low-level visual tasks, indicating challenges in large-scale reasoning architectures for fine-grained details.
*   **Foundation for Future Research:** UDVideoQA, including the dataset, annotation tools, and benchmarks for both VideoQA and VideoQGen, provides a robust, privacy-aware, and real-world platform for advancing multimodal reasoning, facilitating ethically aligned AI research in complex urban dynamics.
*   **Open-Source Availability:** All resources are publicly available at [https://ud-videoqa.github.io/UD-VideoQA/](https://ud-videoqa.github.io/UD-VideoQA/).
```