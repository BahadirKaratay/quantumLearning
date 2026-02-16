"""
Multi-Qubit Gates
CNOT, Toffoli, and controlled operations
"""
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def demonstrate_cnot():
    """CNOT gate demonstration"""
    print("CNOT Gate Truth Table:")
    print("=" * 30)
    print("Input (control, target) -> Output")
    
    test_cases = [
        (0, 0, "|00⟩"),
        (0, 1, "|01⟩"),
        (1, 0, "|10⟩"),
        (1, 1, "|11⟩")
    ]
    
    for control, target, label in test_cases:
        qc = QuantumCircuit(2, 2)
        
        # Set initial state
        if control:
            qc.x(0)
        if target:
            qc.x(1)
        
        # Apply CNOT
        qc.cx(0, 1)
        
        # Measure
        qc.measure([0, 1], [0, 1])
        
        # Simulate
        simulator = AerSimulator()
        result = simulator.run(qc, shots=1).result()
        output = list(result.get_counts().keys())[0]
        
        print(f"  {label} -> |{output}⟩")
    
    print("\nNote: Target qubit flips if control is |1⟩")
    print("=" * 30)

def demonstrate_toffoli():
    """Toffoli (CCNOT) gate demonstration"""
    print("\n\nToffoli Gate (CCNOT) Truth Table:")
    print("=" * 40)
    print("Input (c1, c2, target) -> Output")
    
    for c1 in [0, 1]:
        for c2 in [0, 1]:
            for target in [0, 1]:
                qc = QuantumCircuit(3, 3)
                
                # Set initial state
                if c1:
                    qc.x(0)
                if c2:
                    qc.x(1)
                if target:
                    qc.x(2)
                
                # Apply Toffoli
                qc.ccx(0, 1, 2)
                
                # Measure
                qc.measure([0, 1, 2], [0, 1, 2])
                
                # Simulate
                simulator = AerSimulator()
                result = simulator.run(qc, shots=1).result()
                output = list(result.get_counts().keys())[0]
                
                input_state = f"|{c1}{c2}{target}⟩"
                print(f"  {input_state} -> |{output}⟩")
    
    print("\nNote: Target flips ONLY if both controls are |1⟩")
    print("=" * 40)

def visualize_cnot_circuit():
    """Create visual representation of CNOT"""
    qc = QuantumCircuit(2, 2)
    qc.h(0)  # Superposition on control
    qc.cx(0, 1)  # CNOT
    qc.measure([0, 1], [0, 1])
    
    print("\n\nCNOT Circuit (with superposition):")
    print(qc.draw())
    
    # Simulate
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1000).result()
    counts = result.get_counts()
    
    # Plot
    plot_histogram(counts)
    plt.title("CNOT with Superposition: Creates Entanglement")
    plt.savefig('01-fundamentals/cnot_entanglement.png', dpi=150)
    print("\n✓ cnot_entanglement.png saved")
    plt.close()

if __name__ == "__main__":
    demonstrate_cnot()
    demonstrate_toffoli()
    visualize_cnot_circuit()