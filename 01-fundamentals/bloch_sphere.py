"""
Bloch Sphere Visualization
Single qubit state representation from Coding with Qiskit Ep2
"""
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

def visualize_states():
    """Show different qubit states on Bloch sphere"""
    
    # State |0⟩
    qc_zero = QuantumCircuit(1)
    state_zero = Statevector.from_instruction(qc_zero)
    
    # State |1⟩
    qc_one = QuantumCircuit(1)
    qc_one.x(0)
    state_one = Statevector.from_instruction(qc_one)
    
    # State |+⟩ (superposition)
    qc_plus = QuantumCircuit(1)
    qc_plus.h(0)
    state_plus = Statevector.from_instruction(qc_plus)
    
    # State |+i⟩
    qc_plusi = QuantumCircuit(1)
    qc_plusi.h(0)
    qc_plusi.s(0)
    state_plusi = Statevector.from_instruction(qc_plusi)
    
    # Plot each state separately
    fig1 = plot_bloch_multivector(state_zero)
    fig1.suptitle('|0⟩ State (North Pole)')
    plt.savefig('01-fundamentals/bloch_zero.png', dpi=150)
    plt.close()
    
    fig2 = plot_bloch_multivector(state_one)
    fig2.suptitle('|1⟩ State (South Pole)')
    plt.savefig('01-fundamentals/bloch_one.png', dpi=150)
    plt.close()
    
    fig3 = plot_bloch_multivector(state_plus)
    fig3.suptitle('|+⟩ State (X+ axis)')
    plt.savefig('01-fundamentals/bloch_plus.png', dpi=150)
    plt.close()
    
    fig4 = plot_bloch_multivector(state_plusi)
    fig4.suptitle('|+i⟩ State (Y+ axis)')
    plt.savefig('01-fundamentals/bloch_plusi.png', dpi=150)
    plt.close()
    
    print("Bloch sphere visualizations saved:")
    print("  - bloch_zero.png: |0⟩ State (North pole - Z+ axis)")
    print("  - bloch_one.png: |1⟩ State (South pole - Z- axis)")
    print("  - bloch_plus.png: |+⟩ State (Equator - X+ axis)")
    print("  - bloch_plusi.png: |+i⟩ State (Equator - Y+ axis)")

if __name__ == "__main__":
    visualize_states()