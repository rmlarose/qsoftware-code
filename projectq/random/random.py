#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==========================================================
# random.py
#
# Random number generator circuit in ProjectQ.
#
# written by Ryan LaRose <laroser1@msu.edu>
# at Michigan State University 05-14-2018
# ==========================================================

# ---------------------------------------------------------
# imports
# ---------------------------------------------------------
from projectq import MainEngine
import projectq.ops as ops

eng = MainEngine()

qbits = eng.allocate_qureg(1)

ops.H | qbits[0]
ops.Measure | qbits[0]

eng.flush()

print(int(qbits[0]))


# --------------------------------------------------------
# optionally draw the circuit
# --------------------------------------------------------

from projectq.backends import CircuitDrawer

drawing_engine = CircuitDrawer()
print(drawing_engine.get_latex())
