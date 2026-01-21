# Kakugo: Distillation of Low-Resource Languages into Small Language Models

- **Category:** NLP
- **Date:** 2026-01-20
- **Link:** http://arxiv.org/abs/2601.14051v1

---
This research paper introduces Kakugo, a novel and cost-effective pipeline for developing Small Language Models (SLMs) for low-resource languages.

### Problem

*   Small Language Models (SLMs) offer efficiency and data sovereignty but typically underperform in low-resource language settings compared to larger models.
*   Existing efforts to create language-specific SLMs for low-resource languages are often expensive, require specialized teams, and intimate knowledge of data sources, limiting their accessibility.
*   There is a need for a democratized, general-purpose method to create effective, language-specific AI tools for low-resource communities.

### Method

The Kakugo pipeline is a fully automated model distillation process that takes only the language name as input to train a monolingual SLM.

1.  **Teacher Model:** Utilizes a large teacher model, GPT-OSS 120B, known for its cross-language proficiency.
2.  **Student Model:** Trains IBM's Granite 4 Micro, an open-source model chosen for its performance relative to its size.
3.  **Data Creation:**
    *   **Synthetic Prompt Generation:** The teacher model generates diverse prompts in the target language using three methods:
        *   **Topic-based:** Generates prompts based on general and language-specific topics.
        *   **Scenario-based:** Creates prompts reflecting realistic AI assistant usage scenarios.
        *   **Context-based:** Generates prompts (e.g., translation, summarization, QA) related to text samples from the FineWeb2 corpus in the target language.
        *   Half of the generated prompts are further elaborated to increase complexity.
    *   **Response Generation:** The teacher model generates responses to these synthetic prompts, naturally capturing "chain-of-thought" reasoning traces.
    *   **Instruction Data Translation:** Translates 15,000 high-quality English conversational examples from the InfinityInstruct dataset into the target language using the teacher model. Translated data undergoes quality filtering to ensure formatting and appropriate length, accommodating the tokenization characteristics of low-resource languages.
4.  **Model Training:**
    *   The generated and translated data are combined into a single, shuffled dataset.
    *   A conditional "thinking mode" system instruction is added to the generated data (which includes reasoning traces) to teach the student model to conditionally generate reasoning steps. Translated data uses a standard prompt.
    *   The student model undergoes full fine-tuning for one epoch using Llama Factory to develop generalist abilities across various tasks.
5.  **Evaluation:**
    *   Developed datasets and models for 54 low-resource languages (14 for in-depth analysis, 40 additional).
    *   Evaluated performance across diverse NLP tasks: translation (FLORES NLLB Team), classification (SIB-200), and question answering (Belebele, GlobalMMLU) using 3-shot learning.
    *   Conducted a double-blind manual preference analysis by native speakers for Galician, Javanese, and Yoruba, comparing Kakugo's output to the base model on translated MT-Bench prompts.

### Impact

*   **Significant Performance Improvement:** Kakugo consistently and significantly improves performance over base models across a diverse set of general NLP tasks for 54 low-resource languages. For the full model, average gains include +9.9% accuracy on Belebele, +8.8% on SIB200, and +13.1 CHRF++ on FLORES (en-xx).
*   **Cost-Effectiveness & Accessibility:** The pipeline achieves this for less than $50 per language, making it an accessible method for low-resource communities to develop language-specific AI.
*   **Democratization of AI:** Lowers the technical and financial barriers for creating general-purpose SLMs for languages often overlooked by mainstream AI development.
*   **Open-Source Contributions:** Releases the Kakugo pipeline code, open-source training datasets, and monolingual SLMs for all 54 languages, including the *first generalist conversational SLMs* for many (e.g., Bashkir, Maori, Mongolian).
*   **Methodological Insights:** Demonstrates that combining diverse data generation methods (topic, scenario, context-based synthetic data, and translated instruction data) is most effective for training generalist SLMs. It also suggests prioritizing target-language tokens over reasoning traces if training budgets are constrained, but leveraging reasoning traces if they are a "free" by-product of generation.
*   **Targeted Effectiveness:** Kakugo provides the most substantial improvements for languages where existing SLMs initially struggle, showing an inverse relationship between base model performance and the gains achieved.