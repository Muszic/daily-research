# Decoupling Adaptive Control in TeaStore

- **Category:** Software Engineering
- **Date:** 2025-12-29
- **Link:** http://arxiv.org/abs/2512.23495v1

---
This paper discusses approaches to decouple self-adaptive control logic from the application code in microservice-based systems, using the Adaptable TeaStore specification as a case study.

### Problem

The Adaptable TeaStore specification proposes embedding monitoring (M) and effector (E) interfaces directly within microservices, leaving Analysis (A) and Planning (P) phases of the MAPE-K control loop open. This approach poses significant challenges for:

1.  **System-wide consistency:** Ensuring coordinated adaptations across multiple replicas of a microservice.
2.  **Planning:** Separating the deployment of adaptation strategies from their activation, allowing for complex scenarios like dark launches or conditional fallbacks.
3.  **Modularity:** Integrating self-adaptation logic non-invasively, making it reusable, and avoiding code duplication within microservices.

### Method

The paper examines four approaches to decouple adaptation logic, analyzing their trade-offs regarding fine-grained expressiveness, system-wide control, and reusability:

1.  **Architecture-based adaptation:** Externalizing the MAPE-K control loop into a distinct architectural layer (e.g., Rainbow-like frameworks) that interacts with the system via an abstract API. This approach gains reusability when built on a standardized platform like Kubernetes REST API.
2.  **Kubernetes Operator Pattern:** Extending Kubernetes with Custom Resource Definitions (CRDs) and custom controllers that declaratively reconcile the desired and actual state of domain-specific applications. This provides strong support for system-wide consistency through level-based reconciliation.
3.  **Aspect-Oriented Programming (AOP):** Programming language techniques that allow modularizing cross-cutting concerns, such as adaptation logic, by injecting code (advice) at specific points (join points) without modifying the core application code.
4.  **Context-Oriented Programming (COP):** Programming language techniques that enable dynamic activation of behavioral variations based on the current execution context, improving the modularity of context-specific adaptation logic within a microservice.

### Impact

*   The analysis reveals that architecture-based adaptation and the Kubernetes Operator pattern offer strong mechanisms for achieving system-wide consistency and explicit planning, particularly when leveraging the Kubernetes REST API.
*   AOP and COP provide effective means for modularizing adaptation logic *within* microservices, enhancing separation of concerns and reducing code duplication.
*   A key insight is that these approaches are **not mutually exclusive** and can be combined into a multi-tiered architecture, where external layers handle system-wide coordination and planning, while internal techniques manage fine-grained, modular adaptation within individual microservices.
*   The paper identifies essential missing elements in the current Adaptable TeaStore specification, providing concrete guidance for future extensions of the benchmark to support robust, reusable, and comparable self-adaptive implementations.