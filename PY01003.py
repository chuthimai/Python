# PY01003 - LÀM TRÒN SỐ
import math

def round_num(n: int, r: int) -> int:
    if r >= n:
        return n
    else:
        log = math.log10(r)
        add = 0
        if n % r >= 10**log/2:
            add = 10**log
        n = n//r * 10**log + add
        return round_num(n, r*10)


def oneTime():
    n = int(input().split()[0])
    print(int(round_num(n, 10)))


times = int(input().split()[0])
for i in range(times):
    oneTime()

