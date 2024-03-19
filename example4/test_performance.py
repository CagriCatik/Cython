# file: benchmark.py
import timeit

# Pure Python functions
def add_py(a, b):
    return a + b

def subtract_py(a, b):
    return a - b

def multiply_py(a, b):
    return a * b

# Cython functions
try:
    import mymodule
    add_cy = mymodule.add
    subtract_cy = mymodule.subtract
    multiply_cy = mymodule.multiply
except ImportError:
    print("Cython module not found. Make sure you've compiled it.")

if __name__ == "__main__":
    # Benchmark pure Python functions
    print("Pure Python:")
    print("Addition:", timeit.timeit("add_py(10, 5)", globals=globals(), number=1000000))
    print("Subtraction:", timeit.timeit("subtract_py(10, 5)", globals=globals(), number=1000000))
    print("Multiplication:", timeit.timeit("multiply_py(10, 5)", globals=globals(), number=1000000))

    # Benchmark Cython functions
    print("\nCython:")
    print("Addition:", timeit.timeit("add_cy(10, 5)", globals=globals(), number=1000000))
    print("Subtraction:", timeit.timeit("subtract_cy(10, 5)", globals=globals(), number=1000000))
    print("Multiplication:", timeit.timeit("multiply_cy(10, 5)", globals=globals(), number=1000000))
