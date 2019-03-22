"""Quantum teleportation algorithm in QISKit v0.8.0."""

# =============================================================================
# imports
# =============================================================================

from qiskit import (Aer, ClassicalRegister, execute,
                    QuantumRegister, QuantumCircuit)

# =============================================================================
# quantum/classical registers and quantum circuit
# =============================================================================

qreg = QuantumRegister(3)
creg = ClassicalRegister(3)
qcircuit = QuantumCircuit(qreg, creg)

# =============================================================================
# do the circuit
# =============================================================================

# Alice teleports |1> to qubit Bob
qcircuit.x(qreg[0])

# main circuit
qcircuit.h(qreg[1])
qcircuit.cx(qreg[1], qreg[2])
qcircuit.cx(qreg[0], qreg[1])
qcircuit.h(qreg[0])
qcircuit.measure(qreg[0], creg[0])
qcircuit.measure(qreg[1], creg[1])

# conditional operations
qcircuit.z(qreg[2]).c_if(creg[0][0], 1)
qcircuit.x(qreg[2]).c_if(creg[1][0], 1)

# measure qubit three
qcircuit.measure(qreg[2], creg[2])

# =============================================================================
# run the circuit and print the results
# =============================================================================

backend = Aer.get_backend("qasm_simulator")
result = execute(qcircuit, backend).result()
counts = result.get_counts()

print(counts)

# optionally print the qasm code
print(qcircuit.qasm())

# optionally draw the circuit
print(qcircuit)
