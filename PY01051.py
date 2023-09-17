# PY01051 - TỔNG CHỮ SỐ THUẬN NGHỊCH

def isReversible(num: str) -> bool:
    if len(num) == 1: return False
    if num == num[::-1]:
        return True
    return False

times = int(input())
for i in range(times):
    num = input()
    sum = 0
    for j in num:
        sum += int(j)
    # print(sum)
    if isReversible(str(sum)):
        print("YES")
    else:
        print("NO")


