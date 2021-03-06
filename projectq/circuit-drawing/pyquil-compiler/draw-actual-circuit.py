#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:44:38 2018

@author: ryan
"""

# ==========================================================
# draw-actual-circuit.py
# 
# A script to test the capabilities of ProjectQ's simulator.
#
# written by Ryan LaRose <laroser1@msu.edu>
# at Michigan State University 05-12-18
# ==========================================================

from projectq import MainEngine
from projectq.backends import CircuitDrawer
import projectq.ops as ops


# create a main compiler engine
drawing_engine = CircuitDrawer()
eng = MainEngine(drawing_engine)

a = eng.allocate_qubit()
b = eng.allocate_qubit()
c = eng.allocate_qubit()

ops.H | a
ops.H | b
ops.H | c
ops.CNOT | (a, c)
ops.CNOT | (b, c)

eng.flush()
print(drawing_engine.get_latex())
