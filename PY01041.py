# PY01041 - SỐ TĂNG GIẢM

def check(n: str):
    inc = True
    for i in range(1, len(n)):
        if n[i] == n[i-1]: return False
        if inc and n[i] > n[i-1]: continue
        if inc and n[i] < n[i-1]: inc = False
        if not inc and n[i] > n[i-1]: return False
    if inc: return False
    return True

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        b = check(input())
        if b: print("YES")
        else: print("NO")

