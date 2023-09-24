# PY02005 - CẶP NGHỊCH THẾ

n = int(input())
arr = [int(i) for i in input().split()]
count = 0

for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            count += 1
            # print(f"{arr[i]} {arr[j]}")

print(count)
