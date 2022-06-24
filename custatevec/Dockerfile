# Mounted gpu has cuda v11.6
FROM nvcr.io/nvidia/cuquantum-appliance:22.02-cirq

WORKDIR /app

# https://askubuntu.com/questions/1408016/the-following-signatures-couldnt-be-verified-because-the-public-key-is-not-avai
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub && \
    apt-get update

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
