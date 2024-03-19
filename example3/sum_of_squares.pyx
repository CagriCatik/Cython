# sum_of_squares.pyx

def sum_of_squares_cython(long n):
    cdef long i
    cdef long sum = 0
    for i in range(1, n + 1):
        sum += i * i
    return sum
