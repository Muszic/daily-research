# Mon3tr: Monocular 3D Telepresence with Pre-built Gaussian Avatars as Amortization

- **Category:** Artificial Intelligence
- **Date:** 2026-01-12
- **Link:** http://arxiv.org/abs/2601.07518v1

---
## Problem

Immersive 3D telepresence aims to revolutionize remote interaction by providing lifelike full-body holographic representations in AR/VR. However, existing systems face several critical limitations:
*   **Hardware-intensive & Costly:** They typically rely on complex, expensive multi-camera or RGB-D setups, requiring precise calibration and synchronization.
*   **High Bandwidth Demand:** Volumetric streaming of traditional 3D representations (meshes, point clouds) or even raw 3D Gaussian Splatting (3DGS) data requires prohibitively high bandwidth, making real-time performance challenging, especially on mobile or constrained networks.
*   **Performance & Latency Issues:** NeRF-based approaches incur high inference latency, while other methods struggle to maintain photorealistic visual quality and real-time interactive latency (below 100ms) on consumer-grade hardware.
*   **Trade-off:** Current systems struggle to simultaneously achieve high visual fidelity, low latency, and low bandwidth requirements.

## Method

Mon3tr proposes a novel monocular 3D telepresence framework that addresses these challenges through an **amortized computation strategy** and the integration of **3D Gaussian Splatting (3DGS)** based parametric human modeling. The method is divided into two phases:

1.  **Offline Amortization (Pre-computation):**
    *   **Objective:** To build a high-fidelity, personalized, animatable 3DGS avatar for a user once.
    *   **High-fidelity Parametric Template (SPMM3):** Introduces a novel "Skinned Person Model for Mon3tr" (SPMM3) – a hybrid parametric human model constructed by fusing a personalized body mesh (from multi-view reconstruction) with highly expressive FLAME-based face and MANO-based hand models. This captures detailed geometry, including loose garments, hair, and intricate expressions, beyond standard models like SMPL-X.
    *   **Gaussian Binding & Corrective Models:** Binds 3D Gaussians to the SPMM3 mesh. Two lightweight networks are trained:
        *   A **mesh deformation network (`F_mesh`)** learns non-rigid deformations (e.g., clothing wrinkles) and vertex offsets in canonical space.
        *   An **attribute deformation network (`F_attr`)** comprises multiple local attribute controllers to refine Gaussian properties (position, rotation, scale, opacity, color) to capture appearance dynamics based on motion parameters.
    *   **Output:** The pre-built avatar (template mesh, baseline Gaussians, pre-trained deformation networks in ONNX format) is stored in a cloud server for later download.

2.  **Online Inference (Real-time Telepresence):**
    *   **Sender (Monocular Input):** A single monocular RGB camera (e.g., on a PC) captures the user. It employs a highly optimized, parallel pipeline to extract compact semantic motion parameters in real-time: global body pose (`θ_b,t`), facial expressions (`ψ_t`), and hand gestures (`θ_h,t`).
    *   **Low-Bandwidth Transmission:** These compact parameters (total <0.2 Mbps) are compressed and transmitted over a low-latency WebRTC data channel, *instead of* raw volumetric data.
    *   **Receiver (Mobile VR):** A consumer-grade VR headset (e.g., Meta Quest 3) downloads the pre-built avatar during initialization. Upon receiving the motion parameters, it performs real-time on-device inference:
        *   The `F_mesh` network deforms the avatar mesh.
        *   The `F_attr` network dynamically generates corrective Gaussian attributes.
        *   The updated Gaussians are then rendered using an optimized 3DGS rasterization pipeline.

This "Computing for Communication" philosophy, combined with "Cost Amortization" and "Divide and Conquer" for modular animation, allows Mon3tr to decouple visual fidelity from per-frame computational and network loads.

## Impact

Mon3tr achieves state-of-the-art performance, significantly advancing real-time immersive 3D telepresence:
*   **Dramatic Bandwidth Reduction:** Achieves a transmission rate of **<0.2 Mbps** for motion parameters, representing over **1000x bandwidth reduction** compared to point-cloud streaming.
*   **Low Latency:** Delivers an impressive **~80 ms end-to-end latency**, crucial for natural, interactive telepresence.
*   **Photorealistic Visual Quality:** Synthesizes photorealistic motion and appearance, demonstrating a **PSNR of >28 dB for novel poses** and >32 dB for novel views.
*   **Real-time Performance on Consumer Hardware:** Runs smoothly at **~60 FPS** on devices like Meta Quest 3 and standard PCs, making high-fidelity telepresence accessible for consumer applications.
*   **Simplified Hardware & Cost:** Operates effectively with a **single monocular RGB camera**, significantly reducing hardware complexity and cost compared to multi-camera volumetric capture systems.
*   **Novelty:** It is the first framework to integrate 3DGS-based parametric human modeling into telepresence with an amortized computation strategy, paving the way for scalable and practical AR/VR human interaction and remote collaboration.