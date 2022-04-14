import dataclasses
import timeit
import qsimcirq
import cirq
import numpy as np
from zquantum.core.circuits import create_random_circuit
from qecirq.conversions import export_to_cirq
from qecirq.simulator import CirqSimulator


@dataclasses.dataclass
class Experiment:
    n_qubits: int
    n_gates: int
    random_seed: int


# https://quantumai.google/qsim/tutorials/gcp_gpu#optional_use_the_nvidia_cuquantum_sdk
def run_experiment(
    experiment: Experiment, include_cirq: bool = False, n_iterations: int = 1000
):
    z_circuit = create_random_circuit(
        experiment.n_qubits,
        experiment.n_gates,
        np.random.default_rng(experiment.random_seed),
    )
    cirq_circuit = export_to_cirq(z_circuit)
    # this is done in qe-cirq, not sure if we need it
    cirq_circuit.append(cirq.measure_each(*cirq_circuit.all_qubits()))

    # Try With qe-cirq, no gpu
    cirq_avg_walltime = -1.0
    if include_cirq:
        cirq_simulator = CirqSimulator()
        cirq_avg_walltime = (
            timeit.timeit(
                lambda: cirq_simulator.get_wavefunction(z_circuit), number=n_iterations
            )
            / n_iterations
        )

    # Try WITH custatevec (gpu_mode=1)
    qsim_simulator = qsimcirq.QSimSimulator(
        qsim_options=qsimcirq.QSimOptions(gpu_mode=1)
    )
    custatevec_avg_walltime = (
        timeit.timeit(
            lambda: qsim_simulator.simulate(cirq_circuit), number=n_iterations
        )
        / n_iterations
    )

    # Try WITHOUT custatevec (gpu_mode=0), only CUDA mode
    qsim_simulator = qsimcirq.QSimSimulator(
        qsim_options=qsimcirq.QSimOptions(gpu_mode=0)
    )
    cuda_avg_walltime = (
        timeit.timeit(
            lambda: qsim_simulator.simulate(cirq_circuit), number=n_iterations
        )
        / n_iterations
    )

    print(
        f"{experiment} N={n_iterations} Avg wall time CPU/CUSTATEVEC/CUDA is | {cirq_avg_walltime} | {custatevec_avg_walltime} | {cuda_avg_walltime}"
    )


if __name__ == "__main__":
    experiments = [
        Experiment(8, 8**2, 1),
        Experiment(12, 12**2, 1),
        Experiment(16, 16**2, 1),
        Experiment(20, 20**2, 1),
        Experiment(24, 24**2, 1),
    ]
    _ = [run_experiment(experiment, True, 10000) for experiment in experiments]
