# PY02008 - KHOẢNG CÁCH NGUYÊN TỐ

sang = [True] * 1000000
sang[0] = sang[1] = False
for i in range(1000000):
    if sang[i]:
        for j in range(i+i, 1000000, i):
            sang[j] = False

if __name__ == "__main__":
    n, x = map(int, input().split())
    primes = []
    i = 2
    while len(primes) != n:
        if sang[i]:
            primes.append(i)
        i += 1
    print(x, end=" ")
    for i in range(n):
        x = x + primes[i]
        print(x, end=" ")



