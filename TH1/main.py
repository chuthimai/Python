# 1
def is_divisible_3(n: int) -> bool:
    is_true = True
    if n < 50 or n > 100:
        is_true = False
    if n % 3 != 0:
        is_true = False
    return is_true

# 2
def is_integer(a: float) -> bool:
    if a == int(a):
        return True
    else:
        return False

# 3
def check_calculate(a, b, c) -> bool:
    d = (a + b) ** c
    if d >= 100 and d <= 200:
        return True
    else:
        return False

# 4
def solve(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phuong trinh vo nghiem"
    elif delta == 0:
        return "Phuong trinh co nghiem kep la " + str(-b/(2*a))
    else:
        return "Phuong trinh co 2 nghiem la " + str((-b+delta**(1/2))/(2*a)) + " " +str((-b-delta**(1/2))/(2*a))

# 5
def days_of_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if year % 4 == 0:
            return 29
        else:
            return 28

# 6
def point():
    is_loop = True
    while is_loop:
        is_loop = False
        p = input("Nhập điểm toán, văn, anh lần lượt theo thứ tự ").split()
        p = [float(i) for i in p]
        for i in p:
            if i < 0 or i > 10:
                is_loop = True
                break
    mean = (p[0] + p[1] + p[2]) / 3
    if mean >= 8 and (p[0] >= 8 or p[1] >= 8) and p[0] >= 6.5 and p[1] >= 6.5 and p[2] >= 6.5:
        print("Học sinh giỏi")
    elif mean >= 6.5 and (p[0] >= 6.5 or p[1] >= 6.5) and p[0] >= 5 and p[1] >= 5 and p[2] >= 5:
        print("Học sinh khá")
    elif mean >= 5 and (p[0] >= 5 or p[1] >= 5) and p[0] >= 3.5 and p[1] >= 3.5 and p[2] >= 3.5:
        print("Học sinh trung bình")
    elif mean >= 3.5 and (p[0] >= 3.5 or p[1] >= 3.5) and p[0] >= 2 and p[1] >= 2 and p[2] >= 2:
        print("Học sinh yếu")
    else:
        print("Học sinh kém")

# 7
def sum_1_to_n (n: int):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

# 8
def all_divisor (a: int):
    divisors = []
    for i in range(1, a+1):
        if a % i == 0:
            divisors.append(i)
    return divisors

# 9
def all_common_divisor (a: int, b: int):
    common_divisors = []
    divisors_a = all_divisor(a)
    divisors_b = all_divisor(b)
    for i in divisors_a:
        if i in divisors_b:
            common_divisors.append(i)
    return common_divisors

# 10
def fibonacci_max (a: int):
    fib = [0, 1, 1]
    while fib[-1] <= a:
        fib.append(fib[-1] + fib[-2])
    return fib[-2]

# 11
def input_integer():
    integers = []
    is_input = True
    while is_input:
        data = input().split()
        data = [int(i) for i in data]
        for i in data:
            if i == -1:
                is_input = False
                break
            else:
                integers.append(i)
    print(f"max: {max(integers)}, min: {min(integers)}")

# 12
def arrange_room (n: int, m: int, doan_khach: list):
    arranged = []
    for i in range(n):
        arranged.append(0)
    for khach in range(m):
        for i in range(n):
            if doan_khach[khach] == 0:
                break
            if arranged[i] == 0:
                if doan_khach[khach] >= 2:
                    arranged[i] = 2
                    doan_khach[khach] -= 2
                elif doan_khach[khach] == 1:
                    arranged[i] = 1
                    doan_khach[khach] -= 1
        if doan_khach[khach] > 0:
            for i in range(n):
                if doan_khach[khach] == 0:
                    break
                if arranged[i] == 1:
                    arranged[i] += 1
                    doan_khach[khach] -= 1
    return arranged

# 13
def bill():
    ga_ran = int(input("Số lượng gà rán: "))
    hamburger = int(input("Số lượng hamburger: "))
    cocacola = int(input("Số lượng cocacola: "))
    thue = 10 # (%)
    sum = ga_ran*30000 + hamburger*25000 + cocacola*10000
    print(f"Tổng trước thuế: {sum}đ")
    print(f"Thuế: {int(sum*thue/100)}đ")
    print(f"Tổng sau thuế: {int(sum - sum*thue/100)}đ")


if __name__ == "__main__":
    choose_num = int (input("Nhập số từ 0 - 13 (0 để thoát): "))
    while choose_num != 0:
        if choose_num == 1:
            print("Nhập vào số nguyên a, nếu a là số chia hết cho 3 và nằm trong khoảng từ 50 - 100 thì in ra True, ngược lại in ra False")
            print(is_divisible_3(int(input("Nhập vào số nguyên a: "))))
        elif choose_num == 2:
            print("Nhập vào số thực a, kiểm tra xem a có phải là số nguyên hay không, nếu có thì in ra True, ngược lại in ra False")
            print(is_integer(float(input("Nhập vào số thực a: "))))
        elif choose_num == 3:
            print("Nhập vào 3 số a, b, c. Tính và in ra d = (a + b)^c Nếu d là số trong khoảng từ 100 - 200 thì in ra True, ngược lại in ra False")
            arr = input("Nhập vào 3 số a, b, c: ").split()
            arr = [float(i) for i in arr]
            print(check_calculate(arr[0], arr[1], arr[2]))
        elif choose_num == 4:
            print("Giải phương trình ax^2 + bx + c = 0")
            arr = input("Nhập vào 3 số a, b, c: ").split()
            arr = [float(i) for i in arr]
            print(solve(arr[0], arr[1], arr[2]))
        elif choose_num == 5:
            print("Nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày")
            arr = input("Nhập tháng, năm: ").split()
            arr = [int(i) for i in arr]
            print(f"Số ngày của tháng {arr[0]} năm {arr[1]} là: {days_of_month(arr[0], arr[1])}")
        elif choose_num == 6:
            point()
        elif choose_num == 7:
            print("Nhập vào n Tính S = 1 + 2 + 3 + 4 + … + n")
            print(sum_1_to_n(int(input("Nhập vào n: "))))
        elif choose_num == 8:
            print("Nhập vào số nguyên dương a, in toàn bộ ước của a")
            a = int(input())
            print(all_divisor(a))
        elif choose_num == 9:
            print("Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b")
            a, b = input("Nhập vào số nguyên dương a và b: ").split()
            a = int(a)
            b = int(b)
            print(all_common_divisor(a, b))
        elif choose_num == 10:
            print("Nhập vào A, hãy tìm số trong dãy số fibonacci lớn nhất nhưng không vượt quá A")
            a = float(input("Nhập vào A: "))
            print(fibonacci_max(a))
        elif choose_num == 11:
            print("Nhập vào một dãy số nguyên, ngưng nhập khi người dùng nhập -1. Sau khi nhập xong, in số lớn nhất, số nhỏ nhất trong những số vừa nhập")
            input_integer()
        elif choose_num == 12:
            print("Xếp phòng")
            n, m = input("Nhập vào số nguyên dương N phòng đôi và M đoàn khách: ").split()
            doan_khach = input("Nhập đoàn khách ").split()
            doan_khach = [int(i) for i in doan_khach]
            n = int(n)
            m = int(m)
            print(arrange_room(n, m, doan_khach))
        elif choose_num == 13:
            bill()

        choose_num = int(input("Nhập số từ 0 - 13 (0 để thoát): "))

