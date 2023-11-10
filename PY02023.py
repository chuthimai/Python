# PY02023 - SẮP XẾP THEO TỔNG CHỮ SỐ

def sum_digit(num:str):
    sum = 0
    for digit in num:
        sum += int(digit)
    return sum

def one_time():
    n = int(input().split()[0])
    arr = list(input().split()[:n])
    arr = sorted(arr, key=lambda x: (sum_digit(x), int(x)))
    print(*arr)

n = int(input())
for i in range(n):
    one_time()

