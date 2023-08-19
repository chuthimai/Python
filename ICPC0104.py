def oneTime():
    str = input()
    str += '/'
    num = ''
    arr = []
    for i in str:
        if i >= '0' and i <= '9':
            num += i
        else:
            if num != '':
                arr.append(int(num))
                num = ''
    print(min(arr))

times = int(input())
for i in range(times):
    oneTime()