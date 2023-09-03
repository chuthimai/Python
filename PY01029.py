# PY01029 - SỐ ĐẢO NGUYÊN TỐ CÙNG NHAU
import math

times = int(input().split()[0])
for i in range(times):
    num = input().split()[0]
    if math.gcd(int(num), int(num[::-1])) == 1:
        print("YES")
    else:
        print("NO")



