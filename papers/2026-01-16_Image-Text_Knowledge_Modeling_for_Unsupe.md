# Image-Text Knowledge Modeling for Unsupervised Multi-Scenario Person Re-Identification

- **Category:** Computer Vision
- **Date:** 2026-01-16
- **Link:** http://arxiv.org/abs/2601.11243v1

---
Here's a summary of the research paper in Markdown format:

### Problem

Existing unsupervised person re-identification (ReID) methods struggle with diverse and challenging scenarios like visible-infrared (UVI-ReID), clothing change (UCC-ReID), and cross-resolution (UCR-ReID). Current **Unsupervised Scenario-Specific (USS-ReID)** methods are tailored to individual scenarios, leading to two key limitations:
1.  **Lack of Generalizability & Scalability:** They focus on scenario-unique identity features, requiring separate models with distinct training and multiple weight sets for different scenarios. This increases system complexity and deployment costs.
2.  **Inefficient Data Utilization:** They do not support joint training across multiple scenarios, failing to leverage the performance benefits of increased data diversity.

The paper proposes a new task: **Unsupervised Multi-Scenario Person Re-Identification (UMS-ReID)**, aiming to train a single general model to handle multiple diverse scenarios simultaneously.

### Method

The paper introduces **Image-Text Knowledge Modeling (ITKM)**, a three-stage framework leveraging pre-trained Vision-Language Models (VLMs), specifically CLIP, to address UMS-ReID.

1.  **Stage I: Unsupervised Homogeneous Learning**
    *   **Objective:** Adapt a pre-trained CLIP image encoder to generate scenario-specific identity representations.
    *   **Mechanism:**
        *   A dual-branch frontend is introduced in the CLIP image encoder for two homogeneous groups within each scenario.
        *   A novel **scenario embedding** is incorporated into the image encoder to adaptively leverage knowledge from multiple scenarios.
        *   Instance-level image representations are clustered within each homogeneous group to generate pseudo-labels.
        *   The image encoder is optimized using a **homogeneous contrastive loss** based on these pseudo-labels.

2.  **Stage II: Text Representation Learning**
    *   **Objective:** Learn identity-related, scenario-specific text representations.
    *   **Mechanism:**
        *   Utilizes a *second, frozen* pre-trained CLIP model (both image and text encoders).
        *   A set of learnable text embeddings in the prompt "A photo of a [X1][X2]...[XM] person" are optimized to associate with the pseudo-labels generated in Stage I.
        *   A **multi-scenario separation loss** is introduced to increase the divergence between inter-scenario text representations, encouraging scenario-specific text features.
        *   The learned text representations are saved as "offline" text representations.

3.  **Stage III: Unsupervised Heterogeneous Learning**
    *   **Objective:** Optimize the image encoder for effective UMS-ReID by bridging intra-scenario heterogeneity and maintaining consistency with text signals.
    *   **Mechanism (Iterative Process):**
        *   **Dynamic Text Representation Update (DRU):** Addresses inconsistencies between fixed "offline" text representations and newly generated pseudo-labels. It dynamically updates cluster-level and instance-level text representations based on the latest pseudo-labels, ensuring text-image supervision consistency.
        *   **Cluster-level Heterogeneous Matching (CHM):** Identifies reliable cluster-level heterogeneous positive pairs (e.g., visible and infrared clusters of the same person) within each scenario using a graph matching strategy.
        *   **Instance-level Heterogeneous Matching (IHM):** Obtains reliable instance-level heterogeneous positive sets by finding common top-k neighbors in both image and text representation spaces for each instance.
        *   The image encoder is then updated using a combined objective function comprising homogeneous, cluster-level heterogeneous, instance-level heterogeneous, and text-guided contrastive losses.

### Impact

*   **Novel Task & Solution:** ITKM successfully introduces and addresses the novel UMS-ReID task, offering the first framework for unsupervised person re-identification across multiple diverse scenarios within a single coherent model.
*   **Superior Performance:**
    *   ITKM (even when trained on a single scenario) outperforms existing unsupervised traditional ReID methods.
    *   ITKM (single-scenario training) is competitive with or significantly outperforms state-of-the-art unsupervised scenario-specific ReID methods across UVI-ReID, UCC-ReID, and UCR-ReID benchmarks.
    *   Crucially, ITKM trained jointly across multiple scenarios (ITKM(M)) not only *improves* upon its single-scenario performance but also *significantly outperforms* existing scenario-specific methods attempting multi-scenario training (which typically suffer performance degradation).
*   **Enhanced Generalization:** By incorporating knowledge from multiple scenarios and using mechanisms like scenario embedding and multi-scenario separation loss, ITKM demonstrates superior generalizability and adaptability to different heterogeneous conditions.
*   **Validated Components:** Ablation studies confirm the effectiveness of key ITKM components, including the novel scenario embedding, multi-scenario separation loss (shown to improve inter-scenario text separability), Dynamic Text Representation Update (DRU), Cluster-level Heterogeneous Matching (CHM), and Instance-level Heterogeneous Matching (IHM).