# Statistical inference with belief functions: A survey

- **Category:** Artificial Intelligence
- **Date:** 2026-05-08
- **Link:** http://arxiv.org/abs/2605.07908v1

---
# Statistical inference with belief functions: A survey
Fabio Cuzzolin

## Problem
Traditional statistical inference (e.g., estimating parameters, quantifying uncertainty) often relies on precise probability distributions and, in Bayesian contexts, requires specifying a prior distribution. This becomes problematic in situations characterized by:
*   **Lack of data:** Making it impractical to learn precise probability distributions.
*   **Epistemic uncertainty/ignorance:** Where data is imprecise, qualitative, or knowledge is partial, preventing the assignment of exact probabilities.

The core challenge is how to perform statistical inference and quantify uncertainty about model parameters (e.g., θ in `f(x|θ)`) from observed data (`x`) using belief functions, without necessarily having to specify a prior distribution, thereby leveraging their ability to represent various forms of uncertainty beyond classical additive probabilities.

## Method
This paper surveys and categorizes various approaches to performing statistical inference using belief functions, classifying them primarily by their relationship to established probabilistic inference paradigms:

1.  **Likelihood-based Inference:**
    *   **Traditional Likelihood:** Constructs a belief function (typically a consonant one, whose contour function is proportional to the classical likelihood) from the maximum likelihood estimate.
    *   **Belief Likelihood Function:** Proposes defining a "belief likelihood" directly as a family of belief functions parameterized by θ, allowing for likelihood computations of set-valued observations and aligning with the random set philosophy.

2.  **(Robust) Bayesian Inference:**
    *   Views a belief function as defining a "credal set" (a set of consistent probability distributions) that represents an imprecise prior.
    *   Updates each probability in this credal set using Bayes' rule, thereby obtaining lower and upper bounds on posterior probabilities without committing to a single, precise prior.

3.  **Fiducial Inference:**
    *   **Dempster's Auxiliary Variable:** Supplements a parametric statistical model with an "a-equation" that relates observed data, the parameter, and an unobservable "pivotal" auxiliary variable with a known distribution. This setup then induces a belief function on the parameter space.
    *   **Inferential Models (Weak & Elastic Belief):** Extends Dempster's fiducial idea by introducing "predictive random sets" to account for uncertainty in the auxiliary variable itself, resulting in less committed belief functions.
    *   **Statistical Inference with Hints:** Uses "functional models" where observations generate "hints" (structures combining an event, conditioned probabilities, and possible parameter values), which can then be combined using Dempster's rule to update beliefs about parameters.

4.  **Frequentist Inference:**
    *   **Theory of Lower Probability:** Formulates a frequentist theory for estimating lower probabilities from observed frequencies, demonstrating their convergence properties analogous to the law of large numbers.
    *   **Dempster's (p,q,r) Interpretation:** Associates any assertion within the belief framework with a triple representing the probability "for" the assertion, "against" it, and "don't know."
    *   **From Confidence Intervals:** Interprets confidence intervals as credal sets of feasible probability intervals, from which lower and upper probabilities for events can be derived.
    *   **Theory of Confidence Structures:** Constructs observation-conditional random sets (which induce belief functions) from statistical models, ensuring that the resulting belief values are commensurate with Neyman-Pearson confidence levels.

## Impact
*   **Strengths of Belief Functions:** The framework provides a powerful means to characterize and quantify uncertainty, particularly under partial knowledge or ignorance, without relying on the strong assumptions of classical probability (e.g., precise priors, full additivity). This is crucial when simple parametric models are unavailable.
*   **Limitations of Specific Approaches:**
    *   **Wasserman's (Robust Bayesian):** While mathematically sound, it is general to credal sets and not specifically tailored for belief functions, often being incompatible with Dempster's combination rule, which has limited its widespread adoption within the full Dempster-Shafer theory.
    *   **Dempster's Fiducial & Hints:** These approaches, while avoiding the need for prior distributions, often involve complex calculations (requiring Monte-Carlo simulations) and depend on auxiliary variables or "a-equations" that are unobservable, not uniquely determined, or lack clear justification.
    *   **Weak/Elastic Belief & Confidence Structures:** These methods introduce additional, complex design choices (like predictive random sets or observation-conditional random sets) that can lead to "model overfit" and lack direct links to observables.
    *   **Most Frequentist Methods:** Many frequentist approaches tend to produce *lower and upper probabilities* (a broader concept) rather than *random sets* (the fundamental representation of belief functions), thus not fully leveraging the specific structure and expressive power of belief theory.
    *   **Traditional Likelihood-based:** This approach primarily yields *consonant belief functions* (which are equivalent to possibility distributions), thereby not exploiting the full expressive power of general belief functions. It also faces issues regarding consistency with the likelihood principle due to the ordering of operations.
*   **Promising Directions:**
    *   **Belief Likelihood Function (Cuzzolin):** This approach is seen as promising because it directly generates full belief functions without relying on extra hidden variables or structures, providing a natural setting for set-valued observations.
    *   **Extending Hypothesis Testing (Dempster's dull hypothesis):** Offers an interesting avenue for generalizing statistical significance testing within the belief framework, accounting for "don't know" states.
    *   **Confidence Structure Theory:** Despite its design choices, it shows potential for a fundamental reconciliation with frequentist statistics, and further investigation into its extension (e.g., to Bayesian credible intervals) is warranted.