# NeuroCommitSSM: Decision-Centric Shared Autonomy for Safe Assistive Manipulation via EEG-EMG-ET Commit Readiness

- **Category:** Robotics
- **Date:** 2026-07-16
- **Link:** http://arxiv.org/abs/2607.15395v1

---
Here's a summary of the research paper "NeuroCommitSSM: Decision-Centric Shared Autonomy for Safe Assistive Manipulation via EEG–EMG–ET Commit Readiness" in Markdown:

---

### Problem

Current assistive robotic manipulation systems primarily focus on deciphering *what* a user intends to do (intent recognition) but largely neglect the crucial aspect of *when* it is safe and appropriate to execute that intent. This leads to several significant challenges:

*   **False Activations:** Multimodal biosignals (EEG, EMG) are noisy and prone to false positives during periods of user rest (no intent to act), resulting in erroneous robot actions and user frustration.
*   **Decision Instability:** Traditional methods like thresholding or temporal smoothing conflate recognition confidence with readiness to commit, leading to unstable decision boundaries, especially near rest-action transitions.
*   **Lack of Feasibility Checks:** Even with correct intent, execution can be unsafe or impossible due to environmental obstacles, unreachable robot poses, joint limits, or potential collisions. Existing systems often lack formal multi-state supervisors that couple user readiness with real-time robot and scene feasibility.
*   **Absence of Standardized Datasets:** There's a lack of synchronized, multimodal biosignal datasets (EEG, EMG, Eye-tracking) for functionally complete Activities of Daily Living (ADL) tasks, hindering robust development and benchmarking of assistive interfaces.

### Method

NeuroCommitSSM is a decision-centric framework designed to address the "when to execute" problem for safe assistive manipulation:

1.  **Multimodal Signal Acquisition & Preprocessing:**
    *   Synchronized electroencephalography (EEG), electromyography (EMG), and eye-tracking (ET) signals are collected from users performing 5 ICF-aligned ADL tasks.
    *   A deterministic pipeline preprocesses these signals, including filtering, re-referencing (EEG), rectification (EMG), and validity checks/interpolation (ET), and segments them into 2.0-second windows labeled (ACTION/REST) using an HSMM-based pipeline.
    *   Data is evaluated under Leave-One-Subject-Out (LOSO) cross-validation and seven sensor-dropout scenarios (S0: all sensors, S1-S6: various combinations of missing/unimodal sensors) to test generalization and robustness.

2.  **NeuroCommitSSM Architecture (Intent-to-Commit Model):**
    *   **Modality-Specific Encoders:** NeuroCommitSSM employs neurophysiology-aware encoders for EEG (multiscale depthwise filterbank, virtual channel weighting), EMG (envelope and burst proxies with learned synergy channels), and ET (velocity/acceleration proxies, salient event tokens).
    *   **Uncertainty-Weighted Multimodal Fusion:** The encoded tokens from each modality are fused using uncertainty-aware weighting based on modality availability and reliability cues. This fusion is regularized by an entropy penalty to prevent single-modality dominance and is designed to perform robustly under sensor dropout.
    *   **Joint Prediction Heads:** The fused representation predicts three outputs: (i) REST vs. ACTION classification, (ii) specific task class (T1-T5) for ACTION windows, and (iii) a continuous `commit-readiness score` (c_t ∈ [0,1]).
    *   **Dwell/Hysteresis Filtering:** The continuous `commit-readiness score` is converted into discrete commit events using a two-state hysteresis filter with a dwell time, which actively rejects brief spikes and stabilizes commit decisions.

3.  **HAC Shared-Autonomy Supervisor:**
    *   A three-state finite-state supervisor (HOLD–ASSIST–COMMIT) is implemented in ROS2.
    *   It gates robotic execution by integrating the action-gated commit-readiness signal with real-time feasibility checks from the robot and environment.
    *   **Perception Feasibility:** A markerless RGB-D computer vision pipeline provides `f_cv(t)` (target visibility, depth support, scene stability, obstacle proximity).
    *   **Robot Feasibility:** Checks `f_robot(t)` include Inverse Kinematics (IK) solvability, collision-free planning, and joint-limit satisfaction.
    *   The system only enters the COMMIT state if *both* the dwell/hysteresis gate is active (user readiness) *and* perception and robot feasibility cues are simultaneously stable for a predefined period. It features anti-flap safeguards and abort/recovery behaviors.

4.  **Hardware-in-the-Loop (HIL) Validation:**
    *   The complete system is validated on a Kinova Gen3 robotic arm using repeatable HIL replay of recorded biosignals, allowing for analysis of false starts, infeasible starts, abort rates, and task success/safety.

5.  **Dataset Release:** The paper introduces and publicly releases a novel, synchronized EEG–EMG–ET dataset for functionally complete, ICF-aligned assistive ADL intent decoding, benchmarked under a balanced-window LOSO protocol.

### Impact

NeuroCommitSSM demonstrates significant advancements in safe and reliable assistive manipulation:

*   **Superior Safety and Reduced False Positives:** Achieves high action-balanced accuracy (0.950) with remarkably low false commit events (0.75 FP/1k REST) in nominal conditions. This drastically reduces the risk of unintended robot actions and user frustration compared to baselines which can have orders of magnitude higher false positives (e.g., TCN: 99.95 FP/1k REST).
*   **Robustness to Sensor Loss:** Maintains strong performance (e.g., 0.701 action-balanced accuracy with ET-only, 0.29 FP/1k REST with EEG-only) and stable state transitions even under severe sensor dropout scenarios, outperforming baselines that collapse under similar conditions.
*   **Enhanced Execution Safety and Stability:** The HAC supervisor, with its integrated feasibility checks, significantly reduces false starts and decision instability during HIL validation on a physical robot. It prevents unsafe motions without compromising task success or responsiveness.
*   **Decision-Centric Paradigm:** Establishes a novel "intent-to-commit" pipeline that effectively models *when* to execute, moving beyond mere intent classification.
*   **Valuable Dataset Contribution:** The release of the first synchronized EEG–EMG–ET dataset for ICF-aligned ADL tasks provides a critical, standardized resource for the assistive robotics and BCI research communities.