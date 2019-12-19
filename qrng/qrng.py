from qiskit import IBMQ, Aer, QuantumRegister, ClassicalRegister, QuantumCircuit, execute
from qiskit.providers.ibmq import least_busy

circuit = None
provider = IBMQ.load_account()

def makeCircuit(n):
    global circuit
    qr = QuantumRegister(n)
    cr = ClassicalRegister(n)
    circuit = QuantumCircuit(qr,cr)
    circuit.h(qr)
    circuit.measure(qr,cr)


def setBackend(device='qasm_simulator'):
    global backend
    if device=="ibmq_16_melbourne":
        backend = provider.get_backend(device)
        makeCircuit(14)
    if device == "ibmq_qasm_simulator":
        backend = provider.get_backend(device)
        makeCircuit(32)
    if device == 'ibmq_ourense':
        backend = provider.get_backend(device)
        makeCircuit(5)
    if device == 'ibmq_essex':
        backend = provider.get_backend(device)
        makeCircuit(5)
    if device == 'ibmq_vigo':
        backend = provider.get_backend(device)
        makeCircuit(5)
    else:
        backend = Aer.get_backend('qasm_simulator')
        makeCircuit(8)
        
def randBinary():
    setBackend(device='qasm_simulator')
    job = execute(circuit,backend=backend,shots=1)
    result = job.result().get_counts()
    value = [k for k,v in result.items() if v == 1][0]
    return value

value = randBinary()

def randInt():
    global value
    randint = int(value,2)
    print(randint)
    return randint