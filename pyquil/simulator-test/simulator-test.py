#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =====================================
# simulator-test.py
#
# Testing the simulator in pyQuil.
# =====================================

# -------------------------------------------
# imports
# -------------------------------------------

from pyquil.quil import Program
from pyquil import api
import pyquil.gates as gates
import sys
import time

# --------------------------------------------
# program and simulator
# --------------------------------------------

qprog = Program()
qvm = api.QVMConnection(use_queue=True)

#qvm = QVMConnection()

# -------------------------------------------
# number of qubits, depth, and backend to use
# -------------------------------------------

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 24

if len(sys.argv) > 1:
    depth = int(sys.argv[2])
else:
    depth = 10 

# -------------------------------------------
# circuit to test simulator
# -------------------------------------------

# main (arbitrary) circuit
for level in range(depth):
    for ii in range(n):
        qprog.inst(gates.H(ii),
                   gates.X(ii))
        if ii != 0:
            qprog.inst(gates.CNOT(ii, 0))
            
# measurements
for ii in range(n):
    qprog.inst(gates.MEASURE(ii, ii))

# -----------------------------------
# run the circuit and print the results
# -----------------------------------
# timing -- get the start time
start = time.time()

output = qvm.run(qprog)

# timing -- get the end time
runtime = time.time() - start

# print out the runtime
print(n, depth, runtime)
