import func

def tab_mult(n):
    for i1 in range(1, n+1):
        for i2 in range(1, n+1):
            print(i1 * i2, end = " ")
        print()

if __name__ == "__main__":
    sizes = [2, 3, 4, 10]
    for n in sizes:
        t = func.measure_time2(tab_mult, n)
        print(n, t)