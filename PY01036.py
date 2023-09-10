# PY01036 - TÍNH TỔNG PHÂN THỨC

times = int(input().split()[0])
for i in range(times):
    n = int(input().split()[0])
    sum = 0
    start = None
    if n % 2 == 0:
        start = 2
    else:
        start = 1
    for j in range(start, n+2, 2):
        sum += 1/j
    print("%.6f" % sum)

