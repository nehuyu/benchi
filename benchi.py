import time
from functools import reduce

def benchi(func, times):
    elasted_times = []

    for i in range(times):

        start = time.time()
        func()
        elasted_time = time.time() - start
        elasted_times.append(elasted_time)

    print("------------------------------------------------")
    print("mean: ", reduce(lambda x, y: x + y, elasted_times) / i)
    print("min : ", min(elasted_times))
    print("max : ", max(elasted_times))
    print("------------------------------------------------")

