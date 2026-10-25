import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
from lattice import construct_aubry_andre_hamiltonian

def map_zoomed_butterfly(n_sites=200, Lambda=2.0, alpha_min=0.55, alpha_max=0.62, alpha_steps=400):
    """
    Performs a high-density spectral sweep over a targeted region of alpha
    to reveal micro-fractal structures around the Spiral of Fifths line.
    """
    alpha_vals = np.linspace(alpha_min, alpha_max, alpha_steps)
    alpha_points = []
    energy_points = []
    
    print(f"Executing high-res zoom sweep across {alpha_steps} points (\u03b1: {alpha_min} -> {alpha_max})...")
    
    for alpha in alpha_vals:
        # Utilizing larger n_sites to isolate clean, thin spectral lines in the zoom
        H = construct_aubry_andre_hamiltonian(n_sites=n_sites, J=1.0, Lambda=Lambda, alpha=alpha)
        eigenvalues = la.eigvalsh(H)
        
        for E in eigenvalues:
            alpha_points.append(alpha)
            energy_points.append(E)
            
    return alpha_points, energy_points

def plot_zoomed_butterfly(alpha_points, energy_points, Lambda):
    """Renders the high-resolution microscopic view of the Hofstadter spectrum."""
    plt.figure(figsize=(10, 8), facecolor='black')
    ax = plt.axes()
    ax.set_facecolor('black')
    
    # Using ultra-fine markers (s=0.1) and high density for crystalline resolution
    ax.scatter(alpha_points, energy_points, s=0.1, c='#00FFCC', alpha=0.8, edgecolors='none')
    
    # Native Spiral of Fifths line
    native_alpha = np.log2(1.5)
    ax.axvline(x=native_alpha, color='#FF3366', linestyle='-', alpha=0.8, linewidth=1.2,
               label=r'Spiral of Fifths Line ($\alpha \approx 0.58496$)')
    
    # Golden Ratio line (the primary topological boundary anchoring this wing)
    golden_alpha = 1 / ((1 + np.sqrt(5)) / 2)  # \phi - 1 \approx 0.61803
    ax.axvline(x=golden_alpha, color='#FFA500', linestyle='--', alpha=0.6, linewidth=1.0,
               label=r'Golden Ratio Boundary ($\alpha \approx 0.61803$)')
    
    plt.title(f"Hofstadter Micro-Spectrum (Zoom Range: [0.55 - 0.62], $\\Lambda = {Lambda}$)", 
              color='white', fontsize=13, pad=15)
    plt.xlabel(r'Targeted Modulation Field ($\alpha$)', color='white', fontsize=11)
    plt.ylabel(r'Energy Eigenvalues ($E$)', color='white', fontsize=11)
    
    # Formatting adjustments for deep-space visualization
    ax.tick_params(colors='white')
    ax.set_xlim(0.55, 0.62)
    ax.grid(True, color='#222222', linestyle=':', alpha=0.4)
    ax.legend(facecolor='#111111', edgecolor='#333333', labelcolor='white', loc='lower left')
    
    output_path = 'docs/images/hofstadter_butterfly_zoom.png'
    plt.savefig(output_path, dpi=400, facecolor='black', bbox_inches='tight')
    plt.close()
    print(f"Zoomed fractal spectrum successfully exported to: {output_path}")

if __name__ == "__main__":
    # Increased n_sites to 200 and alpha_steps to 400 for rich structural detail
    alpha_pts, energy_pts = map_zoomed_butterfly(n_sites=200, Lambda=2.0, alpha_steps=400)
    plot_zoomed_butterfly(alpha_pts, energy_pts, Lambda=2.0)
