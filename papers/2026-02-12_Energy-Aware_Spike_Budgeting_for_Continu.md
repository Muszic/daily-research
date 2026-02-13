# Energy-Aware Spike Budgeting for Continual Learning in Spiking Neural Networks for Neuromorphic Vision

- **Category:** Computer Vision
- **Date:** 2026-02-12
- **Link:** http://arxiv.org/abs/2602.12236v1

---
```markdown
### Problem

Neuromorphic vision systems based on Spiking Neural Networks (SNNs) offer ultra-low-power perception, but their practical deployment in continually evolving environments is hindered by two main challenges:
1.  **Catastrophic Forgetting:** SNNs, like other neural networks, tend to abruptly lose previously learned knowledge when new tasks are introduced in continual learning settings.
2.  **Lack of Joint Optimization for Accuracy and Energy:** Existing continual learning methods (primarily developed for Artificial Neural Networks) seldom jointly optimize both accuracy and energy efficiency, especially for diverse input modalities like event-based datasets. This gap limits the practical viability of SNNs on energy-constrained neuromorphic hardware.

### Method

The authors propose an **energy-aware spike budgeting framework** for continual learning in SNNs, which integrates three key components:

1.  **Adaptive Spike Scheduler:** This is a novel proportional feedback control mechanism that dynamically regulates network activity during training. It treats energy (proxied by spike rate) as a first-class optimization objective alongside accuracy.
    *   It uses a penalty term `λ_rate * (r_spike - r_target)^2` in the total loss, where `r_spike` is the current spike rate and `r_target` is a dataset-specific target spike rate.
    *   The regularization coefficient `λ_rate` is adaptively updated: if spike rates exceed the target, `λ_rate` increases, enforcing sparsity; if rates fall below the target, `λ_rate` decreases, relaxing the energy constraint to allow activity needed for accurate feature extraction.
2.  **Learnable LIF Neuron Parameters:** To enhance the network's ability to capture diverse temporal dynamics, the membrane decay rate (`β`) and firing threshold (`V_thr`) of the Leaky Integrate-and-Fire (LIF) neurons are made learnable. These are layer-wise scalars, adding negligible parameter overhead.
3.  **Experience Replay:** A standard and effective continual learning strategy is employed to mitigate forgetting. A fixed-size, class-balanced episodic memory buffer stores samples from previous tasks, which are replayed alongside current-task samples during training.

The framework is applied to LIF-based SNN architectures (fully-connected or CNNs) trained end-to-end with surrogate-gradient backpropagation under a class-incremental protocol.

### Impact

The proposed framework demonstrates significant improvements in both accuracy and energy efficiency, revealing a "modality-dependent duality":

1.  **Frame-based datasets (MNIST, CIFAR-10):** Spike budgeting acts as a **sparsity-inducing regularizer**. It *improves accuracy while significantly reducing spike rates (up to 47% reduction on MNIST)*. This suggests that dense Poisson encoding can lead to redundant activations that can be pruned without information loss.
2.  **Event-based datasets (DVS-Gesture, N-MNIST, CIFAR-10-DVS):** Controlled budget relaxation enables **substantial accuracy gains (up to 17.45 percentage points on DVS-Gesture)** with only a minimal increase in spike activity, maintaining ultra-sparse operations (below 1% on DVS-Gesture and below 8% across all DVS benchmarks). This prevents underfitting in naturally sparse data.

Overall, the method:
*   Achieves **consistent performance improvements** across five benchmarks spanning both frame-based and event-based vision.
*   **Minimizes dynamic power consumption** by explicitly optimizing for energy efficiency.
*   Shows strong absolute performance (e.g., 91.93% on DVS-Gesture) and substantial improvements in **Backward Transfer** (e.g., from -25.35% to -5.90% on DVS-Gesture), indicating better retention of past knowledge.
*   Advances the practical viability of continual learning in neuromorphic vision systems by offering a framework that jointly optimizes accuracy and energy for diverse input modalities.
```