namespace Random
{
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Primitive;

    // operation that sets a qubit to be in the desired state
    operation Set(desired_state: Result, qubit: Qubit) : Unit {
        // measure the qubit
        let current = M(qubit);

        // perform a NOT operation if necessary
        if (current != desired_state) {
            X(qubit);
        }
    }

    operation random () : Int {
        // to store output of measurement
        mutable measured = 0;

        // get a qubit
        using (qubits = Qubit[1]) {

            // put it in the zero state
            Set (Zero, qubits[0]);

            // apply a hadamard gate
            H(qubits[0]);

            // measure the qubit
            let res = M (qubits[0]);

            // get the measurement outcome
            if (res == One) {
                set measured = 1;
            }
        // make sure the qubit is zero to avoid a System.AggregateException
        Set(Zero, qubits[0]);
        }
        // return the measurement outcome
        return measured;
        }
}
