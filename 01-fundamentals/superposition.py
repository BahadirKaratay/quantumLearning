"""
Quantum Superposition with Hadamard Gate
Demonstrates equal probability outcomes from Coding with Qiskit Ep1
"""
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def demonstrate_superposition(shots=1000):
    """Show superposition via Hadamard gate"""
    # Create circuit: 1 qubit, 1 classical bit
    qc = QuantumCircuit(1, 1)
    
    # Apply Hadamard (creates superposition)
    qc.h(0)
    
    # Measure
    qc.measure(0, 0)
    
    # Print circuit
    print("Quantum Circuit:")
    print(qc.draw())
    print()
    
    # Simulate
    simulator = AerSimulator()
    result = simulator.run(qc, shots=shots).result()
    counts = result.get_counts()
    
    print(f"Results after {shots} shots:")
    print(f"  |0⟩: {counts.get('0', 0)} (~50% expected)")
    print(f"  |1⟩: {counts.get('1', 0)} (~50% expected)")
    
    # Visualize
    plot_histogram(counts)
    plt.title("Superposition: Equal |0⟩ and |1⟩ Probability")
    plt.savefig('01-fundamentals/superposition_results.png')
    print("\nHistogram saved: superposition_results.png")
    plt.close()
    
    return counts

if __name__ == "__main__":
    demonstrate_superposition()