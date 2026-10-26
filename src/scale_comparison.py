"""
PROJECT: Pentatonic Quantum Walks (P-QW)
FILE: src/scale_comparison.py
PATHWAY: 1 (Comparative Material Framework)

Simulates wave-packet diffusion across four distinct tuning architectures 
treated as unique quantum material crystals. Tracks Mean Squared Displacement (MSD).
"""

import os
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

def generate_hamiltonian(N, J, lmbda, alpha):
    """
    Constructs a 1D tight-binding Hamiltonian with an Aubry-André style modulated potential.
    """
    H = np.zeros((N, N), dtype=complex)
    
    # Off-diagonal hopping terms (Kinetic Energy)
    for i in range(N - 1):
        H[i, i + 1] = -J
        H[i + 1, i] = -J
    # Periodic boundary conditions
    H[0, N - 1] = -J
    H[N - 1, 0] = -J
    
    # Diagonal site energies (Potential Energy mapped from frequency steps)
    for n in range(N):
        H[n, n] = lmbda * np.cos(2 * np.pi * alpha * n)
        
    return H

def calculate_msd(state, N):
    """
    Calculates the Mean Squared Displacement (MSD) relative to the center site.
    """
    center = N // 2
    sites = np.arange(N) - center
    probabilities = np.abs(state) ** 2
    return np.sum((sites ** 2) * probabilities)

def run_experiment():
    # --- SIMULATION PARAMETERS ---
    N = 201              # System size (odd number ensures a definitive center site)
    J = 1.0              # Kinetic coupling constant
    lmbda = 1.5          # Potential strength (Sub-critical regime where materials diverge)
    t_max = 50           # Time ceiling
    dt = 0.5             # Time resolution
    times = np.arange(0, t_max + dt, dt)
    
    # --- SCALE DESIGNATIONS ---
    scales = {
        "Chromatic (Periodic)":   {"alpha": 0.0,           "color": "#1f77b4"},
        "Pentatonic (Native QC)": {"alpha": np.log2(1.5),  "color": "#ff7f0e"},
        "Augmented (Alt QC)":    {"alpha": np.log2(1.25), "color": "#2ca02c"},
        "Diminished (Symmetric)": {"alpha": 0.25,          "color": "#d62728"}
    }
    
    results = {name: [] for name in scales}
    center_site = N // 2

    print(f"🔬 Initialising Pathway 1 Experiment: N={N}, Lambda={lmbda}, J={J}")
    
    for name, config in scales.items():
        print(f" -> Propagating wave-packet through: {name} (alpha = {config['alpha']:.5f})")
        
        # Build Hamiltonian & find eigenvalues/eigenvectors for clean time evolution
        H = generate_hamiltonian(N, J, lmbda, config["alpha"])
        eigenvalues, eigenvectors = la.eigh(H)
        
        # Define initial state localized at the center site
        psi_0 = np.zeros(N, dtype=complex)
        psi_0[center_site] = 1.0
        
        # Project initial state into the energy eigenbasis
        c = eigenvectors.T.conj() @ psi_0
        
        for t in times:
            # Time-evolve state vectors in the diagonal basis
            c_t = c * np.exp(-1j * eigenvalues * t)
            # Transform back to spatial position basis
            psi_t = eigenvectors @ c_t
            
            # Calculate and record structural metrics
            msd = calculate_msd(psi_t, N)
            results[name].append(msd)
            
    # --- DATA VISUALISATION ---
    plt.style.use('seaborn-v0_8-darkgrid' if 'seaborn-v0_8-darkgrid' in plt.style.available else 'default')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    
    for name, msd_values in results.items():
        ax.plot(times, msd_values, label=name, color=scales[name]["color"], linewidth=2.2)
        
    ax.set_title("Quantum Wave-Packet Diffusion Across Musical Crystals (Pathway 1)", fontsize=13, fontweight='bold', pad=15)
    ax.set_xlabel("Evolution Time ($t$)", fontsize=11)
    ax.set_ylabel("Mean Squared Displacement ($\langle x^2 \\rangle$)", fontsize=11)
    ax.legend(frameon=True, facecolor='white', edgecolor='none', fontsize=10)
    
    # Diagnostic text overlay
    param_text = f"System Parameters:\n$N$ = {N}\n$J$ = {J}\n$\\lambda$ = {lmbda} (Sub-critical)"
    ax.text(0.02, 0.95, param_text, transform=ax.transAxes, verticalalignment='top',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8, edgecolor='none'))

    plt.tight_layout()
    
    # Save directly to the project's documentation image repository
    output_dir = "docs/images"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "scale_diffusion_comparison.png")
    plt.savefig(output_path)
    plt.close()
    
    print(f"\n✅ Simulation complete. Telemetry visualization saved to: {output_path}")

if __name__ == "__main__":
    run_experiment()
