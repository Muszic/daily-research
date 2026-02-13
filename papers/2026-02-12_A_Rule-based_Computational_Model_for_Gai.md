# A Rule-based Computational Model for Gaidhlig Morphology

- **Category:** NLP
- **Date:** 2026-02-12
- **Link:** http://arxiv.org/abs/2602.12132v1

---
## A Rule-based Computational Model for G`aidhlig Morphology

### Problem

The vitality of low-resource languages like G`aidhlig (Scottish Gaelic) is hindered by a severe lack of data. This data scarcity prevents the application of currently popular neural language models, which require vast amounts of training data, for creating essential tools like grammar-checkers, dependency parsers, and effective learning materials. Additionally, Celtic languages possess unusual linguistic features (e.g., initial mutations, VSO word order, vowel harmony, inflected prepositions) that make their morphological modeling a complex and interesting problem. Existing online resources, such as G`aidhlig Wiktionary, contain valuable information but are not structured in a way that allows for easy computational leverage.

### Method

The research describes work-in-progress to construct a rule-based computational model for G`aidhlig morphology, specifically for 'content words' (nouns, verbs, adjectives). The approach leverages limited existing data and prioritizes interpretability, requiring modest computational resources.

1.  **Data Acquisition:** A custom Python script was used to process a large Wiktionary XML dump, extracting only the G`aidhlig entries into a structured JSON file (reducing 11 GiB of XML to 17 MiB of JSON).
2.  **Data Parsing and Standardization:** Another Python script parsed the G`aidhlig JSON data to extract the "principal parts" (lemma, gender, plural forms for nouns; imperative, verbal noun for verbs; positive, comparative for adjectives) of 4956 nouns, 1025 adjectives, and 534 verbs, noting 24 irregular forms. This information was then stored in a Structured Vocabulary Format (SVF) text file.
3.  **Data Cleaning:** The SVF data underwent manual cleaning to resolve near-duplicates arising from differences in capitalization or accents, distinguishing between true variants and distinct words. Missing principal parts were marked for future improvement.
4.  **Model Construction:**
    *   **Relational Database:** The SVF data was loaded into an SQL relational database. This allows for querying and analysis of G`aidhlig lexical patterns.
    *   **Rule-based Generation System:** Python utilities, informed by the SVF data, were developed to derive inflected forms of G`aidhlig words using a declarative rule-base. This rule-based system accounts for G`aidhlig's complex morphological features, including suffixes, slenderization, and initial mutations (lenition, prothesis, glottalisation), as well as vowel harmony constraints.

### Impact

This rule-based computational model for G`aidhlig morphology offers several significant impacts:

*   **Support for Low-Resource Languages:** It demonstrates an effective strategy for creating essential language tools where vast datasets for neural models are unavailable, making it applicable to other typologically similar low-resource languages.
*   **Enhanced Data Value:** It adds considerable value to the existing knowledge in G`aidhlig Wiktionary by transforming unstructured data into a structured and computable format.
*   **Interpretability and Explainability:** Rule-based systems are inherently explainable, which is crucial for understanding language patterns and for pedagogical purposes.
*   **Educational Tool Development:** The model provides a foundation for creating:
    *   Educational tools that teach and explain G`aidhlig language patterns and inflected word forms.
    *   Analysis tools to study the evolution of G`aidhlig by comparing inflected forms in time-stamped texts, aiding in the design of effective teaching materials.
*   **Foundation for Higher-Level NLP:** The derived morphological functionality can serve as a lower-level morphology stack for developing more advanced rule-based NLP utilities, such as lemmatizers and dependency parsers, for G`aidhlig.