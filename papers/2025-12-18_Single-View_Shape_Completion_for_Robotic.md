# Single-View Shape Completion for Robotic Grasping in Clutter

- **Category:** Robotics
- **Published:** 2025-12-18
- **Source:** [Original ArXiv Link](http://arxiv.org/abs/2512.16449v1)

---

## 🧐 Problem

Vision-based robot manipulation faces significant challenges in cluttered environments due to incomplete object geometry. A single camera view inherently provides only partial observations, and clutter further restricts visibility. This leads to:

*   **Suboptimal Grasp Estimation:** Grasp planning algorithms perform poorly as they operate on incomplete data, resulting in grasps that are prone to collision or rely on non-existent surfaces.
*   **Limited Real-World Applicability of Prior Work:** Existing shape completion methods often assume objects are isolated, in minimal clutter, or require canonical alignment, which is impractical for real-world scenarios with arbitrary object poses and occlusions.
*   **Difficulty with Ambiguity:** Partial views can lead to ambiguities where local geometric features are similar across different object categories (e.g., a curved surface could be a bottle, mug, or bowl), making accurate shape inference difficult without additional context.

## 🛠️ Method

The paper proposes a modular, systems-level approach for robotic grasping in clutter that integrates learning-based components:

1.  **Scene Acquisition:** Uses an RGB-D camera to capture scene information.
2.  **Object Segmentation:** Leverages **LangSAM**, a language-guided segmentation model, to accurately segment target objects from the RGB-D input based on text prompts (e.g., "red bowl"). This helps isolate the object's point cloud and overcomes issues of over-segmentation or merging in cluttered scenes.
3.  **Single-View Shape Completion:**
    *   Employs **Diffusion-SDF**, a diffusion-based generative model, to reconstruct complete 3D object geometries from partial, unaligned point clouds obtained from the segmented depth image.
    *   Objects are represented using Signed Distance Fields (SDFs).
    *   To resolve ambiguities and improve robustness, a "category-level shape completion" approach is used, training a separate Diffusion-SDF model (checkpoint) for each object category (e.g., apple, bottle, bowl, box, can, hammer).
    *   The model is trained on a custom dataset of household items, synthetically augmented with realistic partial views generated via virtual raycasting to simulate real-world occlusions.
4.  **Grasp Pose Estimation:**
    *   Utilizes **GraspGen**, a state-of-the-art diffusion-based grasp inference network, to predict 6-DoF grasp poses on the **completed 3D object shapes** (rather than partial observations).
    *   Predicted grasps are scored, ranked, and selected with a preference for vertical approaches (within a 40° cone) to minimize collision risk. A multi-attempt strategy (top K=5 grasps) is used for robustness against motion planning failures.
5.  **Grasp Execution:** The selected grasp is then executed by a Franka Emika Panda robot using a standard motion planner (MoveIt2).

## 📊 Impact

The proposed method demonstrates significant improvements in robotic grasping performance in challenging, cluttered environments:

*   **Increased Grasp Success Rates:** Preliminary real-robot evaluations show a **23% improvement** in grasp success rates over a naive baseline (without shape completion) and **19% improvement** over a recent state-of-the-art shape completion approach (ZeroGrasp) in cluttered scenarios.
*   **Enhanced Robustness in Clutter:** Unlike prior work often limited to isolated objects or minimal clutter, this approach is validated in realistic household clutter scenarios, proving the practical benefits of complete shape information.
*   **Novel Integration of Diffusion Models:** Introduces the first integration of diffusion-based shape completion in robotic manipulation, with robust training routines designed to handle significant occlusions and arbitrary object orientations.
*   **Reliable Shape Reconstruction:** Achieves 100% successful reconstruction rates on the ReOcS real-world dataset, while a compared state-of-the-art method (ZeroGrasp) failed for 30-35% of samples, highlighting the reliability of the shape completion module.
*   **Modular and Flexible System:** The modular design allows for independent development and swapping of components (segmentation, shape completion, grasp generation), facilitating future research and adaptation.
