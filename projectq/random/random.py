"""Random number generator circuit in ProjectQ v0.4.1."""

# =============================================================================
# imports
# =============================================================================

from projectq import MainEngine
import projectq.ops as ops
from projectq.backends import CircuitDrawer

# =============================================================================
# imports
# =============================================================================

# grab an engine
eng = MainEngine()

# get some qubits
qbits = eng.allocate_qureg(1)

# add instructions to the circuit
ops.H | qbits[0]
ops.Measure | qbits[0]

# run the circuit
eng.flush()

# display the result
print(int(qbits[0]))

# =============================================================================
# generate tex code for drawing the circuit with tikz
# =============================================================================

drawing_engine = CircuitDrawer()
print(drawing_engine.get_latex())
