"""Quantum teleportation algorithm in ProjectQ v0.4.1."""

# =============================================================================
# imports
# =============================================================================

from projectq import MainEngine
from projectq.meta import Control
import projectq.ops as ops

# =============================================================================
# engine and qubit register
# =============================================================================

# engine
eng = MainEngine()

# allocate qubit register
qbits = eng.allocate_qureg(3)

# =============================================================================
# teleportation circuit
# =============================================================================

# Alice teleports |1> to qubit Bob
ops.X | qbits[0]

# main circuit
ops.H | qbits[1]
ops.CNOT | (qbits[1], qbits[2])
ops.CNOT | (qbits[0], qbits[1])
ops.H | qbits[0]
ops.Measure | (qbits[0], qbits[1])

# conditional operations
with Control(eng, qbits[1]):
    ops.X | qbits[2]
with Control(eng, qbits[1]):
    ops.Z | qbits[2]
    
# measure qubit three
ops.Measure | qbits[2]

# =============================================================================
# run the circuit and print the results
# =============================================================================
    
eng.flush()
print("Measured:", int(qbits[2]))

"""
# --------------------------------------------------------
# optionally draw the circuit
# --------------------------------------------------------

from projectq.backends import CircuitDrawer

drawing_engine = CircuitDrawer()
print(drawing_engine.get_latex())
"""
