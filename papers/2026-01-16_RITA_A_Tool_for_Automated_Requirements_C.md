# RITA: A Tool for Automated Requirements Classification and Specification from Online User Feedback

- **Category:** Software Engineering
- **Date:** 2026-01-16
- **Link:** http://arxiv.org/abs/2601.11362v1

---
## RITA: A Tool for Automated Requirements Classification and Specification from Online User Feedback

### Problem

*   Online user feedback (e.g., app reviews, forum discussions) is a valuable resource for Requirements Engineering (RE), but its immense volume and informal, noisy nature make manual analysis extremely difficult.
*   Existing automated tools for feedback analysis are fragmented, offering support for individual tasks (e.g., classification, sentiment analysis) but lacking integrated, end-to-end support that transforms raw user feedback into structured, deployable requirements artifacts.
*   This absence of a unified workflow limits the practical adoption of RE tools and makes it challenging to assess their real-world utility in addressing practitioner needs.

### Method

RITA addresses these challenges by presenting an integrated tool that leverages lightweight open-source Large Language Models (LLMs) to create a unified, end-to-end workflow for feedback-driven Requirements Engineering:

*   **Integrated Workflow:** RITA combines multiple LLM-based analysis tasks (feedback classification, non-functional requirement identification, requirements specification generation) into a single, seamless process.
*   **User-Centric Capabilities:**
    *   **Feedback Upload:** Allows users to upload diverse online feedback datasets (e.g., app reviews, survey responses) in common formats (txt, csv, xls).
    *   **Configurable Analysis:** Users can configure classification schemes (e.g., User Request Types, Non-Functional Requirements), select specific LLMs, and define prompt strategies to tailor the analysis.
    *   **Automated Processing:** Automates the classification of user requests, identification of non-functional concerns, and generation of natural-language requirements specifications (SRS documents) and agile-style user stories.
    *   **Results Inspection:** Provides a user-friendly graphical interface to inspect classification results and generated artifacts.
*   **Jira Integration:** Features seamless integration with Jira, enabling users to transfer selected user stories directly into their development backlogs as Jira issues.
*   **Architecture & Implementation:** RITA is a lightweight, Docker-containerized system with a React-based user interface, a Python FastAPI backend, a local SQLite database for data storage, and utilizes an Ollama local service for LLM inference (ensuring data locality and privacy).

### Impact

*   **Bridging Research and Practice:** RITA facilitates the transition of previously evaluated LLM-based RE techniques from isolated academic studies into a practical, integrated, end-to-end tool.
*   **Enhanced Efficiency for Practitioners:** Enables requirements engineers, product managers, and software developers to efficiently transform high volumes of raw, noisy user feedback into structured requirements artifacts (classified feedback, SRS, user stories) with lightweight support.
*   **Facilitating Practical Adoption:** Provides a user-friendly system that fits into existing development workflows (via Jira integration), thus promoting the practical adoption of LLM-based techniques for early and ongoing RE activities that rely on continuous user feedback.
*   **Enabling Future Research:** By offering a working, integrated system, RITA creates a platform for future empirical studies on how LLM-based RE techniques are used and validated in real-world practice.