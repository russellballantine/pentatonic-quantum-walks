import numpy as np

def generate_spiral_potentials(n_sites=21):
    """
    Generates on-site energy values using the pure irrational 
    logarithmic steps of the Spiral of Fifths.
    """
    # log2(1.5) approx 0.5849625 (The irrational perfect fifth step)
    alpha = np.log2(1.5)
    sites = np.arange(n_sites)
    
    # Cosine modulation creates the Aubry-André quasi-periodic field
    potentials = np.cos(2 * np.pi * alpha * sites)
    return potentials

def construct_aubry_andre_hamiltonian(n_sites=21, J=1.0, Lambda=2.5):
    """
    Builds the tight-binding Hamiltonian matrix:
    - J: Kinetic hopping strength between adjacent nodes (symmetric)
    - Lambda: Potential energy scaling factor driven by the Spiral of Fifths
    """
    H = np.zeros((n_sites, n_sites))
    potentials = generate_spiral_potentials(n_sites)
    
    for i in range(n_sites):
        # 1. On-site Spiral Energy Potential (Diagonal elements)
        H[i, i] = Lambda * potentials[i]
        
        # 2. Kinetic Hopping to adjacent sites (Off-diagonal elements)
        if i < n_sites - 1:
            H[i, i + 1] = -J
            H[i + 1, i] = -J
            
    return H
