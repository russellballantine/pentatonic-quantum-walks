"""
PROJECT: P-QW Simulation Framework
FILE: src/disorder_robustness.py
PATHWAY: 3 (Robustness to Spatial Hopping Noise)

Measures wave-packet structural immunity against randomized kinetic bond disorder 
(J +/- delta_J) across multiple lattice configurations.
"""

import os
import yaml
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

def generate_disordered_hamiltonian(N, J, lmbda, alpha, delta_J):
    """
    Constructs a 1D tight-binding Hamiltonian with an incommensurate potential
    and off-diagonal structural hopping noise (bond disorder).
    """
    H = np.zeros((N, N), dtype=complex)
    
    # Generate uncorrelated random off-diagonal fluctuations [-delta_J, +delta_J]
    noise = np.random.uniform(-delta_J, delta_J, N)
    
    for i in range(N - 1):
        actual_hopping = -(J + noise[i])
        H[i, i + 1] = actual_hopping
        H[i + 1, i] = actual_hopping
        
    # Enforce periodic boundary conditions with noise
    boundary_hopping = -(J + noise[-1])
    H[0, N - 1] = boundary_hopping
    H[N - 1, 0] = boundary_hopping
    
    # Diagonal modulated potential
    for n in range(N):
        H[n, n] = lmbda * np.cos(2 * np.pi * alpha * n)
        
    return H

def run_disorder_experiment():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
        
    N = config["global_system"]["lattice_size"]
    J = config["global_system"]["kinetic_coupling"]
    lmbda = config["global_system"]["potential_amplitude"]
    
    samples = config["disorder_system"]["disorder_samples"]
    delta_J = config["disorder_system"]["noise_amplitude"]
    eval_time = config["disorder_system"]["evaluation_time"]
    
    phases = config["topological_phases"]
    center_site = N // 2
    
    print(f"🔬 Starting Pathway 3 Experiment: N={N}, Lambda={lmbda}, Bond Disorder Delta_J={delta_J}")
    print(f" -> Averaging over {samples} randomized structural samples per configuration...")
    
    final_ipr_averages = {}
    
    for phase_key, phase_info in phases.items():
        alpha = phase_info["alpha"]
        label = phase_info["label"]
        
        sample_ipr_records = []
        
        for s in range(samples):
            H = generate_disordered_hamiltonian(N, J, lmbda, alpha, delta_J)
            energies, vectors = la.eigh(H)
            
            # Localized wave injection
            psi_0 = np.zeros(N, dtype=complex)
            psi_0[center_site] = 1.0
            
            # Dynamic time propagation to evaluation snapshot point
            c = vectors.T.conj() @ psi_0
            c_t = c * np.exp(-1j * energies * eval_time)
            psi_t = vectors @ c_t
            
            # Compute spatial Inverse Participation Ratio (IPR)
            ipr = np.sum(np.abs(psi_t) ** 4)
            sample_ipr_records.append(ipr)
            
        final_ipr_averages[label] = np.mean(sample_ipr_records)
        print(f"    ↳ {label:52} | Ensemble Mean IPR = {final_ipr_averages[label]:.4f}")

    # --- Plotting Peer-Review Telemetry Figure ---
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=200)
    
    # Injects text wrapping newlines into long incommensurate phase labels to block horizontal clipping
    names = []
    for lbl in final_ipr_averages.keys():
        name = lbl.split(" (")[0]
        if "Incommensurate" in name:
            name = name.replace("Phase ", "Phase\n")
        names.append(name)
        
    ipr_values = list(final_ipr_averages.values())
    
    bars = ax.bar(names, ipr_values, color=['#1f77b4', '#d62728', '#2ca02c', '#ff7f0e'], alpha=0.85, width=0.45)
    
    # Value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.4f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax.set_title(f"Lattice Robustness Under Kinetic Bond Disorder (Snapshot $t={eval_time}$)", fontsize=11, fontweight='bold', pad=12)
    ax.set_ylabel(r"Ensemble Mean Inverse Participation Ratio $\langle \mathrm{IPR} \rangle$", fontsize=10)
    ax.set_xlabel("Topological Lattice Configuration Class", fontsize=10, labelpad=10)
    ax.set_ylim(0, max(ipr_values) * 1.2)
    
    # Parameters box overlay
    info_str = f"Disorder Metrics:\n$\delta J = \pm {delta_J}$\nSamples = {samples}\n$\\lambda = {lmbda}$"
    ax.text(0.02, 0.95, info_str, transform=ax.transAxes, verticalalignment='top', fontsize=8.5,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#f8f9fa', alpha=0.9, edgecolor='#e9ecef'))

    plt.tight_layout()
    
    output_path = "docs/images/disorder_robustness_comparison.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()
    print(f"\n✅ Disorder simulation complete. Visualization saved to: {output_path}")

if __name__ == "__main__":
    run_disorder_experiment()
