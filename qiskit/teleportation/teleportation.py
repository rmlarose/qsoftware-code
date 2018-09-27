# ========================================================
# teleportation.py
#
# Teleportation circuit in QISKit.
# ========================================================

# --------------------------------------------------------
# imports
# --------------------------------------------------------

from qiskit import QuantumProgram

# --------------------------------------------------------
# backend and quantum program 
# --------------------------------------------------------

backend = "local_qasm_simulator"

QPS_SPECS = {
    "circuits": [{
        "name": "teleport",
        "quantum_registers": [{
            "name": "q",
            "size": 3
        }],
        "classical_registers": [
            {"name": "c0",
             "size": 1},
            {"name": "c1",
             "size": 1},
            {"name": "c2",
             "size": 1},
        ]}]
}

qp = QuantumProgram(specs=QPS_SPECS)
qc = qp.get_circuit("teleport")
q = qp.get_quantum_register("q")
c0 = qp.get_classical_register("c0")
c1 = qp.get_classical_register("c1")
c2 = qp.get_classical_register("c2")

# --------------------------------------------------------
# teleportation circuit
# --------------------------------------------------------

# arbitrary initial state to teleport 
qc.h(q[0])
qc.rz(1.21, q[0])

# main circuit
qc.h(q[1])
qc.cx(q[1], q[2])
qc.barrier(q)
qc.cx(q[0], q[1])
qc.h(q[0])
qc.measure(q[0], c0[0])
qc.measure(q[1], c1[0])

# conditional operations 
qc.z(q[2]).c_if(c0, 1)
qc.x(q[2]).c_if(c1, 1)
qc.measure(q[2], c2[0])

# --------------------------------------------------------
# run the circuit
#---------------------------------------------------------

# First version: not mapped
result = qp.execute(["teleport"], backend=backend,
                    coupling_map=None, shots=1024)
print(result)
print(result.get_counts("teleport"))

# optionally print the QASM code for the circuit
print(result.get_ran_qasm("teleport"))

