# PY01020 - SỐ PHÁT LỘC

times = int(input().split()[0])
for i in range(times):
    num = input().split()[0]
    if num[-2:] == "86":
        print("YES")
    else:
        print("NO")

