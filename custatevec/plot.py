import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/brian/projects/zapata/z/z-qml/custatevec/results.csv")

df["n_qubits"] = df["n_qubits"].astype(int)

df["norm_cirq"] = df["cirq_avg_walltime"] / df["custatevec_avg_walltime"]
df["norm_cirq"] = df[df["norm_cirq"] > 0.0]["norm_cirq"]
df["norm_cuda"] = df["cuda_avg_walltime"] / df["custatevec_avg_walltime"]

axes = df.plot.line(
    x="n_qubits",
    xlabel="# Qubits",
    y=["norm_cirq", "norm_cuda"],
    ylabel="Normalized Wall Time",
    label=["Cirq (CPU)", "Qsim Cuda"],
    logy=True,
)
axes.axhline(y=1.0, color="black", linestyle="--")
axes.set_xticks(df["n_qubits"].unique())

plt.show()
