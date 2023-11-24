# PY02009 - TRÚNG THƯỞNG

class Number:
    def __init__(self, num, times):
        self.num = num
        self.times = times

def one_time():
    n = int(input())
    arr = []
    mark = {}
    for i in range(n):
        arr.append(int(input()))
        mark[arr[-1]] = 0
    for i in arr:
        mark[i] += 1
    arr = []
    for i in mark.keys():
        arr.append(Number(i, mark[i]))
    arr.sort(key=lambda x: (-x.times, x.num))
    print(arr[0].num)


if __name__ == '__main__':
    n = int(input())
    for i in range(n): one_time()




