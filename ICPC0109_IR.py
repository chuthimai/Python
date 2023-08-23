import numpy as np

def oneTime():
    n = int(input().split()[0])
    arr = input().split()
    arr = np.array([int(i) for i in arr[:n]], dtype=int)
    min1 = np.inf
    min2 = np.inf
    min3 = np.inf
    for i in arr:
        if i < min1:
            min1 = i
    for i in arr:
        if i < min2 and i != min1:
            min2 = i
    for i in arr:
        if i < min3 and i != min1 and i != min2:
            min3 = i

    # print(min1, min2, min3)
    print(min1 + min2 + min3)


if __name__ == '__main__':
    times = int(input().split()[0])
    for i in range(times):
        oneTime()
