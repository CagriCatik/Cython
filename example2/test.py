import numpy as np
import matrix_multiply
import timeit

# Create two random matrices
a = np.random.rand(3, 3)
b = np.random.rand(3, 3)

# Define the function to perform matrix multiplication using Cython
def cython_matrix_multiply():
    return matrix_multiply.matrix_multiply(a, b)

# Perform matrix multiplication using NumPy's
execution_time = timeit.timeit(cython_matrix_multiply, number=1)

print("Matrix A:")
print(a)
print("\nMatrix B:")
print(b)
print("\nResult:")
 
print("\nExecution Time:", execution_time, "seconds")
