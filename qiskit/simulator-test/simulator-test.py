"""Test the QISKit v0.6.1  simulators."""

# =============================================================================
# imports
# =============================================================================

from qiskit import (Aer, ClassicalRegister, execute,
                    QuantumCircuit, QuantumRegister)
import sys
import time

# =============================================================================
# number of qubits, depth, and backend to use
# =============================================================================

# number of qubits in circuit
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 16

# depth of test circuit
if len(sys.argv) > 2:
    depth = int(sys.argv[2])
else:
    depth = 10 

# key for which backend to use
# 0 == qasm_simulator, 1 == qasm_simulator_py, 2 == statevector_simulator,
# 3 == statevector_simulator_py, 4 == unitary_simulator, 5 == clifford_sim
if len(sys.argv) > 3:
    backend_key = int(sys.argv[3])
else:
    backend_key = 0

# =============================================================================
# create a circuit, get the simulator
# =============================================================================

qreg = QuantumRegister(n)
creg = ClassicalRegister(n)
qcirc = QuantumCircuit(qreg, creg)

# =============================================================================
# add the cicuit operations
# =============================================================================

# main (arbitrary) circuit
for level in range(depth):
    for ii in range(len(qreg)):
        q = qreg[ii]
        qcirc.h(q)
        qcirc.x(q)
        if q != qreg[0]:
            qcirc.cx(q, qreg[0])

# measure
for ii in range(len(qreg)):
    qcirc.measure(qreg[ii], creg[ii])

# =============================================================================
# get the backend
# =============================================================================
    
backends = Aer.backends()
backend = backends[backend_key]

# =============================================================================
# execute the circuit and time it
# =============================================================================

start = time.time()
result = execute(qcirc, backend)
runtime = time.time() - start

# print out the runtime
print(n, depth, runtime)
