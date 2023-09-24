# ICPC0112 - PRIME – TRIPLET

is_prime = [True] * 1000001

def eraser() :
    is_prime[0] = is_prime[1] = False
    for i in range(2, 1000) :
        if is_prime[i]:
            for j in range(i * i, 1000001, i) : is_prime[j] = False

eraser()

times = int(input())
for i in range(times):
    n = int(input())
    count = 0
    for x in range(2, n-6):
        if is_prime[x] and is_prime[x+6]:
            if is_prime[x+2] or is_prime[x+4]:
                count += 1
                # if is_prime[x+2]: print(f"{x} {x+2} {x+6}")
                # else: print(f"{x} {x+4} {x+6}")
    print(count)









