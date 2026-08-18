# GeoPose: Patient-agnostic CTA-to-DSA registration through projection-space calibration

- **Category:** Computer Vision
- **Date:** 2026-08-17
- **Link:** http://arxiv.org/abs/2608.16600v1

---
Here's a summary of the research paper in Markdown format:

### Problem

Aligning intraoperative biplanar Digital Subtraction Angiography (DSA) with pre-procedural Computed Tomography Angiography (CTA) is crucial for guiding interventions like endovascular thrombectomy (EVT) in acute ischemic stroke, where treatment delays significantly impact patient outcomes. Current 3D-to-2D registration methods face limitations:
*   **Optimization-based approaches:** Are highly sensitive to initialization and can require hundreds of computationally expensive iterations.
*   **Learning-based approaches:** Often necessitate patient-specific training or adaptation, which introduces undesirable delays in time-critical clinical workflows.
There is a need for a rapid, accurate, and patient-agnostic registration method that avoids both patient-specific model training and explicit 3D volume preregistration.

### Method

The authors propose **GeoPose**, a population-trained framework for rapid CTA-to-DSA registration that estimates C-arm pose without patient-specific adaptation. The core idea is to train pose estimation in a shared canonical frame and then transfer these predictions to an unseen patient's native CTA frame via a novel projection-space calibration.

1.  **Population-Trained Pose Estimation (GeoPose-Init):** A residual network (`GeoPose-Init`) is trained on synthetic renderings from a population of CTA volumes, all aligned to a shared canonical coordinate frame. This network directly regresses a 6-degree-of-freedom C-arm pose (as a residual from view-dependent isoposes) and the view class (e.g., PA, LAT) from a DSA Maximum Intensity Projection (MAP) image.
2.  **Projection-Space Calibration:** To apply the canonical-frame predictions to an unregistered patient's native CTA, GeoPose introduces a single-shot, projection-space calibration. This involves:
    *   Rendering the patient's native CTA at a known isocentric calibration pose (`Tnat_cal`) to create a synthetic DRR.
    *   Processing this DRR with the `GeoPose-Init` network, which outputs an estimated canonical pose (`bTcan_cal`).
    *   Composing the known `Tnat_cal` with `(bTcan_cal)^-1` to derive a rigid transform (`bA`) that maps the canonical frame to the patient's native CTA frame. This `bA` is then used to convert all subsequent canonical pose predictions to the native CTA frame for that patient. This step entirely bypasses the need for explicit 3D volume preregistration.
3.  **Population-Trained Pose Refinement (GeoPose-Refine):** A second residual network (`GeoPose-Refine`), also population-trained, refines the initial pose estimate. It takes as input a pair of images: an appearance-augmented, MAP-like DRR (representing the optimal view) and a clean DRR (rendered from the current pose estimate). It predicts a residual transformation to correct the pose. This refinement is optionally image-similarity-gated, ensuring only beneficial updates are applied.
4.  **Optional Low-Budget Optimization:** The refined pose from GeoPose-Refine provides an excellent initialization for a minimal number (e.g., 25) of iterations of gradient-based optimization using the GeoReg objective, enabling further accuracy improvements within a very short timeframe.

### Impact

GeoPose significantly advances CTA-to-DSA registration by offering a rapid, accurate, and patient-agnostic solution:

*   **Superior Accuracy & Speed:**
    *   **Optimization-Free Mode:** GeoPose achieved a carotid mean projected centerline distance (mPCD) of **5.8 mm** and a clDice of **0.45** in just **0.15 seconds**, drastically outperforming the best-performing baseline (14.5 mm mPCD, 0.28 clDice).
    *   **Low-Budget Optimization:** With only 25 optimization iterations (approximately **2 seconds**), GeoPose further improved to an mPCD of **4.6 mm** and a clDice of **0.58**, compared to 14.6 mm mPCD and 0.15 clDice for native-initialized optimization under the same budget.
*   **Patient-Agnostic Operation:** The framework uses fixed, population-level weights and requires no patient-specific training, fine-tuning, or explicit 3D volume preregistration, making it suitable for acute, time-critical interventions.
*   **Clinical Utility:** Provides the rapid and accurate geometric correspondence between pre-procedural CTA and intraoperative DSA, which is essential for:
    *   Enabling CTA-based anatomical roadmapping directly in the acquired DSA views.
    *   Providing the necessary geometric basis for downstream biplanar 3D vascular reconstruction.