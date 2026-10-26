# RESEARCH NOTE 03: COMPARATIVE MATERIAL FRAMEWORK & TRANSPORT TELEMETRY
**Date:** October 26, 2026  
**Project:** Pentatonic Quantum Walks (P-QW)  
**Objective:** Pathway 1 Experiment - Wave-Packet Diffusion across Musical Crystal Classes  

## 1. Experimental Configuration
Continuous-Time Quantum Walks (CTQW) were simulated on a 1D spatial lattice to contrast transport physics across four distinct tuning topologies mapped as unique solid-state crystal lattices:
* **System Size ($N$):** 201 sites (Odd integer to establish true central injection site)
* **Kinetic Coupling ($J$):** 1.0 (Uniform spatial hopping)
* **Potential Modulation ($\lambda$):** 1.5 (Sub-critical Aubry-André regime)
* **Temporal Boundaries ($t_{max}$):** 50.0 ($\Delta t = 0.5$)
* **Initial State ($\psi_0$):** Fully localized Kronecker delta function at the central lattice node ($n = 100$).

---

## 2. Quantitative Telemetry Summary

| Quantum Material Crystal | Spatial Frequency Parameter ($\alpha$) | Final MSD ($\langle x^2 \rangle$) | Final IPR | Diffusion Regime |
| :--- | :--- | :--- | :--- | :--- |
| **Chromatic** | `0.00000` | **4981.66** | **0.0095** | Pure Ballistic ($x \sim t^2$) |
| **Diminished** | `0.25000` (Rational) | **1158.87** | **0.0356** | Quantized Gapped Bloch Transport |
| **Augmented** | `log2(1.25)` $\approx 0.32193$ | **963.56** | **0.0268** | Anomalous Intermediate Quasicrystalline |
| **Pentatonic** | `log2(1.5)` $\approx 0.58496$ | **286.56** | **0.0581** | Severe Sub-diffusion / Deep Cantor Trapping |

---

## 3. Core Physics Insights

### A. Chromatic Ballistic Expansion
With $\alpha = 0$, the potential energy landscape remains perfectly uniform. The wave-packet experiences zero backscattering, executing ideal quadratic expansion ($\langle x^2 \rangle \sim t^2$). This matches standard Bloch-wave propagation in an unmodulated 1D periodic crystal.

### B. Pentatonic Quasiparticle Trapping
The native Spiral of Fifths lattice topology ($\alpha = \log_2(1.5)$) exhibits an order of magnitude suppression in its Mean Squared Displacement compared to the periodic baseline. Despite the system operating below the true localized phase transition threshold ($\lambda < 2J$), the irrational spatial rhythm generates extensive destructive interference. The wave-packet remains deeply pinned near the injection center with a highly elevated final Inverse Participation Ratio (IPR = 0.0581).

### C. Symmetry vs. Incommensurability (Diminished vs. Augmented)
Up to $t \approx 30$, the Diminished (4-fold symmetric periodic crystal) and Augmented (Major-Thirds based incommensurate quasicrystal) paths evolve almost identically. Beyond this temporal horizon, their wave-packets diverge:
* **The Diminished Scale** settles into predictable, gapped ballistic behavior governed by its rational periodic boundary bands.
* **The Augmented Scale** encounters the structural limits of its alternative self-similar spatial frequency, slowing down as it enters an anomalous intermediate diffusion phase.

---

## 4. Visual Artifact Tracking
* **Telemetry Visual:** `docs/images/scale_diffusion_comparison.png` successfully saved, capturing the clean quadratic divergence of the periodic matrix against the heavy localization profiles of the quasicrystals.
