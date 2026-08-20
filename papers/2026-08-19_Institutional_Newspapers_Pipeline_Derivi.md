# Institutional Newspapers Pipeline: Deriving billions of high quality tokens from historical newspapers

- **Category:** NLP
- **Date:** 2026-08-19
- **Link:** http://arxiv.org/abs/2608.18972v1

---
## Institutional Newspapers Pipeline: Deriving billions of high-quality tokens from historical newspapers

### Problem

Historical newspapers represent a vast record of public life, but their complex, dense, irregular, and often noisy layouts make it notoriously difficult to computationally access and extract data at scale. General-purpose tools struggle with features like columned text, decorative headings, and varied scan quality. Consequently, existing Optical Character Recognition (OCR) outputs from many collections are often of such low quality that they are primarily useful only for unreliable keyword searches, rather than enabling robust computational analysis. This limited access hinders historical research and restricts the ability of modern computational tools, including Large Language Models (LLMs), to learn from and analyze these rich historical materials effectively.

### Method

The researchers developed the "Institutional Newspapers Pipeline," a modular, computationally frugal system designed in collaboration with the Boston Public Library to extract high-quality, structured datasets from historical newspaper scans. Key aspects of their method include:

*   **Modular and Interpretable Design:** The pipeline is architected so that each step is separate, interpretable, customizable for other collections, and computationally efficient enough to run on workstation-level hardware.
*   **Multi-step Processing:** Each newspaper scan undergoes a comprehensive process:
    1.  **Segmentation:** Scans are first segmented into individual "crops," defined as rectangular bounding boxes around an uninterrupted flow of text or visual elements. Unlike prior art, segmentation is separated from classification to better leverage limited annotations and improve accuracy. A YOLO26x object detection model, trained on 1,020 annotated scans (47,485 bounding boxes), is used for this step, favoring bounding box detection over precise pixel-level segmentation to handle dense, noisy layouts.
    2.  **Crop-level OCR:** Optical Character Recognition is performed on each individual crop.
    3.  **Comprehensive Analysis & Enrichment:** Following OCR, the pipeline performs a suite of analyses on every crop, including: text analysis, type classification (combining text and image classifiers for disambiguation), reading order detection (at the scan level), named entity recognition (NER), subject classification, language detection, and pre-computed embeddings generation.
*   **Computational Frugality:** The design prioritizes small, efficient methods and models to ensure the pipeline remains accessible and scalable for knowledge institutions with varying computational resources.

### Impact

The Institutional Newspapers Pipeline successfully processed a significant portion of Boston Public Library's holdings, yielding several key impacts:

*   **Massive Open Dataset:** The creation and release of an open dataset containing an unprecedented **16.3 billion high-quality text tokens** across **83.1 million individual crops**. This data was extracted from **1,473,635 public domain newspaper scans** published between 1795 and 1930. The dataset includes rich crop-level metadata such as bounding boxes, crop types, OCR outputs (from Tesseract and a specialized VLM), reading order, NER entities, subject classes, and text/language analysis metrics.
*   **Production-Ready Tools:** The entire pipeline and its series of small, efficient detection and classification models are released as production-ready tools, enabling other knowledge institutions to apply similar high-quality processing to their own historical newspaper collections.
*   **Enhanced Computational Access to Historical Materials:** This work represents a substantial step towards unlocking high-quality data from tens of millions of newspaper scans globally, moving beyond mere keyword search to enable deep computational analysis.
*   **Improved AI "Digital Diet":** The high-quality and structured data derived from historical newspapers can significantly contribute to improving the "digital diet" of LLMs, enhancing their pre-training, performance, and understanding of historical contexts and language.
*   **Facilitation of Novel Research:** By making historical newspaper content computationally accessible and analyzable, the project enables new insights into the past at a scale previously impossible, supporting diverse research and patron access initiatives.
*   **Open Science Contribution:** All contributions, including the dataset, pipeline, and models, are openly available on Hugging Face and GitHub.