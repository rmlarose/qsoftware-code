"""Test the QISKit v0.8.0  simulators."""

from qiskit import (Aer, ClassicalRegister, execute,
                    QuantumCircuit, QuantumRegister)
import sys
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

def benchmark(n, depth):
    qreg = QuantumRegister(n)
    creg = ClassicalRegister(n)
    qcirc = QuantumCircuit(qreg, creg)

    # main (arbitrary) circuit
    for level in range(depth):
        for ii in range(len(qreg)):
            q = qreg[ii]
            qcirc.h(q)
            qcirc.x(q)
            qcirc.t(q)
            if q != qreg[0]:
                qcirc.cx(q, qreg[0])

    # measure
    for ii in range(len(qreg)):
        qcirc.measure(qreg[ii], creg[ii])

    backend = Aer.get_backend('qasm_simulator')

    start = time.time()
    result = execute(qcirc, backend).result()
    return time.time() - start

for n in (16, 17, 18, 19, 20, 21, 22, 23, 24):
    for d in (5, 10, 15, 20, 25, 30):
        t = benchmark(n, d)
        print(n, d, t)

