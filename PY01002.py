math = input()
math = math.split(' ')

if int(math[0]) + int(math[2]) == int(math[4]):
    print('YES')
else:
    print('NO')