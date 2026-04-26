import func
import random

def bin_find(arr):
    arr.sort()
    a = random.choice(arr)
    while True:
        z = len(arr)
        if arr[z//2] == a:
            return True
        elif a > arr[z//2]:
            arr = arr[z//2 + 1:]
        else:
            arr = arr[:z//2]
            
            
if __name__ == "__main__":
    sizes = [100, 1000, 5000, 10_000]
    for n in sizes:
        arr = func.generate_array(n)
        t = func.measure_time2(bin_find, arr)
        print(n, t)