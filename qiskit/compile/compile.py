#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ========================================================
# compile.py
#
# Test the QISKit compiler.
#
# written by Ryan LaRose <laroser1@msu.edu>
# at Michigan State University 05-14-18
# ========================================================

from qiskit import QuantumProgram, available_backends, register, compile

# --------------------------------------------------------
# register so that we can use backends
# --------------------------------------------------------

qprog= QuantumProgram()
qbits = qprog.create_quantum_register("qbits", 3)
cbits = qprog.create_classical_register("cbits", 3)
qcirc = qprog.create_circuit("random", [qbits], [cbits])

# TODO: unitary you want ot compile goes here
qcirc.h(qbits[0])
qcirc.h(qbits[1])
qcirc.h(qbits[2])
qcirc.cx(qbits[0],qbits[1])
qcirc.cx(qbits[0],qbits[2])

job = compile(qcirc, 'ibmqx5')
compiled_circ = job['circuits'][0]['compiled_circuit']['operations']

for i in range(len(compiled_circ)):
    print(compiled_circ[i])