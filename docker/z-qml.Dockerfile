# Dockerfile for the base QE docker image
FROM zapatacomputing/qe-tools-base
WORKDIR /app
USER root

RUN pip3 install pennylane==0.8.1
RUN pip3 install pennylane-qiskit==0.8.2
RUN pip3 install pennylane-cirq==0.8.0
RUN pip3 install pennylane-forest==0.8.0
RUN pip3 install pennylane-qsharp==
RUN pip3 install qiskit==
RUN pip3 install forest/pyquil==
RUN pip3 install tensorflow quantum==
RUN pip3 install Q#==

ENTRYPOINT bash
