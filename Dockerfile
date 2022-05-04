# Copyright Zapata Computing, Inc. All rights reserved.

FROM ubuntu:18.04
WORKDIR /app
USER root

# Install python, pip, CLI tools and other utilities
# Set the default version of Python3 to Python 3.7 (Orquestra recommended version)
# Install basic packages and dependecies for QVM
RUN apt-get update -y --fix-missing && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get install -y python3.7 python3-pip python3.7-dev && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1 && \
    update-alternatives --set python3 /usr/bin/python3.7 && \
    apt-get install -y curl git openssh-client && \
    apt-get install -y \
        wget vim htop sbcl clang-7 gfortran \
        libzmq3-dev libz-dev libblas-dev liblapack-dev && \
    apt-get clean

ENV PYTHONPATH="/usr/local/lib/python3.7/dist-packages:${PYTHONPATH}"
# PYTHONUNBUFFERED will dump python stdout to logs directly, rather than buffering
# should resolve issue of not seeing python print statements in orquestra logs
ENV PYTHONUNBUFFERED="1"

# Install ML Libraries
# pytorch installation will OOM fail without --no-cache-dir
# https://stackoverflow.com/questions/59800318/how-to-install-torch-in-python
RUN pip3 install --upgrade pip setuptools && \
    pip3 install --no-cache-dir \
        dill \
        numpy \
        scipy \
        scikit-learn \
        torch \
        jax \
        jaxlib \
        autograd \
        flax \
        cirq \
        qiskit \
        optuna \
        gpyopt \
        cvxopt

WORKDIR /app
ENTRYPOINT bash
