def oneTime():
    num = input()
    if num[0] == num[-1]:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        oneTime()