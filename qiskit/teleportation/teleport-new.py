#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 15:12:32 2018

@author: ryan
"""

# --------------------------------------------------------
# imports
# --------------------------------------------------------

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute

# --------------------------------------------------------
# quantum/classical registers and quantum circuit
# --------------------------------------------------------

qreg = QuantumRegister(3)
creg = ClassicalRegister(3)
qcircuit = QuantumCircuit(qreg, creg)

# --------------------------------------------------------
# do the circuit
# --------------------------------------------------------

# teleport |1> to qubit three
qcircuit.x(qreg[0])

# main circuit
qcircuit.h(qreg[0])
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

# --------------------------------------------------------
# run the circuit and print the results
# --------------------------------------------------------
result = execute(qcircuit, 'local_qasm_simulator').result()
counts = result.get_counts()

print(counts)

# optionally print the qasm code
print(qcircuit.qasm())

# optionally draw the circuit
from qiskit.tools.visualization import circuit_drawer
circuit_drawer(qcircuit)
