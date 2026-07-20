# NexForge: Scaling Agent Capabilities through Requirement-Driven Task Synthesis for LLMs

- **Category:** Software Engineering
- **Date:** 2026-07-15
- **Link:** http://arxiv.org/abs/2607.14186v2

---
## NEXFORGE: Scaling Agent Capabilities through Requirement-Driven Task Synthesis for LLMs

### Problem

Scaling LLM agent capabilities through post-training is severely hampered by limitations in current **substrate-bound task synthesis** methods. These methods generate tasks from predefined, fixed tools, repositories, or skill graphs, leading to three fundamental scaling limitations:

1.  **Input-bounded scale:** The diversity and volume of generated tasks are constrained by the size and scope of the underlying substrate. Expanding coverage requires costly manual curation and engineering of new substrates.
2.  **High transfer cost:** Each new domain or capability typically demands bespoke infrastructure and pipelines (e.g., skill libraries for terminal tasks, repository harnesses for software engineering), making it expensive and time-consuming to transfer the approach to new areas.
3.  **Substrate-biased distributions:** The resulting task distributions often reflect the biases of the substrate (e.g., over-representing implementation or debugging tasks in repository-based methods) rather than accurately reflecting real-world user demand or broader task types like configuration, data processing, or system operation.

This bottleneck results in a scarcity of high-quality, diverse training data that includes task descriptions, grounded materials, executable environments, and long-horizon interaction trajectories, hindering the development of truly capable LLM agents.

### Method

NexForge proposes a novel **requirement-driven framework** that decouples task generation from predefined substrates. It synthesizes diverse, executable agent tasks and expert trajectories for Supervised Fine-Tuning (SFT) directly from high-level capability requirements. The framework operates in three main stages:

1.  **Research-Based Demand Discovery:**
    *   Given a high-level capability requirement (e.g., "terminal operations" or "office work"), a web-enabled research agent investigates real-world demand.
    *   This process profiles the domain into a weighted **task demand profile** (defining the intended distribution over task types, deliverables, runtime environments, etc.) and a diverse **scenario reservoir** (containing concrete working contexts like organizational roles, workflows, or software systems).

2.  **Distribution-Aware Task Compilation:**
    *   The system composes the discovered task demands and scenarios into concrete **task directives**.
    *   For each scenario, it samples compatible task-form dimensions (e.g., task type, expected deliverable, source strategy, runtime environment) according to the profile weights and any batch-level constraints.
    *   A compatibility filter ensures internal consistency, producing a directive that specifies *what* the agent should practice, aligned with real-world distributions.

3.  **Agent Post-Training Trajectory Generation:**
    *   Each task directive is instantiated into a complete, executable workspace. This involves:
        *   **Material Mining:** A research agent collects or specifies resources (repositories, documents, datasets, config files).
        *   **Blueprint Planning:** A planning agent creates a structured blueprint for the task, including objectives, materials, workspace organization, and dependencies.
        *   **Workspace Generation & Validation:** A coding agent constructs an unprivileged Docker environment, adapting repositories, generating local artifacts, and installing dependencies. Automated checks verify completeness and consistency.
    *   A teacher model (e.g., GPT-5.5) interacts with the executable workspace using available tools, producing detailed interaction trajectories (model responses, tool calls, observations, failures, recovery behaviors).
    *   These interactions are then distilled into standardized training trajectories through task-independent cleaning, suitable for agent post-training without requiring manual reference answers or task-specific success verifiers.

Crucially, NexForge's architecture allows the *same pipeline* to scale across substantially different capability domains without requiring new domain-specific infrastructure.

### Impact

NexForge significantly advances LLM agent capabilities by providing a scalable, generalized method for synthesizing high-quality, diverse training data.

1.  **Domain Generalization & Efficiency:**
    *   The same NexForge pipeline successfully generated **3,600 terminal tasks** and **2,000 office tasks** from scratch *without any domain-specific engineering*, demonstrating its ability to span disparate domains.
    *   This addresses the high transfer cost of previous substrate-bound methods.

2.  **Significant Performance Improvements:**
    *   Training with NexForge-synthesized data dramatically improved a base LLM:
        *   Qwen3.5-35B-A3B Base's performance on **Terminal-Bench 2.0** increased from 22.5% to **52.0%** (using 3.6K terminal tasks).
        *   The same model's Elo score on **GDPval** (for office tasks) improved from 813 to **1338** (using 2K office tasks).

3.  **Scalability and State-of-the-Art Results:**
    *   Scaling up the terminal task synthesis to **43.2K tasks** further boosted performance to **58.4%** on Terminal-Bench 2.0, **surpassing Claude Opus 4.6**.
    *   NexForge-synthesized trajectories were used to supervise the SFT of **Nex-N2**, a family of open agent models. Nex-N2 achieved **75.3% on Terminal-Bench 2.1** and **1585 Elo on GDPval**, establishing **state-of-the-art open-source performance** and outperforming several frontier proprietary systems.
    *   The Nex-N2 models are publicly available, contributing to the open-source agent community.

NexForge demonstrates that by focusing on requirement-driven task synthesis, it's possible to generate a vast volume of diverse, executable training data, decoupling the *what* from the *how*, leading to more capable and generalized LLM agents.