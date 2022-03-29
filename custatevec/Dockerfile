# Mounted gpu has cuda v11.6
FROM nvcr.io/nvidia/cuda:11.6.0-devel-ubuntu20.04

# Install python/pip and git/cmake (needed for qsim-custatevec build)
ARG CMAKE_VERSION=3.22.1
RUN apt-get update && \
    apt-get install -y wget git vim libssl-dev python3-ipython python3-pip && \
    wget -O /opt/cmake-${CMAKE_VERSION}.tar.gz https://github.com/Kitware/CMake/releases/download/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION}.tar.gz && \
    tar xvf /opt/cmake-${CMAKE_VERSION}.tar.gz -C /opt/ && \
    rm /opt/cmake-${CMAKE_VERSION}.tar.gz && \
    cd /opt/cmake-${CMAKE_VERSION} && \
    ./bootstrap && \
    make && \
    make install


# Get cuquantum
ENV CUQUANTUM_ROOT=/opt/cuquantum
ARG TARFILE=cuquantum-linux-x86_64-22.03.0.40-archive.tar.xz
RUN wget -O /tmp/${TARFILE} https://developer.download.nvidia.com/compute/cuquantum/redist/cuquantum/linux-x86_64/${TARFILE} && \
    mkdir -p ${CUQUANTUM_ROOT} && \
    tar xvf /tmp/${TARFILE} -C ${CUQUANTUM_ROOT} --strip-components=1 && \
    #lib64/ is missing, symlink it to lib/
    ln -s ${CUQUANTUM_ROOT}/lib ${CUQUANTUM_ROOT}/lib64 && \
    rm /tmp/${TARFILE}

ENV LD_LIBRARY_PATH=/opt/conda/lib:${CUQUANTUM_ROOT}/lib:${LD_LIBRARY_PATH}
ENV CUSTATEVEC_ROOT=${CUQUANTUM_ROOT}
ENV CUTENSORNET_ROOT=${CUQUANTUM_ROOT}
#CUQUANTUM_DIR needs to be set for qsim make
ENV CUQUANTUM_DIR=${CUQUANTUM_ROOT}
ENV PATH=/usr/local/cuda/bin/:${PATH}

# Install cuquantum python bindings, remove previous cupy version
# RUN pip uninstall -y cupy-cuda115 && \
# RUN conda install -c conda-forge cuquantum-python

# Get samples repo
# ARG TARFILE=v0.1.0.0.tar.gz
# RUN wget -O /tmp/${TARFILE} https://github.com/NVIDIA/cuQuantum/archive/refs/tags/${TARFILE} && \
#     mkdir -p ${CUSTATEVEC_ROOT}/code_samples && \
#     tar xvf /tmp/${TARFILE} -C ${CUSTATEVEC_ROOT}/code_samples --strip-components=1 && \
#     rm /tmp/${TARFILE}

# Get qsim v0.12.1, build from source for custatevec backend
ARG TARFILE=v0.12.1.tar.gz
RUN wget -O /tmp/${TARFILE} https://github.com/quantumlib/qsim/archive/refs/tags/${TARFILE} && \
    mkdir -p /opt/qsim && \
    tar xvf /tmp/${TARFILE} -C /opt/qsim --strip-components=1 && \
    rm /tmp/${TARFILE} && \
    cd /opt/qsim && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    # not recommended
    pip install "pybind11[global]" 
# pip install pybind
#&& make qsim-custatevec && (make run-py-tests || exit 0)
