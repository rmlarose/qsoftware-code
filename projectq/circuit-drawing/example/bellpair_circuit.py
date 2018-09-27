# ==========================================================
# simulator-test.py
# 
# A script to test the capabilities of ProjectQ's simulator.
#
# written by Ryan LaRose <laroser1@msu.edu>
# at Michigan State University 05-12-18
# ==========================================================

from projectq import MainEngine
from projectq.backends import CircuitDrawer
from projectq.ops import H, X, Y, CNOT, Measure
import projectq.ops as ops


# create a main compiler engine
drawing_engine = CircuitDrawer()
eng = MainEngine(drawing_engine)

a = eng.allocate_qubit()
b = eng.allocate_qubit()
c = eng.allocate_qubit()

H | a
X | a
X | b
Y | b

CNOT | (a, b)

Measure | a
H | a

ops.CX | (b, c)

ops.Swap | (a, b)

ops.QFT | (a, b, c)

ops.SqrtX | a
ops.Barrier | b

del c

d = eng.allocate_qubit()

ops.X | d

ops.CX | (d, a)
ops.CX | (d, b)

eng.flush()
print(drawing_engine.get_latex())
