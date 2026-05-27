# MAIGO: Mitigating Lost-in-Conversation with History-Cleaned On-Policy Self-Distillation

- **Category:** NLP
- **Date:** 2026-05-26
- **Link:** http://arxiv.org/abs/2605.27186v1

---
```markdown
### Problem

Large Language Models (LLMs) often struggle with "Lost-in-Conversation" (LiC) scenarios, where task requirements unfold over multiple turns. While LLMs can solve tasks from a single, fully specified prompt (FULL view), their performance degrades significantly in a conversational (SHARDED) setting, even when the same information is eventually revealed. This degradation, known as the LiC gap, is partly attributed to **self-contamination**: intermediate assistant replies, which may contain premature assumptions or errors, become part of the later dialogue history, compounding deviations and biasing subsequent responses. Existing methods typically provide answer-level rewards or runtime checks but do not directly supervise or prevent this self-contamination at intermediate turns.

### Method

MAIGO (Mitigating Lost-in-Conversation with History-Cleaned On-Policy Self-Distillation) is an on-policy self-distillation method designed to reduce self-contamination without requiring verifier rewards, state labels, or inference-time scaffolding.

1.  **On-Policy Self-Distillation:** MAIGO trains the model on its own generated sharded rollouts (on-policy), meaning the student's own intermediate assistant replies (`_a_hat_t-1`) are part of the context for subsequent turns.
2.  **History-Cleaned Middle-Turn Supervision:** For intermediate turns (before the final answer), MAIGO constructs "history-cleaned references." This involves removing previous *assistant replies* from the conditioning context (`Cref_t,mid = (system_prompt, u1, ..., ut)`) while preserving the user-visible sharded prefix (all user turns up to the current point). This teaches the model to respond to the current conversational state without inheriting its own earlier mistakes. A reliability weight further downweights middle-turn samples that show significant discrepancy with the clean reference.
3.  **Answer-Turn Recovery Supervision:** For the final answer turn, MAIGO distills from "paired full-view references." This reference context (`Cref_T,ans = (system_prompt, u1, ..., uT, canonical_full_spec(x))`) conditions on the *completed user-side dialogue* (all user turns) and appends a canonical reserialization of the *full task specification* (`x`), importantly, *previous student replies are removed before this serialization*. This aligns the final answer with the fully specified task, encouraging solution recovery.
4.  **FULL-view Preservation:** A separate branch uses an Exponential Moving Average (EMA) self-anchor on the FULL-view task to prevent performance degradation on single-turn capabilities.

### Impact

Evaluated on Qwen2.5-7B-Instruct across Math, Actions, Database, and Code tasks under the LiC paired-view protocol:

*   **SHARDED Accuracy:** MAIGO significantly improved SHARDED accuracy from 52.8% to 66.1%.
*   **SHARDED/FULL Ratio:** The SHARDED-to-FULL accuracy ratio increased from 66.5% to 84.1%.
*   **FULL Accuracy Preservation:** FULL accuracy was preserved, remaining within 2.3 points of the base model.

These results demonstrate that self-contamination is a trainable component of the LiC gap, and MAIGO effectively mitigates it, leading to substantially more robust multi-turn task solving without compromising single-turn capabilities.
```