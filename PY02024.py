# PY02024 - SẮP XẾP THEO TÍCH CHỮ SỐ

def tich_chu_so(num:str):
    res = 1
    for i in num:
        res *= int(i)
    return res

def one_time():
    n = int(input())
    arr = list(input().split()[:n])
    arr = sorted(arr, key=lambda x: (tich_chu_so(x), int(x)))
    print(*arr)

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        one_time()




