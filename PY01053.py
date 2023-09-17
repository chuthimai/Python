# PY01053 - SỐ CHIA HẾT CHO 3

times = int(input())
for i in range(times):
    num = input()
    sum = 0
    for j in num:
        sum += int(j)
    # print(sum)
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")
