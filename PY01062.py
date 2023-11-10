# PY01062 - ƯU THẾ NGUYÊN TỐ

def is_prime(n: int) -> bool:
    if n < 2: return False
    elif n == 2: return True
    elif pow(2, n-1, n) == 1: return True
    else: return False

def check(num):
    isTrue = True
    if not is_prime(len(num)):
        isTrue = False
    else:
        snt = 0
        for i in num:
            if is_prime(int(i)): snt += 1
        if snt <= len(num)/2: isTrue = False
    if isTrue: print("YES")
    else: print("NO")

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        num = input()
        check(num)



