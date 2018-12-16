"""Random bit generator circuit in PyQuil 2.1.1."""

# imports
from pyquil.quil import Program
import pyquil.gates as gates
from pyquil import api

# get a program and classical memory register 
qprog = Program()
creg = qprog.declare(name="ro", memory_size=1)

# REQUIRES: api key, qvm running in background ("qvm -S" in a linux terminal
# after it is installed. See Rigetti website for download instructions
# https://www.rigetti.com/forest)
qvm = api.QVMConnection()

# add instructions to the program
qprog += [gates.H(0),
           gates.MEASURE(0, creg[0])]

print(qprog)
print(qvm.run(qprog, trials=1))