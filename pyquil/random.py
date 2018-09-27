#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ===========================================
# random.py
#
# Random number generator circuit in PyQuil.
#
# written by Ryan LaRose <laroser1@msu.edu>
# at Michigan State University 05-14-18
# ===========================================

from pyquil.quil import Program
import pyquil.gates as gates
from pyquil import api

qprog = Program()
qprog += [gates.H(0),
           gates.MEASURE(0, 0)]

qvm = api.QVMConnection()
print(qvm.run(qprog))

print(qprog)