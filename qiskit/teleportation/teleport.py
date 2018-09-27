#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ========================================================
# teleport.py
#
# Teleportation circuit in QISKit.
#
# written by Ryan LaRose <laroser1@msu.edu>
# at Michigan State University 05-13-18
# ========================================================

# --------------------------------------------------------
# imports
# --------------------------------------------------------

from qiskit import QuantumProgram available_backends

# --------------------------------------------------------
# quantum program, registers, and circuit
# --------------------------------------------------------

qprog = QuantumProgram()
qbits = qprog.create_quantum_register("qbits", 3)
cbits = qprog.create_classical_register("cbits", 3)
qcirc = qprog.create_circuit("teleport", [qbits], [cbits])

# --------------------------------------------------------
# teleportation circuit
# --------------------------------------------------------

# teleport |1> to qubit three
qcirc.x(qbits[0])

# main circuit
qcirc.h(qbits[1])
qcirc.cx(qbits[1], qbits[2])
qcirc.barrier(qbits)
qcirc.cx(qbits[0], qbits[1])
qcirc.h(qbits[0])
qcirc.measure(qbits[0], cbits[0])
qcirc.measure(qbits[1], cbits[1])

# conditional operations 
qcirc.z(qbits[2]).c_if(cbits[0][0], 1)
qcirc.x(qbits[2]).c_if(cbits[1][0], 1)
qcirc.measure(qbits[2], cbits[2])

# --------------------------------------------------------
# run the circuit and print the results
#---------------------------------------------------------

job = qprog.execute("teleport", backend='ibmqx4')
result = job.result()

# optionally print the QASM code for the circuit
print(result)
print(result.get_data())
print(result.get_ran_qasm("teleport"))
