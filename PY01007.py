# PY01007 - LÃI SUẤT NGÂN HÀNG

def interest_rate(n, x):
    return n + n*x/100

def oneTime():
    val = input().split()
    val = [float(i) for i in val]
    n, x, m = val[0], val[1], val[2]
    year = 0
    while m > n:
        n = interest_rate(n, x)
        year += 1
    print(year)



times = int(input().split()[0])
for i in range(times):
    oneTime()



