# Physics-Informed Neural Systems for the Simulation of EUV Electromagnetic Wave Diffraction from a Lithography Mask

- **Category:** Artificial Intelligence
- **Date:** 2026-03-16
- **Link:** http://arxiv.org/abs/2603.15584v1

---
Here's a summary of the research paper:

### Problem
Simulating the diffraction of Extreme Ultraviolet (EUV) electromagnetic waves from lithography masks is a critically important but "massively computationally intensive" task in semiconductor manufacturing. Traditional rigorous electromagnetic (EM) simulators demand extensive computational resources, while existing approximation models are still resource-intensive and don't fully capture electromagnetic interaction nonlocality. Prior deep learning approaches, relying on supervised learning (e.g., CNNs, GANs), require large datasets, long training times, and often lack the necessary accuracy and generalization for 3D mask effects.

### Method
The paper introduces and evaluates **Physics-informed Neural Networks (PINNs)** and **Neural Operators (NOs)** for solving the EUV diffraction problem from 3D masks. These neural systems are trained in an unsupervised manner, leveraging the governing physical equations (Maxwell's equations, specifically systems for magnetic field components Hx and Hy) directly as part of the loss function, along with boundary conditions.

A **novel hybrid Waveguide Neural Operator (WGNO)** is proposed, which integrates the established Waveguide method. In this hybrid approach, the most computationally expensive component of the Waveguide method—solving a large global system of linear equations to determine mode amplitudes—is replaced by a neural network. The performance of these neural systems (PINNs, NOs, WGNO) is compared against modern numerical solvers like the Finite Element Method (FEM) and the high-fidelity Waveguide method itself, using benchmark problems with known exact solutions and realistic 2D and 3D mask models at 13.5 nm and 11.2 nm wavelengths.

### Impact
The research demonstrates that PINNs and neural operators achieve **competitive accuracy** while delivering **significantly reduced prediction times** compared to traditional numerical solvers. The proposed **WGNO architecture notably reaches state-of-the-art performance**. A key finding is the **pronounced generalizing properties** of the neural operators, meaning they can provide accurate solutions for unseen problem parameters, close to the accuracy achieved for trained parameters. These results offer a **highly efficient solution for accelerating the design and optimization workflows of next-generation EUV lithography masks**, crucial for advancing semiconductor manufacturing.