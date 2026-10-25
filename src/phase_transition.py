import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
from lattice import construct_aubry_andre_hamiltonian

def calculate_ipr(state):
    """Calculate the Inverse Participation Ratio (IPR) of a quantum state vector."""
    probabilities = np.abs(state) ** 2
    return np.sum(probabilities ** 2)

def run_lambda_sweep(lambda_min=0.1, lambda_max=4.0, steps=60, n_sites=250, t_max=100.0, num_t_steps=150):
    """Sweeps Lambda systematically to locate the localization transition using mean IPR."""
    lambda_vals = np.linspace(lambda_min, lambda_max, steps)
    mean_iprs = []
    
    # Define temporal resolution grid
    times = np.linspace(0, t_max, num_t_steps)
    center_idx = n_sites // 2  # Matches Center Index 10 if n_sites=21, scales dynamically
    
    # Initial localized wave packet injection
    psi_0 = np.zeros(n_sites, dtype=complex)
    psi_0[center_idx] = 1.0
    
    print(f"Starting parameter sweep across {steps} points for Lambda...")
    
    for lam in lambda_vals:
        # 1. Build Hamiltonian using your specific lattice function
        H = construct_aubry_andre_hamiltonian(n_sites=n_sites, J=1.0, Lambda=lam)
        
        # 2. Exact diagonalization for efficient time evolution
        eigenvalues, eigenvectors = la.eigh(H)
        
        # Project initial state onto the eigenbasis
        c_0 = eigenvectors.conj().T @ psi_0
        
        ipr_accumulator = 0.0
        
        # 3. Time evolution loop to sample spatial distribution
        for t in times:
            c_t = c_0 * np.exp(-1j * eigenvalues * t)
            psi_t = eigenvectors @ c_t
            ipr_accumulator += calculate_ipr(psi_t)
            
        # Record time-averaged structural localization for this Lambda
        mean_iprs.append(ipr_accumulator / num_t_steps)
        
    return lambda_vals, np.array(mean_iprs)

def plot_transition(lambda_vals, mean_iprs):
    """Plots the structural phase transition curve and saves the visual asset."""
    plt.figure(figsize=(8, 5))
    plt.plot(lambda_vals, mean_iprs, 'o-', color='#2ca02c', linewidth=2, label='Time-Averaged IPR')
    
    # Added 'r' prefix for raw string literal to support LaTeX correctly
    plt.axvline(x=2.0, color='r', linestyle='--', alpha=0.8, label=r'Theoretical Threshold ($\Lambda = 2J$)')
    
    plt.title('Aubry-André Phase Transition (Spiral of Fifths Lattice)', fontsize=12)
    plt.xlabel(r'Quasiperiodic Potential Amplitude ($\Lambda$)', fontsize=10)
    plt.ylabel(r'Mean Inverse Participation Ratio $\langle \mathrm{IPR} \rangle$', fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    
    output_path = 'docs/images/phase_transition_sweep.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Phase transition diagnostic plot successfully saved to: {output_path}")


if __name__ == "__main__":
    # Executing sweep with scaled site count to see a sharp phase transition elbow
    lambda_vals, mean_iprs = run_lambda_sweep(lambda_min=0.1, lambda_max=4.0, steps=60, n_sites=101)
    plot_transition(lambda_vals, mean_iprs)
