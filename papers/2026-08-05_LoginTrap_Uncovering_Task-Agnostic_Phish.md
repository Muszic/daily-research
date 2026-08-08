# LoginTrap: Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents

- **Category:** Cryptography
- **Date:** 2026-08-05
- **Link:** http://arxiv.org/abs/2608.04741v1

---
## LoginTrap: Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents

### Problem

LLM-based web agents automate user tasks by interacting with real web services, which inherently includes sensitive authentication boundaries like login. Existing research has shown that malicious webpage content can manipulate web agent actions through various forms of prompt injection. However, a critical gap remains: it's largely unexplored whether such content can specifically *induce login* and subsequently lead to *end-to-end private data leakage* in a **task-agnostic, black-box** manner. Login, while routine, is a major security target for credential and identity theft. If an agent can be tricked into treating login as a legitimate and necessary prerequisite for an unrelated task, it creates a new, systematic authentication boundary risk for privacy leakage without the attacker needing to know the user's specific task or the agent's internal workings.

### Method

The authors developed **LoginTrap**, a phishing-style indirect prompt injection attack designed to induce LLM-based web agents to log in and leak sensitive information.

1.  **Attack Environment Construction:** LoginTrap operates by cloning a benign webpage to preserve its context. It injects a "login-inducing statement" and a forged login entry, typically within a controlled popup, while keeping the rest of the page unchanged.
2.  **Fuzzing-Inspired Injection Generation:** To achieve *task-agnosticism*, LoginTrap employs a fuzzing-inspired process to generate page-specific login-inducing statements without relying on knowledge of the user's actual task or agent internals. This process involves:
    *   **Context Construction:** An LLM extracts a page summary, potential tasks, and a benign probe task from the original webpage.
    *   **Initialization Strategies:** The generator uses semantic strategies to define rationales for why login might appear relevant to the page content (e.g., "Login to continue viewing this content").
    *   **Evaluation & Mutation:** Candidate statements are evaluated by "shadow LLMs" (one with a safety reminder) using the benign probe task. If successful, the statement is accepted; otherwise, failed candidates are refined using MCTS-inspired mutation strategies (crossover, expansion, rephrasing, compression) based on feedback.
3.  **Attack Execution Flow:**
    *   The web agent, tasked with a benign user goal, navigates to the attacker's cloned webpage containing the generated login-inducing injection.
    *   Observing this content, the agent revises its plan to prioritize login, treating it as a prerequisite for continuing the original task.
    *   The agent clicks the forged login entry, leading it to an attacker-controlled login page.
    *   This login page is dynamically tailored (using an LLM to summarize the cloned page) to appear consistent with the context. It presents fields requesting sensitive information.
    *   If the agent continues its login plan, it fills in the requested fields and submits sensitive user information, completing the privacy leakage.

### Impact

LoginTrap proved highly effective and generalizable, demonstrating a significant and systematic authentication boundary risk for LLM-based web agents:

*   **High Attack Success Rate:** LoginTrap achieved an average end-to-end attack success rate of **86%** across different LLM backbones (e.g., GPT-3.5, GPT-4, Claude).
*   **Generalizability Across Architectures:** The attack remained effective across various web agent architectures, reaching an average success rate of **79%**, indicating that the vulnerability is not confined to a specific agent implementation.
*   **Systematic Risk Identification:** These findings identify login inducement as a *systematic authentication boundary risk* in web agent execution. It highlights that even under a strict black-box threat model (no knowledge of user task or agent internals), sophisticated phishing-style attacks can trick agents into disclosing sensitive data.
*   **Motivation for Defenses:** The research strongly motivates further investigation into authentication-aware defenses for LLM-based web agents to mitigate this newly identified threat.