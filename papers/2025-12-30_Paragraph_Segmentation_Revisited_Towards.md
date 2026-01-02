# Paragraph Segmentation Revisited: Towards a Standard Task for Structuring Speech

- **Category:** NLP
- **Published:** 2025-12-30
- **Source:** [Original ArXiv Link](http://arxiv.org/abs/2512.24517v1)

---

## 🧐 Problem

Automatic Speech Recognition (ASR) transcripts are typically delivered as unstructured word streams, severely impeding readability, comprehension, and repurposing. While sentence-level structuring has received much attention, paragraph segmentation remains a largely underexplored area in speech processing. This neglect is primarily due to the absence of standardized benchmarks and a scarcity of high-quality labeled datasets for spoken content. Consequently, the broader text segmentation field also lacks robust and naturalistic benchmarks, hindering systematic evaluation and model development. Furthermore, applying Large Language Models (LLMs) to this task via unconstrained decoding often introduces "hallucinations"—modifications or omissions of content—which undermines the reliability and comparability of evaluations.

## 🛠️ Method

The authors address these problems by introducing new resources and a novel methodological approach:

*   **New Benchmarks:**
    *   **TEDPara:** A high-quality, human-annotated benchmark derived from 5,193 multi-paragraph TED Talk transcripts, focusing on formal spoken presentations. The dataset provides talk IDs and scripts for download and preprocessing to ensure reproducibility and legal compliance.
    *   **YTSegPara:** An augmented dataset covering diverse, real-world spoken content from YouTube videos. Its paragraph boundaries are synthetically labeled using an LLM (LLaMA 3.1 70B) via a novel constrained decoding method, which also establishes a benchmark for hierarchical segmentation.
*   **Constrained Decoding for LLMs:** A new, efficient formulation casts paragraph segmentation as a constrained completion task. At each sentence boundary, the LLM makes a binary decision: "continue" (emit standard punctuation) or "break" (emit punctuation followed by newlines). This prevents the LLM from hallucinating arbitrary text, ensuring the original transcript is preserved verbatim, which is crucial for faithful and sentence-aligned evaluation. This method operates in O(m) runtime, where 'm' is the number of sentences, significantly more efficient than full re-writes.
*   **Compact Hierarchical Model (MiniSeg):** The existing MiniSeg model is extended to perform hierarchical segmentation. By framing chapter and paragraph segmentation as a multi-class classification problem, the model jointly predicts both levels of granularity within a shared framework, demonstrating efficiency and minimal computational cost.
*   **Comprehensive Evaluation:** Experiments establish strong baselines on TEDPara and YTSegPara using various models (LLaMA 3 series in zero-shot, MiniSeg with different pretraining/fine-tuning regimes, random, and rule-based baselines). Evaluation employs automatic metrics (F1 score, Boundary Similarity, Pk) and human studies (pairwise ELO ratings and Likert-scale judgments) to assess segmentation quality.

## 📊 Impact

This work lays a robust foundation for standardizing paragraph segmentation in speech processing, with several key impacts:

*   **Standardized Task and Benchmarks:** It successfully establishes paragraph segmentation as a standardized, practical, and measurable task, filling a long-standing gap in both speech processing and the broader text segmentation research. The TEDPara and YTSegPara benchmarks provide crucial, high-quality resources for training and evaluating future models.
*   **Enhanced Transcript Readability:** The methods significantly improve the readability, navigation, and visual clarity of automatic speech transcripts, addressing a major concern for users and supporting human comprehension. Human evaluations confirm a strong preference for paragraph-segmented transcripts.
*   **Faithful and Efficient LLM Integration:** The proposed constrained decoding method enables LLMs to insert paragraph structures efficiently and faithfully without altering the original content. Crucially, human evaluations rate these LLM-generated segmentations on par with, or even above, human references, validating their potential for pseudo-labeling and benchmarking.
*   **Pioneering Hierarchical Structuring:** The research demonstrates that paragraph and chapter segmentation can be modeled jointly with minimal performance trade-offs, yielding the first hierarchical segmentation model for speech and audiovisual transcripts. This provides an efficient solution for multi-granularity structuring.
*   **Foundation for Downstream Applications:** The improved transcript structuring directly supports various downstream tasks, including summarization, information retrieval, education, accessibility tools, and knowledge management, thereby offering substantial practical value across multiple domains.
