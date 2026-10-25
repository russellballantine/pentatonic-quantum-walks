================================================================================
          PROJECT MANIFEST: PENTATONIC QUANTUM WALKS (P-QW)
================================================================================

[PROJECT OVERVIEW]
An advanced quantum simulation framework uncoupling the physics of the untempered 
Spiral of Fifths into a standalone Continuous-Time Quantum Walk (CTQW) environment. 
By mapping irrational logarithmic frequency steps onto a 1D spatial lattice, 
the project simulates a native 1D Quasicrystal to explore the boundary lines 
between quantum wave-packet diffusion, fractal spectra, and localization.

[WORKSPACE MANAGEMENT STATE]
- Repository Name: pentatonic-quantum-walks
- Isolated Directory Path: ~/Developer/pentatonic-quantum-walks/
- Environment: Isolated Python local `.venv` active.
- Git Status: All tracking scripts, images, and requirements.txt staged and synchronized.
- Documentation: GitHub Pages (README.md) updated with recent telemetry.

[CORE ARCHITECTURE DEPLOYED]
1. `requirements.txt`: Formally updated via pip freeze to capture environment states.
2. `src/lattice.py`: Refactored to accept dynamic frequency parameter `alpha` 
   (defaults cleanly to native Spiral value alpha = log2(1.5)).
3. `src/simulation.py`: Handles state propagation and spatial wave injection.
4. `src/phase_transition.py`: Systematically sweeps Lambda vs Mean IPR. 
   Validated suppression of finite-size noise at N=250, t_max=100.
5. `src/butterfly.py`: Generates global Hofstadter fractal spectrum at Lambda=2.0.
6. `src/butterfly_zoom.py`: High-resolution micro-sweep ([0.55 -> 0.62]) isolating 
   the alpha=0.60 rational pinch point and the Golden Ratio boundary.
7. `docs/images/`: Stores phase_transition_sweep.png and hofstadter_butterfly_zoom.png.
8. `docs/research_notes/`: NOTE_01 and NOTE_02 fully logged and pushed.

[EMPIRICAL RECENT DISCOVERIES]
- Verified the Aubry-André localization threshold occurs precisely at Lambda = 2J, 
  where the peak potential energy scale perfectly balances the true 1D kinetic scale (2J).
- Microscale zoom mathematically isolates the Spiral of Fifths slice as a Cantor dust 
  regime sitting tightly on the rugged boundary of the robust Golden Ratio gap.

[NEXT STAGE: COMPARATIVE MATERIAL FRAMEWORK]
Ready to branch the workspace into a comparative analysis between different musical scales 
treated as unique quantum material crystals. 

Options for immediate pickup:
1. Build `src/scale_comparison.py` to launch the Pathway 1 Experiment: Run the Pentatonic 
   (Quasicrystal), Chromatic (Periodic Crystal), Augmented (Alternative Quasicrystal), and 
   Diminished (Symmetric Crystal) fields side-by-side to track wave-packet diffusion.
2. Advance to Pathway 2 or 3 to test spectral fractal dimension or structural robustness 
   against randomized hopping noise (J).
================================================================================
