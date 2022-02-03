FROM nvcr.io/nvidia/pytorch:22.01-py3

# Get cuquantum
ENV CUQUANTUM_ROOT=/opt/cuquantum0.1.0.30
ARG TARFILE=cuquantum-linux-x86_64-0.1.0.30-archive.tar.xz
RUN wget -O /tmp/${TARFILE} \
    https://developer.download.nvidia.com/compute/cuquantum/redist/linux-x86_64/${TARFILE} && \
    mkdir -p ${CUQUANTUM_ROOT} && \
    tar xvf /tmp/${TARFILE} -C ${CUQUANTUM_ROOT} --strip-components=1 && \
    #lib64/ is missing, symlink it to lib/
    ln -s ${CUQUANTUM_ROOT}/lib ${CUQUANTUM_ROOT}/lib64 && \
    rm /tmp/${TARFILE}
ENV LD_LIBRARY_PATH=/opt/conda/lib:${CUQUANTUM_ROOT}/lib:${LD_LIBRARY_PATH}

# Install cuquantum python bindings, remove previous cupy version
RUN pip uninstall -y cupy-cuda115 && \
    conda install -c conda-forge cuquantum-python

ENV CUSTATEVEC_ROOT=${CUQUANTUM_ROOT}
ENV CUTENSORNET_ROOT=${CUQUANTUM_ROOT}
ENV PATH=/usr/local/cuda/bin/:${PATH}

# Get samples repo
ARG TARFILE=v0.1.0.0.tar.gz
RUN wget -O /tmp/${TARFILE} https://github.com/NVIDIA/cuQuantum/archive/refs/tags/${TARFILE} && \
    mkdir -p ${CUSTATEVEC_ROOT}/code_samples && \
    tar xvf /tmp/${TARFILE} -C ${CUSTATEVEC_ROOT}/code_samples --strip-components=1 && \
    rm /tmp/${TARFILE}

#from https://github.com/NVIDIA/cuQuantum/issues/1#issuecomment-1028333564
# ENV CUSTATEVEC_ROOT=/opt/conda 