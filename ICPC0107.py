import sys

def replace(string: str, index: int, val: str) -> str:
    if index == 0:
        return val + string[1:]
    elif index == len(string) - 1:
        return string[:-1] + val
    else:
        return string[:index] + val + string[index+1:]


def max_sum(max_num, min_num, num1, num2):
    for i in range(len(num1)):
        if num1[i] == min_num:
            num1 = replace(num1, i, max_num)
    for i in range(len(num2)):
        if num2[i] == min_num:
            num2 = replace(num2, i, max_num)
    return int(num1) + int(num2)


def min_sum(max_num, min_num, num1, num2):
    for i in range(len(num1)):
        if num1[i] == max_num:
            num1 = replace(num1, i, min_num)
    for i in range(len(num2)):
        if num2[i] == max_num:
            num2 = replace(num2, i, min_num)
    return int(num1) + int(num2)


def oneTime():
    numbers = input().split(' ')
    p = numbers[0]
    q = numbers[1]
    min_num = min(p, q)
    max_num = max(p, q)
    num = input().split()
    num1 = num[0]
    try:
        num2 = num[1]
    except:
        num2 = input()

    print(f'{min_sum(max_num, min_num, num1, num2)} {max_sum(max_num, min_num, num1, num2)}')


if __name__ == '__main__':
    times = int(input())
    for i in range(times):
        oneTime()