# MM-WebAgent: A Hierarchical Multimodal Web Agent for Webpage Generation

- **Category:** NLP
- **Date:** 2026-04-16
- **Link:** http://arxiv.org/abs/2604.15309v1

---
Here's a summary of the research paper "MM-WebAgent: A Hierarchical Multimodal Web Agent for Webpage Generation" in Markdown format:

### Problem

The rapid progress in Artificial Intelligence Generated Content (AIGC) tools enables the on-demand creation of images, videos, and visualizations for webpage design. However, directly integrating these tools into automated webpage generation often leads to significant challenges:
*   **Style Inconsistency:** Elements generated in isolation lack a unified visual style.
*   **Poor Global Coherence:** The overall webpage design lacks a cohesive aesthetic and functional flow, as elements are not coordinated.
*   **Geometry Mismatch:** Generated media often don't fit well into the reserved slots in the layout.
Existing large language model (LLM) and agent-based systems for webpage generation typically populate multimodal elements via retrieval or placeholders, or generate them independently, failing to *coherently generate* them as an integral part of the design process.

### Method

The authors propose **MM-WebAgent**, a hierarchical agentic framework designed to overcome these challenges by treating multimodal webpage generation as a structured "plan-and-refine" process.

**Key Components:**

1.  **Hierarchical Planning and Generation:**
    *   **Global Layout Planning:** An agent generates an overall plan defining the webpage's section hierarchy, ordering, coarse spatial organization, and page-level style attributes. This plan *explicitly includes placeholders and constraints for multimodal components*, ensuring they are integrated from the start.
    *   **Local Element Planning:** For each multimodal element identified in the global plan, a detailed local plan is created. This plan specifies the element's functional role, surrounding section context, expected size/aspect constraints, and fine-grained style guidance (e.g., visual style, color tone, motion, specific data requirements). It also designates which specialized AIGC tool should be invoked for generation.
    *   **Plan Execution:** The global layout plan is converted into the initial HTML/CSS structure. Then, each local element plan is executed by its designated generation tool (e.g., image, video, or chart generator) to produce the corresponding asset, which is subsequently inserted into the webpage.

2.  **Hierarchical Self-Reflection:** Inspired by human designers, MM-WebAgent iteratively refines the generated webpage at three complementary levels:
    *   **Local Refine:** Focuses on improving the intrinsic quality of *individual multimodal assets* (e.g., image inpainting, color adjustment, chart label/axis fixes) using specialized agents or localized HTML/CSS updates.
    *   **Context Refine:** Addresses *integration issues* of assets into their surrounding layout (e.g., misalignment, overflow, inconsistent spacing) by analyzing relevant HTML snippets and applying targeted structural adjustments like CSS patches or block resizing.
    *   **Global Refine:** Evaluates the *entire webpage* using both the HTML code and rendered screenshots to detect and resolve high-level layout imbalances and style inconsistencies across all sections, performing targeted edits to enforce overall coherence.

**Evaluation Framework:**
*   **MM-WebGEN-Bench:** A new benchmark dataset curated for multimodal webpage generation, reflecting realistic and diverse webpage designs across various intents, layouts, styles, and complex multimodal compositions.
*   **Multi-level Evaluation Protocol:** Designed for systematic assessment, it decomposes webpage quality into:
    *   **Global-level criteria:** Layout correctness, style coherence, and overall aesthetics.
    *   **Local-level criteria:** Quality, relevance, visibility, and consistency of individual embedded multimodal elements (images, videos, charts).

### Impact

**MM-WebAgent** significantly advances automated webpage generation by:

*   **Producing Coherent and Visually Consistent Webpages:** It successfully overcomes the issues of style inconsistency and poor global coherence by jointly optimizing global layout, local multimodal content, and their integration through a structured agentic workflow.
*   **Outperforming Baselines:** Experiments on MM-WebGEN-Bench demonstrate that MM-WebAgent consistently outperforms both traditional code-generation and existing code-only agent-based baselines.
*   **Strong Gains in Multimodal Integration:** The framework shows particularly strong improvements in the quality of multimodal element generation and their seamless integration into the webpage, highlighting the advantage of enabling agentic coordination with native multimodal asset generation.
*   **Introducing a Novel Paradigm:** It establishes a new multimodal web agent paradigm that extends beyond code-only generation, enabling hierarchical planning over native multimodal asset creation, coupled with context-aware local planning.
*   **Enabling Robust Evaluation:** The introduction of MM-WebGEN-Bench and its multi-level evaluation protocol provides a systematic and fine-grained method for benchmarking future advancements in multimodal webpage generation.