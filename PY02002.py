# PY02002 - LIỆT SỐ FIBONACCI

fib = [0, 1, 1]
for i in range(3, 93):
    fib.append(fib[i-1] + fib[i-2])

times = int(input())
for _ in range(times):
    a, b = [int(i) for i in input().split()]
    for i in range(a, b+1): print(fib[i], end=" ")
    print()




