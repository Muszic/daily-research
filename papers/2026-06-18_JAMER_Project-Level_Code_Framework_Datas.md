# JAMER: Project-Level Code Framework Dataset and Benchmark on Professional Game Engines

- **Category:** Software Engineering
- **Date:** 2026-06-18
- **Link:** http://arxiv.org/abs/2606.19830v1

---
This paper introduces **JAMER**, the first project-level game code framework dataset and benchmark built on a professional game engine, Godot.

---

### Problem

AI-driven game development has seen progress in asset generation, gameplay design, and web-based game coding. However, **project-level code engineering on professional game engines remains largely unexplored.** This gap exists due to two main challenges:
1.  **Absence of large-scale datasets:** There's no reliable way to filter high-quality projects from noisy open-source repositories for this complex domain.
2.  **Lack of deterministic evaluation methods:** Traditional unit testing is insufficient for capturing context-dependent, interactive runtime game behaviors. Existing alternatives (hand-written scripts, VLM/LLM-based scoring) are either prohibitively expensive to scale or introduce subjectivity and lack reproducibility.

### Method

The authors address these challenges by leveraging the Godot engine and Game Jam competitions:

1.  **Data Source & Engine:** They identify Game Jam competitions as a source of thousands of compact, complete, open-source game projects. Godot's text-based format and headless execution mode enable automated processing and deterministic runtime behavior collection.
2.  **Deterministic Verification Pipeline:** A four-level pipeline is designed to filter and evaluate projects:
    *   **L1: File Integrity:** Verifies project structure, Godot version, and reachable file references.
    *   **L2: Compilation Correctness:** Runs headless Godot compilation to check for syntax, type errors, and essential code patterns.
    *   **L3a: Runtime Stability:** Launches the game headless for 30 seconds without input to verify no crashes.
    *   **L3b: Runtime Behavior Collection:** Automatically generates a deterministic input strategy based on LLM-assisted project annotations (`eval_config.json`) and runs the game for 60 seconds, collecting multi-dimensional behavioral data (e.g., node changes, position changes, event counts, signal triggers). This step is crucial for behavioral evaluation, not just pass/fail.
3.  **Dataset Construction:**
    *   From over 240,000 candidate repositories, the pipeline distills **8,133 verified Godot projects.**
    *   **JamSet:** Comprises 7,833 projects, processed into multi-turn training data (ranging from 21K to 197K tokens) for fine-tuning LLMs.
    *   **JamBench:** A subset of 300 manually verified projects, used as the benchmark test set. Projects are categorized by code size (Small, Medium, Large) and cover over 40 game genres.
4.  **Benchmark Tasks:**
    *   **Task 1: Theme-driven Generation:** Models generate a complete Godot project from scratch, given a Game Jam theme (with or without a gameplay description).
    *   **Task 2: Multi-granularity Code Completion:** Models complete missing code portions within existing projects at function, script, or full-script levels.
5.  **Evaluation Metrics:**
    *   **Compilation Pass Rates:** L1, L2, L3a verify basic project functionality.
    *   **Structural Completeness Score (SCS):** Measures the static structural coverage of generated code (e.g., script count, scene count, function count, node count) against reference projects or dataset means.
    *   **Behavioral Alignment Score (BAS):** Measures the similarity of runtime behaviors (collected via L3b) between generated and reference projects across 7 numeric and 1 set dimension. This provides an objective, scalable measure of functional correctness beyond just compilation.

### Impact

1.  **New Benchmark and Dataset:** JAMER provides the community with the first large-scale, project-level game code framework dataset (JamSet) and benchmark (JamBench) on a professional game engine, filling a critical void in AI-driven game development research.
2.  **Revealed Capability Cliff in LLMs:** Evaluations of 9 frontier LLMs and Code Agents on JamBench reveal a significant "capability cliff": runtime pass rates for code completion (Task 2a) drop drastically from 80.4% on small projects to 5.7% on large ones, highlighting the difficulty for current models to handle increasing project scale and complexity.
3.  **Limitations of Code Agents:** Code Agents significantly improve compilation pass rates but yield virtually no gains in runtime behavioral quality. This indicates that the bottleneck for project-level game code generation is not merely syntactic correctness or simple bug fixing, but rather architectural design, complex inter-file logic, and emergent runtime behavior.
4.  **Effective Training Data:** Fine-tuning on JamSet validates its effectiveness as training data, improving base models' compilation rates, structural completeness, and their adoption of human-like engineering practices (e.g., input abstraction, global state management).
5.  **Public Availability:** All data and code for JAMER are publicly available, fostering open research and development in this nascent field.