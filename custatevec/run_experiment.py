import dataclasses
import qsimcirq
import cirq
import numpy as np
from zquantum.core.circuits import create_random_circuit
from qecirq.conversions import export_to_cirq


@dataclasses.dataclass
class Experiment:
    n_qubits: int
    n_gates: int
    random_seed: int


# https://quantumai.google/qsim/tutorials/gcp_gpu#optional_use_the_nvidia_cuquantum_sdk
def run_experiment(experiment: Experiment):
    z_circuit = create_random_circuit(
        experiment.n_qubits,
        experiment.n_gates,
        np.random.default_rng(experiment.random_seed),
    )
    cirq_circuit = export_to_cirq(z_circuit)
    # this is done in qe-cirq, not sure if we need it
    cirq_circuit.append(cirq.measure_each(*cirq_circuit.all_qubits()))
    gpu_options = qsimcirq.QSimOptions()
    qsim_simulator = qsimcirq.QSimSimulator(qsim_options=gpu_options)
    qsim_results = qsim_simulator.run(cirq_circuit)
    print(qsim_results)


if __name__ == "__main__":
    experiments = [
        Experiment(8, 8 * 8, 1),
        Experiment(8, 8 * 8, 2),
        Experiment(8, 8 * 8, 3),
        Experiment(8, 8 * 8, 4),
        Experiment(8, 8 * 8, 5),
    ]
