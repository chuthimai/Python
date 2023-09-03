# PY01025 - CHÈN DẤU PHẨY

num = input().split()[0]
count = 0
res = ""
for digit in num[::-1]:
    res = digit + res
    count += 1
    if count % 3 == 0:
        res = ',' + res

if res[0] == ',':
    print(res[1:])
else:
    print(res)


