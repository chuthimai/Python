# PY01039 - KIỂM TRA SỐ ĐẸP

def oneTime():
    num = input()
    isBeautiful = True
    if num[0] == num[1]:
        isBeautiful = False
    for i in range(2, len(num)):
        if num[i] != num[i-2]:
            isBeautiful = False
    if isBeautiful:
        print("YES")
    else:
        print("NO")

times = int(input())
for i in range(times):
    oneTime()