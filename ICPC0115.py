# ICPC0115 - SỐ KRISH

arr = [1, 1]
for i in range(2, 10):
    arr.append(arr[i-1] * i)

times = int(input())
for i in range(times):
    n = input()
    sum = 0
    for x in n:
        sum += arr[int(x)]
    if sum == int(n):
        print("Yes")
    else:
        print("No")


