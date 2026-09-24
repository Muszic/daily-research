# FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents

- **Category:** Software Engineering
- **Date:** 2026-09-22
- **Link:** http://arxiv.org/abs/2609.26048v1

---
Here's a summary of the research paper using the Problem, Method, and Impact structure:

## Problem

Language Model (LLM) agents frequently demonstrate the ability to find working solutions but struggle with consistently delivering them. This leads to common "procedural losses" where the agent fails at the execution or delivery stage, even after successfully producing the core solution (e.g., a server exiting with the agent's shell, corrupting a database before copying it, or altering output with a formatter). This issue manifests as poor reliability and repeatability, with a significant number of tasks (16-19 per model tier on Terminal-Bench 2.1) failing in exactly one of two identical attempts. Existing remedies often compare against no intervention, failing to distinguish the effect of a targeted rule's content from the mere act of interrupting the agent.

## Method

The authors propose **Failure-Informed Runtime Engineering (FIRE)**, implementing "runtime policies" to address these delivery failures.

1.  **Policy Derivation:** Policies are systematically derived from analyzing observed procedural losses in failed agent trajectories (e.g., a 1/2 success rate or specific 0/2 failures indicating an omission). This ensures policies target concrete, repeatable failure patterns.
2.  **Policy Structure:** A runtime policy is a tuple `(E, G, A, R, S)`:
    *   `E` (Eligibility Predicate): Matches the task description to determine if the policy is in scope.
    *   `G` (Runtime Predicate): Watches the agent's action history and state at specific harness events (e.g., before tool calls, at stop attempts) that preceded observed failures.
    *   `A` (Intervention): Either injects a targeted natural-language instruction into the agent's context or denies a proposed tool call.
    *   `R` (Release Condition) and `S` (Nudge Limit/Tracking Rules): Prevent loops and manage policy state.
3.  **Intervention Mechanism:** Policies are applied by an agent harness *without modifying model weights or the user prompt*. They intervene at critical moments *before* a known failure point. The instructions guide the agent to perform specific corrective behaviors (e.g., launching a server detached, copying a database before modifying it).
4.  **Experimental Design (Attribution):** A randomized five-arm panel experiment was conducted on a subset of 30 tasks (14 eligible for policies, 16 silent tasks) using the Terra model tier. This design aimed to isolate the impact of policy *content* from mere *interruption*:
    *   **Real Policy:** The proposed targeted interventions.
    *   **Triggered Sham:** Intervenes at the same timing and events as real policies but provides generic review text.
    *   **Always Verify:** Adds a generic stop-time instruction to verify artifacts on every task.
    *   **Reconsider:** Adds a generic request for the agent to reconsider its solution.
    *   **Silent Tasks:** Control tasks where policies should not fire, to check for off-target effects.
5.  **Evaluation:** Performance is measured on the 87-task Terminal-Bench 2.1 suite using two attempts per task. Key metrics include `pass@1` (mean attempt success), `pass@2` (best of two attempts), and critically, `pass^2` (succeeding on *both* attempts, indicating repeated delivery and reliability).

## Impact

The FIRE framework demonstrates a significant and attributable improvement in the reliability and repeatability of LLM agents:

1.  **Attribution of Gain:** The randomized five-arm panel conclusively shows that the targeted *content* of the policies, not merely the act of interruption or generic self-correction, drives the observed gains. Real policies achieved +25.0 points over a timing-matched sham (95% CI [7.1, 46.4], p=0.061) and +21.4 points over baseline (p=0.032) on eligible tasks, while generic verification and reconsideration showed no comparable improvement. Policies also correctly exhibited targeted intervention, never firing on silent tasks.
2.  **Mechanism Confirmed:** A funnel analysis revealed that while the problematic runtime state arises equally often across all arms, only the real policy text reliably produces the intended corrective behavior (22 of 24 coded attempts vs. 11–14 elsewhere). This confirms policies specifically guide agents to overcome procedural failures. The corrected procedure, while necessary, is not always sufficient if a fundamental capability gap exists.
3.  **Enhanced Reliability (Repeated Success):** Across the full 87-task Terminal-Bench 2.1 suite, policies substantially increase `pass^2` (succeeding on both attempts), which is the metric for repeated delivery and reliability, in all three GPT-5.6 tiers:
    *   Luna: 50.6% → 54.0% (+3.4 points)
    *   Terra: 55.2% → 60.9% (+5.7 points)
    *   Sol: 64.4% → 73.6% (+9.2 points)
    Notably, for Sol, `pass^2` increased by 9.2 points, while `pass@2` (best of two) only increased by 1.2 points, solidifying the claim that policies convert already-reachable solutions into dependable, repeatable deliveries.
4.  **Model-Tier Leverage & Cost-Effectiveness:** Policies enable a mid-tier model (Terra) to achieve performance comparable to a higher-tier, more expensive model (Sol). Policy-guided Terra reached 71.4% success on its 14 eligible tasks, outperforming unassisted Sol (64.3%) at approximately half the cost. This highlights how system-level engineering around LLMs can unlock dependability and reduce operational expenses.
5.  **Practical Reliability Layer:** FIRE introduces a practical, non-intrusive reliability layer that makes existing agent capabilities substantially more repeatable and dependable without requiring model retraining or changes to user prompts.