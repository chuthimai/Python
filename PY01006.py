# PY01006 - SỐ MAY MẮN - 2

times = int(input().split()[0])
for i in range(times):
    num = input().split()[0]
    is_true = True
    for i in num:
        if i!='4' and i!='7':
            is_true = False
            break
    if is_true:
        print("YES")
    else:
        print("NO")