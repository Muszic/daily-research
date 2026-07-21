# DeLIVeR: Decomposed Learning for Information-grounded Veracity Recognition via Reinforced Knowledge Graph Exploration

- **Category:** NLP
- **Date:** 2026-07-20
- **Link:** http://arxiv.org/abs/2607.17935v1

---
Here's a summary of the research paper in Markdown:

```markdown
### Problem

Automated fact-checking faces significant challenges, particularly for Large Language Models (LLMs) which are prone to "hallucinations" due to reliance on static internal knowledge. Existing Retrieval-Augmented Generation (RAG) frameworks struggle with "query brittleness," static query limitations, and fixed retrieval policies, leading to an inability to handle complex claims requiring multi-hop reasoning. Standard RAG systems often retrieve unstructured text using single, ambiguous queries, failing to capture the relational structure crucial for claims involving multiple entities and linked events, thus making veracity prediction unreliable without explicit grounding.

### Method

The paper proposes **DeLIVeR (Decomposed Learning for Information-grounded Veracity Recognition)**, a framework that transforms fact verification into a reinforced, closed-loop optimization process for evidence retrieval. Key components include:

1.  **Knowledge Graph (KG) Construction:** A structured KG is built from ground-truth evidence corpora using GPT-4 for Open Information Extraction (OpenIE) to form (subject, predicate, object) triples. This process includes provenance tracking, temporal metadata for sensitivity, and a frequency-based filter to ensure high-fidelity, multi-hop evidence paths.
2.  **Set-based Question Generation:** A dedicated Planner LLM (a secondary LLM) decomposes complex claims into a cohesive set of diverse, targeted questions. These questions are designed to explore specific angles of the claim (e.g., source, context, contradictions, factual/temporal/causal aspects) to reduce query ambiguity and improve evidence coverage. Vector similarity search (cosine similarity) maps generated questions to KG nodes and edges, and a diversity constraint (entropy maximization) encourages the generation of questions spanning distinct subgraphs.
3.  **Reinforced KG Exploration:** The generated set of questions collectively queries the KG to retrieve complementary and high-precision structured evidence.
4.  **GRPO-driven Policy Optimization:** The Planner LLM's question generation policy is optimized using **Group Relative Policy Optimization (GRPO)**. A sophisticated reward system encourages valid question format, structural diversity in the retrieved evidence, and ultimately, the verdict accuracy produced by a frozen primary LLM that synthesizes the retrieved evidence with the claim to generate a final verdict (True/False/Not Enough Information) and an explanation. This closed-loop mechanism aims to learn a robust and stable information-seeking strategy.

### Impact

DeLIVeR significantly advances automated fact-checking with several key impacts:

*   **Superior Performance:** The framework consistently outperforms state-of-the-art baselines, achieving peak F1-scores of 83.73 on LIAR, 84.57 on FEVER, and 79.70 on PolitiFact using Qwen2.5-7B. This represents a substantial **10-15% improvement over strong RAG baselines** like HippoRAG2.
*   **Enhanced Reasoning & Grounding:** By shifting to a reinforced question-planning strategy and leveraging structured KGs, DeLIVeR effectively bridges multi-hop reasoning gaps, providing more precise and contextually relevant evidence than traditional RAG systems.
*   **Transparency & Audibility:** The question-driven retrieval process, combined with structured evidence paths mapped back to source documents, offers an inherently auditable and transparent mechanism for verifiable misinformation detection, providing clear evidence chains for model decisions.
*   **Robust Policy Learning:** GRPO-driven optimization yields a more stable and interpretable information-seeking policy, contributing to more robust and explainable fake news detection.
```