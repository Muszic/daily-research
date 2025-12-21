# EPSM: A Novel Metric to Evaluate the Safety of Environmental Perception in Autonomous Driving

- **Category:** Robotics
- **Published:** 2025-12-17
- **Source:** [Original ArXiv Link](http://arxiv.org/abs/2512.15195v1)

---

## 🧐 Problem

Conventional performance metrics (e.g., precision, recall, F1-score, average precision) used to evaluate environmental perception systems in autonomous driving primarily assess overall detection accuracy. However, these metrics often fail to capture safety-relevant aspects. As a result, perception systems achieving high scores in these traditional metrics can still cause critical misdetections that could lead to severe accidents.

Furthermore, existing safety evaluation approaches for perception tasks typically consider object detection and lane detection independently. This overlooks the crucial interdependencies between these tasks, where an error in one (e.g., misclassification of a lane) can significantly influence the safety criticality of the other (e.g., an object in a nearby lane). There is a lack of a single, unified metric that jointly evaluates the safety of these most critical perception tasks while accounting for their interdependencies.

## 🛠️ Method

The authors propose **EPSM (Environmental Perception Safety Metric)**, a novel, lightweight metric designed for the joint safety evaluation of object and lane detection systems in autonomous driving, specifically incorporating their interdependencies.

EPSM comprises three main components:

1.  **Lightweight Object Safety Metric (`Sobj`):** This metric focuses on detection (removing tracking components from prior work) and is built upon:
    *   **Criticality (`Co`):** Determines the necessity of perceiving an object to avoid a safety-critical situation. It uses a multi-metric aggregation approach, combining Time-to-Collision (TTC), Time-To-Closest-Encounter (TTCE), minimum distance in closest encounter (`dTTCE`), and a bidirectional rating (for rear-end collisions). These are mapped to a continuous criticality score `C ∈ [0.0, 1.0]`. Vulnerable Road Users (VRUs) like pedestrians have a specialized circular criticality zone due to their unpredictable movement.
    *   **Severity (`Io`):** Quantifies the potential impact of a collision if an object is missed. It employs object-type specific logistic regression models:
        *   For VRUs, the model by Saad et al. is used, considering vehicle velocity and pedestrian age to predict fatality or serious injury probabilities, which are then mapped to a severity score `I ∈ [0.0, 1.0]`.
        *   For vehicles, the model by Malliaris et al. is used, considering relative velocity and impact direction to predict injury severities (MAIS 2+, MAIS 3+, fatal), also mapped to `I ∈ [0.0, 1.0]`.
    *   **Weighting (`Wo`):** The criticality and severity are combined (`Wo = Co * Io`). The final object safety score (`Sobj`) applies a "worst-case weighting" strategy, prioritizing the most safety-critical misdetections.

2.  **Lane Safety Metric (`Slane`):** This metric is based on an existing Lane Safety Metric (LSM) and evaluates three aspects:
    *   Longitudinal safety rating (detection range).
    *   Lateral safety rating (mean deviation between detected and ground-truth lanes).
    *   Scenario semantic rating (criticality of deviations based on driving context, e.g., impact velocity for opposing-lane collisions).

3.  **Combined Safety Score and Task Interdependence (`SF`):**
    *   The `Sobj` and `Slane` scores are first combined into an intermediate score (`Sp`) using a power mean function.
    *   This `Sp` is then fine-tuned based on a decision tree that models various scenarios where object and lane detection exhibit **interdependence**. For example:
        *   A "bonus" factor is applied if accurate lane detection can avoid a collision, even if an object in an adjacent lane is missed.
        *   A "penalty" factor is applied if an unsafe lateral lane detection coincides with a missed object within the detected lane, with the penalty's severity tied to the Time-to-Collision of the missed object.
    *   The final `SF` score `∈ [0.0, 1.0]` is then classified into five interpretable safety levels (e.g., "insufficient, high risk of fatality" to "very good, high probability of safe status").

The metric was evaluated using controllable statistical sensor models for object and lane detection on safety-critical scenarios extracted from the DeepAccident dataset.

## 📊 Impact

The EPSM demonstrates significant advantages over conventional performance metrics by effectively identifying safety-critical perception errors that traditional metrics fail to capture.

*   **Failure of Performance Metrics:** The paper illustrates with an exemplary scenario where conventional F1-score remained high (0.76-0.93), misleadingly indicating good perception, while EPSM's object safety score (`Sobj`) plummeted from 0.74 to 0.04 as an unperceived vehicle led to an impending collision. This highlights the crucial necessity for safety-centric evaluation.
*   **DeepAccident Evaluation:** On the DeepAccident dataset, while traditional performance metrics for both object and lane detection showed high mean scores (e.g., F1 > 0.95 for object detection), EPSM's final safety score (`SF`) had a mean of 0.552 and a minimum of 0.012 (representing potential fatalities). This accurately reflects the presence of severe accident scenarios within the dataset, which were overlooked by performance metrics.
*   **Comprehensive and Interpretable Safety Assessment:** EPSM provides a unified, single interpretable score that offers a more comprehensive and meaningful evaluation of perception safety. By integrating a novel lightweight object safety metric (with multi-metric criticality and object-type-based severity) and a lane safety metric, and crucially, by modeling the interdependencies between these tasks, EPSM offers a more holistic view of environmental perception safety.
*   The findings emphasize the importance of safety-centric evaluation methods for perception systems in autonomous driving, moving beyond simple accuracy metrics to truly assess accident prevention capabilities.
