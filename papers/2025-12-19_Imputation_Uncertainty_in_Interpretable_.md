# Imputation Uncertainty in Interpretable Machine Learning Methods

- **Category:** Machine Learning
- **Published:** 2025-12-19
- **Source:** [Original ArXiv Link](http://arxiv.org/abs/2512.17689v1)

---

## 🧐 Problem

Real-world datasets frequently suffer from missing values, which can significantly hinder the ability to reliably interpret machine learning models using Interpretable Machine Learning (IML) methods. While previous research has acknowledged that different imputation strategies can introduce *bias* into IML explanations (e.g., altering Shapley values or feature importance), it has largely ignored the *additional imputation uncertainty* introduced by the missing data handling process itself.

This oversight means that the variance and confidence intervals (CIs) of IML explanations are not adequately accounted for, especially when using single imputation methods. Consequently, interpretations may appear misleadingly precise, leading to an underestimation of the true uncertainty and potentially flawed conclusions about model behavior and feature importance.

## 🛠️ Method

This paper extends the concept of "learner uncertainty" in IML by explicitly incorporating "imputation uncertainty" to provide more reliable confidence intervals for explanations. The methodology involves a comprehensive simulation study and a real-world data example:

1.  **IML Methods Investigated:** The study focuses on three prominent global IML methods: Permutation Feature Importance (PFI), Partial Dependence (PD) plots, and global Shapley values (SHAP).
2.  **Imputation Strategies Compared:**
    *   **Single Imputation (SI):** Mean Imputation and MissForest.
    *   **Multiple Imputation (MI):** Multivariate Imputation by Chained Equations (MICE) with Predictive Mean Matching (MICE PMM) and Random Forests (MICE RF).
3.  **Experimental Setup:**
    *   **Data Generation:** Synthetic datasets are generated from both linear and non-linear Data-Generating Processes (DGPs).
    *   **Missingness Simulation:** Missing values are introduced according to Missing Completely At Random (MCAR), Missing At Random (MAR), and Missing Not At Random (MNAR) patterns, with proportions ranging from 10% to 40%.
    *   **Model Training:** Linear models and XGBoost models are trained on the (imputed) datasets.
    *   **Uncertainty Quantification:** The study employs resampling techniques (bootstrap and subsampling with 20 refits) to estimate "learner uncertainty." For multiple imputation, a "MI Boot" approach is used, where resampling is applied to *each* imputed dataset, and results are pooled using "Rubin's rules" to correctly combine within-imputation and between-imputation variance. Adjusted variance estimators are used to improve accuracy.
4.  **Evaluation Metrics:** The performance of different imputation methods is assessed based on:
    *   Confidence Interval (CI) coverage probability (against a nominal 0.95).
    *   Average CI width.
    *   Bias of the IML estimates.
5.  **Real Data Example:** A real-world wine dataset with simulated missingness is used to illustrate the practical implications of different imputation methods on interpretation.

## 📊 Impact

The study delivers critical insights into the reliable interpretation of machine learning models in the presence of missing data:

*   **Underestimation of Uncertainty by Single Imputation:** The research conclusively shows that single imputation methods (Mean Imputation, MissForest) consistently lead to a significant *underestimation of variance* for IML explanations. This results in confidence interval coverage probabilities far below the nominal level and misleadingly narrow confidence intervals, suggesting a false sense of precision in the interpretations. Mean imputation, in particular, exhibits poor coverage and can introduce substantial bias (e.g., underestimating important feature effects).
*   **Superiority of Multiple Imputation:** Multiple imputation methods (MICE PMM, MICE RF) are shown to drastically improve variance estimation and achieve CI coverage probabilities much closer to the nominal rate. By properly accounting for imputation uncertainty and pooling results using Rubin's rules, these methods provide more accurate and robust confidence intervals, reflecting the true uncertainty in IML explanations.
*   **Improved Bias and Realistic CI Widths:** While single imputation often produces smaller (and deceptively precise) CI widths, multiple imputation methods yield wider, more realistic confidence intervals that appropriately capture the combined uncertainty from model fitting and imputation. Multiple imputation also generally maintains lower bias for IML explanations compared to single imputation.
*   **Critical Recommendation for Practice:** The findings underscore that when working with missing data, it is crucial to employ **multiple imputation methods** to obtain reliable confidence intervals for IML explanations (e.g., PFI, PD, Shapley values). Failing to do so can lead to overconfidence in interpretations and potentially erroneous conclusions, especially in high-stakes domains where robust and transparent explanations are essential.
