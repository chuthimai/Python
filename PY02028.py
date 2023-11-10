# PY02028 - SẮP XẾP NGUYÊN TỐ

def is_prime(n: int) -> bool:
    if n < 2: return False
    elif n == 2: return True
    elif pow(2, n-1, n) == 1: return True
    else: return False

if __name__ == "__main__":
    n = int(input())
    arr = [int(i) for i in input().split()[:n]]
    primes = []
    for i in range(n):
        if is_prime(arr[i]):
            primes.append(arr[i])
            arr[i] = -1
    primes.sort()
    j = 0
    for i in range(n):
        if arr[i] == -1:
            arr[i] = primes[j]
            j += 1
    print(*arr)
