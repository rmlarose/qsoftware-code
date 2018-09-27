# ==========================================================
# teleport.py
#
# Quantum teleportation using ProjectQ
# ==========================================================

# ---------------------------------------------------------
# imports
# ---------------------------------------------------------
from projectq import MainEngine
from projectq.ops import H, X, Z, Rz, CNOT, Measure
from projectq.meta import Dagger, Control

# make engine
eng = MainEngine()

# allocate qubits
psi = eng.allocate_qubit()
b1 = eng.allocate_qubit()
b2 = eng.allocate_qubit()

# ----------------------------------------------------------
# teleportation circuit
# ----------------------------------------------------------

# arbitrary initial state to send
H | psi
Rz(1.21) | psi

H | b1
CNOT | (b1, b2)
CNOT | (psi, b1)
H | psi
Measure | (psi, b1)

with Control(eng, b1):
    X | b2
with Control(eng, psi):
    Z | b2
with Dagger(eng):
    H | b2
    Rz(1.21) | b2 

#del b2
#eng.flush()

# optionally draw the circuit
from projectq.backends import CircuitDrawer

drawing_engine = CircuitDrawer()

print(drawing_engine.get_latex())
