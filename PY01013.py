# PY01013 - ƯỚC SỐ CHUNG NGUYÊN TỐ
import math

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

def oneTime():
    a, b = input().split()
    a, b = int(a), int(b)
    gcd = str(math.gcd(a, b))
    sum_digit = 0
    for i in gcd:
        sum_digit += int(i)
    if isPrime(sum_digit):
        print("YES")
    else:
        print("NO")
    return


times = int(input().split()[0])
for i in range(times):
    oneTime()