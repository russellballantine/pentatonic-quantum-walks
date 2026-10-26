"""
PROJECT: P-QW Simulation Framework
FILE: tests/test_physics.py

Unit tests verifying standard physical conservation laws on the generated lattices.
"""

import pytest
import numpy as np
from src.lattice import TightBindingLattice

def test_hamiltonian_hermitian():
    """Validates that H matches its conjugate transpose (H == H^dagger)."""
    lattice = TightBindingLattice(N=50, J=1.0, lmbda=2.0, alpha=np.log2(1.5))
    H = lattice.H
    # Check if matrix is equal to its conjugate transpose
    np.testing.assert_array_almost_equal(H, H.conj().T)

def test_probability_conservation():
    """Validates that time propagation preserves total system quantum probability (~1.0)."""
    N = 51
    lattice = TightBindingLattice(N=N, J=1.0, lmbda=1.5, alpha=np.log2(1.5))
    energies, vectors = lattice.diagonalize()
    
    # Initialize localized wave-packet state at center site
    psi_0 = np.zeros(N, dtype=complex)
    psi_0[N // 2] = 1.0
    
    # Evolve forward to arbitrary time t=25.0
    t = 25.0
    c = vectors.T.conj() @ psi_0
    c_t = c * np.exp(-1j * energies * t)
    psi_t = vectors @ c_t
    
    total_prob = np.sum(np.abs(psi_t) ** 2)
    assert pytest.approx(total_prob, abs=1e-9) == 1.0
