# PY01005 - SỐ MAY MẮN

num = input().split()[0]
num4 = 0
num7 = 0
for i in num:
    if i == '4':
        num4 += 1
    elif i == '7':
        num7 += 1

if num4 + num7 == 4 or num4 + num7 == 7:
    print("YES")
else:
    print("NO")

