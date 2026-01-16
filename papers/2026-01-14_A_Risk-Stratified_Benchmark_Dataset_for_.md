# A Risk-Stratified Benchmark Dataset for Bad Randomness (SWC-120) Vulnerabilities in Ethereum Smart Contracts

- **Category:** Cryptography
- **Date:** 2026-01-14
- **Link:** http://arxiv.org/abs/2601.09836v1

---
Here's a summary of the research paper in Markdown format:

```markdown
# A Risk-Stratified Benchmark Dataset for Bad Randomness (SWC-120) Vulnerabilities in Ethereum Smart Contracts

## Problem

Ethereum smart contracts frequently use predictable block attributes (e.g., `block.timestamp`, `blockhash`) for "random" number generation in applications like lotteries and games. These values are easily manipulated by miners or predictable via front-running attacks, leading to the "Bad Randomness" (SWC-120) vulnerability and real-world exploits (e.g., SmartBillions).

Current vulnerability detection tools suffer from high false positive and false negative rates because they:
1.  **Detect only simple patterns** (e.g., direct modulo operations), missing complex cases involving `keccak256` hashing, type casting, and indirect variable usage.
2.  **Operate at a contract level**, failing to verify whether protective modifiers (e.g., `onlyOwner`) actually guard the *specific functions* containing the vulnerable code, leading to mislabeled "protected" contracts that are, in fact, exploitable.

A major obstacle to improving these tools is the severe **lack of large, accurately labeled, and granularly classified benchmark datasets**. Existing datasets are either too small (2-384 contracts), lack function-level validation, or do not provide risk stratification, hindering the development of robust detection mechanisms.

## Method

The authors developed a five-phase methodology to construct a large, accurately labeled, and risk-stratified benchmark dataset of Ethereum smart contracts for SWC-120 vulnerabilities:

1.  **Data Collection and Keyword Filtering:**
    *   Started with 47,398 contracts from the SmartBugs-Wild dataset.
    *   Filtered to 17,466 contracts containing at least one block attribute keyword (`block.timestamp`, `blockhash`, `block.difficulty`, etc.) to broadly identify potential candidates, avoiding domain-specific limitations of prior work.

2.  **Vulnerability Pattern Labeling:**
    *   Developed **58 regular expressions** organized into 9 semantic groups to capture both simple and complex bad randomness patterns (e.g., direct modulo, `keccak256` hashing, type casting, indirect variable usage).
    *   Contracts using Chainlink VRF were immediately labeled SAFE. 1,903 contracts matched one or more patterns.

3.  **Risk-Level Classification (Initial):**
    *   Initially classified contracts into four risk levels (SAFE, LOW RISK, MEDIUM RISK, HIGH RISK) based on detected mitigation patterns and exploitability by different attacker types (external, miner, owner).
    *   This initial classification revealed a high proportion (61.3%) of contracts marked as LOW RISK (partially protected by `onlyOwner` or similar).

4.  **Function-Level Validation (Core Novelty):**
    *   **Motivation:** To address the critical flaw of contract-level analysis, this phase explicitly verifies if protective modifiers are applied *directly to the functions* containing bad randomness. For `internal`/`private` functions, it traces call chains to public callers.
    *   **Impact:** This validation revealed significant misclassification: **49% of contracts initially classified as LOW RISK were reclassified as exploitable** (FALSE POSITIVE) because their mitigation was not applied to the vulnerable function. An additional 48.7% of initially validated LOW RISK contracts were reclassified after call-chain analysis. This process reduced the LOW RISK category from 1,167 to 172 contracts.

5.  **Context-Aware Refinement:**
    *   Analyzed contracts where patterns appeared outside function bodies (e.g., in storage variables) to distinguish legitimate uses of block attributes (e.g., mining tokens for proof-of-work, time tracking) from actual bad randomness vulnerabilities (e.g., lotteries, gambling). This step helped reduce false positives.

## Impact

The research provides significant advancements in smart contract security and vulnerability detection:

1.  **Largest & Most Granular SWC-120 Dataset:**
    *   **1,752 validated vulnerable contracts**, 51x larger than the previous largest (RNVulDet: 34 contracts).
    *   The first dataset to offer **function-level validation** and **four-level risk stratification** (SAFE, LOW RISK, MEDIUM RISK, HIGH RISK) based on attacker exploitability (external, miner, owner).
    *   Includes 6 SAFE, 37 MEDIUM RISK, 172 LOW RISK, and 1,543 HIGH RISK contracts.

2.  **Novel and Accurate Labeling Methodology:**
    *   Introduces a **pivotal function-level mitigation validation technique** that significantly improves labeling accuracy by confirming whether protective mechanisms genuinely guard vulnerable code, exposing substantial misclassifications by prior methods. This methodology can serve as a template for other vulnerability categories.
    *   **Context-aware analysis** effectively reduces false positives by distinguishing between legitimate and vulnerable uses of block attributes.

3.  **Revealed Significant Gaps in Existing Tools:**
    *   Empirical evaluation demonstrated that widely used tools like **Slither and Mythril failed to detect any of the vulnerable contracts** in the authors' sample. This highlights their limitations in handling complex randomness patterns (beyond simple modulo operations, including `keccak256` hashing and indirect variable usage).

4.  **Public Availability:**
    *   The dataset and validation scripts are publicly available on GitHub, providing a crucial resource for future research, development, and training of more robust smart contract security tools.
```