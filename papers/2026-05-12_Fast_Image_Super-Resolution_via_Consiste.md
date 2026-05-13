# Fast Image Super-Resolution via Consistency Rectified Flow

- **Category:** Computer Vision
- **Date:** 2026-05-12
- **Link:** http://arxiv.org/abs/2605.12377v1

---
```markdown
### Problem

Diffusion models (DMs) have achieved remarkable success in real-world image super-resolution (SR), but their practical application is significantly hampered by the reliance on time-consuming multi-step sampling processes. While recent efforts have introduced few- or single-step SR solutions, these existing methods often suffer from inefficiencies (e.g., modeling the process from noisy input, which can lose crucial information) or fail to fully leverage iterative generative priors, leading to compromised fidelity and overall quality of the reconstructed images. Specifically, a naive consistency distillation (CD) objective, while enforcing self-consistency, does not guarantee that the final distilled output precisely aligns with the ground-truth high-resolution (HR) image, potentially introducing teacher-induced errors and hindering the reconstruction of fine-grained details.

### Method

The proposed **FlowSR** approach addresses these issues by reformulating the SR problem as a **rectified flow** from low-resolution (LR) to high-resolution (HR) images. This establishes a simple and straight ordinary differential equation (ODE)-based mapping between LR and HR. To enable high-quality SR in a single step, FlowSR leverages an improved consistency learning strategy with two key innovations:

1.  **HR-Regularized Consistency Learning:** The original consistency distillation process is refined by incorporating HR regularization. This explicitly ensures that the learned SR flow not only enforces self-consistency across points on a trajectory but also converges precisely to the ground-truth HR target, mitigating teacher-induced approximation errors and enhancing fidelity to real HR data.
2.  **Fast-Slow Time Scheduling Strategy:** To improve efficiency and robustness, adjacent timesteps for consistency learning are sampled from two distinct schedulers: a "fast" scheduler with fewer timesteps (for efficiency) and a "slow" scheduler with more granular timesteps (for capturing fine-grained texture details and maintaining alignment with SR flow objectives). This mixed sampling introduces flexible jumps and mild perturbations, enhancing the model's robustness to distribution shifts.

The training process involves:
*   Initially fine-tuning a pre-trained Stable Diffusion model to align with the SR flow objective.
*   Subsequently performing consistency SR flow distillation with the HR regularization and fast-slow scheduling.
*   Incorporating an **adversarial GAN loss** for enhanced texture synthesis.
*   Introducing an **image quality alignment loss** (based on CLIP) to promote desirable text-described attributes (e.g., "sharp," "detailed") in the restored images.

### Impact

FlowSR achieves outstanding performance in both **efficiency** and **image quality**, enabling high-quality image super-resolution in a single inference step. Extensive experiments demonstrate that the method achieves superior or competitive quantitative results across various metrics (PSNR, SSIM, LPIPS, FID, MUSIQ, MANIQA, CLIPIQA) compared to state-of-the-art diffusion-based SR methods, including both multi-step and existing few/single-step approaches. Qualitatively, FlowSR generates faithful SR results, effectively recovering structures and textures with high fidelity, outperforming methods that often produce inaccurate textures or blurry outputs. This approach introduces a novel paradigm for efficient and high-quality one-step SR.
```