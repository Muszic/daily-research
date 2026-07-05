# QFedAgent: Quantum-Enhanced Personalized Federated Learning for Multi-Agent Activity Recognition

- **Category:** Artificial Intelligence
- **Date:** 2026-07-02
- **Link:** http://arxiv.org/abs/2607.02426v1

---
## QFedAgent: Quantum-Enhanced Personalized Federated Learning for Multi-Agent Activity Recognition

### Problem

Autonomous multi-agent robotic systems generate heterogeneous, non-independent and identically distributed (non-IID) multimodal sensor streams (e.g., accelerometer, gyroscope) due to varying environments and motion patterns. Centralizing this data for training is impractical due to communication overhead, latency, and privacy concerns. While Federated Learning (FL) offers a privacy-preserving solution, conventional FL algorithms struggle with non-IID data, leading to degraded convergence and personalization. Furthermore, existing classical multimodal fusion techniques (e.g., attention, transformers) introduce substantial parameter overhead and communication costs, which complicates aggregation across heterogeneous clients in FL settings. There is a need for compact yet expressive fusion mechanisms that can handle complex cross-modal interactions efficiently within personalized FL frameworks for robotic sensing.

### Method

The paper proposes **QFedAgent**, a hybrid quantum-classical personalized Federated Learning framework for multi-agent activity recognition using multimodal IMU data.

1.  **Architecture:** Each agent processes accelerometer and gyroscope signals using separate shared Convolutional Neural Network (CNN) encoders to produce modality embeddings.
2.  **Quantum Fusion Module:** These embeddings are then fed into a **Variational Quantum Circuit (VQC)** fusion layer. This VQC models accelerometer-gyroscope interactions by:
    *   Encoding classical input embeddings into quantum states via AngleEmbedding (RX rotations).
    *   Exploiting quantum entanglement operations (StronglyEntanglingLayers with CNOT gates) to capture complex cross-modal correlations.
    *   Measuring Pauli-Z expectation values to produce a compact, fused representation.
    *   The VQC uses significantly fewer trainable parameters (e.g., 72 quantum rotation parameters) compared to classical Multi-Layer Perceptron (MLP)-based fusion (33K parameters).
3.  **Personalized FL Protocol:** QFedAgent employs a personalized FL strategy:
    *   **Globally Aggregated Parameters:** The weights of the CNN encoders and the VQC fusion module are shared and aggregated across clients using weighted FedAvg.
    *   **Client-Specific Local Parameters:** A lightweight adapter and a classification head are maintained locally by each client and are never transmitted, enabling adaptation to individual agent characteristics and environments.
4.  **Optimization:** The VQC parameters are optimized using the parameter-shift rule, allowing gradient-based learning compatible with classical backpropagation.

### Impact

*   **High Accuracy & Robustness:** QFedAgent achieves a high mean test accuracy of **97.7%** on the challenging OPPORTUNITY activity recognition dataset under subject-based non-IID partitions. This performance is competitive with, and in some cases surpasses, conventional federated baselines like FedAvg (96.6%), FedProx (96.7%), and a classical MLP-FL (97.2%) variant.
*   **Significant Parameter Reduction:** The VQC-based fusion module achieves an approximate **10x total parameter reduction** for the fusion component compared to classical MLP-based fusion (72 quantum rotation parameters versus 33K for the MLP, with a total fusion module parameter count of 3,144 including classical interface projections). This addresses the critical overhead issue in multimodal FL.
*   **Efficient Cross-Modal Interaction:** The results demonstrate that quantum entanglement effectively models complex cross-modal interactions with far fewer parameters, leading to stable federated optimization and competitive performance even in non-IID settings.
*   **Future Potential:** While classical simulation of the quantum circuits currently incurs higher per-round training time (121.4 s vs. ~10 s for classical methods), the paper highlights that this overhead is expected to diminish on real quantum hardware, where circuit execution scales independently of parameter count, making QFedAgent a promising approach for future resource-constrained distributed robotic systems.