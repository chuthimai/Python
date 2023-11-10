# PY02026 - TẬP HỢP SỐ BẰNG NHAU

n, m = map(int, input().split())
a = {int(i) for i in input().split()[:n]}
b = {int(i) for i in input().split()[:m]}

if a == b: print("YES")
else: print("NO")
