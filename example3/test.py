import timeit
from sum_of_squares import sum_of_squares_cython

def sum_of_squares_python(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

def test_python_sum_of_squares(n):
    start_time = timeit.default_timer()
    result = sum_of_squares_python(n)
    end_time = timeit.default_timer()
    print("Python Sum of Squares:", result)
    print("Time:", end_time - start_time, "seconds")

def test_cython_sum_of_squares(n):
    start_time = timeit.default_timer()
    result = sum_of_squares_cython(n)
    end_time = timeit.default_timer()
    print("Cython Sum of Squares:", result)
    print("Time:", end_time - start_time, "seconds")

if __name__ == "__main__":
    num_runs = 100
    n = 100  # Adjust this number as desired

    total_python_time = 0
    total_cython_time = 0

    print("Testing Pure Python implementation:")
    for _ in range(num_runs):
        python_start_time = timeit.default_timer()
        test_python_sum_of_squares(n)
        python_end_time = timeit.default_timer()
        total_python_time += (python_end_time - python_start_time)

    print("\nTesting Cython implementation:")
    for _ in range(num_runs):
        cython_start_time = timeit.default_timer()
        test_cython_sum_of_squares(n)
        cython_end_time = timeit.default_timer()
        total_cython_time += (cython_end_time - cython_start_time)

    avg_python_time = total_python_time / num_runs
    avg_cython_time = total_cython_time / num_runs

    print("\nAverage Pure Python Time:", avg_python_time, "seconds")
    print("Average Cython Time:", avg_cython_time, "seconds")
    print("Performance improvement:", avg_python_time / avg_cython_time, "x")
