# Pentatonic Quantum Walks & Fractal Localization Dynamics

An advanced quantum simulation framework exploring continuous-time quantum walks (CTQW) across non-periodic, untempered lattices. By treating the irrational logarithmic frequency steps of the pure **Spiral of Fifths** as a spatial physical landscape, this project models quasi-periodic field structures to study wave-packet diffusion, localization thresholds, and fractal energy states.

## 🔬 Theoretical Foundation

### 1. The Untempered Quasi-Crystal Mapping
Unlike standard equal-tempered musical scales which round values to fit a closed 12-note cycle, the pure **Spiral of Fifths** progresses endlessly via an irrational base-2 logarithm:
$$\alpha = \log_2(1.5) \approx 0.5849625...$$

Because $\alpha \in \mathbb{R} \setminus \mathbb{Q}$ (is an irrational number), mapping these steps sequentially along a 1D spatial lattice creates a structure that is perfectly ordered but entirely non-periodic. This mathematically mirrors the configuration of a physical **Quasicrystal** (such as a 1D Fibonacci chain).

### 2. The Aubry-André Tight-Binding Hamiltonian
We implement a continuous-time quantum walk where a single particle hops symmetrically between adjacent notes while encountering an on-site energy field modulated strictly by the untempered spiral coordinates:

$$H = -J \sum_{\langle i, j \rangle} (|i\rangle\langle j| + |j\rangle\langle i|) + \lambda \sum_{i} \cos(2\pi \alpha i) |i\rangle\langle i|$$

Where:
* **$J$**: The kinetic hopping amplitude (kinetic energy shifting probability between adjacent wires).
* **$\lambda$**: The potential energy coupling strength driven by the untempered spiral intervals.

## 🧪 Current R&D Phases
* **Phase 1: Wave-Packet Dynamics:** Tracking the temporal evolution ($U(t) = e^{-iHt}$) of a localized state injected at the root note to analyze the transition between quantum diffusion and **Anderson/Aubry Localization**.
* **Phase 2: Spectral Fractals:** Diagonalizing the pentatonic tight-binding matrix across varying tuning ranges to compute the energy eigenvalues and map the underlying quantum fractal geometries (**Hofstadter’s Butterfly**).

## 🛠️ Repository Architecture
* `src/lattice.py`: Generates the tight-binding matrices driven by the spiral fields.
* `src/simulation.py`: Handles unitary statevector time-propagation loops and numerical data extraction.
