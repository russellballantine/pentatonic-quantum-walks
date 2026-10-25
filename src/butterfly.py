import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

def generate_custom_potentials(n_sites, alpha):
    """
    Generates on-site energy values using a flexible alpha parameter
    to map out the shifting periodicities of the lattice.
    """
    sites = np.arange(n_sites)
    return np.cos(2 * np.pi * alpha * sites)

def construct_dynamic_hamiltonian(n_sites=144, J=1.0, Lambda=2.0, alpha=0.58496):
    """
    Builds the tight-binding matrix with an adjustable irrational step alpha.
    - n_sites: Size of the lattice matrix (higher sizes yield sharper fractal resolution)
    """
    H = np.zeros((n_sites, n_sites))
    potentials = generate_custom_potentials(n_sites, alpha)
    
    for i in range(n_sites):
        # On-site potential modulated by alpha
        H[i, i] = Lambda * potentials[i]
        
        # Kinetic hopping elements
        if i < n_sites - 1:
            H[i, i + 1] = -J
            H[i + 1, i] = -J
            
    return H

def map_hofstadter_butterfly(n_sites=150, Lambda=2.0, alpha_steps=200):
    """
    Sweeps the irrational frequency step parameter alpha from 0 to 1
    and collects the energy eigenvalues to resolve the fractal butterfly spectrum.
    """
    # Sweep alpha across its full periodic domain
    alpha_vals = np.linspace(0.0, 1.0, alpha_steps)
    
    alpha_points = []
    energy_points = []
    
    print(f"Computing energy spectra across {alpha_steps} alpha points...")
    
    for alpha in alpha_vals:
        # Build Hamiltonian for the current alpha step
        H = construct_dynamic_hamiltonian(n_sites=n_sites, J=1.0, Lambda=Lambda, alpha=alpha)
        
        # Extract all eigenvalues (energy levels)
        eigenvalues = la.eigvalsh(H)
        
        # Accumulate coordinate pairs for the scatter plot
        for E in eigenvalues:
            alpha_points.append(alpha)
            energy_points.append(E)
            
    return alpha_points, energy_points

def plot_butterfly(alpha_points, energy_points, Lambda):
    """Plots and saves the Hofstadter Butterfly fractal spectrum."""
    plt.figure(figsize=(10, 8), facecolor='black')
    ax = plt.axes()
    ax.set_facecolor('black')
    
    # Scatter plot with high transparency and small markers to highlight fractal gaps
    ax.scatter(alpha_points, energy_points, s=0.3, c='#00FFCC', alpha=0.6, edgecolors='none')
    
    # Visual line marking your native Spiral of Fifths step (log2(1.5) ~ 0.58496)
    native_alpha = np.log2(1.5)
    ax.axvline(x=native_alpha, color='#FF3366', linestyle=':', alpha=0.7, 
               label=f'Spiral of Fifths Line ($\\alpha \\approx {native_alpha:.5f}$)')
    
    plt.title(f"Hofstadter's Butterfly Spectrum (Pentatonic Lattice, $\\Lambda = {Lambda}$)", 
              color='white', fontsize=14, pad=15)
    plt.xlabel(r'Modulation Frequency Field ($\alpha$)', color='white', fontsize=11)
    plt.ylabel(r'Energy Eigenvalues ($E$)', color='white', fontsize=11)
    
    # Style ticks and grid lines for a dark dashboard aesthetic
    ax.tick_params(colors='white')
    ax.grid(True, color='#333333', linestyle='--', alpha=0.5)
    ax.legend(facecolor='#111111', edgecolor='#333333', labelcolor='white', loc='upper right')
    
    output_path = 'docs/images/hofstadter_butterfly.png'
    plt.savefig(output_path, dpi=300, facecolor='black', bbox_inches='tight')
    plt.close()
    print(f"Fractal spectrum visualization successfully saved to: {output_path}")

if __name__ == "__main__":
    # Lambda=2.0 sits exactly at the critical point, perfect for beautiful fractal structures
    alpha_pts, energy_pts = map_hofstadter_butterfly(n_sites=120, Lambda=2.0, alpha_steps=250)
    plot_butterfly(alpha_pts, energy_pts, Lambda=2.0)
