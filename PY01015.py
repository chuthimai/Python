# PY01015 - SỐ KHÔNG GIẢM

def oneTime():
    num = input().split()[0]
    is_true = True
    for i in range(1, len(num)):
        if num[i] < num[i-1]:
            is_true = False
            break
    if is_true:
        print("YES")
    else:
        print("NO")

times = int(input().split()[0])
for i in range(times):
    oneTime()
