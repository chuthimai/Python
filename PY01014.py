# PY01014 - CHIA HẾT CHO K

arr = []
a, k, n = input().split()
a, k, n = int(a), int(k), int(n)
r = a % k
b = k - r
while a + b <= n:
    arr.append(b)
    b += k
if len(arr) == 0:
     print(-1)
else:
    for i in arr:
        print(i, end=' ')


