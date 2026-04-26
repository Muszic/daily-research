# Revisiting Non-Verbatim Memorization in Large Language Models: The Role of Entity Surface Forms

- **Category:** NLP
- **Date:** 2026-04-23
- **Link:** http://arxiv.org/abs/2604.21882v1

---
Here's a summary of the research paper in Markdown format:

### Revisiting Non-Verbatim Memorization in Large Language Models: The Role of Entity Surface Forms

#### Problem

Traditional evaluations of non-verbatim factual memorization in Large Language Models (LLMs) often query entities using a single, canonical surface form. This approach makes it difficult to ascertain whether an LLM has truly memorized a fact about an entity or merely learned to access that fact through a specific name. Entities are frequently referred to by multiple surface forms (aliases, abbreviations, misspellings), and preliminary diagnostics show that LLM predictions can be inconsistent (e.g., 23.7% flip rate) when only the entity's surface form changes, even if the underlying fact remains the same. This highlights a gap in understanding LLM reliability and limitations regarding factual knowledge access.

#### Method

The researchers introduce **RedirectQA**, a novel entity-based QA dataset designed to systematically analyze surface-conditioned factual memorization.
1.  **Dataset Construction:**
    *   Factual triples (subject, relation, object) are collected from Wikidata.
    *   Using Wikipedia redirect information, each subject entity is associated with its canonical surface form and multiple *redirect surface forms*. These redirects are categorized into broad types: "Alternative Names and Abbreviations," "Spelling Variants," and "Typical Errors."
    *   The core design ensures that for each instance, the factual relation and gold answer remain fixed, while only the subject entity's surface form (canonical vs. redirect) varies.
    *   Each surface instance is rendered into two question realizations using different relation-specific templates to reduce sensitivity to question wording.
    *   RedirectQA contains 30,560 surface instances (14,672 canonical, 15,888 redirect) derived from 14,672 factual triples, totaling 61,120 question realizations.
2.  **Evaluation:**
    *   13 LLMs (including transparent models like Pythia, OpenSciRef, OLMo 2; open-weight models like Qwen 3 and Llama 3.1; and the proprietary GPT-4o-mini) were evaluated in a 15-shot setting.
    *   **Consistency Analysis:** For each canonical–redirect pair, prediction correctness was compared. A pair is "consistent" if both predictions are correct or both are incorrect, and "inconsistent" otherwise.
    *   **Frequency Analysis:** Entity-level and surface-level frequencies were extracted from pretraining corpora (The Pile, OLMo Mix 1124) using DBpedia Spotlight to determine their association with factual QA accuracy.

#### Impact

The study reveals critical insights into LLM factual memorization:
*   **Surface-Conditioned Inconsistency:** LLM prediction outcomes frequently change when only the entity surface form varies, even for the same underlying fact. This indicates that factual memorization is not fully surface-invariant.
*   **Category-Dependent Robustness:**
    *   Models exhibit higher consistency for minor orthographic variations ("Spelling Variants," e.g., punctuation, capitalization, diacritics).
    *   Models show significantly lower consistency for larger lexical variations ("Alternative Names and Abbreviations," e.g., aliases, abbreviations, initialisms), with initialisms being particularly challenging. "Typical Errors" fall between these two.
*   **Granularity of Memorization:** Both the frequency of a specific surface form and the aggregate frequency of the corresponding entity are associated with accuracy. Crucially, *entity frequency often contributes to accuracy beyond surface frequency*, suggesting a degree of cross-surface coupling in factual access rather than purely independent memorization of each surface form.
*   **Overall Conclusion:** Factual memorization in LLMs appears to be **neither purely surface-specific nor fully surface-invariant**, presenting an intermediate picture.
*   **Implication:** Evaluating LLMs solely with canonical entity names provides an incomplete picture. The findings underscore the importance of **surface-form diversity** in thoroughly assessing what factual knowledge LLMs memorize and how reliably they can access it, which is crucial for evaluating their reliability and trustworthiness.