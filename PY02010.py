# PY02010 - LỚN NHẤT VÀ NHỎ NHẤT

def one_time() -> bool:
    n = int(input())
    if n == 0: return False
    arr = []
    for i in range(n):
        arr.append(int(input()))
    gtln = max(arr)
    gtnn = min(arr)
    if gtnn == gtln: print("BANG NHAU")
    else: print(f"{gtnn} {gtln}")
    return True

loop = True
while loop:
    loop = one_time()
