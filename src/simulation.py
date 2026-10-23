import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
from lattice import construct_aubry_andre_hamiltonian

def run_quantum_walk_simulation(n_sites=21, total_time=5.0, steps=100, Lambda=2.5):
    """Evolves a localized initial state vector under the Pentatonic field."""
    H = construct_aubry_andre_hamiltonian(n_sites=n_sites, J=1.0, Lambda=Lambda)
    
    # Define time steps
    times = np.linspace(0, total_time, steps)
    
    # Initial state: Particle completely localized at the center site (Root Note)
    psi_0 = np.zeros(n_sites, dtype=complex)
    psi_0[n_sites // 2] = 1.0
    
    # Track spatial probability distribution profiles over time
    probability_history = []
    
    # Unitary Time Evolution Execution Loop
    for t in times:
        # Compute the matrix exponential propagator: U(t) = exp(-i * H * t)
        U = la.expm(-1j * H * t)
        psi_t = np.dot(U, psi_0)
        
        # Capture Born rule state probabilities: P(x) = |psi|^2
        prob = np.abs(psi_t)**2
        probability_history.append(prob)
        
    return times, np.array(probability_history)

def plot_simulation_results(probability_history, Lambda):
    """Renders a spatial-temporal heatmap tracking the quantum walk."""
    plt.figure(figsize=(10, 6))
    plt.imshow(
        probability_history.T, 
        cmap="magma", 
        aspect="auto", 
        origin="lower",
        extent=[0, probability_history.shape[0], 0, probability_history.shape[1]]
    )
    plt.colorbar(label="Quantum Probability Density")
    plt.title(f"Pentatonic Quantum Walk Space-Time Evolution ($\lambda$ = {Lambda})")
    plt.xlabel("Simulation Time Steps")
    plt.ylabel("Physical Qubit / Lattice Index")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Test a heavily localized state landscape (High Lambda = 3.0)
    print("🔮 Simulating Pentatonic Quantum Walk Wave-Packet Dynamics...")
    times, history = run_quantum_walk_simulation(n_sites=21, total_time=10.0, Lambda=3.0)
    plot_simulation_results(history, Lambda=3.0)

