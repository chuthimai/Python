# PY02016 - XUẤT HIỆN NHIỀU LẦN NHẤT

class Number:
    def __init__(self, num, times):
        self.num = num
        self.times = times

def one_time():
    n = int(input())
    arr = [int(i) for i in input().split()]
    mark = {}
    for i in arr:
        mark[i] = 0
    for i in arr:
        mark[i] += 1
    arr = []
    for i in mark.keys():
        arr.append(Number(i, mark[i]))
    arr.sort(key=lambda x: (-x.times, x.num))
    if arr[0].times > n/2:
        print(arr[0].num)
    else:
        print("NO")


if __name__ == '__main__':
    n = int(input())
    for i in range(n): one_time()




