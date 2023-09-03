# PY01019 - KHOẢNG CÁCH KÝ TỰ

times = int(input().split()[0])
for i in range(times):
    string = input().split()[0]
    r_string = string[::-1]
    isTrue = True
    for j in range(1, len(string)):
        if abs(ord(string[j]) - ord(string[j-1])) != abs(ord(r_string[j]) - ord(r_string[j-1])):
            isTrue = False
            break
    if isTrue:
        print("YES")
    else:
        print("NO")


