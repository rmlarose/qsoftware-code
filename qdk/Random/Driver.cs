using System;

using Microsoft.Quantum.Simulation.Core;
using Microsoft.Quantum.Simulation.Simulators;

namespace Random
{
    class Driver
    {
        static void Main(string[] args)
        {
            using (var qsim = new QuantumSimulator())
            {
                var measured = random.Run(qsim).Result;

                System.Console.WriteLine(
                    $"Measurement: {measured, 0}.");
            }
        }
    }
}