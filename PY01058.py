# PY01058 - ĐOẠN CUỐI NGUYÊN TỐ

def is_prime(n: int) -> bool:
    if n < 2: return False
    elif n == 2: return True
    elif pow(2, n-1, n) == 1: return True
    else: return False

n = int(input())
for i in range(n):
    num = input()
    if is_prime(int(num[-4:])):
        print("YES")
    else:
        print("NO")
