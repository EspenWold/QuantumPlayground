import numpy as np
import time
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile, execute, QuantumRegister, ClassicalRegister
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram
from qiskit import IBMQ
from qiskit.providers.jobstatus import JOB_FINAL_STATES

# Only needs to run once with your IMB Quantum token to locally store your credentials
# IBMQ.save_account(<INSERT_TOKEN>)

# IBMQ.load_account()
# provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')
# real_backends = provider.backends(simulator=False, operational=True)
# print(real_backends)
# system = provider.get_backend('ibm_oslo')
# system.configuration()

system = QasmSimulator()

q_reg = QuantumRegister(7, 'q')
c_reg = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(q_reg, c_reg)

circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])

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
print("\nTotal count for 00 and 11 are:", counts)


