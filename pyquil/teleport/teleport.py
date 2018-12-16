"""Teleportation algorithm in PyQuil 2.1.1."""
# imports
from pyquil.quil import Program
from pyquil import api
import pyquil.gates as gates

# get program, classical memory, simulator
qprog = Program()
creg = qprog.declare("ro", memory_size=3)
# REQUIRES: api key, qvm running in background ("qvm -S" in a linux terminal
# after it is installed. See Rigetti website for download instructions
# https://www.rigetti.com/forest)
qvm = api.QVMConnection()

# =============================================================================
# teleportation circuit
# =============================================================================

# Alice wants to send |1> to Bob
qprog += gates.X(0)

# main circuit
qprog += [gates.H(1),
          gates.CNOT(1, 2),
          gates.CNOT(0, 1),
          gates.H(0),
          gates.MEASURE(0, creg[0]),
          gates.MEASURE(1, creg[1])]

# conditional operations
qprog.if_then(creg[0], gates.Z(2))
qprog.if_then(creg[1], gates.X(2))

# measure qubit three
qprog.measure(2, creg[2])

# =============================================================================
# run the circuit and print the results. Note Bob always measures 1
# =============================================================================

print(qvm.run(qprog))

# print the quil code
print(qprog)