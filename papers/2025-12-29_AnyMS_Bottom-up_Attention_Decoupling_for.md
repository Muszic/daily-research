# AnyMS: Bottom-up Attention Decoupling for Layout-guided and Training-free Multi-subject Customization

- **Category:** Computer Vision
- **Published:** 2025-12-29
- **Source:** [Original ArXiv Link](http://arxiv.org/abs/2512.23537v1)

---

## 🧐 Problem

Multi-subject customization aims to synthesize multiple user-specified subjects into a coherent image. Existing methods struggle with several critical issues:

1.  **Lack of Balance:** Current approaches have difficulty simultaneously balancing three crucial objectives: text alignment (semantic consistency with the prompt), subject identity preservation (faithfully retaining subject features), and layout control (placing subjects at designated spatial locations). This trade-off becomes even more challenging as the number of subjects increases.
2.  **Subject Conflicts and Omission:** Methods often result in subjects missing or their attributes becoming confused due to interference between different subjects.
3.  **Reliance on Training:** Many existing techniques require additional training for subject learning or adapter tuning, leading to:
    *   Strong data dependency (requiring curated multi-subject datasets with layout labels).
    *   Substantial computational overhead.
    *   Limited scalability and generalization capability to unseen subjects or combinations.
    *   Specific issues with layout-guided methods:
        *   **Latent Injection:** Undermines text alignment, leading to incoherent generation.
        *   **Attention Rectifying:** Causes conflicts between visual and textual conditions, resulting in imprecise identity preservation.
        *   **Adapter Tuning:** Incurs heavy training costs and limits generalization.

## 🛠️ Method

AnyMS proposes a novel **training-free** framework for layout-guided multi-subject customization, leveraging a **bottom-up dual-level attention decoupling mechanism** to harmonize textual, visual, and layout conditions:

1.  **Global Decoupling:**
    *   Separates the cross-attention process for textual conditions (text prompt) and visual conditions (subject images) into distinct streams.
    *   This mitigates global conflicts between textual semantics and visual identity, ensuring text alignment while preserving subjects faithfully. The final output of each cross-attention block is a sum of text-based and image-based cross-attention results.
2.  **Local Decoupling:**
    *   Further disentangles the image cross-attention by using layout constraints (bounding boxes).
    *   It employs a "crop-and-merge" operation: For each subject, the corresponding subregion of the latent query feature (based on its bounding box) is extracted. Subject-specific features are then injected into this localized region via cross-attention.
    *   This ensures that each spatial area only attends to its designated subject, preventing subject-subject conflicts and guaranteeing both subject identity preservation and layout control. Semantic priority rules are used to resolve overlaps.
3.  **Training-free Subject Feature Extraction:**
    *   AnyMS utilizes **pre-trained image adapters** (e.g., IP-Adapter) to directly extract subject-specific visual features. These adapters produce features already aligned with the diffusion model.
    *   This eliminates the need for time-consuming subject learning (fine-tuning) or additional adapter tuning, significantly improving efficiency and generalizability.

This dual-level attention decoupling is applied across all cross-attention layers of the U-Net and throughout the denoising process during inference.

## 📊 Impact

AnyMS achieves state-of-the-art performance in layout-guided multi-subject customization, effectively addressing the limitations of previous methods:

*   **Superior Performance Across Objectives:**
    *   **Layout Control:** Achieves the highest mean Intersection-over-Union (mIoU) and AP@50 scores, demonstrating accurate spatial control.
    *   **Text Alignment:** Attains the highest CLIP-T similarity, ensuring faithful adherence to textual descriptions.
    *   **Identity Preservation:** Shows superior performance on CLIP-I and DreamSim, and competitive DINO scores, indicating high fidelity in retaining subject identities.
    *   This overall balanced trade-off among the three critical objectives is a significant improvement over prior art.
*   **Enhanced Scalability and Robustness:**
    *   AnyMS supports complex compositions with diverse subject combinations and demonstrably scales effectively to a larger number of subjects (from 2 to 5), maintaining strong performance even with increased scene complexity.
*   **Efficiency and Generalizability:**
    *   As a **training-free** framework, AnyMS operates with minimal GPU memory consumption and offers notably fast generation speeds. This significantly improves efficiency and generalizability by removing the dependency on extensive data annotation and computational overhead for training or tuning.
*   **Qualitative Excellence:**
    *   Qualitative evaluations show that AnyMS produces visually harmonious images with coherent layouts, high fidelity, and accurate prompt alignment, avoiding common failure patterns like object omission, fidelity degradation, and poor prompt adherence observed in baseline methods.
