# PY02004 - DÃY SỐ NHỊ PHÂN

n = int(input())
arr = input().split()
count = 0

for i in range(n-1):
    if arr[i] != arr[i+1]: count += 1
print(count)

