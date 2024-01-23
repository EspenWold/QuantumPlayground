import time
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, execute, QuantumRegister, ClassicalRegister, transpile
from qiskit.providers.aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit import IBMQ
from qiskit.providers.jobstatus import JOB_FINAL_STATES
from grover_algorithm import grover_algo

# Only needs to run once with your IMB Quantum token to locally store your credentials
# IBMQ.save_account(<INSERT_TOKEN>)

# This loads a simulated, idealised backend
sim = AerSimulator()
print(sim.configuration().to_dict())

# This loads a real IMB quantum backend
IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')
real_backends = provider.backends(simulator=False, operational=True)
real = provider.get_backend('ibm_oslo')

print(real.configuration().to_dict())

q_reg = QuantumRegister(7, 'q')
c_reg = ClassicalRegister(7, 'c')
circuit = QuantumCircuit(q_reg, c_reg)

num_data_bits = 3
ancilla_bit_index = 6

grover_algo(circuit, num_data_bits, ancilla_bit_index, 1)

idealised_circuit = transpile(circuit, sim, optimization_level=3)
print("Idealised circuit depth", idealised_circuit.depth())
idealised_circuit.draw('mpl')
plt.show()

adapted_circuit = transpile(circuit, real, optimization_level=3)
print("Transpiled circuit depth", adapted_circuit.depth())
print('Gate counts:', adapted_circuit.count_ops())
if adapted_circuit.depth() < 200:
    adapted_circuit.draw('mpl')
plt.show()

# Change to run on real/simulated machine
simulation = True

if simulation:
    job = execute(idealised_circuit, sim)
else:
    job = execute(adapted_circuit, sim)
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
