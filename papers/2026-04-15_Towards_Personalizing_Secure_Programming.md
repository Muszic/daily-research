# Towards Personalizing Secure Programming Education with LLM-Injected Vulnerabilities

- **Category:** Software Engineering
- **Date:** 2026-04-15
- **Link:** http://arxiv.org/abs/2604.13955v1

---
This paper introduces `InjectEd`, an agentic AI system designed to personalize secure programming education by injecting Common Weakness Enumerations (CWEs) directly into students' own code.

# Problem

Generic examples of software vulnerabilities often fail to engage students and connect with their prior work, leading to limited understanding and difficulty in internalizing secure programming practices. This disconnect hinders students' ability to recognize, understand, and prevent real security flaws. Constructivist learning theory suggests that personalized examples, grounded in a student's own code, would foster deeper understanding and engagement, but creating such customized instructional materials has historically been labor-intensive for instructors.

# Method

The researchers developed `InjectEd`, a modular agentic AI system leveraging Large Language Models (LLMs) (specifically GPT-4o-mini) and tool-driven reasoning pipelines. The full system comprises four autonomous agents:

*   **Injector Agent:** Inserts specific CWE-aligned vulnerabilities into a student's own assignment code. It uses Abstract Syntax Tree (AST) analysis to identify viable modification regions and employs syntax and behavioral validation tools to ensure the injected code compiles and preserves core functionality.
*   **Evaluator Agent:** Assesses the pedagogical quality of each injected code variant, scoring it on dimensions like relevance, cognitive load, and semantic coherence. (In the reported study, this role was performed manually by the instructor).
*   **Ranker Agent:** Selects the most pedagogically valuable CWE injection from a pool of candidates based on the Evaluator's feedback. (In the reported study, this role was performed manually by the instructor).
*   **Learning Outcome Generator Agent:** Transforms the selected injection into personalized formative assessments, including CWE explanations, multiple-choice questions, and open-ended reflection prompts. (In the reported study, this role was performed manually by the instructor).

The study deployed the `Injector Agent` in two undergraduate computer science courses (N=71). Students' final project code was used. For the study, the instructor manually vetted the injected outputs, selected the most useful examples, and developed uniform reflection questions. Students were randomly assigned to a **treatment group** (reviewed their own project code with an LLM-injected vulnerability) or a **control group** (received a generic, textbook-style example of the same CWE). A post-project survey with Likert-scale items and open-ended questions measured perceived understanding, clarity, relevance, and engagement.

# Impact

The study's findings highlight the potential and areas for refinement for personalized secure programming education:

*   **Quantitative Results:**
    *   **Statistically Significant:** Students in the `InjectEd` group reported a statistically significant **reduction in reported confusion** compared to the control group (p<.05, small to medium effect size), suggesting improved conceptual clarity.
    *   **Trends (not significant):** While not statistically significant, the `InjectEd` group consistently rated learning impact measures (e.g., perceived understanding, fixing capability, real-world connection) slightly higher than the control group.
*   **Qualitative Results:**
    *   Students overwhelmingly found the LLM-injected vulnerabilities in their *own code* to be **more relevant, clearer, and more engaging** than generic textbook examples.
    *   Many described the experience as "eye-opening," prompting them to "think differently about their code" and reflect more deeply on their own security practices.
    *   The personalized flaws were often perceived as "subtle" and "realistic," enhancing their instructional value.
*   **Limitations & Future Work:**
    *   The lack of widespread statistical significance for learning outcomes suggests the need for further studies with larger sample sizes and potentially longitudinal evaluations over multiple injections or projects to capture cumulative benefits.
    *   Variability in injection quality and occasional mismatches between the randomly selected CWEs and student code highlighted the importance of integrating the `Evaluator` and `Ranker` agents more fully, or refining the injection selection strategy to ensure optimal pedagogical alignment.
    *   Future work aims for more comprehensive evaluation, improved adaptive selection of vulnerabilities based on student code characteristics, and seamless integration with instructor feedback.