from qiskit import QuantumCircuit
from qiskit.quantum_info import Pauli, SparsePauliOp
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit_ibm_runtime import EstimatorOptions
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_aer.primitives import Estimator as SimEstimator
import matplotlib.pyplot as plt

def get_qc_for_n_qubit_GHZ_state(n):
    qc = QuantumCircuit(n)
    qc.h(0)
    for i in range(n-1):
        qc.cx(i, i+1)
    return qc


n = 100
qc = get_qc_for_n_qubit_GHZ_state(n)
# qc.draw("mpl")
# plt.show()

operator_strings = ['Z' + 'I' * i + 'Z' + 'I' * (n-2-i) for i in range(n-1)]
operators = [SparsePauliOp(string) for string in operator_strings]

# Get a real quantum backend and adapt circuit to said backend
backend_name='ibm_brisbane'
backend = QiskitRuntimeService().backend(backend_name)
pass_manager = generate_preset_pass_manager(optimization_level=1, backend=backend)
qc_transpiled = pass_manager.run(qc)
operators_transpiled_list = [op.apply_layout(qc_transpiled.layout) for op in operators]

# Set up estimator for real backend
options = EstimatorOptions()
options.resilience_level = 1
options.dynamical_decoupling.enable = True
options.dynamical_decoupling.sequence_type = "XY4"

# Choose simulator or real backend
# estimator = SimEstimator()
# job = estimator.run([qc] * len(operators), operators)
estimator = Estimator(backend, options)
job = estimator.run([(qc_transpiled, operators_transpiled_list)])
job_id = job.job_id()
print(job_id)

result = job.result()

data=operator_strings
values=result.values
plt.plot(data,values,'-0')
plt.xlabel( 'Observables')
plt.ylabel( 'Expectation value')
plt.show()

# Return a drawing of the circuit using MatPlotLib ("mpl"). This is the
# last line of the cell, so the drawing appears in the cell output.
# Remove the "mpl" argument to get a text drawing.
# qc.draw("mpl")
# plt.show()