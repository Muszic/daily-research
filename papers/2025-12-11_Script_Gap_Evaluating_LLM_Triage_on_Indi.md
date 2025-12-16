# Script Gap: Evaluating LLM Triage on Indian Languages in Native vs Roman Scripts in a Real World Setting

- **Category:** NLP
- **Published:** 2025-12-11
- **Source:** [Original ArXiv Link](http://arxiv.org/abs/2512.10780v1)

---

## 🧐 Problem

Large Language Models (LLMs) are increasingly deployed in high-stakes clinical applications in India, particularly for patient-facing tasks like medical triage. However, a significant portion of communication in Indian languages, especially in informal digital settings, occurs using **romanized text** (Indian languages written in the Roman script) rather than native scripts. Existing research rarely evaluates LLM performance on this orthographic variation using **real-world user-generated data**.

Current LLM benchmarks for healthcare often fall short by:
1.  **Relying on synthetic data or curated clinical literature** instead of messy, informal patient-provider conversations.
2.  **Focusing on English and Chinese**, with minimal coverage of Indian languages and their script variations.
3.  **Ignoring the challenge of romanized input** in high-stakes domains like medical triage, even though it's pervasive in multilingual online communication.

This creates a critical **safety blind spot**: models might appear to understand romanized input, but their reliability for sensitive tasks like triage in a real-world, multilingual context remains unassessed, potentially leading to significant errors in patient care.

## 🛠️ Method

The authors conducted the first benchmarking evaluation of real-world LLM triage performance on Indian languages across both native and Roman scripts.

1.  **Dataset Creation:**
    *   They partnered with a maternal health organization in India and collected a de-identified corpus of approximately 133,000 short WhatsApp messages related to maternal and newborn care.
    *   From this, a stratified random sample of **3,156 single-turn user messages** was selected, spanning five Indian languages (Hindi, Telugu, Kannada, Marathi, Punjabi), Nepali, and English.
    *   Each message was meticulously tagged by language and script type (English, Native script, Roman script) using GPT-4o, with 97.0% agreement with human annotators.
    *   **Triage Labels:** Messages were assigned one of three mutually exclusive labels: `Emergency`, `Non-emergency`, or `Insufficient Information`. Pseudo-labels for the primary dataset (`P`) were generated using a validated **LLM ensemble** (GPT-4o, Claude 4.5 Sonnet, Qwen 3-80B), which achieved 89.8% weighted F1 on a human-annotated gold set (`H`).

2.  **Benchmarking Leading LLMs:**
    *   Nine LLMs were evaluated: frontier proprietary (GPT-4o, Claude 4.5 Sonnet), large open-weight (DeepSeek V3, LLaMA 4 Maverick, Qwen3-80B), and compact+Indic-specialized (GPT-OSS-20B, Mixtral-7B, Qwen2.5-7B, Sarvam).
    *   All models were prompted with a fixed **"SOP+KB" (Standard Operating Procedure + Knowledge Base) template**, which was found to be most effective in pilot tests, ensuring consistent evaluation.
    *   Models were required to provide both a discrete triage label and a brief natural language rationale.

3.  **Extensive Error Analysis:**
    *   **Performance Metrics:** F1 scores were compared across models, script types (Native, Roman, English), and individual languages.
    *   **Uncertainty Assessment:** Cross-model consensus levels were analyzed to understand epistemic uncertainty associated with different script types.
    *   **Confusion Matrix Analysis:** Examined misclassification patterns (e.g., rate of missed emergencies, over-assignment of "Insufficient Information") stratified by script.
    *   **Impact of Code-Mixing:** Investigated performance differences within romanized messages between code-mixed (with English) and non-code-mixed variants.
    *   **Script-Sensitive Misclassification:** Provided qualitative examples of semantically similar queries classified differently based on script.
    *   **Model-Generated Reasoning:** Analyzed reasoning summaries for shared vocabulary, explicit language/script awareness cues, and lexical copying from user queries to diagnose the nature of model failures.

4.  **Diagnosing the Script Gap via Normalization:**
    *   **Script Normalization Experiments:** To determine if the gap was orthographic or semantic, they translated messages:
        *   Native script and Roman script messages into a common **English pivot language**.
        *   Romanized messages back into their corresponding **native scripts** using GPT-4o.
    *   Triage classification was re-evaluated on these normalized subsets using LLaMA 4 and GPT-4o.

## 📊 Impact

The study reveals a critical performance disparity in LLM-based clinical triage, with significant safety and practical implications:

1.  **Consistent Performance Degradation for Romanized Text:**
    *   LLMs consistently show **5–12 points lower F1 scores** on romanized messages compared to native scripts and English.
    *   This gap is particularly substantial for languages like Kannada, Telugu, Marathi, and Nepali, where performance on romanized messages drops by **10–20 points**.
    *   Even Sarvam, an Indic-specialized model, performs weakest on Indian languages written in Roman script when compared to native scripts.

2.  **High Risk of Excess Errors in Real-World Settings:**
    *   At the partner maternal health organization alone, this "script gap" could lead to nearly **2 million excess errors** in LLM-based triage annually.
    *   Romanized messages show higher rates of **missed Emergency cases** (7.7% vs. 5.3% for English, 6.5% for native) and a markedly higher tendency to be misclassified as **"Insufficient Information"** (20.15% vs. 13.9% for English, 11.0% for native), even for clear non-emergency queries.
    *   Romanized queries also exhibit lower cross-model consensus, indicating higher epistemic uncertainty in triage decisions.

3.  **Nature of the Script Gap: Orthographic Noise, Not Clinical Reasoning:**
    *   The degradation is primarily due to **orthographic and tokenization challenges** in romanized inputs, not a failure in clinical reasoning or semantic understanding. Models often correctly infer the user's intent and show explicit awareness of language/script as a source of difficulty in their rationales, but still fail at the final classification.
    *   **Script normalization experiments** strongly support this: translating romanized messages back into their native scripts largely **recovers most of the performance gap**, bringing F1 scores very close to the native script baseline. Normalization into English also yields gains for romanized inputs, but less effectively than native script normalization.
    *   Interestingly, **code-mixed romanized messages (with English) perform substantially better (F1 80.3%)** than purely romanized messages (F1 70.4%), suggesting that English lexical anchors can mitigate some of the orthographic noise.

4.  **Critical Safety Blind Spot:**
    *   The findings highlight that LLMs can **appear to understand romanized input but still fail to act on it reliably** for critical tasks like triage, posing a significant safety risk in healthcare systems relying on such models.
    *   The study provides a concrete framework for evaluating triage performance and offers crucial insights into the "script gap" in frontier models, which is broadly applicable to other healthcare platforms implementing LLM-powered solutions in multilingual, low-resource settings.
