# https://quantumai.google/qsim/tutorials/gcp_gpu#optional_use_the_nvidia_cuquantum_sdk
import qsimcirq
import cirq

q0, q1 = cirq.LineQubit.range(2)
circuit = cirq.Circuit(cirq.H(q0), cirq.CX(q0, q1))
gpu_options = qsimcirq.QSimOptions(use_gpu=True, gpu_mode=1)
qsim_simulator = qsimcirq.QSimSimulator(qsim_options=gpu_options)
print(circuit)
qsim_results = qsim_simulator.compute_amplitudes(circuit, bitstrings=[0b00, 0b01])
print(qsim_results)
