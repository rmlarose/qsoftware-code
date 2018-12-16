"""QVM simulator performance test in PyQuil 2.1.1."""

# =============================================================================
# imports
# =============================================================================

from pyquil.quil import Program
from pyquil import api
import pyquil.gates as gates
import sys
import time

# =============================================================================
# program and simulator
# =============================================================================

qprog = Program()
qvm = api.QVMConnection()

# =============================================================================
# number of qubits, depth, classical memory
# =============================================================================

# grab the number of qubits
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 12

# grab the depth
if len(sys.argv) > 1:
    depth = int(sys.argv[2])
else:
    depth = 10

# allocate classical memory
creg = qprog.declare("ro", memory_size=n)

# =============================================================================
# circuit to test simulator
# =============================================================================

# main (arbitrary) circuit
for level in range(depth):
    for ii in range(n):
        qprog.inst(gates.H(ii),
                   gates.X(ii))
        if ii != 0:
            qprog.inst(gates.CNOT(ii, 0))
            
# measurements
for ii in range(n):
    qprog.inst(gates.MEASURE(ii, creg[ii]))

# =============================================================================
# run the circuit and print the results
# =============================================================================
    
# timing -- get the start time
start = time.time()

output = qvm.run(qprog)

# timing -- get the end time
runtime = time.time() - start

# print out the runtime
print(n, depth, runtime)
