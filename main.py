import time
import random

def multiplication_8085(a, b):
    result = 0
    while b > 0:
        if b & 1:
            result += a
        a <<= 1
        b >>= 1
    return result

def multiplication_6502(a, b):
    result = 0
    for i in range(32):
        if b & (1 << i):
            result += a << i
    return result

def multiplication_nsc(a, b):
    if a < 10 or b < 10:
        return a * b

    m = max(len(str(a)), len(str(b)))
    m2 = m // 2

    high1, low1 = divmod(a, 10 ** m2)
    high2, low2 = divmod(b, 10 ** m2)

    z0 = multiplication_nsc(low1, low2)
    z1 = multiplication_nsc((low1 + high1), (low2 + high2))
    z2 = multiplication_nsc(high1, high2)

    result = z2 * 10 ** (2 * m2) + (z1 - z2 - z0) * 10 ** m2 + z0
    return result

def benchmark_algorithm(algorithm, name, iterations, a, b):
    total_time = 0
    for _ in range(iterations):
        start_time = time.time()
        algorithm(a, b)
        end_time = time.time()
        total_time += end_time - start_time
    average_time = total_time / iterations
    print(f"{name} took {average_time:.6f} seconds on average for {iterations} iterations.")

iterations = 1000
a = random.randint(1, 10000)
b = random.randint(1, 10000)
benchmark_algorithm(multiplication_8085, "8085 Multiplication", iterations, a, b)
benchmark_algorithm(multiplication_6502, "6502 Multiplication", iterations, a, b)
benchmark_algorithm(multiplication_nsc, "NSC Multiplication", iterations, a, b)
