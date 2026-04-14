import func

def find_two_max(arr):
    max1 = arr[0]
    max2 = arr[0]
    for i in arr:
        if max1 < i:
            max1 = i
    
    for i in arr:
        if max2 < i and i != max1:
            max2 = i
    return [max1, max2]

if __name__ == "__main__":
    sizes = [100, 1000, 5000, 10_000]
    for n in sizes:
        arr = func.generate_array(n)
        t = func.measure_time2(find_two_max, arr)
        print(n, t)