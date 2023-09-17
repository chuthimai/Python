# PY01049 - CHỮ SỐ NGUYÊN TỐ
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
prime = ['2', '3', '5', '7']
for i in range(times):
    count_prime = 0
    num = input()
    is_true = True
    if not isPrime(len(num)):
        is_true = False
    for j in num:
        if j in prime:
            count_prime += 1
    if count_prime <= len(num) - count_prime:
        is_true = False
    if is_true: print("YES")
    else: print("NO")

