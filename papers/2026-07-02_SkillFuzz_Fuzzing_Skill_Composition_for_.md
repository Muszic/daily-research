# SkillFuzz: Fuzzing Skill Composition for Implicit Intents Discovery in Open Skill Marketplaces

- **Category:** NLP
- **Date:** 2026-07-02
- **Link:** http://arxiv.org/abs/2607.02345v1

---
Here's a summary of the research paper "SkillFuzz: Fuzzing Skill Composition for Implicit Intents Discovery in Open Skill Marketplaces" in Markdown format:

### Problem

Open skill marketplaces allow users to combine community-contributed skills to build LLM-based agents. However, skills are typically audited in isolation. When multiple skills are co-activated, they can interact in unforeseen ways, reshaping the agent's belief state and redirecting it towards unintended objectives, which the paper terms **implicit intents**.

Detecting these implicit intents is challenging due to three main reasons:
1.  **Lack of Execution Environments:** Marketplace operators often cannot execute agent workflows in real deployment environments during admission, making run-time validation infeasible at scale.
2.  **Emergent Effects:** Compositional effects emerge within the LLM's belief state (i.e., in the natural language plan), making them invisible to static analysis of individual skill documents.
3.  **Exponential Search Space:** The space of possible skill co-activations grows exponentially with the number of skills in the marketplace, making exhaustive search intractable.

### Method

The authors formulate the implicit-intent discovery as a **fuzzing problem** over skill compositions. They propose **SKILLFUZZ**, an execution-free testing approach that leverages the "plan-then-act" paradigm of LLM agents.

SKILLFUZZ operates in two main steps:

1.  **Skill Contract Construction & Pruning:**
    *   **Contract Extraction:** For each skill, a structured "skill contract" is extracted (via an LLM) from its natural language instruction document. This contract captures properties like preconditions, postconditions, modifications, invariants, domain scope, and abstract actions, along with an extraction confidence score.
    *   **Semantic Embedding:** Each contract is embedded into a semantic space.
    *   **Candidate Pruning & Seed Prioritization:** The library is pruned to include only task-relevant skills. Initial test cases (seeds) are prioritized based on "conflict potential" (e.g., shared modification sets, mutually exclusive invariants) between skill contract pairs and skills with low extraction confidence.

2.  **Execution-Free Fuzzing via Differential Activation Search:**
    *   **Fuzzing Formulation:** SKILLFUZZ treats skill activations as test inputs and uses **plan drift** as a differential oracle. Plan drift measures the semantic deviation of an agent's plan (generated with co-activated skills) from a baseline plan (generated with no skills). This detects deviations in agent intent *before* any execution.
    *   **Search Strategy:** A **contract-guided Monte Carlo Tree Search (MCTS)** explores the exponential skill co-activation space under a fixed query budget.
    *   **Objective:** The search aims to maximize **Intent Coverage Quality (ICQ)**, a metric that combines the severity of plan drift with the novelty (semantic distinctness from previously found intents) of the discovered implicit intents.
    *   **Contract-Guided Mutation:** When selecting the next skill to add to a composition, SKILLFUZZ uses the semantic centroid of high-ICQ (i.e., severe and novel) activations to steer the MCTS towards regions of the contract semantic space where implicit intents are more likely to emerge.

### Impact

SKILLFUZZ demonstrates significant capabilities in identifying compositional risks in skill marketplaces:

*   **Discovery Scale:** Discovers over **1,000 distinct implicit intents** under a fixed query budget across representative skill-marketplace workloads.
*   **Real-World Validation (RQ2):** More than **80% of the highest-risk flagged compositions** (identified as having implicit intents at the planning level) were confirmed during execution-time validation, demonstrating that plan-level findings translate to real execution-layer risks.
*   **Efficiency (RQ3):** Substantially more high-severity implicit intents were identified by SKILLFUZZ compared to alternative search strategies, while exploring only a fraction of the pairwise interaction space.
*   **Generality (RQ1):** Implicit intents were found to generalize across all evaluated LLM-based planning agents (both open-weight and proprietary models), indicating that this is a general risk of skill composition rather than a model-specific artifact.
*   **Insights (RQ4):** The approach revealed recurring semantic patterns of implicit intents, offering valuable insights into common compositional vulnerabilities.