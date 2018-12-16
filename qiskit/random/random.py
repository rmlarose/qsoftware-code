"""Random bit generator circuit in QISKit v0.6.1."""

# =============================================================================
# imports
# =============================================================================

from qiskit import (Aer, 
                    ClassicalRegister,
                    execute,
                    QuantumCircuit,
                    QuantumRegister)
from qiskit.tools.visualization import circuit_drawer

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
backend = Aer.backends("qasm_simulator")[0]
result = execute(qcircuit, backend).result()
counts = result.get_counts()

print(counts)

# draw the circuit
circuit_drawer(qcircuit)
