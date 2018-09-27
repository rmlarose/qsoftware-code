#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ========================================================
# random.py
#
# Random number generator circuit in QISKit.
#
# written by Ryan LaRose <laroser1@msu.edu>
# at Michigan State University 05-14-18
# ========================================================

# --------------------------------------------------------
# imports
# --------------------------------------------------------

from qiskit import QuantumCircuit

# --------------------------------------------------------
# register so that we can use backends
# --------------------------------------------------------

APItoken = '3ce852634bcc0d3fc6a5af0920aff9ad4be74ec6972f2a8e06b384796d4b28fd933c7386d2e1296ee5b0425afb317f75d44f558ba6ba18cd8fc899a1fe9fcbb8'
url = 'https://quantumexperience.ng.bluemix.net/api'

register(APItoken, url)

# --------------------------------------------------------
# make a program, bit registers, and circuit
# --------------------------------------------------------

qprog = QuantumProgram()
qbits = qprog.create_quantum_register("qbits", 2)
cbits = qprog.create_classical_register("cbits", 1)

qcirc = qprog.create_circuit("random", [qbits], [cbits])

# --------------------------------------------------------
# do the circuit
# --------------------------------------------------------

qcirc.h(qbits[0])
qcirc.measure(qbits[0], cbits[0])

# --------------------------------------------------------
# run the job and print the results
# --------------------------------------------------------

job = qprog.execute(["random"], 'ibmqx4')
result = job.result()

print(result, result.get_counts("random"))
#print(qcirc.qasm())
