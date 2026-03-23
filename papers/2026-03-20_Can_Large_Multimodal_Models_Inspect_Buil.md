# Can Large Multimodal Models Inspect Buildings? A Hierarchical Benchmark for Structural Pathology Reasoning

- **Category:** Computer Vision
- **Date:** 2026-03-20
- **Link:** http://arxiv.org/abs/2603.20148v1

---
This paper introduces a new benchmark, DefectBench, to rigorously evaluate Large Multimodal Models (LMMs) for building facade inspection.

## Problem

Automated building facade inspection is vital for urban resilience, but traditional specialized discriminative models (e.g., YOLO, Mask R-CNN) are limited to passive, pixel-level localization. They lack the visual understanding of structural topology and generalization capabilities for active reasoning or actionable diagnosis. Large Multimodal Models (LMMs) promise a shift towards active reasoning and open-world knowledge, but their application in high-stakes engineering domains like civil inspection lacks rigorous evaluation standards.

Existing challenges include:
1.  **Data Silos and Ontological Inconsistency:** Fragmented public datasets with conflicting taxonomies, incompatible annotation granularities, and a lack of logic-intensive metadata.
2.  **Fragmentation of Evaluation Standards:** Absence of a unified, multi-dimensional benchmarking framework capable of interrogating LMMs across the full cognitive spectrum, from coarse-grained semantic comprehension to fine-grained geometric quantification.

## Method

The authors address these issues by:

1.  **Unified Multi-Granularity Dataset Creation:**
    *   Consolidated 12 fragmented open-source building defect repositories into a unified dataset.
    *   Implemented a three-stage curation pipeline: low-quality filtering (Laplacian variance), semantic deduplication (DINOv2), and contextual relevance filtering (CLIP).
    *   Developed a human-in-the-loop semi-automated annotation framework (Plug-and-Play Annotation Platform) with expert-proposal verification. This platform integrates SOTA detectors (e.g., YOLO, Faster R-CNN) for bounding box refinement and SOTA segmentors (e.g., SAM-3, SegFormer) for zero-shot mask generation, allowing experts to refine outputs.
    *   Established a standardized, multi-level defect ontology (4 primary classes, 11 fine-grained sub-classes) to unify labeling.
    *   The resulting **DefectBench** dataset comprises 1,488 high-resolution images with 4,527 distinct structural anomalies, providing synchronized pixel-level ground truth across classification, object detection, and semantic segmentation.

2.  **Hierarchical Benchmarking Framework (DefectBench):**
    *   Designed the first multi-dimensional evaluation framework for facade inspection, interrogating LMMs across three escalating cognitive dimensions:
        *   **Semantic Perception ("What" Task):** Evaluates defect classification (nature) and defect counting (quantity).
        *   **Spatial Localization ("Where" Task):** Assesses precise bounding box generation and visual spatial reasoning (parsing topological relationships among defects).
        *   **Generative Geometry Segmentation ("How" Task):** Measures the generation of binary pixel-level masks for precise defect morphology.

3.  **Extensive Benchmarking:**
    *   Evaluated 18 state-of-the-art (SOTA) LMMs (both open-source and proprietary) against DefectBench using task-specific metrics (P, R, F1, MAE, RE, mAP50, mIoU, PA).
    *   Employed a multi-turn dialogue protocol to emulate authentic diagnostic workflows.

## Impact

The research yields significant insights and contributions:

1.  **LMM Capabilities and Limitations:**
    *   **Semantic Understanding ("What"):** LMMs demonstrate exceptional topological awareness and semantic understanding, effectively diagnosing the "what" (defect type) and even some "how" (relationships). Open-source models (e.g., Qwen3, GLM, InternVL) show competitive and stable performance. However, they exhibit significant deficiencies in precise numerical counting, especially for multiple symbiotic micro-defects or visually ambiguous categories like surface stains.
    *   **Spatial Localization ("Where"):** Current LMMs struggle with precise metric localization (bounding box accuracy) in a zero-shot setting. They are better suited for qualitative diagnostic inference than quantitative spatial mapping.
    *   **Generative Geometry Segmentation ("How"):** Crucially, the viability of *zero-shot generative segmentation* is validated. SOTA LMMs (e.g., Gemini-3-pro-edit) achieve remarkable proficiency, with performance competitive to specialized *supervised* segmentation models without domain-specific training.
    *   **Error Analysis:** Identified cascading error propagation in multi-turn dialogues and generative instability (e.g., generating RGB textures instead of binary masks) as key limitations, necessitating post-processing.

2.  **New Standard and Open-Source Resource:**
    *   **DefectBench** establishes the first multi-dimensional benchmark and provides a high-quality, open-source database for building facade inspection, setting a new baseline for the advancement of autonomous AI agents in civil engineering.
    *   The open-source annotation toolkit facilitates future data curation and algorithm integration.

This work provides a rigorous evaluation standard and valuable insights into the current state and future potential of LMMs for automated structural pathology reasoning.