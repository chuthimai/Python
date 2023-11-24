# PYKT081 - ĐỊA CHỈ IP
import re

def check(string: str):
    try:
        a, b, c, d = map(int, string.split("."))
    except:
        return False
    if a > 255 or b > 255 or c > 255 or d > 255: return False
    if a < 0 or b < 0 or c < 0 or d < 0: return False
    return True

if __name__ == '__main__':
    n = int(input().split()[0])
    arr = []
    while len(arr) < n:
        inp = input().split()
        for i in inp: arr.append(i)

    for i in range(n):
        if check(arr[i]):
            print("YES")
        else:
            print("NO")




