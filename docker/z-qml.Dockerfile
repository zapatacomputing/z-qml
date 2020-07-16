# Copyright Zapata Computing, Inc. All rights reserved.

# Dockerfile for the base QE docker image
FROM zapatacomputing/qe-tools-base
WORKDIR /app
USER root

# Install basic packages and dependecies for QVM
RUN apt-get clean && apt-get update
RUN apt-get -y install \
                wget \
                vim \
                htop \
                sbcl \
                clang-7 \
                libzmq3-dev \
                libz-dev \
                libblas-dev \
                liblapack-dev

# Install QML Libraries
RUN pip3 install pennylane==0.8.1
RUN pip3 install pennylane-qiskit==0.8.2
RUN pip3 install pennylane-cirq==0.8.0
RUN pip3 install pennylane-forest==0.8.0
RUN pip3 install pennylane-qsharp==0.8.0
RUN pip3 install qiskit==0.18.1
RUN pip3 install pyquil==2.19.0
RUN pip3 install tensorflow==2.1.0
RUN pip3 install tensorflow-quantum==0.2.0
RUN pip3 install gpyopt==1.2.6
RUN pip3 install cvxopt==1.2.5

# Install Rigetti QVM
WORKDIR /root
RUN curl -O https://beta.quicklisp.org/quicklisp.lisp && \
    echo '(quicklisp-quickstart:install)'  | sbcl --load quicklisp.lisp
RUN git clone https://github.com/rigetti/quilc.git && \
                cd quilc && \
                git fetch && \
                git checkout v1.18.0 && \
                git submodule init && \
                git submodule update --init && \
                make && \
                mv quilc /usr/local/bin
RUN git clone https://github.com/rigetti/qvm.git && \
                cd qvm && \
                git fetch && \
                git checkout v1.17.0 && \
                make QVM_WORKSPACE=10240 qvm && \
                mv qvm /usr/local/bin

WORKDIR /app
ENTRYPOINT bash
