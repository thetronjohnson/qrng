from qiskit import IBMQ, BasicAer, QuantumRegister, ClassicalRegister, QuantumCircuit, execute
import math
import struct




bitcache = ''
circuit = None
provider = IBMQ.load_account()
backend = BasicAer.get_backend('qasm_simulator')

def makeCircuit(n):
    global circuit
    qr = QuantumRegister(n)
    cr = ClassicalRegister(n)
    circuit = QuantumCircuit(qr,cr)
    circuit.h(qr)
    circuit.measure(qr,cr)

makeCircuit(4)

def setBackend(device='qasm_simulator'):
    global backend
    if device == "ibmq_qasm_simulator":
        backend = IBMQ.get_backend(device)
        makeCircuit(32)
    if device == 'ibmq_ourense':
        backend = IBMQ.get_backend(device)
        makeCircuit(5)
    if device == 'ibmq_essex':
        backend = IBMQ.get_backend(device)
        makeCircuit(5)
    if device == 'ibmq_vigo':
        backend = IBMQ.get_backend(device)
        makeCircuit(5)
    else:
        backend = BasicAer.get_backend('qasm_simulator')
        makeCircuit(4)

def generate():
    job = execute(circuit,backend,shots=1)
    result = job.result().get_counts()
    return [k for k,v in result.items()][0]