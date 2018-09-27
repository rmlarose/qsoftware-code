#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# define_gate.py
#
# Example of defining a gate in ProjectQ.
#
# written by Ryan LaRose <laroser1@msu.edu>
# at Michigan State University September 2018.
"""

# =============================================================================
# imports
# =============================================================================

from projectq import MainEngine
import projectq.ops as ops

# =============================================================================
# declare an engine and get some qubits
# =============================================================================

eng = MainEngine()
qbits = eng.allocate_qureg(1)

# =============================================================================
# define a custom one-qubit gate
# =============================================================================

class MyGate(ops.BasicGate):
    """Custom one-qubit gate defined via matrix elements."""
    def __str__(self):
        return "my_gate"
    
    @property
    def matrix(self):
        """Defines the gate in terms of it's matrix elements."""
        return ops.np.matrix([[0, 1], [-1j, 0]])
    
# instantiate the class so we can use it in a circuit
mygate = MyGate()
    
# =============================================================================
# do a circuit with the gate
# =============================================================================
    
# declare the circuit   
mygate | qbits[0]
ops.Measure | qbits[0]

# run the circuit
eng.flush()

# mygate takes |0> to -i * |1>, so we should always get 1 as output
print(int(qbits[0]))
