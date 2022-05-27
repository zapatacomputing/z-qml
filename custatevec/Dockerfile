# Mounted gpu has cuda v11.6
FROM nvcr.io/nvidia/cuquantum-appliance:22.02-cirq

# Install python/pip and git/cmake (needed for qsim-custatevec build)
# ARG CMAKE_VERSION=3.22.1
# RUN apt-get update && \
#     apt-get install -y wget git vim libssl-dev python3-ipython python3-pip && \
#     wget -O /opt/cmake-${CMAKE_VERSION}.tar.gz https://github.com/Kitware/CMake/releases/download/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION}.tar.gz && \
#     tar xvf /opt/cmake-${CMAKE_VERSION}.tar.gz -C /opt/ && \
#     rm /opt/cmake-${CMAKE_VERSION}.tar.gz && \
#     cd /opt/cmake-${CMAKE_VERSION} && \
#     ./bootstrap && \
#     make && \
#     make install

# Get z-quantum-core and qe-cirq
RUN pip install git+https://github.com/zapatacomputing/z-quantum-core.git && \
    pip install git+https://github.com/zapatacomputing/qe-cirq

COPY ./run_experiment.py /workspace/run_experiment.py