import numpy as np
from qiskit import QuantumCircuit, execute, QuantumRegister, ClassicalRegister
from qiskit.circuit.library.standard_gates.x import MCXGate


def stupid_all_ones_oracle(data_qubits):
    num_qubits = len(data_qubits) + 1
    control_string = ''.join(['1' for _ in data_qubits])
    oracle_circuit = QuantumCircuit(num_qubits, name='oracle')
    oracle_circuit.append(MCXGate(len(data_qubits), None, control_string), range(num_qubits))
    oracle_gate = oracle_circuit.to_gate()
    return oracle_gate


def grover_algo(circuit, num_data_bits, ancilla_bit):
    data_qubits = [q for q in range(num_data_bits)]
    all_qubits = data_qubits + [ancilla_bit]
    num_qubits = len(all_qubits)
    grover_iterations = int(np.round((np.pi / 4) * np.sqrt(2 ** num_data_bits)))

    # Construct gate for oracle
    oracle_gate = stupid_all_ones_oracle(data_qubits)

    # Construct gate for reflection about equal superposition state
    reflection_circuit = QuantumCircuit(num_qubits, name='reflection')
    reflection_circuit.h(data_qubits)
    zero_string = ''.join(['0' for _ in data_qubits])
    reflection_circuit.append(MCXGate(num_data_bits, None, zero_string), range(num_qubits))
    reflection_circuit.h(data_qubits)
    reflection_gate = reflection_circuit.to_gate()

    # Construct Grover operator gate
    grover_circuit = QuantumCircuit(num_qubits, name='Grover')
    grover_circuit.append(oracle_gate, range(num_qubits))
    grover_circuit.append(reflection_gate, range(num_qubits))
    grover_gate = grover_circuit.to_gate()

    # Prepare equal superposition
    circuit.h(data_qubits)

    # Prepare ancilla qubit
    circuit.h(6)
    circuit.z(6)
    circuit.barrier()
    for i in range(grover_iterations):
        circuit.append(grover_gate, all_qubits)
        circuit.barrier()

    circuit.measure(data_qubits, data_qubits)


