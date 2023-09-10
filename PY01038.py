# PY01038 - KIỂM TRA CHIA HẾT CHO 7

def sum_with_rnum(num: int) -> int:
    return num + int(str(num)[::-1])

def oneTime():
    num = int(input())
    canFind = False
    for i in range(1000):
        if num % 7 == 0:
            canFind = True
            break
        num = sum_with_rnum(num)
    if canFind:
        print(num)
    else:
        print(-1)

times = int(input())
for i in range(times):
    oneTime()
