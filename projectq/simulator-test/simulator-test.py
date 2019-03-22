# """Test the ProjectQ simulators."""

import sys
import time

from projectq import MainEngine
import projectq.ops as ops
from projectq.backends import Simulator

eng = MainEngine(backend=Simulator(gate_fusion=True), engine_list=[])


def benchmark(num_qubits, depth):
    qbits = eng.allocate_qureg(num_qubits)

    start_time = time.time()

    for level in range(depth):
        for q in qbits:
            ops.H | q
            ops.SqrtX | q
            ops.T | q
            if q != qbits[0]:
                ops.CNOT | (q, qbits[0])
    
    # measure to get rid of runtime error message
    for q in qbits:
        ops.Measure | q

    eng.flush()

    return time.time() - start_time


for n in (16, 17, 18, 19, 20, 21, 22, 23, 24):
    for d in (5, 10, 15, 20, 25, 30):
        t = benchmark(n, d)
        print(n, d, t)

