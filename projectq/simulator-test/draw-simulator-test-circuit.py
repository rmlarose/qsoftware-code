#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 17:31:12 2018

@author: ryan
"""

# ==========================================================
# draw-simulator-test-circuit.py
# 
# A script to draw the circuit used to test the simulator.
#
# written by Ryan LaRose <laroser1@msu.edu>
# at Michigan State University 05-12-18
# ==========================================================

from projectq import MainEngine
from projectq.backends import CircuitDrawer
import projectq.ops as ops

n = 4
depth = 2

# create a main compiler engine
drawing_engine = CircuitDrawer()
eng = MainEngine(drawing_engine)

# allocate qubits
qbits = eng.allocate_qureg(n)

for level in range(depth):
    for q in qbits:
        ops.H | q
        ops.SqrtX | q
        ops.T | q
        if q != qbits[0]:
            ops.CNOT | (q, qbits[0])
            
# measure to get rid of annoying runtime error message
for q in qbits:
    ops.Measure | q

# flush the engine and draw the circuit
eng.flush()
print(drawing_engine.get_latex())
