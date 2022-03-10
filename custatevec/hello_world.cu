
#include <cuda_runtime_api.h> // cudaMalloc, cudaMemcpy, etc.
#include <cuComplex.h>        // cuDoubleComplex
#include <custatevec.h>       // custatevecApplyMatrix
#include <stdio.h>            // printf
#include <stdlib.h>           // EXIT_FAILURE

#include "helper.hpp"         // HANDLE_ERROR, HANDLE_CUDA_ERROR

__global__ void cuda_hello(){
    printf("Hello World from GPU!\n");
}


int main(void) {
    printf("Hello from CPU!\n");
    cuda_hello<<<1,1>>>(); 
    return EXIT_SUCCESS;
}