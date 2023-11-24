# PY02013 - BIẾN ĐỔI VỀ 1
def process_even(num: int):
    return num/2
def process_odd(num: int):
    return num*3 + 1

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0: break
        count = 1
        while n != 1:
            if n%2 == 0:
                n = process_even(n)
            else:
                n = process_odd(n)
            count += 1
        print(count)





