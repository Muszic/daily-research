# Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code Repair

- **Category:** NLP
- **Date:** 2026-07-27
- **Link:** http://arxiv.org/abs/2607.24604v1

---
This research paper investigates the reliability of generate-test-revise loops in coding agents, highlighting that repetition alone does not guarantee a correct and stable solution. It studies the gap between discovering a correct patch and reliably retaining, verifying, and submitting it.

## Problem

Current generate-test-revise loops in coding agents lack inherent reliability guarantees, leading to:
*   **Regressions from Correctness:** Correct code patches are often lost in subsequent revisions. A sealed study showed current correctness falling from 82.0% after one revision to 67.3% after two, even as the "ever-correct" rate increased. This indicates correctness is not an absorbing state.
*   **Harm from Stale Evidence:** Using diagnostic feedback (traces or binary outcomes) that are not aligned with the current code state (stale evidence) can significantly harm already correct programs. In a 14B model replication, stale traces led to 34/135 correct starts regressing, compared to 4/135 with current traces.
*   **Correlated Verifier Errors:** Even strong verifiers (low risk) may not be independent, meaning their errors can be correlated across model families. This positive dependence can inflate the ensemble false acceptance rate, undermining the reliability benefits of using multiple verifiers.
*   **Lack of Formal Guarantees:** Existing agentic systems primarily focus on end-task success and cost, lacking formal mechanisms for admission, preservation, grounded certification, and risk-aware stopping.

## Method

The paper employs a multi-faceted experimental approach and proposes a novel solution:

1.  **Trajectory Study:**
    *   **Design:** 900 three-revision trajectories across 30 HumanEval repair tasks, using Qwen2.5-7B-Instruct.
    *   **Variables:** Six evidence conditions (current binary/trace, stale binary/trace, unavailable, flipped binary).
    *   **Evaluation:** Judged by self-declaration, Qwen2.5-7B, Qwen2.5-14B, DeepSeek-Coder-6.7B, and an executable challenge verifier.
    *   **Purpose:** To observe correctness transitions (RQ1) and verifier quality/dependence (RQ3).

2.  **Common-State Intervention:**
    *   **Design:** 2,430 single-step branches from identical frozen wrong and correct code states across 27 tasks, for Qwen2.5-7B and Qwen2.5-14B coders.
    *   **Variables:** Nine state-evidence branches (e.g., current binary/trace, stale wrong trace, unavailable, matched control).
    *   **Purpose:** To isolate the impact of evidence content and state alignment on repair and continuation harm (RQ2), removing post-treatment risk-set bias.

3.  **Prospective Paired Online Commit-Admission Comparison:**
    *   **Design:** 540 rollouts (27 tasks, 5 seeds) comparing a baseline (commits any parseable patch) with a guarded arm.
    *   **Guarded Arm:** Employs state-bound evidence, admission only after a challenge gate, and retention of last-known-good checkpoints.
    *   **Purpose:** To test how enforcing the proposed contract changes subsequent model behavior.

4.  **Repository-Agent Factorials:**
    *   **Design:** Multiple factorials (288-rollout, 576-rollout) over 24 real-world Python bugs, using various LLM coders (Qwen2.5-14B, Qwen2.5-Coder-32B, Qwen3-Coder-Next, Devstral Small 2).
    *   **Variables:** Crossed current vs. stale diagnostic evidence, contract OFF vs. ON, and various component/depth factorials.
    *   **Purpose:** To test the bundled system consequences of the contract in a realistic Git worktree (RQ5) and probe stack generality.

5.  **Proposed Solution:**
    *   **Evidence-Bound Typed Loop Contract:** The paper derives a formal contract that separates admission, preservation, grounded certification, competence, and liveness.
    *   **Reference Implementation:** Instantiates a mechanically enforceable subset of this contract as an admission layer. This implementation binds verifier evidence to exact code states, preserves verified checkpoints, and emits auditable admission receipts.

## Impact

The paper makes significant contributions to understanding and mitigating reliability issues in agentic code repair:

*   **Empirical Demonstration of Reliability Gaps:** It definitively shows that correctness is not an absorbing state in iterative repair loops and that stale evidence can actively harm correct code.
*   **Quantification of Evidence Effects:** Current execution traces are shown to aid repair, while stale traces significantly increase the rate of regressions, especially in stronger models (14B model: +22.2-point increase in harm from stale traces compared to current traces, p=0.0337).
*   **Verifier Dependence Uncovered:** It highlights that verifier quality (low risk) does not imply independence, as evidenced by significant positive error dependence between Qwen-7B and Qwen-14B verifiers (𝜙=0.641 at 70% coverage).
*   **Reliability Decomposition Framework:** Provides a novel framework that jointly reports correctness discovery and retention, wrong-to-correct and correct-to-wrong transitions, verifier risk–coverage, conditional false-accept dependence, and sound completion.
*   **Executable Contract and Reference Implementation:** The core impact is the derivation and practical instantiation of an "evidence-bound typed loop contract." This implementation acts as an executable specification and conformance artifact, demonstrating how to enforce crucial reliability safeguards:
    *   **State-bound evidence:** Ensures feedback is always tied to the exact code it describes.
    *   **Checkpoint preservation:** Prevents loss of verified correct states.
    *   **Fresh completion certification:** Requires robust verification before acceptance.
    *   **Risk-aware stopping:** Empowers orchestrators to make informed stopping decisions based on verified evidence.
*   **Improved Completion Reliability:** The trajectory study demonstrated that an external "challenge gate" (a key component of the contract) can drastically reduce false completions (e.g., from 29.5% risk to 0% observed risk in the sample) while maintaining high sound completion rates, far outperforming self-only stopping.
*   **Foundational for Agent Orchestration:** While not claiming to improve the agent's *repair competence* directly, the contract provides a robust, auditable framework for orchestrators to manage and verify the reliability of code generated by LLM agents, ensuring that correct patches are retained and submitted safely.