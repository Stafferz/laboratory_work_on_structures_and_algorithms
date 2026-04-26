import time
import random

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def measure_time1(func, data1, data2):
    start = time.perf_counter()
    func(data1, data2)
    end = time.perf_counter()
    return end - start

def measure_time2(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start