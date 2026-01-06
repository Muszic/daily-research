# SingingBot: An Avatar-Driven System for Robotic Face Singing Performance

- **Category:** Artificial Intelligence
- **Date:** 2026-01-05
- **Link:** http://arxiv.org/abs/2601.02125v1

---
Here's a summary of the research paper "SingingBot: An Avatar-Driven System for Robotic Face Singing Performance" in Markdown format:

---

## SingingBot: An Avatar-Driven System for Robotic Face Singing Performance

### Problem

Existing robotic facial animation methods primarily focus on conversational speech or static expression mimicry. These approaches struggle to meet the high demands of robotic singing, which requires:
1.  **Continuous and coherent emotional expression:** Singing necessitates sustained and evolving emotional displays, unlike discrete conversational expressions.
2.  **High-fidelity lip-audio synchronization:** Specific lyrical articulations and prolonged vowel sounds in singing demand precise lip movements.
3.  **Broad emotional breadth:** Appealing singing performances require a wide range of expressive emotions, which current methods, constrained by limited data or fixed expression libraries, fail to achieve.
4.  **Generalizability:** Data-driven methods often lack sufficient paired robot-expression data to generalize to the diverse and nuanced expressions of singing.

### Method

SingingBot proposes a novel avatar-driven framework to generate expressive robotic face singing performances:

1.  **Portrait Animation Synthesis:**
    *   Leverages a pre-trained video diffusion model (e.g., Hallo3) embedded with extensive human priors.
    *   Synthesizes vivid 2D singing avatar videos from vocal audio, a reference portrait image, and a text prompt. This step provides a rich source of emotional and expressive guidance, overcoming data scarcity in the robotic domain.

2.  **Facial Expression Retargeting:**
    *   **Avatar Facial Dynamics Extraction:** Extracts 52-dimensional ARKit blendshape coefficients (semantic expressions like `jawOpen`, `mouthStretch`) from the synthesized avatar video using MediaPipe. These are then smoothed to ensure temporal coherence.
    *   **Semantic-Oriented Avatar to Robot Expression Transfer:** Instead of learning a black-box mapping, a novel "Semantic-Oriented Piecewise Function Design" is employed.
        *   Manually designed piecewise linear functions map avatar blendshape parameters to the robot's specific motor control values.
        *   This strategy explicitly accounts for the structural differences between human facial muscles and robot actuators (e.g., handling missing physical counterparts for some blendshapes, unifying asymmetric expressions).
        *   The mapped motor values are combined with a rest pose, and head movements are controlled by mapping the avatar's 3-DoF pose to neck motors.

### Impact

SingingBot significantly advances robotic singing capabilities with the following impacts:

1.  **Superior Performance:** Achieves state-of-the-art results in both lip-audio synchronization (lower LSE-D, higher LSE-C) and, critically, dramatically richer emotional expressiveness (EDR an order of magnitude higher) compared to existing data-driven baselines.
2.  **Novel Emotional Metric:** Introduces the "Emotion Dynamic Range (EDR)" metric, based on the Valence-Arousal (V-A) space, to quantitatively measure the breadth and richness of emotional expression in robotic performances, highlighting its importance for appealing singing.
3.  **High Perceptual Quality:** User studies confirm that SingingBot produces the most realistic, emotionally resonant, and lip-synchronized robotic singing performances, leading to superior audience perception.
4.  **Enhanced Realism and Nuance:** Qualitatively, the system generates plausible lip shapes, captures large-amplitude movements, prolonged vowels, and subtle micro-expressions essential for conveying rich emotions in singing.
5.  **Generalizability and Controllability:** By leveraging extensive human priors from video diffusion models, the system exhibits enhanced generalizability and emotion diversity. It also offers stylistic control over the singing performance through different reference portraits.
6.  **Progress in Human-Robot Interaction:** Takes a meaningful step towards more empathetic and natural Human-Robot Interaction by enabling robots to perform emotionally engaging and coherent singing.