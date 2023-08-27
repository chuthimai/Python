# PY01009 - CHỮ HOA – CHỮ THƯỜNG

string = input()
upper = 0
lower = 0
for i in string:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1

if upper > lower:
    print(string.upper())
else:
    print(string.lower())


