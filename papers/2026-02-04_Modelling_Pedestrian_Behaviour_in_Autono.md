# Modelling Pedestrian Behaviour in Autonomous Vehicle Encounters Using Naturalistic Dataset

- **Category:** Robotics
- **Date:** 2026-02-04
- **Link:** http://arxiv.org/abs/2602.05142v1

---
Here's a summary of the research paper in Markdown format:

### Problem

The study addresses the critical need to understand how pedestrians adjust their **micro-level movement (speed changes)** moment-to-moment when interacting with Autonomous Vehicles (AVs) at midblock crossings. While pedestrian safety in mixed traffic is a major concern, existing discrete choice models often rely on linear utility specifications, limiting their ability to capture the nonlinear and dynamic effects present in human decision-making. Previous work using advanced models like ResLogit primarily focused on pre-crossing decisions (e.g., waiting time), leaving a gap in understanding the fine-grained, instantaneous speed adjustments pedestrians make *during* a crossing, especially using naturalistic data. The paper aims to answer:
1.  How do pedestrians modulate their speed when interacting with an AV at midblock crossings?
2.  Which spatial, temporal, and perceptual variables most influence these instantaneous movement decisions?
3.  Do pedestrians exhibit distinct directional or temporal sensitivities in perceived risk, particularly between frontal and rear collision exposure?

### Method

The researchers analyzed pedestrian–AV interactions using the **NuScenes dataset**, which provides naturalistic multimodal AV data from Singapore and Boston.
*   **Data Extraction:** They selected 137 unique adult pedestrians who completed a full midblock crossing in front of an AV, resulting in 1,875 valid decision time steps (resampled to 1-second intervals).
*   **Dependent Variable:** Pedestrian's instantaneous speed adjustment, categorized into a binary choice:
    *   **Choice 1:** Modest adjustment/deceleration (speed change increment between [0, 0.99]).
    *   **Choice 2:** Stronger acceleration (speed change increment between [0.99, 2.17]).
*   **Independent Variables (Indicators):** A comprehensive set of spatial, temporal, kinematic, and perceptual indicators were derived at each time step:
    *   **Kinematic:** Relative speed (pedestrian–AV), recent change in relative speed (3-sample moving average).
    *   **Perceptual/Conflict:** Visual looming rate (change in AV's apparent angular size), Frontal Collision Risk Proximity (CRP), Rear Collision Risk Proximity (CRP), and 3-second lagged versions of Frontal and Rear CRP. CRP combines Collision Angle Intensity (CAI) and Closing Time-to-Collision (CTTC).
    *   **Spatial:** Remaining distance to destination.
*   **Modeling Framework:** A **hybrid discrete choice–machine learning framework** based on the **Residual Logit (ResLogit) model** was employed. ResLogit embeds residual neural network components within a random utility maximization structure, allowing it to capture nonlinear patterns while retaining behavioral interpretability. The model was trained on 70% of the data and validated on 30%.

### Impact

The ResLogit model achieved **moderate predictive accuracy (0.58)**, indicating that while behavioral structure exists, significant variability in pedestrian micro-movements remains unexplained, possibly due to unmeasured psychological cues. Despite this, the study revealed several important insights into pedestrian behavior:

*   **Directional Asymmetry in Risk Perception:** Pedestrians exhibit strong directional sensitivities. Frontal Collision Risk Proximity (CRP) sometimes leads to acceleration (speeding up to clear the path), while Rear CRP consistently encourages deceleration (slowing down). This suggests distinct cognitive appraisals of threats from different directions.
*   **Mid-Crossing Threshold:** The "remaining distance to destination" showed a non-linear influence, with a peak around 15–20 meters where acceleration becomes more likely. This suggests a potential strategic shift or mid-crossing adjustment zone where pedestrians balance progress with perceived risk.
*   **Prioritization of Risk Cues:** Visual looming and CRP indicators had stronger influences on movement adjustments compared to purely kinematic relative speed cues, suggesting pedestrians prioritize risk-salient information.
*   **Temporal Integration of Risk:** Lagged CRP terms (3-second lag) showed different effects compared to instantaneous CRP, particularly for frontal risk (initial acceleration vs. later caution). This implies pedestrians integrate short-term exposure history into their decisions rather than reacting solely to current conditions.
*   **Dual Behavioral Tendencies:** The findings suggest pedestrians' micro-movements are driven by a blend of **risk perception** and **movement efficiency**.

These insights have significant implications for the design and programming of **Autonomous Vehicles**:
*   **Asymmetric Communication:** AV yielding and communication strategies should account for the directional asymmetry in pedestrian risk perception (e.g., emphasizing cues aligned with forward-facing risk).
*   **Dynamic Prediction Models:** AV prediction models need to incorporate non-linear patterns like the mid-crossing adjustment zone and integrate short-term risk history rather than assuming smooth, instantaneous responses.
*   **Prioritizing Risk-Salient Information:** AVs should prioritize understanding pedestrian intent based on risk-salient cues like looming and CRP, rather than solely on relative speed.

Future work includes integrating the influence of other road users, road geometry, group behavior, environmental conditions, and modeling a richer set of behavioral alternatives.