# Words Speak Louder Than Code: Investigating Cognitive Heuristics in LLM-Based Code Vulnerability Detection

- **Category:** Cryptography
- **Date:** 2026-06-29
- **Link:** http://arxiv.org/abs/2606.30587v1

---
This paper investigates whether Large Language Models (LLMs) used for code vulnerability detection are susceptible to cognitive heuristics, similar to humans, specifically when presented with non-code contextual information.

### Problem

LLMs are increasingly deployed as automated security gatekeepers (e.g., vulnerability detectors in CI/CD pipelines). While prior work has shown LLMs are prone to cognitive heuristics in general reasoning, no systematic study has investigated if these biases affect their assessment of code vulnerabilities. LLM-based scanners in real-world scenarios typically receive non-code context (author, task directives, prior analysis results) alongside the code. If LLMs are biased by this context, their security verdicts could be unreliable, potentially leading to false negatives or positives based on irrelevant information, posing a significant security risk.

### Method

The researchers designed a controlled framework to systematically explore cognitive heuristics in LLM-driven code vulnerability detection.
1.  **Controlled Setup:** The core code snippet under review was kept *fixed* across conditions. Only the *surrounding non-code context* was varied to trigger specific cognitive heuristics.
2.  **Heuristics Studied:**
    *   **Halo Effect:** Induced by varying author attribution (e.g., "principal security engineer" vs. "new junior developer").
    *   **Framing Effect:** Induced by varying task objectives or consequences (e.g., "verify secure coding guidelines" vs. "identify potential violations," or "prevents unnecessary delays" vs. "can result in a security breach").
    *   **Anchoring Effect:** Induced by providing a fabricated prior analysis result (e.g., "marked SAFE" vs. "marked VULNERABLE").
3.  **Polarities:** Each heuristic included two prompt variants, each with two polarities: a "pro-safe" (reassuring) polarity and a "pro-vuln" (alarming) polarity.
4.  **Evaluation:**
    *   Eight state-of-the-art LLMs (5 open-source, 3 proprietary) were evaluated.
    *   Tests were conducted across three programming languages (C/C++, Python, Java).
    *   Metrics included Recall Gap (ΔR) and FPR Gap (ΔFPR) to quantify susceptibility, and a "Utility Index" to assess if biases constructively improved detection.
    *   Both quantitative and code-level qualitative analyses were performed.
5.  **Adversarial Impact Demo:** A proof-of-concept black-box cognitive attack was demonstrated on a simulated CI/CD workflow, manipulating context to suppress vulnerability detection.

### Impact

The study reveals critical insights into the reliability and exploitability of LLM-based vulnerability detectors:
1.  **Universal Susceptibility:** All evaluated LLMs were susceptible to cognitive heuristics. The average susceptibility in C/C++ was highest for framing (33.2%), followed by anchoring (23.5%) and halo (18.4%). Open-source models generally exhibited greater bias.
2.  **Vulnerability Type Sensitivity:** Vulnerabilities requiring semantic reasoning for detection were 1.5x-2x more susceptible to cognitive heuristics than those identifiable via pattern matching.
3.  **No Accuracy Improvement:** Cognitive biases did not improve a model's detection capabilities. Models often changed their verdict (e.g., from "safe" to "vulnerable") based on cognitive conditions *without accurately identifying the actual vulnerability*, leading to stagnant precision.
4.  **High Exploitability:** The biases are highly exploitable. A black-box cognitive attack leveraging manipulated contextual metadata (e.g., author and prior scan reports) successfully suppressed up to **97%** of previously detected vulnerabilities. Combining multiple cognitive signals compounded this suppressive effect.
5.  **Defense Ineffectiveness:** Standard prompt-based defenses designed to mitigate such attacks failed to prevent the cognitive attack.

These findings indicate that cognitive susceptibility is a consistent and exploitable property of LLM-based vulnerability detection, posing significant implications for their reliability and security in real-world deployments.