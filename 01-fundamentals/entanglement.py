"""
Quantum Entanglement - Bell State
Demonstrates correlated measurement outcomes from Coding with Qiskit Ep3
"""
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def create_bell_state(shots=1000):
    """Create and measure Bell state (maximally entangled)"""
    # Create circuit: 2 qubits, 2 classical bits
    qc = QuantumCircuit(2, 2)
    
    # Bell state preparation
    qc.h(0)        # Superposition on qubit 0
    qc.cx(0, 1)    # CNOT: entangle qubit 0 and 1
    
    # Measure both
    qc.measure([0, 1], [0, 1])
    
    # Print circuit
    print("Quantum Circuit (Bell State):")
    print(qc.draw())
    print()
    
    # Simulate
    simulator = AerSimulator()
    result = simulator.run(qc, shots=shots).result()
    counts = result.get_counts()
    
    print(f"Bell State results ({shots} shots):")
    print(f"  |00⟩: {counts.get('00', 0)}")
    print(f"  |11⟩: {counts.get('11', 0)}")
    print(f"  |01⟩: {counts.get('01', 0)} (should be ~0)")
    print(f"  |10⟩: {counts.get('10', 0)} (should be ~0)")
    print("\nNote: Qubits always measured in same state (entangled)")
    
    # Visualize
    plot_histogram(counts)
    plt.title("Bell State: Perfect Correlation")
    plt.savefig('01-fundamentals/entanglement_results.png')
    print("\nHistogram saved: entanglement_results.png")
    plt.close()
    
    return counts

if __name__ == "__main__":
    create_bell_state()