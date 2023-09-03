# PY01024 - CHẴN - LẺ

def check(num: str) -> bool:
    sum_digit = 0
    isTrue = True
    for i in num:
        sum_digit += int(i)
    if sum_digit%10 != 0:
        isTrue = False
    if isTrue:
        for i in range(1, len(num)):
            if abs(int(num[i]) - int(num[i-1])) != 2:
                isTrue = False
                break
    return isTrue

times = int(input().split()[0])
for i in range(times):
    num = input().split()[0]
    if check(num):
        print("YES")
    else:
        print("NO")
