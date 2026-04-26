import tracemalloc
import func

def buble_sort(arr):
    tracemalloc.start()
    n = len(arr)  
    for i in range(n):  
        f = False  
        for j in range(0, n - i - 1):  
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
            f = True  
        if not f:  
            break
    current, peak = tracemalloc.get_traced_memory()
    print(f"Текущая память: {current} байт, пиковая: {peak} байт")
        
if __name__ == "__main__":
    sizes = [100, 1000, 5000, 10_000]
    for n in sizes:
        arr = func.generate_array(n)
        t = func.measure_time2(buble_sort, arr)
        print(n, t)