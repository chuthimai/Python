# PY01059 - TỔNG CHỮ SỐ - TÍCH CHỮ SỐ

def one_time():
    num = input()
    is_all_equal_0 = True
    sum = 0
    product = 1
    for i in range(len(num)):
        if i%2 == 0:
            sum += int(num[i])
        else:
            if int(num[i]) != 0:
                is_all_equal_0 = False
                product *= int(num[i])
    if is_all_equal_0: product = 0
    print(f"{sum} {product}")

if __name__ == "__main__":
    n = int(input())
    for i in range(n): one_time()



