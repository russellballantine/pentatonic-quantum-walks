"""
PROJECT: P-QW Simulation Framework
FILE: src/diffusion_analysis.py

Tracks and compares wave-packet diffusion dynamics across multiple incommensurate
and periodic topological phases using parameters defined in config.yaml.
"""

import os
import yaml
import numpy as np
import matplotlib.pyplot as plt
from src.lattice import TightBindingLattice

def calculate_msd(state, N):
    """Calculates Mean Squared Displacement (MSD) relative to the central injection site."""
    center = N // 2
    sites = np.arange(N) - center
    probabilities = np.abs(state) ** 2
    return np.sum((sites ** 2) * probabilities)

def main():
    # Load parameters from central configuration file
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
        
    N = config["global_system"]["lattice_size"]
    J = config["global_system"]["kinetic_coupling"]
    lmbda = config["global_system"]["potential_amplitude"]
    
    max_time = config["evolution_time"]["max_time"]
    dt = config["evolution_time"]["time_step"]
    times = np.arange(0, max_time + dt, dt)
    
    phases = config["topological_phases"]
    results = {}
    center_site = N // 2

    print(f"🔬 Executing Diffusion Analysis: N={N}, Lambda={lmbda}, J={J}")

    for phase_key, phase_info in phases.items():
        alpha = phase_info["alpha"]
        label = phase_info["label"]
        print(f" -> Evolving wave-packet on: {label}")
        
        # Instantiate the verified lattice object
        lattice = TightBindingLattice(N, J, lmbda, alpha)
        energies, vectors = lattice.diagonalize()
        
        # Initialize fully localized Kronecker delta state at the center node
        psi_0 = np.zeros(N, dtype=complex)
        psi_0[center_site] = 1.0
        
        # Project state into energy eigenbasis
        c = vectors.T.conj() @ psi_0
        
        msd_profile = []
        for t in times:
            # Propagate forward in time
            c_t = c * np.exp(-1j * energies * t)
            psi_t = vectors @ c_t
            
            # Record MSD metric
            msd_profile.append(calculate_msd(psi_t, N))
            
        results[label] = msd_profile

    # --- Plotting to Peer-Review Style Standards ---
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=200)
    
    for label, msd_values in results.items():
        ax.plot(times, msd_values, label=label, linewidth=2)
        
    ax.set_title("Quantum Wave-Packet Dispersion Across Tuning-Derived Topologies", fontsize=12, fontweight='bold', pad=12)
    ax.set_xlabel("Dimensionless Time Vector ($t$)", fontsize=10)
    ax.set_ylabel("Mean Squared Displacement ($\langle x^2 \\rangle$)", fontsize=10)
    ax.legend(frameon=True, facecolor='white', framealpha=0.9, edgecolor='none')
    
    # Text annotation block for system configurations
    param_box = f"Lattice Parameters:\n$N = {N}$\n$\\lambda = {lmbda}$ (Sub-critical)\n$J = {J}$"
    ax.text(0.02, 0.95, param_box, transform=ax.transAxes, verticalalignment='top', fontsize=9,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#f8f9fa', alpha=0.9, edgecolor='#e9ecef'))

    plt.tight_layout()
    
    output_path = "docs/images/spatial_diffusion_comparison.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()
    
    print(f"\n✅ Diffusion visualization successfully written to: {output_path}")

if __name__ == "__main__":
    main()
