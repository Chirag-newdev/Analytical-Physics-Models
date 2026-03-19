# Analytical Physics Models

> Python simulations of analytical physics models combining rigorous mathematical derivations with computational visualizations of classical and modern systems.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![License](https://img.shields.io/badge/License-MIT-green)

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



## License

MIT — see [LICENSE](./LICENSE)
