"""Random bit generator circuit in QISKit v0.8.0."""

# =============================================================================
# imports
# =============================================================================

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import Aer, execute

# =============================================================================
# quantum and classical registers and quantum circuit
# =============================================================================

qreg = QuantumRegister(1)
creg = ClassicalRegister(1)
qcircuit = QuantumCircuit(qreg, creg)

# =============================================================================
# do the circuit
# =============================================================================

# throw in some gates
qcircuit.h(qreg[0])
qcircuit.measure(qreg[0], creg[0])

# run the circuit
backend = Aer.get_backend("qasm_simulator")
result = execute(qcircuit, backend).result()
counts = result.get_counts()

print(counts)

# draw the circuit
print(qcircuit)
