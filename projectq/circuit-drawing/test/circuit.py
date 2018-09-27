#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 08:58:07 2018

@author: ryan
"""

# ==========================================================
# circuit.py
#
# Testing out drawing a circuit
# ==========================================================

# ---------------------------------------------------------
# imports
# ---------------------------------------------------------
from projectq import MainEngine
from projectq.ops import H, Measure
from projectq.backends import CircuitDrawer

# make engine
eng = MainEngine()

# allocate qubits
a = eng.allocate_qubit()

# ----------------------------------------------------------
# some random circuit
# ----------------------------------------------------------

# arbitrary initial state to send
H | a
Measure | a

eng.flush()

drawing_engine = CircuitDrawer()

print(drawing_engine.get_latex())