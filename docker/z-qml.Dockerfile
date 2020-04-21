# Dockerfile for the base QE docker image
FROM zapatacomputing/qe-tools-base
WORKDIR /app
USER root

RUN pip3 install pennylane==0.8.1
RUN pip3 install pennylane-qiskit==0.8.2
RUN pip3 install pennylane-cirq==0.8.0
RUN pip3 install pennylane-forest==0.8.0
RUN pip3 install pennylane-qsharp==0.8.0
RUN pip3 install qiskit==0.18.1
RUN pip3 install pyquil==2.19.0
RUN pip3 install tensorflow==2.1.0
RUN pip3 install tensorflow-quantum==0.4.8
#RUN pip3 install qsharp==0.11.2003.3107

ENTRYPOINT bash
