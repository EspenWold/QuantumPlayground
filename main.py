import time
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, execute, QuantumRegister, ClassicalRegister
from qiskit.providers.aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit import IBMQ
from qiskit.providers.jobstatus import JOB_FINAL_STATES
from grover_algorithm import grover_algo

# Only needs to run once with your IMB Quantum token to locally store your credentials
# IBMQ.save_account(<INSERT_TOKEN>)

# This loads a real IMB quantum backend
# IBMQ.load_account()
# provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')
# real_backends = provider.backends(simulator=False, operational=True)
# print(real_backends)
# system = provider.get_backend('ibm_oslo')
# system.configuration()

# This loads a local classical simulation as a backend
system = AerSimulator()

q_reg = QuantumRegister(7, 'q')
c_reg = ClassicalRegister(7, 'c')
circuit = QuantumCircuit(q_reg, c_reg)

num_data_bits = 3
ancilla_bit = 6

grover_algo(circuit, num_data_bits, ancilla_bit)

# circuit.draw(output='mpl')
# plt.show()

job = execute(circuit, system)
start_time = time.time()
job_status = job.status()
while job_status not in JOB_FINAL_STATES:
    print(f'Status @ {time.time()-start_time:0.0f} s: {job_status.name},'
          f' est. queue position: {job.queue_position()}')
    time.sleep(10)
    job_status = job.status()

result = job.result()
counts = result.get_counts()

plot_histogram(counts)
plt.show()
print("\nTotal counts are:", counts)


