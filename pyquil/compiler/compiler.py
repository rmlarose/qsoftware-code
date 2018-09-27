#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:52:09 2018

@author: ryan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ===========================================
# wavelet.py
#
# Doing the wavelet transform in PyQuil.
#
# written by Ryan LaRose <laroser1@msu.edu>
# at Michigan State University 05-17-18
# ===========================================

from pyquil.quil import Program
import pyquil.gates as gates
from pyquil import api

devices = api.get_devices(as_dict=True)
acorn = devices['8Q-Agave']
compiler = api.CompilerConnection(acorn)

qprog = Program()
qprog.inst(gates.H(0),
           gates.H(1),
           gates.H(2),
           gates.CNOT(0, 2),
           gates.CNOT(1, 2))

job_id = compiler.compile_async(qprog)
job = compiler.wait_for_job(job_id)

print(job.compiled_quil())

qvm = api.QVMConnection()
