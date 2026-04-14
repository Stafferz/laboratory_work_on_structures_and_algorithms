import func
import random

def find_element(arr, x):
    for i in arr:
        if i == x:
            return True
    return False

if __name__ == "__main__":
    sizes = [100, 1000, 5000, 10_000]
    for n in sizes:
        arr = func.generate_array(n)
        t = func.measure_time1(find_element, arr, random.randint(0, 10_000))
        print(n, t)