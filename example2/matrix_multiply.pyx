cimport numpy as np
import numpy as np

# Define a function to perform matrix multiplication
def matrix_multiply(np.ndarray[np.float64_t, ndim=2] a, np.ndarray[np.float64_t, ndim=2] b):
    cdef int m = a.shape[0]
    cdef int n = a.shape[1]
    cdef int p = b.shape[1]

    # Create an empty matrix to store the result
    cdef np.ndarray[np.float64_t, ndim=2] result = np.zeros((m, p), dtype=np.float64)

    # Perform matrix multiplication
    cdef int i, j, k
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i, j] += a[i, k] * b[k, j]

    return result
