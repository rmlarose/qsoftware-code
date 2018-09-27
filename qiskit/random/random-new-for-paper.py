#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 01:06:56 2018

@author: ryan
"""

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
from qiskit.tools.visualization import circuit_drawer

# --------------------------------------------------------
# quantum and classical registers and quantum circuit
# --------------------------------------------------------

qreg = QuantumRegister(1)
creg = ClassicalRegister(1)
qcircuit = QuantumCircuit(qreg, creg)

# --------------------------------------------------------
# do the circuit
# --------------------------------------------------------

# throw in some gates
qcircuit.h(qreg[0])
qcircuit.measure(qreg[0], creg[0])

# run the circuit
result = execute(qcircuit, 'local_qasm_simulator').result()
counts = result.get_counts()

print(counts)

# optinally draw the circuit
circuit_drawer(qcircuit)
