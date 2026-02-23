# Understanding Unreliability of Steering Vectors in Language Models: Geometric Predictors and the Limits of Linear Approximations

- **Category:** NLP
- **Date:** 2026-02-19
- **Link:** http://arxiv.org/abs/2602.17881v1

---
## Understanding Unreliability of Steering Vectors in Language Models

### Problem

Steering vectors are a lightweight and effective method for controlling the behavior of large language models (LLMs) by adding a learned bias to their internal activations during inference. However, their efficacy is often inconsistent, exhibiting significant variation across different samples and proving unreliable for many target behaviors. This unreliability limits their practical application and suggests that the underlying linear approximation of desired behaviors might be insufficient. The core problem investigated is *why* this reliability differs across behaviors and *how* the training data influences it.

### Method

This Master's thesis investigates the geometric properties of latent representations and their relationship to steering vector reliability. The research employed the following methods:

1.  **Steering Method:** Used Contrastive Activation Addition (CAA) to train steering vectors on various "Model-Written Evaluations" (MWE) datasets, aiming to induce specific behaviors in a language model (e.g., Llama-2-7B).
2.  **Reliability Measurement:** Quantified steering reliability by assessing the consistency of steering effect sizes across different samples for various target behaviors.
3.  **Geometric Predictors:**
    *   **Directional Agreement:** Calculated the cosine similarity between individual training activation differences used to construct the steering vector.
    *   **Latent Separability:** Analyzed the separation of positive and negative activations in the model's latent space along the steering direction. This involved projecting activations onto:
        *   The "difference-of-means line" (the steering vector itself).
        *   The first component of a Linear Discriminant Analysis (LDA).
        *   The decision boundary direction of a logistic regression probe.
    *   **Discriminability Index:** Used this metric to quantify the separability of activations along these directions.
4.  **Training Data Impact:** Investigated how different prompt variations used during steering vector training influence the resulting steering vectors and their efficacy.

### Impact

The research offers key insights into the limitations of current steering vector methods, particularly regarding their reliability:

1.  **Geometric Predictors of Reliability:**
    *   **Predictive Power of Training Data Geometry:** Higher cosine similarity (directional agreement) among the individual activation differences used for training significantly predicts more reliable steering. This provides a direct diagnostic for predicting steering vector performance *before* deployment.
    *   **Separability as a Reliability Indicator:** Behavior datasets where positive and negative latent activations are better separated along the steering direction (e.g., the difference-of-means line, LDA component, logistic regression direction) lead to more reliably steerable behaviors. This highlights the importance of the inherent linear separability of a behavior in the latent space for linear steering methods.
2.  **Role of Linear Approximation:** The findings collectively suggest that steering vectors are unreliable when the target behavior's latent representation cannot be effectively approximated by a simple linear direction in the activation space. This empirically supports the hypothesis that the "Linear Representation Hypothesis" has limits in the context of steering.
3.  **Prompt Sensitivity:** Steering vectors trained on different prompt variations, while directionally distinct, can achieve similar performance and exhibit correlated efficacy across datasets. This implies that while the exact vector may vary, the underlying steerable latent dimension for a behavior might be robust across prompt phrasing.
4.  **Future Development:** The study provides a practical diagnostic tool for identifying and understanding steering unreliability. Crucially, it motivates the development of more advanced and robust steering methods that explicitly account for and leverage non-linear latent behavior representations, moving beyond the current limitations of purely linear approaches.