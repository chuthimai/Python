# PY02007 - CHIA DƯ CHO 42

arr = []
while len(arr) < 10:
    nums = [int(i) for i in input().split()]
    for x in nums:
        if len(arr) < 10:
            arr.append(x)
        else:
            break

mod42 = {}
for x in arr:
    mod42[x % 42] = None
print(len(mod42))

