def oneTime():
    str = input()
    str += '/'
    num = ''
    arr = []
    point = False
    for i in str:
        if i >= '0' and i <= '9':
            num += i
        elif num == '' and i == '-':
            num += i
        # elif not point and i == '.':
        #     num += i
        #     point = True
        else:
            if num != '':
                arr.append(int(num))
                num = ''
                point = False
    print(max(arr))


times = int(input())
for i in range(times):
    oneTime()