#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:08:26 2018

@author: ryan
"""

# ============================================
# simulator-test.py
#
# Testing the simulator in QISKit.
#
# written by Ryan LaRose <laroser1@msu.edu>
# at Michigan State University 05-21-18
# ============================================

# --------------------------------------------
# imports
# --------------------------------------------

from qiskit import QuantumProgram, available_backends, register
import sys
import time

# ----------------------------------------------------------
# number of qubits, depth, and backend to use
# ----------------------------------------------------------

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 16

if len(sys.argv) > 2:
    depth = int(sys.argv[2])
else:
    depth = 10 

if len(sys.argv) > 3:
    backend_key = int(sys.argv[3])
else:
    backend_key = 2
    
qprog= QuantumProgram()
qbits = qprog.create_quantum_register("qbits", n)
cbits = qprog.create_classical_register("cbits", n)
qcirc = qprog.create_circuit("test", [qbits], [cbits])
    
# timing -- get the start time
start = time.time()

# main (arbitrary) circuit
for level in range(depth):
    for ii in range(len(qbits)):
        q = qbits[ii]
        qcirc.h(q)
        qcirc.x(q)
        if q != qbits[0]:
            qcirc.cx(q, qbits[0])

# measure
for ii in range(len(qbits)):
    qcirc.measure(qbits[ii], cbits[ii]) if backend_key != 2 else qcirc.h(qbits[ii])
    
backends = available_backends()
backend_used = backends[backend_key]

# timing -- get the start time
start = time.time()

result = qprog.execute("test", backend='local_statevector_simulator', timeout=1000)

# timing -- get the end time
runtime = time.time() - start

# print out the runtime
print(n, depth, runtime)
