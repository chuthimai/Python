# PY01074 TỔNG ƯỚC SỐ

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    elif n == 2:
        return True
    elif pow(2, n-1, n) == 1:
        return True
    else:
        return False

def tong_uoc_so(n: int):
    i = 2
    total = 0
    if is_prime(n):
        return n
    while n > 1:
        if not is_prime(i):
            i += 1
            continue
        if n % i == 0:
            total += i
            n //= i
            if is_prime(n):
                total += n
                break
        else:
            i += 1
    return total

n = int(input())
total = 0
for i in range(n):
    a = int(input())
    total += tong_uoc_so(a)

print(total)





