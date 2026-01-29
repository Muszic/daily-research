# Whitespaces Don't Lie: Feature-Driven and Embedding-Based Approaches for Detecting Machine-Generated Code

- **Category:** Software Engineering
- **Date:** 2026-01-27
- **Link:** http://arxiv.org/abs/2601.19264v1

---
## Whitespaces Don’t Lie: Feature-Driven and Embedding-Based Approaches for Detecting Machine-Generated Code

### Problem

The widespread availability of Large Language Models (LLMs) that can generate high-quality source code from natural language prompts poses significant risks to academic integrity, authorship attribution, and responsible AI use. There is an urgent need for robust and transparent methods to distinguish human-written code from machine-generated code. Current approaches often fall into two categories: lightweight, interpretable stylometric/structural feature-based detectors, and resource-intensive embedding-based classifiers. The central challenge investigated is to systematically compare these two complementary paradigms to understand their trade-offs in terms of accuracy, interpretability, efficiency, and robustness, providing practical guidance for real-world deployment.

### Method

The study adopts a comparative framework, evaluating two distinct detection pipelines on a large-scale benchmark dataset (600k code samples of human and AI-generated Python code, with a 100k held-out test set).

1.  **Feature-Based Approach:**
    *   **Feature Extraction:** Handcrafted metrics are derived from code snippets, categorized into:
        *   **Surface Statistics:** Number of lines, characters, average line length, blank-line/comment ratios.
        *   **Identifier Stylometry:** Counts, average length, snake-/camel-case ratios, token entropy, uniqueness.
        *   **Structural Proxies:** Estimated AST depth, counts of loops, conditionals, imports, comprehensions, and cyclomatic complexity.
    *   **Classifiers:** A range of supervised models were trained on these features, including Logistic Regression, SVM (RBF), Multi-Layer Perceptron (MLP), Random Forest (RF), Histogram-based Gradient Boosting (HGB), and ExtraTrees (ET).

2.  **Embedding-Based Approach:**
    *   **Embedding Generation:** Code snippets are encoded using the frozen `microsoft/codebert-base` transformer model, producing 768-dimensional semantic embeddings.
    *   **Classifiers:** The same set of supervised classifiers as the feature-based approach are then trained on these embeddings.

**Evaluation:** Models were selected based on validation performance (PR-AUC, ROC-AUC) and a decision threshold was calibrated to maximize the F1-score. Final evaluation on the unseen test set used PR-AUC, ROC-AUC, F1-score, Accuracy, Precision, and Recall.

### Impact

The research demonstrates that both feature-based and embedding-based approaches are highly effective for detecting machine-generated code, achieving strong performance metrics but with complementary strengths:

*   **High Accuracy for Both:** Both pipelines achieved remarkably high performance, with the best feature-based model (Random Forest) obtaining an ROC-AUC of 0.995, PR-AUC of 0.995, and F1-score of 0.971. The best embedding-based model (Logistic Regression on CodeBERT embeddings) achieved an ROC-AUC of 0.994, PR-AUC of 0.994, and F1-score of 0.965.
*   **Feature-Based Strengths (Interpretability & Recall):**
    *   Feature-based models (especially ensemble methods) showed slightly stronger F1-scores and recall, making them effective for broad coverage.
    *   **Key Discriminative Cues:** Analysis of feature importance revealed that stylistic and structural cues, particularly whitespace usage (average leading spaces/tabs, blank-line ratio) and AST depth, are highly discriminative signals. This highlights the "whitespaces don't lie" aspect, indicating systematic patterns in AI-generated code.
    *   These models are lightweight and interpretable, which is crucial for stakeholders needing to understand *why* a piece of code was flagged.
*   **Embedding-Based Strengths (Precision & Robustness):**
    *   Embedding-based models, while marginally lower in F1-score and recall, achieved slightly higher precision, reducing false positives where human-written code might be incorrectly flagged.
    *   They capture deeper semantic and syntactic patterns, demonstrating promising robustness under distribution shifts, making them more generalizable to unseen generators or coding styles.
*   **Complementary Approaches:** The findings suggest that these two approaches are complementary rather than competing. Feature-based methods offer efficiency and interpretability for large-scale screening, while embedding-based methods provide enhanced precision and robustness for critical reliability.
*   **Future Directions:** The study advocates for hybrid approaches that combine both interpretable surface features and deep semantic embeddings to create more reliable and robust detectors for real-world deployment. This work provides critical guidance for educational institutions and industry in maintaining academic integrity, ensuring fair evaluation, and supporting responsible AI adoption.