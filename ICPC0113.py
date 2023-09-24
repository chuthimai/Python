# ICPC0113 - EMIRP NUMBER

is_prime = [True] * 1000001

def eraser() :
    is_prime[0] = is_prime[1] = False
    for i in range(2, 1000) :
        if is_prime[i] == True :
            for j in range(i * i, 1000001, i) : is_prime[j] = False

eraser()

times = int(input())
for i in range(times):
    num = int(input())
    for j in range(1, num):
        s = str(j)
        if j < int(s[::-1]) and int(s[::-1]) < num:
            if is_prime[int(s)] and is_prime[int(s[::-1])]:
                print(f"{s} {s[::-1]} ", end="")
    print()



