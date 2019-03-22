# """Test the QCGPU simulators."""

import sys
import time
import qcgpu

qcgpu.backend.create_context()


def benchmark(num_qubits, depth):
    start_time = time.time()

    state = qcgpu.State(num_qubits)

    for _ in range(depth):
        for q in range(num_qubits):
            state.h(q)
            state.x(q)
            state.t(q)
            if q != 0:
                state.cx(q, 0)
    
    state.measure()

    return time.time() - start_time


for n in (16, 17, 18, 19, 20, 21, 22, 23, 24):
    for d in (5, 10, 15, 20, 25, 30):
        t = benchmark(n, d)
        print(n, d, t)

