# PY01055 - SỐ XEN KẼ

times = int(input())
for i in range(times):
    is_true = True
    num = input()
    if len(num) % 2 == 0:
        is_true = False
    if num[0] == num[1]:
        is_true = False
    for j in range(2, len(num), 2):
        if num[j] != num[j-2]:
            is_true = False
            break
    if is_true:
        print("YES")
    else:
        print("NO")

