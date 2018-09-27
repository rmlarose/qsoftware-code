#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =====================================
# teleport.py
#
# Teleportation circuit in pyQuil.
# =====================================

# -------------------------------------
# imports
# -------------------------------------

from pyquil.quil import Program
from pyquil import api
import pyquil.gates as gates

# -------------------------------------
# program and simulator
# -------------------------------------

qprog = Program()
qvm = api.QVMConnection()

# -------------------------------------
# teleportation circuit
# -------------------------------------

# teleport |1> to qubit three
qprog += gates.X(0)

# main circuit
qprog += [gates.H(1),
          gates.CNOT(1, 2),
          gates.CNOT(0, 1),
          gates.H(0),
          gates.MEASURE(0, 0),
          gates.MEASURE(1, 1)]

# conditional operations
qprog.if_then(0, gates.Z(2))
qprog.if_then(1, gates.X(2))

# measure qubit three
qprog.measure(2, 2)

# -----------------------------------
# run the circuit and print the results
# -----------------------------------

print(qvm.run(qprog))

# -----------------------------------
# optionally print the quil code
# -----------------------------------

print(qprog)