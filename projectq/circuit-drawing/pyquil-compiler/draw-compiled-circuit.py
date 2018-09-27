#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:33:12 2018

@author: ryan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:44:38 2018

@author: ryan
"""

# ==========================================================
# draw-compiled-circuit.py
# 
# A script to test the capabilities of ProjectQ's simulator.
#
# written by Ryan LaRose <laroser1@msu.edu>
# at Michigan State University 05-12-18
# ==========================================================

from projectq import MainEngine
from projectq.backends import CircuitDrawer
import projectq.ops as ops
import numpy as np
np.set_printoptions(precision=2)

# create a main compiler engine
drawing_engine = CircuitDrawer()
eng = MainEngine(drawing_engine)

a = eng.allocate_qubit()
b = eng.allocate_qubit()
c = eng.allocate_qubit()

pi = 3.14
mpi = -3.14

ops.Rz(pi/2) | a
ops.Rx(pi/2) | a
ops.Rx(mpi) | b
ops.C(ops.Z) | (b, a)
ops.Rz(pi/2) | c
ops.Rx(pi/2) | c
ops.C(ops.Z) | (b, c)
ops.Rz(mpi/2) | a
ops.Rz(mpi/2) | b
ops.Rx(mpi/2) | b
ops.Rz(pi/2) | b
ops.Rz(mpi/2) | c


eng.flush()
print(drawing_engine.get_latex())
