#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==========================================================
# simulator-test.py
# 
# A script to test the capabilities of ProjectQ's simulator.
#
# written by Ryan LaRose <laroser1@msu.edu>
# at Michigan State University 05-12-18
# ==========================================================

# --------------------------------------------------------
# imports
# --------------------------------------------------------

from projectq import MainEngine
import projectq.ops as ops
from projectq.backends import Simulator
import sys
import time

# ----------------------------------------------------------
# number of qubits and depth
# ----------------------------------------------------------

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 24

if len(sys.argv) > 1:
    depth = int(sys.argv[2])
else:
    depth = 10 

# --------------------------------------------------------
# engine and qubit register
# --------------------------------------------------------

eng = MainEngine(backend=Simulator(gate_fusion=True), engine_list=[])
qbits = eng.allocate_qureg(n)

# --------------------,------------------------------------
# circuit
# --------------------------------------------------------

# timing -- get the start time
start = time.time()

# main (arbitrary) circuit
for level in range(depth):
    for q in qbits:
        ops.H | q
        ops.SqrtX | q
        if q != qbits[0]:
            ops.CNOT | (q, qbits[0])

# measure to get rid of runtime error message
for q in qbits:
    ops.Measure | q

# flush the engine
eng.flush()

# timing -- get the end time
runtime = time.time() - start

# print out the runtime
print(n, depth, runtime)
