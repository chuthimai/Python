# PY01054 - TÍCH CHỮ SỐ

times = int(input())
for i in range(times):
    num = input()
    mul  = 1
    for j in num:
        if int(j) != 0:
            mul *= int(j)
    print(mul)

