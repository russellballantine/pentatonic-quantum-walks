# Project Manifest: Pentatonic Quantum Walks (P-QW)
**Current State Archive:** October 2026  
**Core Thesis:** Evaluating quantum wave-packet dynamics on 1D tight-binding lattices modulated by incommensurate potentials derived from historical musical tuning steps.

---

## 🔬 Core Academic Discoveries & Telemetry
1. **Pathway 1 (Spatial Dynamics):** In a sub-critical potential regime ($\lambda = 1.5$, $N=201$, $t=50$), the Spiral-of-Fifths lattice ($\alpha = \log_2(1.5)$) exhibits severe sub-diffusive trapping ($\langle x^2 \rangle \approx 286.56$, $\text{IPR} \approx 0.0581$), suppressing transport by over an order of magnitude compared to a standard ballistic periodic metal baseline.
2. **Pathway 2 (Spectral Topology):** Applied a 1D box-counting regression across the dense eigenvalue spectrum ($N=1000$) exactly at the self-dual Aubry-André critical boundary ($\lambda = 2.0$). The Spiral-of-Fifths configuration fractures into a deeply fragmented Cantor dust with an exceptionally low Hausdorff dimension of **$D_f = 0.5744$** (compared to the uniform crystalline baseline of $D_f = 0.9877$).
3. **Pathway 3 (Disorder Immunities):** Simulated a high-amplitude uncorrelated kinetic bond disorder envelope ($\delta J = \pm 0.3$, averaged across 50 random ensemble seeds at $t=30$, $\lambda = 1.5$). The Spiral-of-Fifths topology demonstrates robust **topological shielding**, maintaining a tight state confinement profile ($\langle \text{IPR} \rangle = 0.1356$) that out-localizes alternative incommensurate phases (like Major-Thirds) by nearly 2x.

---

## 📂 Active Repository Mapping
* `config.yaml`: Shared, centralized simulation inputs matrix (System size, couplings, noise ceilings, temporal arrays).
* `src/lattice.py`: Verified object-oriented physics engine; constructs tridiagonal Hermitian Hamiltonians with periodic boundaries.
* `src/diffusion_analysis.py`: Executes Pathway 1 dynamics and outputs `docs/images/scale_diffusion_comparison.png`.
* `src/spectral_dimension.py`: Executes Pathway 2 box-counting regressions and outputs `docs/images/spectral_fractal_dimension.png`.
* `src/disorder_robustness.py`: Executes Pathway 3 stochastic noise sweeps and outputs `docs/images/disorder_robustness_comparison.png`.
* `tests/test_physics.py`: Automated `pytest` suite verifying physical conservation laws (Strict matrix Hermiticity and unitary total probability integration).

---

## 📝 Next Steps for Manuscript Assembly
* **Reframing Strategy:** Strictly avoid subjective musical or biological descriptions in the core text. Structure the manuscript layout entirely around Topological Signal Analysis, Quasicrystalline Transport Exponents, and Quantum Complexity Metrics.
* **Target Journals:** *Chaos, Solitons & Fractals*, *Journal of Mathematics and Music*, or computational/condensed-matter physics archives.
* **Writing Platform:** Transition to an online Overleaf portal using a standard American Physical Society (APS) `revtex4-2` document class template to completely bypass local compiler path errors.
