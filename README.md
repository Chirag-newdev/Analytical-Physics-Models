---
title: Analytical Physics Models
emoji: ⚛️
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
pinned: false
---


# Analytical Physics Models

> Python simulations of analytical physics models combining rigorous mathematical derivations with computational visualizations of classical and modern systems.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![License](https://img.shields.io/badge/License-MIT-green)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/satkarjuneja/Analytical-Physics-Models)

---

## Overview

This repository is a collection of physics models implemented from first principles. Each model is derived mathematically and then simulated computationally, with the goal of bridging theoretical understanding and numerical experimentation.

Tools used across simulations: `NumPy`, `Matplotlib`, `Manim` ,`Gaussian` ,`Psi4` ,etc.

---

## Models

| Model | Description | Key Concepts |
|---|---|---|
| [Particles in a Box](https://github.com/satkarjuneja/Analytical-Physics-Models/tree/main/Particles%20in%20a%20Box) | This folder contains Python scripts for simulating particles moving inside a 3D box. The goal is to explore how particles distribute themselves under different potential functions and to study their position profiles. | Quantum confinement, wavefunctions |
| [Ideal Electron](https://github.com/satkarjuneja/Analytical-Physics-Models/tree/main/Ideal%20Electron) | Scripts exploring Random walks of Electrons and related statistical properties. The focus is on Computational Experimentation to understand electron motion and its probabilistic behavior.| Probability Distributions,Expectations |
| [Calculating Activation and Reaction Energy Of  Reactions](https://github.com/satkarjuneja/Analytical-Physics-Models/tree/main/Calculating%20Activation%20and%20Reaction%20Energy%20Of%20An%20SN2%20Reaction) | Activation and reaction energy calculation for an reaction | Potential energy surfaces, transition state,Quantum Chemistry Methods (HF,DFT,etc.) |
| [Visualization Using VMD/Pymol](https://github.com/satkarjuneja/Analytical-Physics-Models/tree/main/Modelling%20Using%20VMD) | Basic Examples on how to use Tools like VMD,Pymol | VMD,Pymol,Visualization|

---

## Running a Simulation

Each model is self-contained. Navigate into the folder and run the script:

```bash
cd particles-in-box
python simulation.py
```

> Dependencies: `numpy`, `matplotlib` (and `manim` for animation-based models). Install individually as needed.

---
## Illustrations

<table>
  <tr>
    <td align="center">
      <img width="340" src="https://github.com/user-attachments/assets/6937740d-2095-45c9-9576-b356fd4d9142" />
      <br><code>Ideal_Electron/3dhist.py</code>
    </td>
    <td align="center">
      <img width="340" src="https://github.com/user-attachments/assets/87b935e6-f401-4318-9b38-71e0c65cf355" />
      <br><code>Calculating_Activation.../report.pdf</code>
    </td>
    <td align="center">
      <img width="340" src="https://github.com/user-attachments/assets/8ee57a9a-0144-4446-828a-db1fdae65aec" />
      <br><code>Monte_Carlo_Methods/estimate_Gaussian.py</code>
    </td>
  </tr>
</table>


## License

MIT — see [LICENSE](./LICENSE)
