# PY01057 - VỊ TRÍ NGUYÊN TỐ

def isPrime(n) :
    if n < 2 : return 0
    for i in range(2, int(n**0.5) + 1) :
        if n % i == 0 : return 0
    return 1
def check(num):
    for j in range(len(num)):
        if isPrime(j) != isPrime(int(num[j])):
            return False
    return True

times = int(input())
for i in range(times):
    num = input()
    if check(num):
        print("YES")
    else:
        print("NO")


