# Copyright Zapata Computing, Inc. All rights reserved.

# Dockerfile for the base QE docker image
FROM zapatacomputing/z-qml:nightly
WORKDIR /app
USER root

RUN apt-get install gcc gfortran g++ && \
    pip install cython && \
    git clone https://github.com/pele-python/pele.git && \
    cd pele && \ 
    python3 setup.py build_ext -i --fcompiler=gfortran

WORKDIR /app
ENTRYPOINT bash
