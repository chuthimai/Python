# PY01052 - TỔNG CHỮ SỐ NGUYÊN TỐ

def isPrime(n):
   if n<=1:
     return False
   elif n==2:
     return True
   else:
     if pow(2,n-1,n)==1:
       return True
     else:
       return False

times = int(input())
for i in range(times):
    num = input()
    sum = 0
    for j in num:
        sum += int(j)
    # print(sum)
    if isPrime(sum):
        print("YES")
    else:
        print("NO")


