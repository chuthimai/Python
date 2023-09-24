# PY01004 - NGUYÊN TỐ
import math

def is_prime(n: int) -> bool:
    if n < 2: return False
    elif n == 2: return True
    elif pow(2, n-1, n) == 1: return True
    else: return False

times = int(input())
for i in range(times):
    n = int(input())
    count = 0
    for x in range(1, n):
        if math.gcd(x, n) == 1: count += 1
    if is_prime(count): print("YES")
    else: print("NO")


