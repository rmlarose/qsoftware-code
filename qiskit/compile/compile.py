"""Example of compiling an algorithm in QISKit v0.8.0."""

# =============================================================================
# imports
# =============================================================================

from qiskit import (IBMQ, compile, QuantumCircuit, QuantumRegister)

# =============================================================================
# get a quantum circuit
# =============================================================================

# make a circuit
qreg = QuantumRegister(3)
circ = QuantumCircuit(qreg)

# add some instructions
circ.h(qreg[0])
circ.h(qreg[1])
circ.h(qreg[2])
circ.cx(qreg[0], qreg[1])
circ.cx(qreg[0], qreg[2])

# =============================================================================
# pick a backend and compile to it
# =============================================================================

# get a backend
backend = IBMQ.backends()[0]

job = compile(circ, backend)

# =============================================================================
# grab the desired info
# =============================================================================

print(job.as_dict())
