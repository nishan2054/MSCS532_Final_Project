import time
import numpy as np

def add_python_loop(a, b):
    """Element wise addition using a Python loop."""
    result = [0.0] * len(a)
    for i in range(len(a)):
        result[i] = a[i] + b[i]
    return result

def add_numpy_vectorized(a, b):
    """Element wise addition using NumPy vectorization."""
    return a + b

def time_function(func, *args, repeats=5):
    """Time a function by running it several times."""
    durations = []
    func(*args)  # warm up
    for _ in range(repeats):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        durations.append(end - start)
    return sum(durations) / len(durations)

def run_experiment():
    sizes = [100000, 1000000, 5000000]
    np.random.seed(0)

    print("n, python_time, numpy_time, speedup")
    for n in sizes:
        a = np.random.rand(n)
        b = np.random.rand(n)

        loop_time = time_function(add_python_loop, a, b)
        numpy_time = time_function(add_numpy_vectorized, a, b)
        speedup = loop_time / numpy_time

        print(f"{n}, {loop_time:.6f}, {numpy_time:.6f}, {speedup:.2f}")

if __name__ == "__main__":
    run_experiment()
