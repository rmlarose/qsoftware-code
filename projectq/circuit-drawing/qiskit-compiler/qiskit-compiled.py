#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 20:11:37 2018

@author: ryan
"""

# ==========================================================
# qiskit-compiled.py
# 
# A script to draw the compiled QISKit circuit.
#
# written by Ryan LaRose <laroser1@msu.edu>
# at Michigan State University 05-22-18
# ==========================================================

from projectq import MainEngine
from projectq.backends import CircuitDrawer
import projectq.ops as ops


# create a main compiler engine
drawing_engine = CircuitDrawer()
eng = MainEngine(drawing_engine)

q = eng.allocate_qureg(3)

ops.Rz(3.14/2) | q[2]
ops.Rx(3.14/2) | q[2]
ops.Rz(3.14/2) | q[2]

ops.CX | (q[1], q[0])

ops.Rz(3.14/2) | q[1]
ops.Rx(3.14/2) | q[1]
ops.Rz(3.14/2) | q[1]

ops.Rz(3.14/2) | q[0]
ops.Rx(3.14/2) | q[0]
ops.Rz(3.14/2) | q[0]

ops.CX | (q[1], q[0])

ops.Rz(3.14/2) | q[1]
ops.Rx(3.14/2) | q[1]
ops.Rz(3.14/2) | q[1]

ops.Rz(3.14/2) | q[0]
ops.Rx(3.14/2) | q[0]
ops.Rz(3.14/2) | q[0]

ops.CX | (q[1], q[0])

ops.Rz(3.14/2) | q[1]
ops.Rx(3.14/2) | q[1]
ops.Rz(3.14/2) | q[1]

ops.Rz(3.14/2) | q[0]
ops.Rx(3.14/2) | q[0]
ops.Rz(3.14/2) | q[0]

ops.CX | (q[1], q[0])
ops.CX | (q[1], q[2])

eng.flush()
print(drawing_engine.get_latex())
