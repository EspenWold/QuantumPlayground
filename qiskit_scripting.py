import time
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.visualization import plot_histogram
from qiskit.providers.jobstatus import JOB_FINAL_STATES
from qiskit_ibm_runtime import QiskitRuntimeService

from grover_algorithm import grover_algo

# Only needs to run once with your IMB Quantum token to locally store your credentials
# QiskitRuntimeService.save_account(channel="ibm_quantum", token="5e4a99f4ed1de3d758b9688b68a3bd91638b3b90db317697fa47920e9ea4c24510193e5bd8ef9e70027496d561ed50cd9af940a47b2c0d7afe8742be3922cf4e")

# This loads a simulated, idealised backend

# This loads a real IMB quantum backend
# IBMQ.load_account()
# provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')
# real_backends = provider.backends(simulator=False, operational=True)
# real = provider.get_backend('ibm_oslo')
#
# print(real.configuration().to_dict())

# q_reg = QuantumRegister(7, 'q')
# c_reg = ClassicalRegister(7, 'c')
# circuit = QuantumCircuit(q_reg, c_reg)
#
# num_data_bits = 3
# ancilla_bit_index = 6
#
# grover_algo(circuit, num_data_bits, ancilla_bit_index, 1)
#
# idealised_circuit = transpile(circuit, sim, optimization_level=3)
# print("Idealised circuit depth", idealised_circuit.depth())
# idealised_circuit.draw('mpl')
# plt.show()
#
# adapted_circuit = transpile(circuit, real, optimization_level=3)
# print("Transpiled circuit depth", adapted_circuit.depth())
# print('Gate counts:', adapted_circuit.count_ops())
# if adapted_circuit.depth() < 200:
#     adapted_circuit.draw('mpl')
# plt.show()
#
# # Change to run on real/simulated machine
# simulation = True
#
# if simulation:
#     job = execute(idealised_circuit, sim)
# else:
#     job = execute(adapted_circuit, sim)
# start_time = time.time()
# job_status = job.status()
# while job_status not in JOB_FINAL_STATES:
#     print(f'Status @ {time.time()-start_time:0.0f} s: {job_status.name},'
#           f' est. queue position: {job.queue_position()}')
#     time.sleep(10)
#     job_status = job.status()
#
# result = job.result()
# counts = result.get_counts()
#
# plot_histogram(counts)
# plt.show()
# print("\nTotal counts are:", counts)
