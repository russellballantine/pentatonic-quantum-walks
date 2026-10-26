"""
PROJECT: P-QW Simulation Framework
FILE: src/lattice.py

Generates one-dimensional tight-binding Hamiltonians governed by modulated
incommensurate potential profiles for Continuous-Time Quantum Walks (CTQW).
"""

import numpy as np
import scipy.linalg as la

class TightBindingLattice:
    def __init__(self, N, J, lmbda, alpha):
        """
        Initializes a 1D modulated tight-binding lattice environment.
        """
        self.N = N
        self.J = J
        self.lmbda = lmbda
        self.alpha = alpha
        self.H = self._build_hamiltonian()

    def _build_hamiltonian(self):
        """Constructs the tridiagonal Hermitian matrix with periodic boundaries."""
        H = np.zeros((self.N, self.N), dtype=complex)
        
        # Off-diagonal kinetic energy assignment (hopping terms)
        for i in range(self.N - 1):
            H[i, i + 1] = -self.J
            H[i + 1, i] = -self.J
            
        # Enforce periodic boundary conditions (Ring topology)
        H[0, self.N - 1] = -self.J
        H[self.N - 1, 0] = -self.J
        
        # Diagonal potential energy modulation
        for n in range(self.N):
            H[n, n] = self.lmbda * np.cos(2 * np.pi * self.alpha * n)
            
        return H

    def diagonalize(self):
        """
        Solves the time-independent Schrödinger equation for the spatial matrix.
        Returns eigenvalues (energy bands) and corresponding eigenvectors.
        """
        return la.eigh(self.H)
