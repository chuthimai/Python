# PY01056 - CHẴN – LẺ - NGUYÊN TỐ

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
    is_true = True
    for j in range(len(num)):
        sum += int(num[j])
        if j % 2 != int(num[j]) % 2:
            is_true = False
            break
    if not isPrime(sum):
        is_true = False
    if is_true:
        print("YES")
    else:
        print("NO")



