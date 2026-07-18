# MARS: Multi-hop Adaptive Retrieval and SPARQL Generation for KGQA

- **Category:** NLP
- **Date:** 2026-07-16
- **Link:** http://arxiv.org/abs/2607.14561v1

---
### Problem

Large Language Models (LLMs) struggle with hallucinations, factual inconsistencies, and multi-hop reasoning failures in knowledge-intensive tasks. While Retrieval-Augmented Generation (RAG) helps, text-based RAG implicitly represents relational structures, limiting its efficacy for complex multi-hop queries. Existing KGQA solutions face several issues:
*   **Inefficiency:** Direct reasoning over large KG subgraphs can exceed LLM context windows.
*   **Limited Coverage/Reliability:** Fine-tuned SPARQL generation models are constrained by training data, and agentic LLM-based approaches are prone to inconsistent behavior and hallucinations at each step, making them unreliable and less predictable.
*   **Scalability Challenges:** Graph-based RAG often requires costly prior graph summarization or indexing for large-scale KGs.
*   **Multilingual Limitations:** Downstream KGQA components are predominantly optimized for English, with translation often losing original semantic intent.
*   **Reproducibility Issues:** Benchmark datasets are frequently released without the specific KG versions used, or with incomplete KGs, hindering fair comparisons.

### Method

MARS proposes a scalable, **non-fine-tuned** Knowledge Graph Question Answering (KGQA) approach that combines pattern-based graph retrieval with context-augmented knowledge for robust SPARQL generation. Its pipeline consists of three main stages:

1.  **Entity Linking and Text Augmentation:**
    *   Identifies relevant entities from the natural language question within the Knowledge Graph (KG).
    *   Augments the query context by incorporating predicted entity type labels using an instruction-tuned LLM.
    *   Employs a hybrid multilingual strategy that uses translation alongside the native question, supporting 10 languages, to preserve semantic intent.

2.  **Iterative Reasoning Loop (Multi-hop Adaptive Retrieval):** This loop repeats until the query is fully grounded:
    *   **Pattern Retrieval and Filtering:** Instead of retrieving entire subgraphs or raw triples, MARS extracts and filters *triple patterns* (e.g., `(entity, predicate, ?object)` or `(?subject, predicate, entity)`). These patterns are verbalized, converted into dense embedding vectors, and ranked by semantic similarity to the input question. Only the top-N most relevant patterns are selected, significantly reducing context size.
    *   **Context Enrichment:** Key features are extracted for the selected patterns, including instance values, frequencies, and typological information (domain/range constraints).
    *   **SPARQL Reasoner (Adaptive Traversal or Generation):** An LLM decides at each step whether to continue the graph traversal (by expanding the set of patterns to capture "next-hop" information) or to generate the final SPARQL query. This mechanism allows MARS to dynamically adapt the retrieval depth to the complexity of the question, ensuring the query is fully grounded.

3.  **SPARQL Query Generation:** Once the reasoning loop determines the query is grounded, the final SPARQL query is generated based on the enriched and filtered pattern set.

MARS avoids open-ended agentic exploration in favor of a structured, pattern-guided abstraction loop, allowing the LLM to focus on path pruning and query generation. It primarily uses open-weight LLMs for transparency and reproducibility.

### Impact

*   **State-of-the-Art Performance:** Achieves competitive performance relative to state-of-the-art methods across three established KGQA benchmarks, consistently outperforming robust baselines, particularly on complex multi-hop queries (e.g., QALD-10).
*   **Efficiency and Scalability:** Remains efficient and scalable by judiciously curtailing the LLM context size through pattern-based retrieval, rather than operating on full subgraphs.
*   **Enhanced Reliability and Predictability:** Its structured, pattern-guided retrieval loop mitigates the risks of hallucination and inconsistent behavior commonly associated with fully agentic LLM approaches.
*   **Adaptive Retrieval Depth:** The adaptive decision-making process for graph traversal or query generation allows the model to tailor retrieval depth to the specific question.
*   **Multilingual Capability:** Provides robust multilingual KGQA support across 10 languages, including low-resource ones, by preserving semantic intent with its hybrid translation strategy.
*   **Reproducibility and Open Science:** Addresses a critical challenge in KGQA by publicly releasing the underlying Wikidata snapshot alongside updated datasets, evaluation results, code, and resources, ensuring fair comparison and reproducibility for future work.