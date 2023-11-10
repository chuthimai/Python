# PY02050 - ĐOẠN LIÊN TIẾP NHỎ HƠN

def one_time():
    n = int(input())
    arr = list(map(int, input().split()[:n]))
    mark = [1]*n
    for i in range(1, n):
        for j in range(0, i)[::-1]:
            if arr[j] <= arr[i]: mark[i] += 1
            else: break

    print(*mark)

n = int(input())
for i in range(n):
    one_time()