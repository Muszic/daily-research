# Point What You Mean: Visually Grounded Instruction Policy

- **Category:** Robotics
- **Published:** 2025-12-22
- **Source:** [Original ArXiv Link](http://arxiv.org/abs/2512.18933v1)

---

## 🧐 Problem

Existing Vision-Language-Action (VLA) models, which align vision and language with embodied control, face significant limitations when relying solely on text for object referring, especially in complex real-world scenarios. This "information bottleneck" of text leads to two core challenges:

*   **Inexpressible References:** Language alone cannot precisely specify irregular or amorphous objects (e.g., a lump of clay), exact spatial targets (e.g., a specific point on a plain tabletop without visual anchors), or particular items within heavily cluttered scenes where many objects look visually similar. This results in inherent referential ambiguity.
*   **Limited Generalization:** Text-based VLA models struggle with complex spatial references or novel, out-of-distribution (OOD) object categories, such as referring to an unseen object or a specific item in a cluttered scene with a name rarely encountered during training. This often leads to misinterpretation and limits the models' ability to generalize.

## 🛠️ Method

The paper introduces **Point-VLA**, a plug-and-play policy designed to overcome the limitations of text-only instructions by augmenting them with explicit pixel-level visual cues.

1.  **Visually Grounded Instructions:**
    *   Point-VLA augments the standard VLA interface by overlaying a visual marker, such as a bounding box, on the first-frame overhead camera image (˜Ig,0).
    *   This grounded view, alongside standard multi-view observations, is fed into the VLA backbone. Textual instructions are kept minimal, expressing high-level intent (e.g., "pick up"), with target-specific information provided by the visual prompt.
    *   The policy then predicts actions conditioned on the text instruction, current observations, and the visually grounded first frame (ˆat =π θ(lt,I t, ˜Ig,0)).

2.  **Automatic Data Annotation Pipeline:**
    *   To enable scalable training without extensive manual labeling, a four-stage automatic annotation pipeline is developed using Multi-modal Large Language Models (MLLMs).
    *   MLLMs perform video-level scene understanding, select key frames where the target object is visible, predict bounding boxes for the referred target, and propagate these boxes to the first frame for supervision.

3.  **Robustness Augmentations:**
    *   Two grounding-aware augmentations are applied to the grounded image input:
        *   **Random translation:** Translates the grounded image (and box) to encourage the policy to rely on the target's relative position rather than absolute pixel coordinates.
        *   **Localized CutMix:** Partially replaces the object's appearance within the bounding box with ImageNet patches to prevent overfitting to specific in-box appearances and improve generalization to novel objects.

4.  **Co-training Strategy:**
    *   Point-VLA is co-trained on a balanced mixture (1:1 ratio) of pure text-only instructions and visually grounded instructions. This creates a unified policy capable of operating in either mode while preserving strong text-following behavior.

5.  **Interactive Inference:**
    *   At inference time, Point-VLA supports interactive visual grounding, allowing users to draw bounding boxes directly on a GUI, or enabling MLLMs to automatically predict bounding boxes based on human pointing or gestural cues.

## 📊 Impact

Point-VLA demonstrates significant improvements in robotic manipulation, particularly in scenarios where precise object and location referring is crucial:

*   **Superior Performance in Challenging Tasks:** Achieves an average success rate of 92.5% across six diverse real-world manipulation tasks, consistently outperforming text-only instruction baselines (average absolute gain of +60.1 percentage points) and Interleave-VLA baselines (+52.5 percentage points).
    *   Specifically, it improved performance by 35 percentage points in unseen-object tasks and over 75 percentage points in the challenging fine-grained egg-slot picking task.
*   **Enhanced Spatial Understanding and Generalization:** Effectively resolves referential ambiguity through pixel-level visual grounding, enabling accurate and unambiguous referring in cluttered, OOD, and linguistically inexpressible scenarios.
*   **Improved Text-Only Instruction Following:** Co-training with visually grounded data also enhances the underlying VLA policy, allowing Point-VLA to follow purely textual spatial references more accurately than text-only baselines, even when visual grounding is not provided at inference.
*   **Robust Plug-and-Play Generalization:** Point-VLA consistently delivers substantial performance gains across different VLA backbones (π0.5 and π0 models) and robot embodiments (dual-arm and full-body humanoid robots), demonstrating reliable transferability and acting as a modular, architecture-agnostic policy interface.
*   **Effective Visual Grounding Formulation:** Ablation studies confirm that the bounding-box overlay is the most effective visual grounding formulation compared to textual coordinates or object-only masking, which can introduce limitations like overfitting or loss of contextual information.
