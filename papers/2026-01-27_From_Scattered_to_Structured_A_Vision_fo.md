# From Scattered to Structured: A Vision for Automating Architectural Knowledge Management

- **Category:** Software Engineering
- **Date:** 2026-01-27
- **Link:** http://arxiv.org/abs/2601.19548v1

---
**Problem:**
Architectural knowledge in software systems is scattered across heterogeneous artifacts such as requirements documents, design diagrams, source code, and documentation. This distribution makes it difficult for developers to effectively access and utilize crucial architectural information. As systems evolve, inconsistencies frequently emerge between these artifacts, leading to architectural erosion, confusion, impeded maintenance activities, and uninformed decision-making. Much of this knowledge is also implicit or requires significant effort for comprehension.

**Method:**
The authors envision an automated, agent-based pipeline to systematically manage architectural knowledge. This vision encompasses several planned steps:
1.  **Knowledge Extraction Framework:** Develop specialized extractors using Natural Language Processing (NLP), Large Language Models (LLMs), static analysis, and parsing techniques for diverse artifact types (text, code, diagrams, multimodal content like recordings). This framework will also support Human-AI collaboration to augment knowledge and correct extraction errors.
2.  **Knowledge Base (KB) Schema Design:** Create a unified schema for the architectural KB to accommodate knowledge from various sources, maintain semantic relationships, and establish traceability links between artifacts.
3.  **Consistency Checking and Resolution:** Implement automated mechanisms (rule-based, learning-based, LLM-based) to identify inconsistencies between extracted knowledge and different artifacts. This includes semi-automated resolution strategies, involving human architects for critical decisions.
4.  **Agent-Based Continuous Monitoring:** Develop an LLM agent that continuously monitors software artifacts (via file system/version control), automatically triggers knowledge extraction and traceability link recovery, and orchestrates consistency checking. The agent will autonomously resolve minor inconsistencies or escalate critical conflicts to human architects with targeted clarification requests and context.
5.  **Question-Answering System Integration:** Build a natural language question-answering interface using Retrieval Augmented Generation (RAG) techniques, allowing developers to query the structured KB conversationally.

**Impact:**
This automated architectural knowledge management system is projected to:
*   Significantly improve access to and utilization of architectural knowledge for developers and architects.
*   Mitigate architectural erosion by systematically identifying and resolving inconsistencies across software artifacts.
*   Enable critical software engineering activities such as architecture conformance checking, change impact analysis, and informed decision-making throughout the software lifecycle.
*   Democratize access to architectural knowledge across development teams through an intuitive, natural language question-answering system.
*   Encourage better documentation practices by demonstrating the tangible benefits of maintaining accurate and consistent architectural knowledge.
*   Maintain knowledge base integrity with minimal human intervention, ensuring efficient processes while keeping critical decisions under human control.