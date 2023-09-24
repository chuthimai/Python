# PY02036 - LIỆT KÊ CẶP SỐ NGUYÊN TỐ CÙNG NHAU
import math

n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
for i in range(n):
    for j in range(i+1, n):
        if math.gcd(arr[i], arr[j]) == 1:
            print(f"{arr[i]} {arr[j]}")



