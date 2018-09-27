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
from qiskit import register
from qiskit.tools.visualization import circuit_drawer
import numpy as np
from time import sleep

# --------------------------------------------------------
# register so that we can use backends
# --------------------------------------------------------

APItoken = '3ce852634bcc0d3fc6a5af0920aff9ad4be74ec6972f2a8e06b384796d4b28fd933c7386d2e1296ee5b0425afb317f75d44f558ba6ba18cd8fc899a1fe9fcbb8'
alex_APItoken = 'e88d764071548d55380f6b32d899f0e293cd92e91eee14cc70488847f1ef0992ef6b0a2df7f40962a74ad03009632a5521d2a63fa494f435ecf1142ce9c16344'
url = 'https://quantumexperience.ng.bluemix.net/api'

register(APItoken, url)

# --------------------------------------------------------
# quantum and classical registers and quantum circuit
# --------------------------------------------------------

qregA = QuantumRegister(1)
qregB = QuantumRegister(1)
cregA = ClassicalRegister(1)
cregB = ClassicalRegister(1)
qcircuit = QuantumCircuit(qregA, cregA, qregB, cregB, name='qcircuit')

# --------------------------------------------------------
# do the circuit
# --------------------------------------------------------

# throw in some gates
qcircuit.h(qregA[0])
qcircuit.measure(qregA[0], cregA[0])
qcircuit.measure(qregB[0], cregB[0])

# run the circuit
results = execute(qcircuit, 'local_qasm_simulator')
sleep(5)
print(results.status)
outcome = results.result()
counts = outcome.get_counts()

print(counts)

# optinally draw the circuit
circuit_drawer(qcircuit)
