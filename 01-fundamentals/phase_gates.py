"""
Phase Gates - Z, S, T
Demonstrates phase manipulation from Coding with Qiskit Ep4
"""
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

def demonstrate_phase_gates():
    """Show effect of different phase gates"""
    
    print("Creating phase gate visualizations...\n")
    
    # Base state: |+⟩
    base_qc = QuantumCircuit(1)
    base_qc.h(0)
    
    # Z gate (π phase)
    qc_z = base_qc.copy()
    qc_z.z(0)
    state_z = Statevector.from_instruction(qc_z)
    fig = plot_bloch_multivector(state_z, title='Z Gate: π phase on |+⟩')
    fig.savefig('01-fundamentals/phase_z.png', dpi=150)
    print("  ✓ phase_z.png saved")
    
    # S gate (π/2 phase)
    qc_s = base_qc.copy()
    qc_s.s(0)
    state_s = Statevector.from_instruction(qc_s)
    fig = plot_bloch_multivector(state_s, title='S Gate: π/2 phase on |+⟩')
    fig.savefig('01-fundamentals/phase_s.png', dpi=150)
    print("  ✓ phase_s.png saved")
    
    # T gate (π/4 phase)
    qc_t = base_qc.copy()
    qc_t.t(0)
    state_t = Statevector.from_instruction(qc_t)
    fig = plot_bloch_multivector(state_t, title='T Gate: π/4 phase on |+⟩')
    fig.savefig('01-fundamentals/phase_t.png', dpi=150)
    print("  ✓ phase_t.png saved")
    
    print("\nPhase gates demonstration complete!")
    print("\nPhase gates summary:")
    print("  Z gate: Adds π phase to |1⟩ component")
    print("  S gate: Adds π/2 phase to |1⟩ component")
    print("  T gate: Adds π/4 phase to |1⟩ component")
    print("\nEffect on |+⟩ state:")
    print("  Z|+⟩ = |-⟩  (flips on equator)")
    print("  S|+⟩ = |+i⟩ (rotates to Y axis)")
    print("  T|+⟩ = rotates 45° on equator")

if __name__ == "__main__":
    demonstrate_phase_gates()