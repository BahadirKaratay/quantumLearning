"""
Measurement and State Collapse
Shows probabilistic nature of quantum measurement
"""
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

def demonstrate_measurement():
    """Show state before and after measurement"""
    # Create circuit
    qc = QuantumCircuit(1)
    
    # Prepare superposition
    qc.h(0)
    
    # State before measurement
    state = Statevector.from_instruction(qc)
    print("State before measurement:")
    print(f"  Amplitudes: {state.data}")
    print(f"  |0⟩ probability: {abs(state.data[0])**2:.3f}")
    print(f"  |1⟩ probability: {abs(state.data[1])**2:.3f}")
    
    # Add measurement
    qc.measure_all()
    
    # Print circuit
    print("\nQuantum Circuit:")
    print(qc.draw())
    print()
    
    # Simulate single shot
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1).result()
    outcome = list(result.get_counts().keys())[0]
    
    print(f"Measurement outcome: |{outcome}⟩")
    print("State collapsed to definite value")
    
    # Multiple measurements
    result_multi = simulator.run(qc, shots=100).result()
    counts = result_multi.get_counts()
    print(f"\n100 independent measurements:")
    print(f"  |0⟩: {counts.get('0', 0)} times")
    print(f"  |1⟩: {counts.get('1', 0)} times")

if __name__ == "__main__":
    demonstrate_measurement()