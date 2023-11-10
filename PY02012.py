# PY02012 - SẮP XẾP CHẴN LẺ

if __name__ == "__main__":
    n = int(input().split()[0])
    n_copy = n
    arr = []
    while True:
        x = [int(x) for x in input().split()]
        arr += x
        if len(arr) == n: break
    odds = []
    evens = []
    for i in range(n):
        if arr[i] % 2 == 0:
            evens.append(arr[i])
            arr[i] = 0
        else:
            odds.append(arr[i])
            arr[i] = 1
    evens = sorted(evens)
    odds = sorted(odds, reverse=True)
    for i in range(n):
        if arr[i] == 0:
            arr[i] = evens[0]
            evens.remove(evens[0])
        else:
            arr[i] = odds[0]
            odds.remove(odds[0])
    print(*arr)
