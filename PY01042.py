# PY01042 - KIỂM TRA HỆ CƠ SỐ 3

times = int(input())
base3 = ['0', '1', '2']

for i in range(times):
    is_true = True
    num = input()
    for char in num:
        if char not in base3:
            is_true = False
            break
    if is_true: print("YES")
    else: print("NO")


