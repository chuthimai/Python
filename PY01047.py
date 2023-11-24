# PY01047 - KIỂM TRA NGUYÊN TỐ

def is_prime(n: int) -> bool:
    if n < 2: return False
    elif n == 2: return True
    elif pow(2, n-1, n) == 1: return True
    else: return False

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        number = input()
        b = is_prime(int(number[-4:]))
        if b: print("YES")
        else: print("NO")



