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
    n = input()
    revert_n = n[::-1]
    check = True
    sum_of_digit = 0

    for i in n:
        if not int(i) in [2, 3, 5, 7]:
            check = False
            break
        sum_of_digit += int(i)
    if check:
        if not isPrime(sum_of_digit):
            check = False
    if check:
        check = isPrime(int(n))
    if check:
        check = isPrime(int(revert_n))

    if check:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        oneTime()
